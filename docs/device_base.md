# Device Identity

The esphome: identity block - device name, friendly_name, comment, project metadata and Home Assistant area. Include this INSTEAD of writing your own esphome: name/friendly_name.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  device_base: !include
    file: esphome_sensor_templates/templates/core/device_base.yaml
    vars: { st_device_name: <value>, st_friendly_name: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  device_base: github://OWNER/esphome_sensor_templates/templates/core/device_base.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_device_name** | **(required)** | Node name / hostname - lowercase letters, digits and hyphens only, <=24 chars (<=31 without a MAC suffix) |
| **st_friendly_name** | **(required)** | Human-friendly display name shown in Home Assistant |
| st_device_comment | `""` | Optional one-line description shown in the ESPHome/HA UI (empty = omitted) |
| st_project_name | `pwsh.esphome_sensor_templates` | Project id in author_name.project_name (namespace.project) format |
| st_project_version | `1.0.0` | Free-form project version string |
| st_area | `""` | Home Assistant area name for this device as a plain string (empty = no area; see note) |
| st_name_add_mac_suffix | `false` | Append the last 3 bytes of the MAC to the name - lets one config serve several physical devices |

## Notes

- This file IS your esphome: block. Include it INSTEAD of writing your own esphome: name/friendly_name. Your top-level config must NOT declare esphome: name - put the board under esp32:, and let the whole identity block come from this package (top-level keys deep-merge, so a second esphome: name would clobber this one).
- project.name MUST be author_name.project_name (namespace.project) - a bare word without a dot fails validation. The version is any string.
- area takes a plain string here. For the structured areas/sub-devices form (esphome: area: {id, name} plus a top-level areas:/devices: list) add that at your top level - it deep-merges with this block.
