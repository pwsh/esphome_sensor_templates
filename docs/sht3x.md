# SHT3x Temperature & Humidity

Reads temperature and humidity from a Sensirion SHT30/SHT31/SHT35 (SHT3x-D) over I2C. Shares the library I2C bus.

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
  sht3x: !include
    file: esphome_sensor_templates/templates/environment/sht3x.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  sht3x: github://OWNER/esphome_sensor_templates/templates/environment/sht3x.yaml@main
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
| st_sht3x_i2c_id | `st_i2c_bus` | id of the I2C bus to use (from core/i2c.yaml) |
| st_sht3x_address | `0x44` | I2C address (0x44 ADDR->GND, 0x45 ADDR->VCC; SHT85 is 0x44 only) One of: `0x44`, `0x45`. |

## Notes

- Requires the shared I2C bus - include core/i2c.yaml. The onboard heater is off by default; enable it via !extend (heater_enabled: true) only to clear condensation, as it skews readings.
