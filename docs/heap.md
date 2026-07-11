# Heap Diagnostics

Reports internal heap health from the debug component - free bytes, largest allocatable block, historical minimum free, and fragmentation percent. The first thing to check when a device reboots under memory pressure.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `sensor` | Heap Free |
| `sensor` | Heap Max Block |
| `sensor` | Heap Min Free |
| `sensor` | Heap Fragmentation |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  heap: !include
    file: esphome_sensor_templates/templates/diagnostics/heap.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  heap: github://OWNER/esphome_sensor_templates/templates/diagnostics/heap.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often the debug hub refreshes heap stats |
| st_name_prefix | `""` | Prefix prepended to every entity name |
| st_disabled_by_default | `false` | Ship the entities disabled in HA |
| st_internal | `false` | Hide the entities from HA/web entirely |
| st_state_class | `measurement` | state_class for the numeric sensors; set "" to opt out of HA long-term statistics |

## Notes

- Several diagnostics templates declare the debug: hub. ESPHome deep-merges the dict across packages, so the last update_interval wins - keep the knob identical everywhere.
- Sustained fragmentation above ~50% is risky - large contiguous allocations (TLS buffers, JSON) can fail even with free bytes available.
