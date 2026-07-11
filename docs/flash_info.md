# Flash Size

Reports the physical SPI flash size in MiB, read from the flash chip at runtime via esp_flash_get_size(). Confirms whether a board really carries the 4/8/16 MiB it was sold as.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `sensor` | Flash Size |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  flash_info: !include
    file: esphome_sensor_templates/templates/diagnostics/flash_info.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  flash_info: github://OWNER/esphome_sensor_templates/templates/diagnostics/flash_info.yaml@main
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
- No state_class is set - a fixed hardware size is not a measurement and needs no HA long-term statistics, so it deliberately does NOT honor the ${st_state_class} knob.
- Flash SPEED and mode are compile-time board settings and are not exposed at runtime; the debug component's device_info text sensor shows them in its summary string.
