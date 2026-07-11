# Home Assistant Connected

Binary sensor that reports whether the device currently has a live connection to Home Assistant (native API or MQTT).

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** api

## Entities

| Domain | Name |
|---|---|
| `binary_sensor` | Connected |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  ha_status: !include
    file: esphome_sensor_templates/templates/network/ha_status.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  ha_status: github://OWNER/esphome_sensor_templates/templates/network/ha_status.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- Reports native-API/MQTT connection state (HA reachability), not raw WiFi association - it complements wifi_signal rather than duplicating it.
- No update_interval var - the status component polls its connection internally (1s); that cadence is by design and not tunable here.
