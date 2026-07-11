# ESPHome Sensor Templates

Reusable, standalone ESPHome template files for ESP32-family devices (ESP-IDF framework).
Each template is a self-contained [package](https://esphome.io/components/packages/): include one
file, get a working, documented sensor with sensible defaults — customize per sensor via
`vars:` or globally via top-level `substitutions:`.

**Minimum ESPHome version: 2026.5.0.** Target platforms: ESP32, ESP32-S2, ESP32-S3, ESP32-C3, ESP32-C6.

## Quick start

```yaml
packages:
  uptime: !include esphome_sensor_templates/templates/diagnostics/uptime.yaml
  wifi_signal: !include
    file: esphome_sensor_templates/templates/network/wifi_signal.yaml
    vars: { st_update_interval: 5min }

substitutions:
  st_update_interval: 120s   # global default for every included template
```

Or use the point-and-click builder: open `web/index.html` in a browser, pick sensors, copy the
generated YAML.

## Global knobs

Set any of these once in your top-level `substitutions:` to affect every included template
(per-include `vars:` still win):

| Substitution | Default | Effect |
|---|---|---|
| `st_update_interval` | `60s` | refresh period of polled sensors |
| `st_state_class` | `measurement` | set to `""` to stop Home Assistant long-term statistics |
| `st_name_prefix` | `""` | prefix on every entity name |
| `st_disabled_by_default` | `false` | ship entities disabled in HA |
| `st_internal` | `false` | hide entities from HA entirely |

<!-- BEGIN GENERATED INDEX -->

### Core

| Template | Description | Entities |
|---|---|---|
| [Home Assistant API](docs/api.md) | Native Home Assistant API preset with encryption and a survival-friendly reboot_timeout. Provides the api: component templates like time_homeassistant require. | preset |
| [Logger](docs/logger.md) | Logger preset with configurable level and UART baud rate. | preset |
| [OTA Updates](docs/ota.md) | Over-the-air update preset (esphome platform) with a password gate and progress logging hooks. | preset |
| [Safe Mode](docs/safe_mode.md) | Tunes the boot-loop recovery safe_mode: after repeated crash-boots the device stops applying its config so an OTA fix can land. | preset |
| [Home Assistant Time](docs/time_homeassistant.md) | Time source synced from Home Assistant. Provides the time: component other templates (daily_restart, last_boot) require. | preset |
| [SNTP Time](docs/time_sntp.md) | SNTP time source with configurable server. Provides the time: component other templates (daily_restart, last_boot) require. | preset |
| [Web Server](docs/web_server.md) | Built-in web UI (v3) with HTTP basic auth and a boot-time gate that can disable auth without editing the config. Keeps the device usable standalone when Home Assistant is down. | preset |

### Diagnostics

| Template | Description | Entities |
|---|---|---|
| [Boot Counter](docs/boot_counter.md) | Counts device boots in an NVS-backed global and publishes the running total. Rising counts between expected reboots point at brown-outs, watchdog resets, or crashes. | 1 |
| [CPU Frequency](docs/cpu_frequency.md) | Reports the current CPU clock from the debug component. Useful for confirming power-save/DFS behaviour or a mis-set framework clock. | 1 |
| [Device Info](docs/device_info.md) | Exposes the debug component's device text sensors - a one-line hardware/firmware summary (chip model, cores, revision, flash size, ESPHome version) and the last reset reason. | 2 |
| [ESPHome Version](docs/esphome_version.md) | Publishes the ESPHome version the firmware was built with via the version text_sensor platform. Handy for spotting devices that missed an OTA. | 1 |
| [Heap Diagnostics](docs/heap.md) | Reports internal heap health from the debug component - free bytes, largest allocatable block, historical minimum free, and fragmentation percent. The first thing to check when a device reboots under memory pressure. | 4 |
| [Internal Temperature](docs/internal_temperature.md) | Reads the on-die temperature sensor and derives a coupled overtemperature warning binary sensor that trips above a configurable threshold. | 2 |
| [Last Boot](docs/last_boot.md) | Publishes the wall-clock timestamp of the last boot as a timestamp sensor. HA renders it as a relative "last seen"-style time. | 1 |
| [Loop Time](docs/loop_time.md) | Reports the main-loop iteration time from the debug component, in milliseconds. Spikes reveal a component that blocks the loop (slow I2C, long lambdas). | 1 |
| [NVS Usage](docs/nvs_usage.md) | Reports NVS entry fill (used/total) and the on-device NVS partition size. Diagnoses ESP_ERR_NVS_NOT_ENOUGH_SPACE before it bites. | 1 |
| [PSRAM Free](docs/psram.md) | Reports free PSRAM (SPI RAM) in bytes from the debug component. Confirms that external PSRAM is detected and tracks headroom for buffer-heavy components. | 1 |
| [Uptime (seconds)](docs/uptime.md) | Reports device uptime in seconds as a monotonic counter. The canonical "is it still up?" signal for HA availability graphs. | 1 |
| [Uptime (human-readable)](docs/uptime_text.md) | Reports device uptime as a human-readable string (e.g. "3d 4h 12m 5s") using the uptime platform's built-in formatting. Nicer to read on a dashboard than raw seconds. | 1 |

### Network

| Template | Description | Entities |
|---|---|---|
| [Connectivity Watchdog](docs/connectivity_watchdog.md) | Config preset that sets the WiFi reboot_timeout, so the device restarts itself if it cannot stay associated to WiFi. Exposes no entities. | preset |
| [Home Assistant Connected](docs/ha_status.md) | Binary sensor that reports whether the device currently has a live connection to Home Assistant (native API or MQTT). | 1 |
| [WiFi Channel](docs/wifi_channel.md) | Reports the primary WiFi channel the device is currently associated on, read directly from the ESP-IDF station driver. | 1 |
| [WiFi Disconnect Counter](docs/wifi_disconnect_counter.md) | Counts WiFi disconnect events since boot and exposes the running total as a sensor. | 1 |
| [WiFi Info](docs/wifi_info.md) | Exposes the device's current WiFi/network identity - IP address, SSID, BSSID, MAC address and DNS - as text sensors. | 5 |
| [WiFi Quality (plain language)](docs/wifi_quality.md) | Translates RSSI into a plain-language rating (Excellent/Good/Fair/Poor/Very Poor). Carries its own internal RSSI source, so it works standalone. | 1 |
| [WiFi Signal Strength](docs/wifi_signal.md) | Reports WiFi RSSI in dBm and a derived signal-quality percentage. The two entities are coupled - the % is a copy of the dBm reading. | 2 |

### Controls

| Template | Description | Entities |
|---|---|---|
| [Daily Scheduled Restart](docs/daily_restart.md) | Reboots the device once a day at a configurable hour by attaching a schedule to an existing time component. | 1 |
| [Factory Reset Button](docs/factory_reset_button.md) | Exposes a button that erases all stored preferences and returns the device to its fresh-flash state. Ships disabled by default because an accidental press is destructive. | 1 |
| [Restart Button](docs/restart_button.md) | Exposes a button in HA/web that soft-reboots the device (equivalent to a normal power cycle, config is re-applied). | 1 |
| [Safe Mode Button](docs/safe_mode_button.md) | Exposes a button that reboots the device into safe mode, where only network/logging/OTA run so a broken config can be re-flashed. | 1 |
| [Shutdown Button](docs/shutdown_button.md) | Exposes a button that shuts the device down into deep sleep with no wake source. Only a physical reset or power cycle brings it back. | 1 |
| [Status LED](docs/status_led.md) | Drives an on-board LED as a firmware status indicator - slow blink on warnings (WiFi/API down), fast blink on errors. | preset |

### Inputs

| Template | Description | Entities |
|---|---|---|
| [HA-Controlled Deep Sleep](docs/deep_sleep_control.md) | The classic Home Assistant-controlled deep sleep pattern. The device sleeps between runs but honors an HA input_boolean that can hold it awake for OTA/config. | preset |
| [Generic Number Input](docs/generic_number.md) | A user-adjustable template number, surfaced in HA as a config control. Use it for thresholds, calibration offsets, setpoints - read the value elsewhere via id(...).state. | 1 |
| [Generic Select Input](docs/generic_select.md) | A user-adjustable template select (dropdown), surfaced in HA as a config control. Use it to pick a mode/profile and read the choice elsewhere via id(...).state. | 1 |
| [Generic Switch (virtual flag)](docs/generic_switch.md) | A virtual template switch, surfaced in HA as a config control. Use it as an on/off flag to gate automations - read it via id(...).state or attach actions with !extend. | 1 |
| [Generic Text Input](docs/generic_text.md) | A user-editable template text field, surfaced in HA as a config control. Use it for free-form notes, labels, or short config strings - read it via id(...).state. | 1 |

<!-- END GENERATED INDEX -->

## Development

- Authoring rules: [CONVENTIONS.md](CONVENTIONS.md)
- Regenerate catalog/docs/README index: `python3 tools/build_catalog.py`
- Validate everything: `tools/validate.sh`
