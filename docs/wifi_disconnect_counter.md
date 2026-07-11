# WiFi Disconnect Counter

Counts WiFi disconnect events since boot and exposes the running total as a sensor.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

| Domain | Name |
|---|---|
| `sensor` | WiFi Disconnects |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  wifi_disconnect_counter: !include
    file: esphome_sensor_templates/templates/network/wifi_disconnect_counter.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  wifi_disconnect_counter: github://OWNER/esphome_sensor_templates/templates/network/wifi_disconnect_counter.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often to publish the current disconnect count |
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- state_class is hardcoded total_increasing (a counter), so st_state_class does not apply here.
- This file's wifi: block merges into the user's wifi config - on_disconnect lists concatenate, so the user's own on_disconnect still runs.
- Counts since boot; restore_value is false to avoid NVS wear. For a lifetime count across reboots, `!extend st_wifi_disconnects_value` and set restore_value: true.
