# Daily Scheduled Restart

Reboots the device once a day at a configurable hour by attaching a schedule to an existing time component.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** time

## Entities

| Domain | Name |
|---|---|
| `button` | Daily Restart (always internal) |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  daily_restart: !include
    file: esphome_sensor_templates/templates/controls/daily_restart.yaml
    vars: { st_restart_hour: 4 }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  daily_restart: github://OWNER/esphome_sensor_templates/templates/controls/daily_restart.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_restart_hour | `4` | Hour of day (0-23, local time) at which to restart |
| st_daily_restart_time_id | `st_time_sntp` | id of the time component to attach the schedule to (st_time_ha for the HA time preset) |

## Notes

- Needs a time: component. Include core/time_sntp.yaml (default) or core/time_homeassistant.yaml (then pass st_daily_restart_time_id: st_time_ha). ESPHome allows only one SNTP instance, so this file deliberately does NOT ship its own clock - it attaches to yours via !extend.
- time.on_time does not reschedule across DST jumps - an event in the 01:00-02:00 window may be skipped or fire twice on the changeover day. Keeping the default 03:00-04:00 window is safe in most zones.
