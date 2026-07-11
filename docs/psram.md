# PSRAM Free

Reports free PSRAM (SPI RAM) in bytes from the debug component. Confirms that external PSRAM is detected and tracks headroom for buffer-heavy components.

**Platforms:** `esp32` `esp32s2` `esp32s3`

**Requires:** psram

## Entities

| Domain | Name |
|---|---|
| `sensor` | PSRAM Free |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  psram: !include
    file: esphome_sensor_templates/templates/diagnostics/psram.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  psram: github://OWNER/esphome_sensor_templates/templates/diagnostics/psram.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often the debug hub refreshes PSRAM stats |
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_state_class | `measurement` | state_class for the sensor; set "" to opt out of HA long-term statistics |

## Notes

- ESP32-C3/C6 have no PSRAM interface - this template is limited to esp32/s2/s3. Requires the psram: component configured AND PSRAM hardware present, otherwise the sensor reports 0.
- Shares the debug: hub with the other debug-based templates; dicts merge across packages and the last update_interval wins.
