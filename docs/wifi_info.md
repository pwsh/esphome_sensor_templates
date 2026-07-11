# WiFi Info

Exposes the device's current WiFi/network identity - IP address, SSID, BSSID, MAC address and DNS - as text sensors.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

| Domain | Name |
|---|---|
| `text_sensor` | IP Address |
| `text_sensor` | SSID |
| `text_sensor` | BSSID |
| `text_sensor` | MAC Address |
| `text_sensor` | DNS Address |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  wifi_info: !include
    file: esphome_sensor_templates/templates/network/wifi_info.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  wifi_info: github://OWNER/esphome_sensor_templates/templates/network/wifi_info.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to every entity name |
| st_disabled_by_default | `false` | Ship the entities disabled in HA |
| st_internal | `false` | Hide the entities from HA/web entirely |

## Notes

- wifi_info is event-driven (values refresh on association change), so there is no update_interval to tune.
- scan_results is deliberately omitted - it is expensive. Add it with `!extend st_wifi_info_ip` ... or a separate wifi_info block if you need it.
