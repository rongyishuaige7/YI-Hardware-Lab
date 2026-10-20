import unittest

from refresh_evidence import latest_current_run


class EvidenceSelectionTest(unittest.TestCase):
    def run_fixture(self, **changes):
        return dict({
            "id": 1, "head_sha": "a" * 40, "head_branch": "main",
            "event": "push", "path": ".github/workflows/ci.yml",
            "run_started_at": "2026-10-20T01:00:00Z",
            "status": "completed", "conclusion": "success",
        }, **changes)

    def select(self, runs):
        return latest_current_run(runs, "main", "a" * 40, ".github/workflows/ci.yml")

    def test_later_manual_failure_cannot_fall_back_to_push_success(self):
        with self.assertRaisesRegex(ValueError, "failure"):
            self.select([self.run_fixture(), self.run_fixture(
                event="workflow_dispatch", run_started_at="2026-10-20T02:00:00Z", conclusion="failure",
            )])

    def test_pr_other_head_branch_or_workflow_cannot_supply_evidence(self):
        for changes in [
            {"event": "pull_request"}, {"head_sha": "b" * 40},
            {"head_branch": "feature"}, {"path": ".github/workflows/other.yml"},
        ]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                self.select([self.run_fixture(**changes)])

    def test_rerun_is_ordered_by_actual_start(self):
        latest = self.run_fixture(id=1, run_attempt=2, run_started_at="2026-10-20T03:00:00Z")
        self.assertEqual(self.select([self.run_fixture(id=2), latest]), latest)


if __name__ == "__main__":
    unittest.main()
