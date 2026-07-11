# RGBW Light (4x LEDC PWM)

An analog RGBW light built from four ESP32 LEDC PWM outputs (R, G, B and a dedicated white channel). Per-output duty caps plus color interlock keep it inside the USB power budget by default.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `light` | RGBW Light |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  rgbw_light: !include
    file: esphome_sensor_templates/templates/lighting/rgbw_light.yaml
    vars: { st_name_prefix: "", st_rgbw_pin_r: <value>, st_rgbw_pin_g: <value>, st_rgbw_pin_b: <value>, st_rgbw_pin_w: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  rgbw_light: github://OWNER/esphome_sensor_templates/templates/lighting/rgbw_light.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_rgbw_light_id | `st_rgbw_light` | Entity id - MUST be overridden on every extra include (see notes) |
| st_rgbw_light_name | `RGBW Light` | Entity name (after st_name_prefix) |
| **st_rgbw_pin_r** | **(required)** | GPIO driving the RED channel |
| **st_rgbw_pin_g** | **(required)** | GPIO driving the GREEN channel |
| **st_rgbw_pin_b** | **(required)** | GPIO driving the BLUE channel |
| **st_rgbw_pin_w** | **(required)** | GPIO driving the WHITE channel |
| st_rgbw_frequency | `1000Hz` | LEDC PWM frequency for all four channels (ESP-IDF LEDC default is 1kHz) |
| st_rgbw_max_power | `0.8` | 0.0-1.0 duty-cycle cap applied to all four outputs - THE power limiter |
| st_rgbw_color_interlock | `true` | Prevent RGB and W being on at once (halves worst-case current) - C++ literal "true"/"false" |
| st_rgbw_restore_mode | `ALWAYS_OFF` | Boot behaviour (default ALWAYS_OFF to avoid a boot brown-out) One of: `RESTORE_DEFAULT_OFF`, `RESTORE_DEFAULT_ON`, `ALWAYS_OFF`, `ALWAYS_ON`, `RESTORE_INVERTED_DEFAULT_OFF`, `RESTORE_INVERTED_DEFAULT_ON`. |

## Notes

- MULTI-INSTANCE - include this file more than once to get several RGBW lights. Each extra include MUST override st_rgbw_light_id, st_rgbw_light_name AND all four pins; duplicate ids or shared pins are errors. Output ids are derived as ${st_rgbw_light_id}_r/_g/_b/_w, so overriding the light id keeps them unique.
- POWER CAP - st_rgbw_max_power caps the duty cycle on every channel via the output max_power (0.8 = 80%). st_rgbw_color_interlock defaults to true: it forbids the RGB and white channels being lit simultaneously, roughly halving the worst-case current draw - an important part of the USB power story. Raise the cap toward 1.0 only with an external supply.
- ESPHome's own default for color_interlock is false; this template flips it to true on purpose for power safety. Set it back to "false" if you want RGB+W mixing and have the supply for it.
