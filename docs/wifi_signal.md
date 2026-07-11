# WiFi Signal Strength

Reports WiFi RSSI in dBm and a derived signal-quality percentage. The two entities are coupled - the % is a copy of the dBm reading.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

| Domain | Name |
|---|---|
| `sensor` | WiFi Signal dBm |
| `sensor` | WiFi Signal % |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  wifi_signal: !include
    file: esphome_sensor_templates/templates/network/wifi_signal.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  wifi_signal: github://OWNER/esphome_sensor_templates/templates/network/wifi_signal.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often to sample RSSI |
| st_name_prefix | `""` | Prefix prepended to every entity name |
| st_disabled_by_default | `false` | Ship the entities disabled in HA |
| st_internal | `false` | Hide the entities from HA/web entirely |
| st_state_class | `measurement` | state_class for both entities; set "" to opt out of HA long-term statistics |

## Notes

- The % is 2*(x+100) clamped to 0..100 - the conventional community approximation, NOT a calibrated RSSI-to-quality mapping.
