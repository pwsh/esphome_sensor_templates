# NVS Usage

Reports NVS entry fill (used/total) and the on-device NVS partition size. Diagnoses ESP_ERR_NVS_NOT_ENOUGH_SPACE before it bites.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `text_sensor` | NVS Usage |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  nvs_usage: !include
    file: esphome_sensor_templates/templates/diagnostics/nvs_usage.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  nvs_usage: github://OWNER/esphome_sensor_templates/templates/diagnostics/nvs_usage.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often to poll NVS statistics |
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- OTA never updates the partition table. A device first flashed with an old ESPHome may still run a 20 kB NVS even though current ESPHome allocates 448 kB - only a wired flash replaces the table.
