# Home Assistant API

Native Home Assistant API preset with encryption and a survival-friendly reboot_timeout. Provides the api: component templates like time_homeassistant require.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  api: !include
    file: esphome_sensor_templates/templates/core/api.yaml
    vars: { st_api_reboot_timeout: 0s, st_api_key: !secret api_key }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  api: github://OWNER/esphome_sensor_templates/templates/core/api.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_api_reboot_timeout | `0s` | How long the API may stay disconnected before the device reboots (0s = never) |
| **st_api_key** | **(required)** | Base64 API encryption key; pass via vars: { st_api_key: !secret api_key } |

## Notes

- Never store the key in this file - it is a required var so the user supplies it with their own !secret.
