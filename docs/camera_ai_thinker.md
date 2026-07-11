# ESP32-CAM Camera (AI-Thinker)

esp32_camera preset with the AI-Thinker ESP32-CAM pinout hardcoded. Exposes the onboard OV2640 camera in Home Assistant. Pins are board-specific to the classic AI-Thinker module.

**Platforms:** `esp32`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `camera` | Camera |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  camera_ai_thinker: !include
    file: esphome_sensor_templates/templates/peripherals/camera_ai_thinker.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  camera_ai_thinker: github://OWNER/esphome_sensor_templates/templates/peripherals/camera_ai_thinker.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_camera_name | `Camera` | Camera entity name (after st_name_prefix) |
| st_camera_resolution | `800x600` | Capture resolution (higher = more RAM/slower) One of: `320x240`, `640x480`, `800x600`, `1024x768`, `1280x1024`, `1600x1200`. |
| st_camera_jpeg_quality | `10` | JPEG quality, 6 (best) to 63 (worst); lower is higher quality and larger frames |
| st_camera_vertical_flip | `false` | Flip the image vertically |
| st_camera_horizontal_mirror | `false` | Mirror the image horizontally |

## Notes

- THIS IS THE AI-THINKER PIN MAP ONLY - it is copied from the ESPHome esp32_camera AI-Thinker example and is specific to the classic AI-Thinker ESP32-CAM. Other camera boards (M5, TTGO, ESP32-S3-EYE) use different pins; override the whole pin map via !extend.
- esp32 (classic) ONLY - the AI-Thinker board is a WROOM/WROVER classic ESP32. The pin map (and this @platforms line) do not apply to S2/S3/C3/C6 boards.
- The camera uses substantial RAM for frame buffers - PSRAM is strongly recommended (the AI-Thinker uses a WROVER module with PSRAM). Add a "psram:" block; without PSRAM you are limited to small resolutions and low quality.
- This template hardcodes its own i2c bus (SCCB) on GPIO26/27 with scan:false - it is the camera's dedicated control bus, not the shared core/i2c.yaml bus.
- On the AI-Thinker board GPIO0 (external clock) is also the boot/flash-mode strap and GPIO16 is wired to PSRAM - do not repurpose them.
