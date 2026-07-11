# Restart Button

Exposes a button in HA/web that soft-reboots the device (equivalent to a normal power cycle, config is re-applied).

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `button` | Restart |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  restart_button: !include
    file: esphome_sensor_templates/templates/controls/restart_button.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  restart_button: github://OWNER/esphome_sensor_templates/templates/controls/restart_button.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- A plain restart re-applies the full config on next boot; use safe_mode_button.yaml instead if a broken config is preventing a normal boot.
