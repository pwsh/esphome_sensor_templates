# Device Info

Exposes the debug component's device text sensors - a one-line hardware/firmware summary (chip model, cores, revision, flash size, ESPHome version) and the last reset reason.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `text_sensor` | Device Info |
| `text_sensor` | Reset Reason |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  device_info: !include
    file: esphome_sensor_templates/templates/diagnostics/device_info.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  device_info: github://OWNER/esphome_sensor_templates/templates/diagnostics/device_info.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often the debug hub refreshes the text sensors |
| st_name_prefix | `""` | Prefix prepended to every entity name |
| st_disabled_by_default | `false` | Ship the entities disabled in HA |
| st_internal | `false` | Hide the entities from HA/web entirely |

## Notes

- Prefer this over hand-rolled esp_reset_reason() lambdas - the debug component decodes the reason string for you.
- Shares the debug: hub with the other debug-based templates; dicts merge across packages and the last update_interval wins.
