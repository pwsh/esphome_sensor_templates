# GPS Module (NEO-6M)

NMEA GPS module (u-blox NEO-6M class) on a dedicated UART. Exposes latitude, longitude, altitude, speed, course and satellite-count sensors, plus a GPS time source.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `sensor` | GPS Latitude |
| `sensor` | GPS Longitude |
| `sensor` | GPS Altitude |
| `sensor` | GPS Speed |
| `sensor` | GPS Course |
| `sensor` | GPS Satellites |
| `sensor` | GPS HDOP |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  gps: !include
    file: esphome_sensor_templates/templates/peripherals/gps.yaml
    vars: { st_update_interval: 60s, st_gps_rx_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  gps: github://OWNER/esphome_sensor_templates/templates/peripherals/gps.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often the GPS sensors publish |
| st_name_prefix | `""` | Prefix prepended to every entity name |
| st_disabled_by_default | `false` | Ship the entities disabled in HA |
| st_internal | `false` | Hide the entities from HA/web entirely |
| st_state_class | `measurement` | state_class for the numeric sensors (set "" to opt out of HA long-term statistics) |
| **st_gps_rx_pin** | **(required)** | GPIO wired to the GPS module's TX pin (the ESP RX). This is the only pin GPS needs. |

## Notes

- The GPS module only TRANSMITS NMEA, so the UART needs just an rx_pin (module TX -> ESP RX) at 9600 baud. If you need to send config commands (e.g. change baud/rate), add a tx_pin to st_gps_uart via !extend.
- ESP32 has 3 hardware UARTs (C3/C6: 2, one often taken by the logger). This template claims one for the GPS; keep it off the logger's UART pins.
- This ships a "time: - platform: gps" source (id st_time_gps). It does NOT collide with core/time_sntp.yaml or time_homeassistant.yaml (different platforms) but they are separate time sources - avoid including several unless you intend it. GPS time only becomes valid once the module has a fix.
- Latitude/longitude report NaN and satellites/hdop stay flat until the module gets a fix - a cold start outdoors can take minutes.
