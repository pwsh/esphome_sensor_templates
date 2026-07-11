# Logger

Logger preset with configurable level and UART baud rate.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  logger: !include
    file: esphome_sensor_templates/templates/core/logger.yaml
    vars: { st_log_level: INFO }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  logger: github://OWNER/esphome_sensor_templates/templates/core/logger.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_log_level | `INFO` | Log verbosity (NONE, ERROR, WARN, INFO, DEBUG, VERBOSE, VERY_VERBOSE) |
| st_log_baud_rate | `115200` | UART baud rate; set 0 to disable UART (serial) logging entirely |

## Notes

- Since ESPHome 2026.4.0 state-change messages are logged at VERBOSE, so INFO/DEBUG stays cheap - the noisy per-state spam no longer floods those levels.
