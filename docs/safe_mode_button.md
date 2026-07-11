# Safe Mode Button

Exposes a button that reboots the device into safe mode, where only network/logging/OTA run so a broken config can be re-flashed.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `button` | Restart (Safe Mode) |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  safe_mode_button: !include
    file: esphome_sensor_templates/templates/controls/safe_mode_button.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  safe_mode_button: github://OWNER/esphome_sensor_templates/templates/controls/safe_mode_button.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- Safe-mode boot brings up only network, logging and OTA - the rest of your config is skipped - so a config that crashes on boot can still be re-flashed over the air.
