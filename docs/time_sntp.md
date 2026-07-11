# SNTP Time

SNTP time source with configurable server. Provides the time: component other templates (daily_restart, last_boot) require.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  time_sntp: !include
    file: esphome_sensor_templates/templates/core/time_sntp.yaml
    vars: { st_ntp_server: 0.pool.ntp.org }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  time_sntp: github://OWNER/esphome_sensor_templates/templates/core/time_sntp.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_ntp_server | `0.pool.ntp.org` | NTP server to sync against |

## Notes

- Timezone is deliberately NOT set here - ESPHome auto-infers it from the build machine. Override per device with "time: - id: !extend st_time_sntp / timezone: Europe/Berlin".
- Do not include together with time_homeassistant.yaml unless you want two time sources.
