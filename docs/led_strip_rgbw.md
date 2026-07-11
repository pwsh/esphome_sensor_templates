# Addressable RGBW LED Strip (RMT, SK6812)

An SK6812 RGBW addressable strip driven by the ESP32 RMT peripheral, with a dedicated white channel. Ships a conservative, USB-safe brightness cap and a curated set of addressable effects.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `light` | LED Strip RGBW |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  led_strip_rgbw: !include
    file: esphome_sensor_templates/templates/lighting/led_strip_rgbw.yaml
    vars: { st_name_prefix: "", st_led_strip_rgbw_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  led_strip_rgbw: github://OWNER/esphome_sensor_templates/templates/lighting/led_strip_rgbw.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_led_strip_rgbw_id | `st_led_strip_rgbw` | Entity id - MUST be overridden on every extra include (see notes) |
| st_led_strip_rgbw_name | `LED Strip RGBW` | Entity name (after st_name_prefix) |
| **st_led_strip_rgbw_pin** | **(required)** | Data-line GPIO the strip is wired to |
| st_num_leds_rgbw | `30` | Number of LEDs on the strip |
| st_rgbw_order | `GRB` | Byte order the chipset expects (SK6812 is GRB) One of: `RGB`, `RBG`, `GRB`, `GBR`, `BRG`, `BGR`. |
| st_power_limit_rgbw | `0.5` | 0.0-1.0 per-channel brightness cap applied via color_correct (USB-safe default) |
| st_rgbw_restore_mode | `ALWAYS_OFF` | Boot behaviour (default ALWAYS_OFF to avoid a boot brown-out) One of: `RESTORE_DEFAULT_OFF`, `RESTORE_DEFAULT_ON`, `ALWAYS_OFF`, `ALWAYS_ON`, `RESTORE_INVERTED_DEFAULT_OFF`, `RESTORE_INVERTED_DEFAULT_ON`. |

## Notes

- MULTI-INSTANCE - include this file more than once to get several strips. Each extra include MUST override st_led_strip_rgbw_id, st_led_strip_rgbw_name AND st_led_strip_rgbw_pin; duplicate ids or shared data pins are errors.
- Chipset is fixed to SK6812 (the common RGBW addressable part); is_rgbw:true enables the fourth white channel.
- POWER CAP - each RGB LED draws ~60 mA at full white, and the dedicated white channel adds up to another ~20 mA/LED at full W. A 500 mA USB budget minus ~150 mA for the ESP32 leaves headroom for only ~5-8 LEDs at 100%. st_power_limit_rgbw defaults to 0.5 (color_correct halves all four channels). Raise it toward 1.0 ONLY with an injected power supply.
- color_correct has 4 entries here (R, G, B, W) to match the RGBW pixel.
- Effects are compiled in but cost nothing until activated - addressable effects work fine on RGBW strips.
