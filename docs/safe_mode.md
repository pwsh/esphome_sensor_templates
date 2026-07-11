# Safe Mode

Tunes the boot-loop recovery safe_mode: after repeated crash-boots the device stops applying its config so an OTA fix can land.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  safe_mode: !include
    file: esphome_sensor_templates/templates/core/safe_mode.yaml
    vars: { st_safe_mode_attempts: 10 }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  safe_mode: github://OWNER/esphome_sensor_templates/templates/core/safe_mode.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_safe_mode_attempts | `10` | Consecutive failed boots before entering safe mode |
| st_safe_mode_reboot_timeout | `5min` | How long to wait in safe mode for an OTA before rebooting to retry |
| st_safe_mode_boot_good_after | `1min` | Uptime after which a boot counts as successful and the attempt counter resets |

## Notes

- Required by the safe_mode button/switch platforms. safe_mode is auto-enabled anyway whenever ota: is present - this preset just tunes its thresholds.
