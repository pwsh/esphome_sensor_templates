# Boot Color (Power-On Color Choice)

Turns a light from this library on at a chosen color and brightness every time the device boots. Give any RGB(W) or addressable strip a fixed power-on look instead of coming up dark.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  boot_color: !include
    file: esphome_sensor_templates/templates/lighting/boot_color.yaml
    vars: { st_boot_color_light_id: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  boot_color: github://OWNER/esphome_sensor_templates/templates/lighting/boot_color.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_boot_color_light_id** | **(required)** | id of the light to turn on at boot - one of st_led_strip, st_rgb_light, st_rgbw_light, st_led_strip_rgbw (or your own override of one of those id vars) |
| st_boot_color_r | `100%` | RED channel level, percent |
| st_boot_color_g | `100%` | GREEN channel level, percent |
| st_boot_color_b | `100%` | BLUE channel level, percent |
| st_boot_color_brightness | `60%` | Overall brightness of the boot color, percent |

## Notes

- PAIR THIS with one of the lighting templates - it declares no light of its own, it only drives one. Point st_boot_color_light_id at that template's light id: st_led_strip (led_strip), st_led_strip_rgbw (led_strip_rgbw), st_rgb_light (rgb_light), st_rgbw_light (rgbw_light). If you overrode the light-id var on that include, use the id you chose.
- BOOT PRIORITY 600 is deliberate. ESPHome sets components up in DESCENDING setup-priority order, and an on_boot entry is itself scheduled at its priority - so a lower number runs LATER. The light output components sit at HARDWARE (800) and light::LightState at HARDWARE-1 (799), while WiFi is at 250 and the API/MQTT at 200. Priority 600 therefore lands after every light component is fully set up but well before any network stack, so the color appears immediately at power-up and does NOT wait for (or depend on) WiFi. Priority 800 would be wrong: it can run before LightState::setup() and the restore_mode write would then clobber the color.
- THIS INTENTIONALLY TURNS THE LIGHT ON at every power-up. It deliberately overrides the outcome of the paired template's restore_mode (ALWAYS_OFF by default) - restore_mode still runs first at 799, then this action turns the light on at 600. If you want a dark boot, do not include this file.
- BROWN-OUT / USB CAUTION - a light coming on the instant the device boots draws its current while the regulator is still stabilising, which is exactly the situation restore_mode ALWAYS_OFF exists to avoid. st_boot_color_brightness defaults to a modest 60% for that reason, and it stacks with the paired template's own power cap (color_correct / max_power). On a board powered from USB with a long strip, lower it further rather than raising it; only push toward 100% with an injected external supply.
- WHITE-CHANNEL LIGHTS only get the RGB target here - there is no white/cold_white/warm_white key in this action. On rgbw_light with st_rgbw_color_interlock at its default "true", asking for an RGB color means the W channel is forced OFF, so the boot color is pure RGB. Set that var to "false" (and accept the higher current) if you want W mixed in. On led_strip_rgbw (SK6812) the dedicated W pixel channel likewise stays dark.
- NO ids ARE DECLARED in this file, so including it twice is safe: point each include at a different light via vars: { st_boot_color_light_id: ... } and you get two independent boot colors. The on_boot lists concatenate across packages.
- No shared knobs and no st_update_interval - this file exposes no entity and polls nothing.
