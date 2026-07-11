# Boot Counter

Counts device boots in an NVS-backed global and publishes the running total. Rising counts between expected reboots point at brown-outs, watchdog resets, or crashes.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `sensor` | Boot Count |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  boot_counter: !include
    file: esphome_sensor_templates/templates/diagnostics/boot_counter.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  boot_counter: github://OWNER/esphome_sensor_templates/templates/diagnostics/boot_counter.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- One NVS write per boot (restore_value) - negligible flash wear. The count survives reboots and OTA but NOT a factory_reset or a wired flash-erase.
- This is a counter - state_class is hardcoded total_increasing and does NOT honor the ${st_state_class} knob. There is no update_interval: the value is published once from on_boot.
