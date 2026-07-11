# Factory Reset Button

Exposes a button that erases all stored preferences and returns the device to its fresh-flash state. Ships disabled by default because an accidental press is destructive.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `button` | Factory Reset |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  factory_reset_button: !include
    file: esphome_sensor_templates/templates/controls/factory_reset_button.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  factory_reset_button: github://OWNER/esphome_sensor_templates/templates/controls/factory_reset_button.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `true` | Ship the entity disabled in HA (overrides the library default - see note) |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- IRREVERSIBLE. Erases all stored preferences - WiFi credentials, restore_value globals (e.g. boot counter), and improv/captive-portal provisioning - and returns the device to a fresh-flash state. It will not reconnect until re-provisioned.
- Ships disabled_by_default: true (unlike the rest of the library) so an accidental tap cannot wipe the device; the user must deliberately enable it in HA.
