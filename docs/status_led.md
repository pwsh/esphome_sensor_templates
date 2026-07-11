# Status LED

Drives an on-board LED as a firmware status indicator - slow blink on warnings (WiFi/API down), fast blink on errors.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  status_led: !include
    file: esphome_sensor_templates/templates/controls/status_led.yaml
    vars: { st_status_led_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  status_led: github://OWNER/esphome_sensor_templates/templates/controls/status_led.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_status_led_pin** | **(required)** | GPIO the status LED is wired to (e.g. GPIO8) |
| st_status_led_inverted | `false` | C++ literal "true"/"false" - set "true" for active-low LEDs (many on-board LEDs) |

## Notes

- Blink semantics are fixed by ESPHome and cannot be customized - slow blink = warning (wifi/api down), fast blink = error. There is no HA entity; the LED reflects internal firmware state only.
- The pin is claimed exclusively by status_led and is otherwise unusable for other outputs.
