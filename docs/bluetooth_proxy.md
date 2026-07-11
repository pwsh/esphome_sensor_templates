# Bluetooth Proxy

Turns the device into a Home Assistant Bluetooth proxy, forwarding nearby BLE advertisements (and optionally active GATT connections) to HA over the native API.

**Platforms:** `esp32` `esp32s3` `esp32c3` `esp32c6`

**Requires:** api

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  bluetooth_proxy: !include
    file: esphome_sensor_templates/templates/bluetooth/bluetooth_proxy.yaml
    vars: { st_bt_proxy_active: true }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  bluetooth_proxy: github://OWNER/esphome_sensor_templates/templates/bluetooth/bluetooth_proxy.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_bt_proxy_active | `true` | C++ literal "true"/"false" - true allows HA to open active GATT connections through this proxy; false is advertisement-only (passive) |
| st_bt_proxy_connection_slots | `3` | Max simultaneous active BLE connections (1-9; keep <=5 for stability/memory) |

## Notes

- This file does NOT declare esp32_ble_tracker - bluetooth_proxy AUTO-LOADS the BLE tracker for you, so the scanner is enabled automatically with default scan parameters.
- SAFE to also include bluetooth/ble_tracker.yaml if you want to tune scan parameters - the auto-loaded tracker and the explicit esp32_ble_tracker block merge cleanly (verified: no duplicate-component error). Include ble_tracker.yaml only when you need to change interval/window/duration/active.
- Active connections are limited (default 3, hard max 9); each open GATT connection uses RAM, so keep the count low.
- NOT available on ESP32-S2 (no Bluetooth radio). Requires the native API (api:) enabled and the device adopted into Home Assistant.
