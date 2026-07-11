# PWM Dimmable Light (LEDC)

A single-channel dimmable LED or single-color strip driven by an ESP32 LEDC PWM output. Duty-cycle cap keeps a MOSFET-driven strip inside the USB power budget by default.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `light` | PWM Light |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  pwm_light: !include
    file: esphome_sensor_templates/templates/lighting/pwm_light.yaml
    vars: { st_name_prefix: "", st_pwm_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  pwm_light: github://OWNER/esphome_sensor_templates/templates/lighting/pwm_light.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_pwm_light_id | `st_pwm_light` | Entity id - MUST be overridden on every extra include (see notes) |
| st_pwm_light_name | `PWM Light` | Entity name (after st_name_prefix) |
| **st_pwm_pin** | **(required)** | GPIO driving the LED/MOSFET gate |
| st_pwm_frequency | `1000Hz` | LEDC PWM frequency (ESP-IDF LEDC default is 1kHz) |
| st_pwm_max_power | `0.8` | 0.0-1.0 duty-cycle cap via the output's max_power - THE power limiter |
| st_pwm_restore_mode | `ALWAYS_OFF` | Boot behaviour (default ALWAYS_OFF to avoid a boot brown-out) One of: `RESTORE_DEFAULT_OFF`, `RESTORE_DEFAULT_ON`, `ALWAYS_OFF`, `ALWAYS_ON`, `RESTORE_INVERTED_DEFAULT_OFF`, `RESTORE_INVERTED_DEFAULT_ON`. |

## Notes

- MULTI-INSTANCE - include this file more than once to get several PWM lights. Each extra include MUST override st_pwm_light_id, st_pwm_light_name AND st_pwm_pin; duplicate ids or shared pins are errors. The LEDC output id is derived as ${st_pwm_light_id}_out, so overriding the light id keeps the output id unique too.
- POWER CAP - st_pwm_max_power caps the LEDC duty cycle via the output max_power (0.8 = 80% of full brightness). For a single onboard LED this is just headroom, but for a MOSFET-driven single-color strip it is the real current limiter: size the cap to your supply. A short WS2812-equivalent single-color run at ~60 mA/LED will exceed a 500 mA USB budget past ~5-8 LEDs at full duty. Raise toward 1.0 only with an external supply.
- LEDC has no per-platform max_power key; max_power is a base float-output option and is the correct place to cap duty.
