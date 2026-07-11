# RGB Light (3x LEDC PWM)

A common-anode/cathode analog RGB light built from three ESP32 LEDC PWM outputs (one per color channel). Per-output duty caps keep it inside the USB power budget by default.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `light` | RGB Light |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  rgb_light: !include
    file: esphome_sensor_templates/templates/lighting/rgb_light.yaml
    vars: { st_name_prefix: "", st_rgb_pin_r: <value>, st_rgb_pin_g: <value>, st_rgb_pin_b: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  rgb_light: github://OWNER/esphome_sensor_templates/templates/lighting/rgb_light.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_rgb_light_id | `st_rgb_light` | Entity id - MUST be overridden on every extra include (see notes) |
| st_rgb_light_name | `RGB Light` | Entity name (after st_name_prefix) |
| **st_rgb_pin_r** | **(required)** | GPIO driving the RED channel |
| **st_rgb_pin_g** | **(required)** | GPIO driving the GREEN channel |
| **st_rgb_pin_b** | **(required)** | GPIO driving the BLUE channel |
| st_rgb_frequency | `1000Hz` | LEDC PWM frequency for all three channels (ESP-IDF LEDC default is 1kHz) |
| st_rgb_max_power | `0.8` | 0.0-1.0 duty-cycle cap applied to all three outputs - THE power limiter |
| st_rgb_restore_mode | `ALWAYS_OFF` | Boot behaviour (default ALWAYS_OFF to avoid a boot brown-out) One of: `RESTORE_DEFAULT_OFF`, `RESTORE_DEFAULT_ON`, `ALWAYS_OFF`, `ALWAYS_ON`, `RESTORE_INVERTED_DEFAULT_OFF`, `RESTORE_INVERTED_DEFAULT_ON`. |

## Notes

- MULTI-INSTANCE - include this file more than once to get several RGB lights. Each extra include MUST override st_rgb_light_id, st_rgb_light_name AND all three pins; duplicate ids or shared pins are errors. Output ids are derived as ${st_rgb_light_id}_r/_g/_b, so overriding the light id keeps them unique.
- POWER CAP - st_rgb_max_power caps the duty cycle on every channel via the output max_power (0.8 = 80%). With all three channels at full duty a MOSFET-driven RGB strip can pull well past a 500 mA USB budget after only a handful of LEDs (~60 mA/LED at full white). Raise toward 1.0 only with an external supply.
