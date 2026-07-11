# Shutdown Button

Exposes a button that shuts the device down into deep sleep with no wake source. Only a physical reset or power cycle brings it back.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `button` | Shutdown |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  shutdown_button: !include
    file: esphome_sensor_templates/templates/controls/shutdown_button.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  shutdown_button: github://OWNER/esphome_sensor_templates/templates/controls/shutdown_button.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- Enters deep sleep with no wake source configured - the device stops responding to WiFi/API/OTA. Only a physical reset button press or power cycle recovers it, so do not press this on a device you cannot reach.
