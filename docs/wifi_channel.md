# WiFi Channel

Reports the primary WiFi channel the device is currently associated on, read directly from the ESP-IDF station driver.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

| Domain | Name |
|---|---|
| `sensor` | WiFi Channel |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  wifi_channel: !include
    file: esphome_sensor_templates/templates/network/wifi_channel.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  wifi_channel: github://OWNER/esphome_sensor_templates/templates/network/wifi_channel.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often to read the current channel |
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- A channel number is not a measurement, so state_class is intentionally omitted (st_state_class does not apply).
- Uses esp_wifi_sta_get_ap_info directly (ESP-IDF). esp_wifi.h is NOT in scope in ESPHome lambdas by default, so this file force-includes it into main.cpp via platformio_options build_src_flags (project sources only - the framework build is untouched).
- Returns NAN (state unknown) when the device is not associated.
