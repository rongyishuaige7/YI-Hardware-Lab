#!/usr/bin/env python3
"""Refresh indexed evidence only after every current HEAD passes its original workflow."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from datetime import datetime, timezone
import json
import re
from urllib.parse import quote, urlencode

from validate_projects import PROJECTS_FILE, README_FILE, get_json, validate_local, validate_readme

TRUSTED_EVENTS = {"push", "workflow_dispatch", "schedule"}
WORKFLOW_RE = re.compile(r"^\.github/workflows/[A-Za-z0-9_.-]+\.ya?ml$")


def latest_current_run(runs: list[dict], branch: str, head: str, workflow: str) -> dict:
    candidates = [run for run in runs if (
        run.get("head_sha") == head
        and run.get("head_branch") == branch
        and run.get("event") in TRUSTED_EVENTS
        and run.get("path", "").split("@", 1)[0] == workflow
    )]
    if not candidates:
        raise ValueError(f"no trusted {workflow} run for current HEAD")
    run = max(candidates, key=lambda item: (
        item.get("run_started_at") or item.get("created_at") or "",
        item.get("run_attempt", 1), item.get("id", 0),
    ))
    if run.get("status") != "completed" or run.get("conclusion") != "success":
        raise ValueError(f"latest current-HEAD run is {run.get('status')}/{run.get('conclusion')}")
    return run


def refresh_project(project: dict) -> dict:
    result = deepcopy(project)
    owner, repo = project["repo"].removeprefix("https://github.com/").split("/")
    base = f"https://api.github.com/repos/{owner}/{repo}"
    metadata = get_json(base)
    if metadata.get("private") is not False:
        raise ValueError(f"{repo}: repository is not public")
    branch = metadata["default_branch"]
    head = get_json(f"{base}/commits/{quote(branch, safe='')}")["sha"]
    previous_id = project["build"]["run_url"].rsplit("/", 1)[1]
    previous = get_json(f"{base}/actions/runs/{previous_id}")
    workflow = previous.get("path", "").split("@", 1)[0]
    if not WORKFLOW_RE.fullmatch(workflow):
        raise ValueError(f"{repo}: original evidence has no valid workflow path")
    if project["build"].get("workflow", workflow) != workflow:
        raise ValueError(f"{repo}: refusing to change the indexed workflow")
    params = urlencode({"branch": branch, "head_sha": head, "per_page": 100})
    runs = get_json(f"{base}/actions/workflows/{quote(workflow.rsplit('/', 1)[1])}/runs?{params}")
    run = latest_current_run(runs.get("workflow_runs", []), branch, head, workflow)
    if project["build"]["artifact_retention_days"] is None:
        artifacts = get_json(f"{base}/actions/runs/{run['id']}/artifacts")
        if artifacts.get("total_count") != 0:
            raise ValueError(f"{repo}: run now uploads artifacts; review its declared scope first")
    result["default_branch"] = branch
    result["head_sha"] = head
    result["build"].update(head_sha=head, workflow=workflow, run_url=run["html_url"])
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the fully verified index and README")
    args = parser.parse_args()
    original = json.loads(PROJECTS_FILE.read_text())
    projects = validate_local(original)
    validate_readme(projects)
    # API reads are independent; no files change until all 22 results are verified.
    with ThreadPoolExecutor(max_workers=4) as pool:
        refreshed = list(pool.map(refresh_project, projects))
    updated = deepcopy(original)
    updated["projects"] = refreshed
    updated["status_date"] = datetime.now(timezone.utc).date().isoformat()
    validate_local(updated)
    readme = README_FILE.read_text()
    for before, after in zip(projects, refreshed):
        readme = readme.replace(before["head_sha"], after["head_sha"])
        readme = readme.replace(before["head_sha"][:12], after["head_sha"][:12])
        readme = readme.replace(before["build"]["run_url"], after["build"]["run_url"])
    readme = readme.replace(original["status_date"], updated["status_date"])
    changed = sum(a["head_sha"] != b["head_sha"] for a, b in zip(projects, refreshed))
    if args.write:
        PROJECTS_FILE.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n")
        README_FILE.write_text(readme)
    print(f"Verified {len(refreshed)} projects; {changed} changed HEADs; {'written' if args.write else 'dry run'}.")


if __name__ == "__main__":
    main()
