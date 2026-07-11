# DHT Temperature & Humidity

Reads temperature and humidity from a DHT11/DHT22/AM2302/RHT03 single-wire sensor. Exposes both readings as primary sensors.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `sensor` | Temperature |
| `sensor` | Humidity |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  dht: !include
    file: esphome_sensor_templates/templates/environment/dht.yaml
    vars: { st_update_interval: 60s, st_dht_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  dht: github://OWNER/esphome_sensor_templates/templates/environment/dht.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often to sample the sensor (min 2s for DHT22) |
| st_name_prefix | `""` | Prefix prepended to every entity name |
| st_disabled_by_default | `false` | Ship the entities disabled in HA |
| st_internal | `false` | Hide the entities from HA/web entirely |
| st_state_class | `measurement` | state_class for both readings; set "" to opt out of HA long-term statistics |
| **st_dht_pin** | **(required)** | GPIO connected to the sensor DATA line |
| st_dht_model | `DHT22` | Sensor variant One of: `AUTO_DETECT`, `DHT11`, `DHT22`, `DHT22_TYPE2`, `AM2302`, `RHT03`, `SI7021`, `AM2120`. |

## Notes

- DHT22/AM2302 need at least 2s between reads - do not set st_update_interval below 2s.
- A 4.7kΩ-10kΩ pull-up between DATA and 3.3V is required. Bare-module boards with an onboard pull-up need pin: { number: X, pullup: false } via !extend st_dht_temperature's parent - or wire your own.
