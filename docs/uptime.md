# Uptime (seconds)

Reports device uptime in seconds as a monotonic counter. The canonical "is it still up?" signal for HA availability graphs.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `sensor` | Uptime |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  uptime: !include
    file: esphome_sensor_templates/templates/diagnostics/uptime.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  uptime: github://OWNER/esphome_sensor_templates/templates/diagnostics/uptime.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often to publish the uptime value |
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- This is a counter - state_class is hardcoded total_increasing and does NOT honor the ${st_state_class} knob.
