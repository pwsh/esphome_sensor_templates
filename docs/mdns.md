# mDNS

mDNS preset - controls whether the device advertises itself on the local network via multicast DNS. Enabled by default; this preset exists mainly to turn it off.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  mdns: !include
    file: esphome_sensor_templates/templates/core/mdns.yaml
    vars: { st_mdns_disabled: false }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  mdns: github://OWNER/esphome_sensor_templates/templates/core/mdns.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_mdns_disabled | `false` | Set "true" to stop advertising this device over mDNS |

## Notes

- Disabling mDNS breaks the ESPHome dashboard's online/offline detection and Home Assistant discovery by hostname (<name>.local). OTA and the API by fixed IP still work - you just have to address the device by IP, not hostname.
- mDNS is already enabled by default in ESPHome; you only need this file to disable it or (later) to add custom advertised services via !extend.
