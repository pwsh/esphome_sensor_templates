# AHT20 Temperature & Humidity

Reads temperature and humidity from an Aosong AHT10/AHT20/AHT30 over I2C. Shares the library I2C bus.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** i2c

## Entities

| Domain | Name |
|---|---|
| `sensor` | Temperature |
| `sensor` | Humidity |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  aht20: !include
    file: esphome_sensor_templates/templates/environment/aht20.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  aht20: github://OWNER/esphome_sensor_templates/templates/environment/aht20.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often to sample the sensor |
| st_name_prefix | `""` | Prefix prepended to every entity name |
| st_disabled_by_default | `false` | Ship the entities disabled in HA |
| st_internal | `false` | Hide the entities from HA/web entirely |
| st_state_class | `measurement` | state_class for both readings; set "" to opt out of HA long-term statistics |
| st_aht20_i2c_id | `st_i2c_bus` | id of the I2C bus to use (from core/i2c.yaml) |
| st_aht20_variant | `AHT20` | Chip variant - use AHT20 for AHT20 and AHT30 modules One of: `AHT10`, `AHT20`. |

## Notes

- Requires the shared I2C bus - include core/i2c.yaml. The AHT10/20/30 all share the fixed I2C address 0x38.
- If an AHT10-labelled module fails to read, switch st_aht20_variant to AHT20 (some clones need it).
