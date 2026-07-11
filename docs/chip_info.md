# Chip Info

Reports the SoC model, silicon revision, core count and radio features decoded from esp_chip_info(). One glance confirms exactly which ESP32 variant a build is running on.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `text_sensor` | Chip Model |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  chip_info: !include
    file: esphome_sensor_templates/templates/diagnostics/chip_info.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  chip_info: github://OWNER/esphome_sensor_templates/templates/diagnostics/chip_info.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- Static per boot - update_interval is never and the value is published exactly once from on_boot at priority -100 (after sensors are set up).
- On IDF5 esp_chip_info_t.revision is encoded as major*100+minor, so it is split back into "major.minor" (e.g. 0.4). The features bitmask is decoded to a "/"-joined radio list (WiFi/BT/BLE/802.15.4).
