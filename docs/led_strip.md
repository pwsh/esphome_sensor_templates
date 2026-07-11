# Addressable RGB LED Strip (RMT)

A WS2812-family addressable RGB strip driven by the ESP32 RMT peripheral. Ships a conservative, USB-safe brightness cap and a curated set of addressable effects.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `light` | LED Strip |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  led_strip: !include
    file: esphome_sensor_templates/templates/lighting/led_strip.yaml
    vars: { st_name_prefix: "", st_led_strip_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  led_strip: github://OWNER/esphome_sensor_templates/templates/lighting/led_strip.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_led_strip_id | `st_led_strip` | Entity id - MUST be overridden on every extra include (see notes) |
| st_led_strip_name | `LED Strip` | Entity name (after st_name_prefix) |
| **st_led_strip_pin** | **(required)** | Data-line GPIO the strip is wired to |
| st_num_leds | `30` | Number of LEDs on the strip |
| st_led_chipset | `WS2812` | LED controller chipset One of: `WS2812`, `WS2811`, `SK6812`, `APA106`, `SM16703`. |
| st_rgb_order | `GRB` | Byte order the chipset expects (see notes) One of: `RGB`, `RBG`, `GRB`, `GBR`, `BRG`, `BGR`. |
| st_power_limit | `0.5` | 0.0-1.0 per-channel brightness cap applied via color_correct (USB-safe default) |
| st_light_restore_mode | `ALWAYS_OFF` | Boot behaviour (default ALWAYS_OFF to avoid a boot brown-out) One of: `RESTORE_DEFAULT_OFF`, `RESTORE_DEFAULT_ON`, `ALWAYS_OFF`, `ALWAYS_ON`, `RESTORE_INVERTED_DEFAULT_OFF`, `RESTORE_INVERTED_DEFAULT_ON`. |

## Notes

- MULTI-INSTANCE - include this file more than once to get several strips. Each extra include MUST override st_led_strip_id, st_led_strip_name AND st_led_strip_pin; duplicate ids or shared data pins are errors.
- POWER CAP - a WS2812-class LED draws ~60 mA at full white. A 500 mA USB budget minus ~150 mA for the ESP32 leaves headroom for only ~5-8 LEDs at 100%. st_power_limit defaults to 0.5 (color_correct halves every channel). Raise it toward 1.0 ONLY when the strip has its own injected power supply.
- RGB ORDER - the WS2812/SK6812/APA106 family is GRB; WS2811 strips are commonly RGB. If red and green look swapped, flip st_rgb_order.
- Effects are compiled in but cost nothing until activated from HA - the curated list below is free to keep.
- rmt_symbols / use_dma are optional RMT tuning knobs; the defaults are fine for typical strips on ESP-IDF, so they are omitted here.
