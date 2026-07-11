# Passive Piezo Buzzer (RTTTL)

A passive piezo buzzer driven by an ESP32 LEDC PWM output through the rtttl tone generator, with a demo test button. rtttl.play is callable from automations or Home Assistant.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `button` | Buzzer Test |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  buzzer_rtttl: !include
    file: esphome_sensor_templates/templates/audio/buzzer_rtttl.yaml
    vars: { st_name_prefix: "", st_buzzer_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  buzzer_rtttl: github://OWNER/esphome_sensor_templates/templates/audio/buzzer_rtttl.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_buzzer_id | `st_buzzer` | rtttl component id - MUST be overridden on every extra include (see notes) |
| st_buzzer_name | `Buzzer` | Base name used for the test button ("<prefix><name> Test") |
| **st_buzzer_pin** | **(required)** | GPIO driving the passive buzzer |
| st_buzzer_gain | `50%` | rtttl output gain / volume (0%-100%) |
| st_buzzer_test_tune | `two_short:d=4,o=5,b=100:16e6,16e6` | RTTTL string played by the test button |

## Notes

- PASSIVE buzzers only. A passive piezo needs a PWM tone signal (this template). An ACTIVE buzzer has its own oscillator and just needs a plain GPIO on/off - use a switch/output template for those, not this file.
- MULTI-INSTANCE - include this file more than once for several buzzers. Each extra include MUST override st_buzzer_id AND st_buzzer_pin (duplicate ids or shared pins are errors). The LEDC output id (${st_buzzer_id}_out) and test button id (${st_buzzer_id}_test) derive from st_buzzer_id, so overriding it keeps them unique too.
- rtttl.play (id ${st_buzzer_id}) is callable from any automation or from Home Assistant to play arbitrary RTTTL ringtones, not just the demo tune.
