# I2C Bus

The shared I2C bus (id st_i2c_bus) that environment-category I2C sensor templates attach to. Include once; every I2C sensor points at it via its *_i2c_id var.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  i2c: !include
    file: esphome_sensor_templates/templates/core/i2c.yaml
    vars: { st_i2c_sda: <value>, st_i2c_scl: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  i2c: github://OWNER/esphome_sensor_templates/templates/core/i2c.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_i2c_sda** | **(required)** | GPIO for the I2C SDA (data) line |
| **st_i2c_scl** | **(required)** | GPIO for the I2C SCL (clock) line |
| st_i2c_scan | `true` | Scan the bus for devices at boot and log the addresses found (handy while wiring) |
| st_i2c_frequency | `50kHz` | Bus clock speed (ESPHome default 50kHz; raise to 100kHz/400kHz for fast sensors on short, well-pulled-up wiring) One of: `10kHz`, `50kHz`, `100kHz`, `200kHz`, `400kHz`, `800kHz`. |

## Notes

- This is the shared bus per the library's "Shared hardware buses" convention. I2C sensor templates declare @requires: i2c and set i2c_id: ${st_<tpl>_i2c_id} defaulting to st_i2c_bus - they never declare their own i2c: block. Include this file exactly once.
- SDA/SCL need external pull-up resistors (typically 4.7k to 3.3V); most breakout boards include them. If the boot scan finds nothing, check wiring and pull-ups before raising the frequency.
