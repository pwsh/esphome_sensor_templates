# PSRAM

Enables external PSRAM (SPI RAM) so buffer-heavy components (camera, audio, large displays) and the psram_free diagnostic have memory to work with.

**Platforms:** `esp32` `esp32s2` `esp32s3`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  psram: !include
    file: esphome_sensor_templates/templates/core/psram.yaml
    vars: { st_psram_mode: quad }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  psram: github://OWNER/esphome_sensor_templates/templates/core/psram.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_psram_mode | `quad` | PSRAM bus mode - quad for classic ESP32/WROVER and quad-PSRAM S3 boards, octal for S3 -N8R8/-N16R8 style boards One of: `quad`, `octal`. |
| st_psram_speed | `80MHz` | PSRAM clock speed (120MHz needs octal mode and an experimental IDF flag on some versions - 80MHz is the safe default) One of: `40MHz`, `80MHz`, `120MHz`. |

## Notes

- The mode MUST match the actual chip - octal mode on a quad-PSRAM board (or vice versa) fails to initialize at runtime, not at compile time. Check your board's suffix: S3 -N8R8/-N16R8 = octal, -N8R2/WROVER = quad.
- ESP32-C3/C6 have no PSRAM interface. On octal-PSRAM S3 boards GPIO35-37 are claimed by the PSRAM bus and unavailable for I/O.
