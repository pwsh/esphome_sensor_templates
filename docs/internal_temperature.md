# Internal Temperature

Reads the on-die temperature sensor and derives a coupled overtemperature warning binary sensor that trips above a configurable threshold.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `sensor` | Internal Temperature |
| `binary_sensor` | Overtemperature |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  internal_temperature: !include
    file: esphome_sensor_templates/templates/diagnostics/internal_temperature.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  internal_temperature: github://OWNER/esphome_sensor_templates/templates/diagnostics/internal_temperature.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often to sample the die temperature |
| st_name_prefix | `""` | Prefix prepended to every entity name |
| st_disabled_by_default | `false` | Ship the entities disabled in HA |
| st_internal | `false` | Hide the entities from HA/web entirely |
| st_state_class | `measurement` | state_class for the temperature sensor; set "" to opt out of HA long-term statistics |
| st_overtemp_threshold | `80` | Warning trips above this many degC (numeric, substituted into C++) |

## Notes

- Some ESP32 variants report bogus values (e.g. a stuck 53.3 degC / raw 128). The internal_temperature component discards invalid readings, and the warning lambda ignores NaN.
