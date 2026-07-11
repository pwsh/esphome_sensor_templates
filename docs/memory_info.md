# Memory Info

Reports total installed internal RAM and total PSRAM in KiB, read from the heap capability registry. Confirms how much DRAM and external SPI RAM the running build actually sees.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `sensor` | RAM Total |
| `sensor` | PSRAM Total |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  memory_info: !include
    file: esphome_sensor_templates/templates/diagnostics/memory_info.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  memory_info: github://OWNER/esphome_sensor_templates/templates/diagnostics/memory_info.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity names |
| st_disabled_by_default | `false` | Ship the entities disabled in HA |
| st_internal | `false` | Hide the entities from HA/web entirely |

## Notes

- Static per boot - update_interval is never and both values are published exactly once from on_boot at priority -100 (after sensors are set up).
- No state_class is set - fixed hardware totals are not measurements and need no HA long-term statistics, so they deliberately do NOT honor the ${st_state_class} knob.
- PSRAM Total reports 0 on boards without external SPI RAM (e.g. ESP32-C3/C6). It reads the heap capability registry (MALLOC_CAP_SPIRAM) directly and does NOT require the psram: component to be configured.
