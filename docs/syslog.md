# Syslog

Forwards ESPHome logs to a remote syslog server over UDP using the official syslog component. Useful for centralised log collection when a device is not attached to a serial console.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi, time

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  syslog: !include
    file: esphome_sensor_templates/templates/core/syslog.yaml
    vars: { st_syslog_host: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  syslog: github://OWNER/esphome_sensor_templates/templates/core/syslog.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_syslog_host** | **(required)** | Syslog server hostname or IP to send log packets to |
| st_syslog_port | `514` | Destination UDP port on the syslog server (standard syslog = 514) |
| st_syslog_level | `DEBUG` | Highest log level to forward to the server One of: `NONE`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `VERBOSE`, `VERY_VERBOSE`. |
| st_syslog_facility | `16` | Syslog facility number (16 = local0, the usual choice for app logs) |
| st_syslog_strip | `true` | Strip ANSI color codes from forwarded messages (most syslog servers can't render them) |
| st_syslog_time_id | `st_time_sntp` | id of the time component used to timestamp messages (st_time_ha for the HA time preset) |

## Notes

- This is the OFFICIAL ESPHome syslog component (https://esphome.io/components/syslog/) - it is in mainline ESPHome, works on ESP-IDF, and pulls NO third-party code. (The older third-party github.com/TheStaticTurtle/esphome_syslog was archived Oct 2025 and is arduino-only, so it is deliberately not used here.)
- Needs a time: component. Include core/time_sntp.yaml (default) or core/time_homeassistant.yaml (then pass st_syslog_time_id: st_time_ha). It also declares its own udp: client (id st_syslog_udp) pointed at the server address.
- Transport is plain UDP with no encryption or delivery guarantee - logs travel in cleartext on your LAN and packets can be dropped. Keep it to a trusted network.
