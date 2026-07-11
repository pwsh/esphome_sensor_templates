# MQTT

MQTT client preset with broker credentials and Home Assistant discovery. An alternative (or complement) to the native api: for brokers-based setups.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  mqtt: !include
    file: esphome_sensor_templates/templates/core/mqtt.yaml
    vars: { st_mqtt_broker: <value>, st_mqtt_password: !secret mqtt_password }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  mqtt: github://OWNER/esphome_sensor_templates/templates/core/mqtt.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_mqtt_broker** | **(required)** | MQTT broker hostname or IP |
| st_mqtt_port | `1883` | MQTT broker TCP port |
| st_mqtt_username | `""` | Broker username (empty = anonymous / no auth) |
| **st_mqtt_password** | **(required)** | Broker password; pass via vars: { st_mqtt_password: !secret mqtt_password } |
| st_mqtt_discovery | `true` | Publish Home Assistant MQTT discovery messages so entities appear automatically |

## Notes

- topic_prefix is intentionally NOT set here - ESPHome defaults it to the device name, and an empty prefix fails validation ("MQTT topic name/filter must not be empty"). Set a custom prefix with a top-level override: mqtt: { topic_prefix: home/living_room } (it deep-merges with this block).
- discovery accepts only "true"/"false". Related knobs (discovery_retain, discovery_unique_id_generator, discovery_prefix) are left at their ESPHome defaults - add them via !extend if needed.
- api: and mqtt: can coexist (both valid). If you run both, Home Assistant may show the device twice - once over the native API and once via MQTT discovery. Include only one unless you specifically want both transports.
