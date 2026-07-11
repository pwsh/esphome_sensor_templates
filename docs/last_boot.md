# Last Boot

Publishes the wall-clock timestamp of the last boot as a timestamp sensor. HA renders it as a relative "last seen"-style time.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** time

## Entities

| Domain | Name |
|---|---|
| `sensor` | Last Boot |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  last_boot: !include
    file: esphome_sensor_templates/templates/diagnostics/last_boot.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  last_boot: github://OWNER/esphome_sensor_templates/templates/diagnostics/last_boot.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- Needs any time: component (e.g. core/time_sntp.yaml). Publishes once after the clock syncs; there is no update_interval (that only applies to type: seconds) and no state_class (device_class timestamp handles it).
