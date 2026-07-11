# WiFi Quality (plain language)

Translates RSSI into a plain-language rating (Excellent/Good/Fair/Poor/Very Poor). Carries its own internal RSSI source, so it works standalone.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

| Domain | Name |
|---|---|
| `text_sensor` | WiFi Quality |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  wifi_quality: !include
    file: esphome_sensor_templates/templates/network/wifi_quality.yaml
    vars: { st_update_interval: 30s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  wifi_quality: github://OWNER/esphome_sensor_templates/templates/network/wifi_quality.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `30s` | How often to sample RSSI and refresh the rating |
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- Includes a hidden wifi_signal sensor (st_wifi_quality_rssi). Including wifi_signal.yaml as well adds a second, independent RSSI read - harmless, but the dBm entity lives there.
