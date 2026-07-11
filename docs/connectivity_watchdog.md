# Connectivity Watchdog

Config preset that sets the WiFi reboot_timeout, so the device restarts itself if it cannot stay associated to WiFi. Exposes no entities.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  connectivity_watchdog: !include
    file: esphome_sensor_templates/templates/network/connectivity_watchdog.yaml
    vars: { st_wifi_reboot_timeout: 15min }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  connectivity_watchdog: github://OWNER/esphome_sensor_templates/templates/network/connectivity_watchdog.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_wifi_reboot_timeout | `15min` | How long WiFi may stay disconnected before the device reboots (0s disables the watchdog) |

## Notes

- This is built-in ESPHome behavior - the device restarts if WiFi association is lost for the whole window. This file just makes the knob explicit and overridable.
- Merge caveat - if the user's own wifi: block also sets reboot_timeout, the main config's value wins over this package.
