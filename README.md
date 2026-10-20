# Hardware Lab

我独立完成的软硬件项目作品集，收录源码、项目介绍、构建记录和可公开的项目资料。

> **更新日期：2026-10-20。** 当前收录 22 个公开项目。“Actions 成功”链接记录截至本次核验的默认分支提交；后续提交可能使索引落后，定时检查会明确报错。部分项目提供短期 Actions Artifact。

## 项目

### [基于ESP32-S3的视觉猜拳游戏](https://github.com/rongyishuaige7/ESP32_RPS_Game)

基于摄像头手势识别的剪刀石头布硬件游戏，包含 OLED、音频、RGB 反馈与可选 MJPEG 推流。

- **技术栈：** ESP32-S3 · C++ · PlatformIO · OV3660
- **构建证据：** [`3730095b6dda`](https://github.com/rongyishuaige7/ESP32_RPS_Game/commit/3730095b6ddacd8bf00196251ae8aaa334730fbb) · [Actions 成功](https://github.com/rongyishuaige7/ESP32_RPS_Game/actions/runs/29669939600)
- **项目资料：** 原理图资料

### [基于ESP32-S3的多模态交互桌面智能花盆](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot)

多模态桌面智能花盆原型，覆盖环境感知、双泵灌溉、本地彩屏、局域网控制、语音与手势交互。

- **技术栈：** ESP32-S3 · C++ · PlatformIO · FreeRTOS · EasyEDA
- **构建证据：** [`bf0cbe5b75a9`](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/commit/bf0cbe5b75a9a3568b0e1aec9cc7ce97bc196beb) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-multimodal-smart-pot/actions/runs/29669976115)
- **项目资料：** 项目照片、PCB 与制造资料

### [基于STM32的多传感器数据采集系统](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition)

多传感器数据采集教学原型，包含 Flash 历史与离线缓存、ESP-01S AT 联网、TCP JSON 工具、OLED 与告警。

- **技术栈：** STM32F103 · C · PlatformIO · STM32Cube HAL · W25Q64 · ESP-01S
- **构建证据：** [`eaf088e4f160`](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/commit/eaf088e4f16077381ddea2bbdef2bdf65414bf9e) · [Actions 成功](https://github.com/rongyishuaige7/stm32-multisensor-data-acquisition/actions/runs/38683114791)
- **项目资料：** 项目照片

### [基于LoRa和ESP32的仓库物品追踪定位系统](https://github.com/rongyishuaige7/lora-warehouse-tracking-system)

仓库区域追踪教学原型，包含 LoRa 标签/网关固件、Flask/SQLite 服务与 Kotlin Android 客户端。

- **技术栈：** ESP32 · LoRa/SX1278 · C++ · PlatformIO · Flask · SQLite · Kotlin
- **构建证据：** [`c8b005855d89`](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/commit/c8b005855d8952f147024863caa52722e14b148f) · [Actions 成功](https://github.com/rongyishuaige7/lora-warehouse-tracking-system/actions/runs/38683092641)
- **项目资料：** 项目照片与原理图资料

### [基于多路ESP32-CAM的车流量自适应交通信号控制系统](https://github.com/rongyishuaige7/adaptive-traffic-signal-system)

四路 ESP32-CAM 车流量自适应交通信号教学原型，包含 YOLOv8 跟踪/过线计数、FastAPI、Vue 3、WebSocket、12 路信号灯和四块 OLED。

- **技术栈：** ESP32-CAM × 4 · ESP32 · YOLOv8 · FastAPI · Vue 3 · WebSocket
- **构建证据：** [`67168f6ba145`](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/commit/67168f6ba145fb85bb5f4028ed4558df9e0e5f64) · [Actions 成功](https://github.com/rongyishuaige7/adaptive-traffic-signal-system/actions/runs/38682970829)
- **项目资料：** 项目照片、界面截图与 PCB 资料

### [基于ESP32-S3的健康科普语音交互终端](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal)

基于本地唤醒、讯飞流式 ASR/TTS、DeepSeek SSE、双 I²S 音频和 LVGL 显示的健康科普语音终端教学原型。

- **技术栈：** ESP32-S3 · ESP-IDF · ESP-SR · 讯飞 · DeepSeek · LVGL · FreeRTOS
- **构建证据：** [`2c9befc6eaa6`](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/commit/2c9befc6eaa606975902b013bc920b1dbfb908b8) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-health-voice-terminal/actions/runs/38683018748)
- **项目资料：** 项目照片

### [基于树莓派和RFID的房卡管理系统](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system)

双 RC522 房卡管理教学原型，包含树莓派 Python 服务、MariaDB、Qt/C++ 管理端、服务端角色权限、房态与审计记录。

- **技术栈：** Raspberry Pi · Python · Qt/C++ · MariaDB · RC522 · SG90
- **构建证据：** [`7933f839acd0`](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/commit/7933f839acd07e222f6a7987fa8a4591affc272c) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-rfid-room-card-system/actions/runs/38683312415)
- **项目资料：** 项目照片与界面截图

### [基于STM32的触摸与隔空手势控制系统](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system)

使用四路电容触摸和 APDS-9960 隔空手势控制四路 LED，并通过 ESP-01S 本地热点展示状态与诊断的教学原型。

- **技术栈：** STM32F103 · C++ · PlatformIO · STM32Cube HAL · TTP223 · APDS-9960 · ESP-01S
- **构建证据：** [`b317da914a9a`](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/commit/b317da914a9a0a1068e1adbbb7132312af0bfbef) · [Actions 成功](https://github.com/rongyishuaige7/stm32-touch-gesture-control-system/actions/runs/38683131161)
- **项目资料：** 项目照片与原理图资料

### [基于ESP32的智能闹钟系统](https://github.com/rongyishuaige7/esp32-smart-alarm-clock)

基于 ESP32、OLED、DHT11、PIR、MAX98357A 与 Flutter 局域网客户端的智能闹钟教学原型。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · OLED · DHT11 · PIR · MAX98357A
- **构建证据：** [`b24cf2c2b50e`](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/commit/b24cf2c2b50e5a3104f68cf7c36987efdecf190a) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-alarm-clock/actions/runs/38683042497)
- **项目资料：** 项目照片、界面截图与原理图资料

### [基于ESP32的智能药盒系统](https://github.com/rongyishuaige7/esp32-smart-pillbox)

基于 ESP32、双 PIR、双 HX711、RGB/蜂鸣器与 Flutter 局域网客户端的智能药盒教学原型。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · PIR · HX711 · SPIFFS · HTTP
- **构建证据：** [`cd627a429c09`](https://github.com/rongyishuaige7/esp32-smart-pillbox/commit/cd627a429c0976787f18cd8311eb19f49e685b69) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-pillbox/actions/runs/38683070719)
- **项目资料：** 项目照片与原理图资料

### [基于ESP32的天气时钟](https://github.com/rongyishuaige7/esp32-weather-clock)

基于 ESP32、DHT22、BH1750、DS3231、SSD1306 OLED 与本地 AP 配网的天气时钟教学原型。

- **技术栈：** ESP32 · Arduino · PlatformIO · DHT22 · BH1750 · DS3231 · SSD1306 · Wi-Fi
- **构建证据：** [`3bb7e7c8b368`](https://github.com/rongyishuaige7/esp32-weather-clock/commit/3bb7e7c8b368fcc9c4beddba5d8a326ed1b5cff6) · [Actions 成功](https://github.com/rongyishuaige7/esp32-weather-clock/actions/runs/38683083370)
- **项目资料：** 项目照片、原理图与 PCB 资料

### [基于ESP32-S3的多传感器智能安全监测系统](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor)

ESP32-S3 多传感器监测教学原型，包含 MQ-2/MQ-5 原始采样、火焰与超声波输入、OLED、本地状态页和低压执行器分时逻辑。

- **技术栈：** ESP32-S3 · ESP-IDF · PlatformIO · FreeRTOS · MQ-2 · MQ-5 · SSD1306 · HC-SR04
- **构建证据：** [`13699f24e20d`](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/commit/13699f24e20d4d0b089035097ad7b71c69555613) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-smart-safety-monitor/actions/runs/38683032828)
- **项目资料：** 原理图、PCB 与制造资料

### [基于树莓派的多传感器小型气象站](https://github.com/rongyishuaige7/raspberry-pi-weather-station)

树莓派采集 DHT22 温湿度与 BH1750 光照，写入 MySQL，经 Flask REST API 供 Avalonia / C# 上位机查看、查询历史和维护阈值的教学原型。

- **技术栈：** Raspberry Pi · Python · Flask · MySQL · C# · Avalonia · DHT22 · BH1750
- **构建证据：** [`108eb73c0296`](https://github.com/rongyishuaige7/raspberry-pi-weather-station/commit/108eb73c02961bd943bc47e4d48e9fb1c9427b54) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-weather-station/actions/runs/38683323688)
- **项目资料：** 界面与日志截图

### [基于ESP32的婴儿状态监测原型](https://github.com/rongyishuaige7/esp32-baby-monitor)

两路距离、温湿度与声音幅度输入驱动 ESP32 中的演示级固定阈值分类、RGB/蜂鸣器本地反馈和可选可信局域网 JSON 接口。

- **技术栈：** ESP32 · Arduino · PlatformIO · HC-SR04 · DHT11 · 模拟声音输入 · WebServer
- **构建证据：** [`050f45da226d`](https://github.com/rongyishuaige7/esp32-baby-monitor/commit/050f45da226d59f1bb51e6deed0be32f7ce7ece2) · [Actions 成功](https://github.com/rongyishuaige7/esp32-baby-monitor/actions/runs/38683273377)
- **项目资料：** 项目照片与原理图资料

### [基于ESP32的蜂箱多传感器数据采集与局域网展示原型](https://github.com/rongyishuaige7/esp32-beehive-monitor)

ESP32 读取 DHT11、BH1750、BMP280、模拟声音幅度和 MQ-2 原始 ADC；使用者本地配置后，Flutter 客户端可在可信局域网请求一条本地 JSON 响应。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · DHT11 · BH1750 · BMP280 · 模拟 ADC · 本地 HTTP
- **构建证据：** [`da4a4a076d8f`](https://github.com/rongyishuaige7/esp32-beehive-monitor/commit/da4a4a076d8f1a94e6d009189f4f108ccc6ee64f) · [Actions 成功](https://github.com/rongyishuaige7/esp32-beehive-monitor/actions/runs/38683001244)
- **项目资料：** 项目照片、原理图与 PCB 资料

### [基于ESP32的多路智能照明控制系统](https://github.com/rongyishuaige7/esp32-smart-light-controller)

基于 ESP32、四路低压 LED 与可选 BH1750 的本地智能照明教学原型，演示四路手动控制、倒计时与环境亮度触发的四路联动自动逻辑。

- **技术栈：** ESP32 · Arduino · PlatformIO · ESPAsyncWebServer · BH1750 · 低压 LED · 可选本地 HTTP
- **构建证据：** [`961a3f012cc9`](https://github.com/rongyishuaige7/esp32-smart-light-controller/commit/961a3f012cc9aab9f67346282f7c4bc8aad0878a) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-light-controller/actions/runs/38683061055)
- **项目资料：** 固件、BOM 与接线说明

### [基于ESP32的智能化妆品收纳与环境管理系统](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet)

基于 ESP32、DHT11、GUVA-S12SD、PIR、RC522 与 Flutter 的智能化妆品收纳与环境管理教学原型；公开默认不提供 Wi-Fi/HTTP 或实体输出。

- **技术栈：** ESP32 · Arduino · PlatformIO · Flutter · DHT11 · GUVA-S12SD · PIR · RC522 · SSD1306 · WS2812B · 可选本地 HTTP
- **构建证据：** [`f6247c52537b`](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet/commit/f6247c52537b3f4c4ba06e7fa47682923e843bc4) · [Actions 成功](https://github.com/rongyishuaige7/esp32-smart-makeup-cabinet/actions/runs/29670325600)
- **项目资料：** 项目照片与界面截图

### [基于ESP32-C3的多传感器健康数据展示手环原型](https://github.com/rongyishuaige7/esp32-c3-smart-band)

基于 ESP32-C3、MAX30102、MPU6050、DS18B20、GPS、OLED 与 Flutter BLE 客户端的多传感器数据展示教学原型。

- **技术栈：** ESP32-C3 · Arduino · PlatformIO · NimBLE · Flutter · MAX30102 · MPU6050 · DS18B20 · GPS · SSD1306
- **构建证据：** [`4c7683f500e4`](https://github.com/rongyishuaige7/esp32-c3-smart-band/commit/4c7683f500e4262ef49f631e7102a0422f291e4c) · [Actions 成功](https://github.com/rongyishuaige7/esp32-c3-smart-band/actions/runs/29669973669)
- **项目资料：** 项目照片、原理图、PCB 与制造资料

### [基于Arduino的多传感器数据展示与音频联动教学原型](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo)

基于 Arduino Uno、MAX30100、DHT11、DS18B20、BH1750、MPU6050、HC-05、DFPlayer 与 Flutter Android 客户端的多传感器数据展示与音频联动教学原型。

- **技术栈：** Arduino Uno · PlatformIO · Flutter · Android · Classic Bluetooth SPP · HC-05 · MAX30100 · DHT11 · DS18B20 · BH1750 · MPU6050 · DFPlayer Mini
- **构建证据：** [`983560336b73`](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo/commit/983560336b7312cdbac5b0569ac140a407712d50) · [Actions 成功](https://github.com/rongyishuaige7/arduino-multisensor-audio-demo/actions/runs/29669942031)
- **项目资料：** 项目照片

### [基于ESP32-S3和Avalonia的智能农业环境监测系统](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system)

基于 ESP32-S3、DHT11、BH1750、ACD10、BMP280、OLED 与 Avalonia/.NET 8 示例数据界面的环境监测教学原型。

- **技术栈：** ESP32-S3 · Arduino · PlatformIO · Avalonia · .NET 8 · DHT11 · BH1750 · ACD10 · BMP280 · SSD1306
- **构建证据：** [`986900de1487`](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system/commit/986900de1487801f6889b4e269215608803a5623) · [Actions 成功](https://github.com/rongyishuaige7/esp32-s3-smart-agriculture-monitoring-system/actions/runs/29670303834)
- **项目资料：** 项目照片、原理图、PCB 与制造资料

### [基于STM32F103的衣柜环境监测与自动通风控制系统](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system)

基于 STM32F103、DHT11、MQ135 原始 ADC、OLED 与默认关闭风扇输出的衣柜环境监测和通风控制教学原型。

- **技术栈：** STM32F103 · C · PlatformIO · STM32Cube · DHT11 · MQ135 · OLED
- **构建证据：** [`5ebccbd8d879`](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system/commit/5ebccbd8d879ee82576c7e9937539a50283b9af9) · [Actions 成功](https://github.com/rongyishuaige7/stm32f103-wardrobe-environment-monitoring-ventilation-system/actions/runs/29670057922)
- **项目资料：** 项目照片

### [基于树莓派的居家环境与活动状态监测教学原型](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo)

基于树莓派、Flask/MySQL 后端与 Android Compose 查看端的居家环境和活动状态监测教学原型。

- **技术栈：** Raspberry Pi · Python · Flask · Socket.IO · MySQL · Kotlin · Jetpack Compose
- **构建证据：** [`d2991515dd86`](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo/commit/d2991515dd86e63fa69cec0c17fd9023ed341523) · [Actions 成功](https://github.com/rongyishuaige7/raspberry-pi-home-environment-activity-monitoring-demo/actions/runs/29670051197)
- **项目资料：** 项目照片

## 索引维护

[`projects.yml`](projects.yml) 是机器可读索引。CI 会核对公开仓库、默认分支、提交 SHA、固定 Actions 链接与 README 同步。

每 6 小时重新核对跨仓库证据，索引本身没有新提交也会检查。检查失败时保留失败状态，不用旧运行冒充新提交已验证。

```bash
# 先核验每个项目当前 HEAD 在原指定工作流上的最新可信运行，再同步索引和 README。
python3 scripts/refresh_evidence.py --write
python3 scripts/validate_projects.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

刷新只更新提交、运行链接、指定工作流与核验日期，不改变项目材料和真机复测范围。任一项目未知、失败或上传产物范围变化时，不写入本次刷新。

项目的接线、供电、网络和使用注意事项以各项目 README 为准。
