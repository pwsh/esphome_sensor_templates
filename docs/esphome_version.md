# ESPHome Version

Publishes the ESPHome version the firmware was built with via the version text_sensor platform. Handy for spotting devices that missed an OTA.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `text_sensor` | ESPHome Version |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  esphome_version: !include
    file: esphome_sensor_templates/templates/diagnostics/esphome_version.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  esphome_version: github://OWNER/esphome_sensor_templates/templates/diagnostics/esphome_version.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_version_hide_timestamp | `false` | "true" drops the compile timestamp and shows just the version string (C++ literal) |

## Notes

- The value is fixed at compile time, so it only changes on a rebuild/OTA.
