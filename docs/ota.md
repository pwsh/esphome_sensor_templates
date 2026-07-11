# OTA Updates

Over-the-air update preset (esphome platform) with a password gate and progress logging hooks.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  ota: !include
    file: esphome_sensor_templates/templates/core/ota.yaml
    vars: { st_ota_password: !secret ota_password }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  ota: github://OWNER/esphome_sensor_templates/templates/core/ota.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_ota_password** | **(required)** | OTA upload password; pass via vars: { st_ota_password: !secret ota_password } |

## Notes

- Presence of ota: also auto-enables safe_mode. Include safe_mode.yaml only to tune its thresholds.
