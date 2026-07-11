# ESP32 BLE Tracker

Enables the ESP32 Bluetooth Low Energy scanner so ble_presence / ble_rssi and related BLE platforms can see nearby devices. Sets sensible scan parameters.

**Platforms:** `esp32` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  ble_tracker: !include
    file: esphome_sensor_templates/templates/bluetooth/ble_tracker.yaml
    vars: { st_ble_scan_interval: 320ms }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  ble_tracker: github://OWNER/esphome_sensor_templates/templates/bluetooth/ble_tracker.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_ble_scan_interval | `320ms` | Time between the start of consecutive scan windows |
| st_ble_scan_window | `30ms` | How long the radio actively listens within each interval (must be <= interval) |
| st_ble_scan_duration | `5min` | How long a scan runs before the stack restarts it (clears the found-devices cache) |
| st_ble_active | `true` | C++ literal "true"/"false" - true sends scan requests to also collect scan-response (active scan); false is passive/lower-power |

## Notes

- NOT available on ESP32-S2 - that chip has no Bluetooth radio at all. Works on esp32, esp32s3, esp32c3 and esp32c6.
- The BLE stack costs a significant chunk of RAM and flash - expect a noticeable heap drop after enabling it. It is frequently paired with bluetooth_proxy.yaml (which depends on this scanner).
- On single-core chips (ESP32-C3) both WiFi and the BLE tracker share one core; enable software_coexistence manually if you see WiFi/BLE contention.
