# Captive Portal

WiFi fallback hotspot plus captive portal. When the device cannot join your WiFi it starts its own access point and serves a page to reconfigure credentials.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  captive_portal: !include
    file: esphome_sensor_templates/templates/core/captive_portal.yaml
    vars: { st_ap_ssid: Fallback Hotspot, st_ap_password: !secret ap_password }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  captive_portal: github://OWNER/esphome_sensor_templates/templates/core/captive_portal.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_ap_ssid | `Fallback Hotspot` | SSID of the fallback access point the device raises when it can't join WiFi |
| **st_ap_password** | **(required)** | Fallback AP password (>=8 chars for WPA2); pass via vars: { st_ap_password: !secret ap_password } |

## Notes

- This declares wifi: ap: - it deep-merges into your own wifi: block (with ssid/password), it does NOT replace it. Keep your station wifi: ssid/password in your top-level config.
- After ~1 minute of failed WiFi connection attempts the device raises the AP and serves the portal at http://192.168.4.1/. Connect a phone/laptop to the fallback SSID to reach it.
- A captive portal without a fallback AP is useless, so this file ships both together. The AP password must be at least 8 characters or WPA2 setup fails.
