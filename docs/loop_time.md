# Loop Time

Reports the main-loop iteration time from the debug component, in milliseconds. Spikes reveal a component that blocks the loop (slow I2C, long lambdas).

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `sensor` | Loop Time |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  loop_time: !include
    file: esphome_sensor_templates/templates/diagnostics/loop_time.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  loop_time: github://OWNER/esphome_sensor_templates/templates/diagnostics/loop_time.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often the debug hub refreshes loop time |
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_state_class | `measurement` | state_class for the sensor; set "" to opt out of HA long-term statistics |

## Notes

- Shares the debug: hub with the other debug-based templates; dicts merge across packages and the last update_interval wins.
