# Generic Switch (virtual flag)

A virtual template switch, surfaced in HA as a config control. Use it as an on/off flag to gate automations - read it via id(...).state or attach actions with !extend.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `switch` | Flag |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  generic_switch: !include
    file: esphome_sensor_templates/templates/inputs/generic_switch.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  generic_switch: github://OWNER/esphome_sensor_templates/templates/inputs/generic_switch.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_switch_id | `st_generic_switch` | Entity id - MUST be overridden on every extra include (see notes) |
| st_switch_name | `Flag` | Entity name (after st_name_prefix) |
| st_switch_restore_mode | `RESTORE_DEFAULT_OFF` | Boot behavior - see enum in notes |

## Notes

- MULTI-INSTANCE - include this file more than once to get several switches. Each extra include MUST override BOTH st_switch_id AND st_switch_name; duplicate ids are a hard "ID redefined!" compile error.
- restore_mode enum: RESTORE_DEFAULT_OFF, RESTORE_DEFAULT_ON, ALWAYS_OFF, ALWAYS_ON, RESTORE_INVERTED_DEFAULT_OFF, RESTORE_INVERTED_DEFAULT_ON, DISABLED. RESTORE_* variants read the last state from NVS (one flash write per change); ALWAYS_* never persist.
- This is a virtual flag - it drives nothing on its own. Read id(st_generic_switch).state in a lambda, or attach on_turn_on/on_turn_off actions via "switch: - id: !extend st_generic_switch".
