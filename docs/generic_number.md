# Generic Number Input

A user-adjustable template number, surfaced in HA as a config control. Use it for thresholds, calibration offsets, setpoints - read the value elsewhere via id(...).state.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `number` | Setpoint |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  generic_number: !include
    file: esphome_sensor_templates/templates/inputs/generic_number.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  generic_number: github://OWNER/esphome_sensor_templates/templates/inputs/generic_number.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_number_id | `st_generic_number` | Entity id - MUST be overridden on every extra include (see notes) |
| st_number_name | `Setpoint` | Entity name (after st_name_prefix) |
| st_number_min | `-100` | Minimum selectable value |
| st_number_max | `100` | Maximum selectable value |
| st_number_step | `1` | Increment between values |
| st_number_initial | `0` | Value used before anything is restored/set |
| st_number_unit | `""` | Unit of measurement shown in HA (e.g. "C", "%") |
| st_number_mode | `box` | UI control style in HA One of: `box`, `slider`, `auto`. |
| st_number_restore | `true` | Persist the value across reboots (C++ literal "true"/"false") |

## Notes

- MULTI-INSTANCE - include this file more than once to get several numbers. Each extra include MUST override BOTH st_number_id AND st_number_name; duplicate ids are a hard "ID redefined!" compile error.
- On a template number, restore_value is INCOMPATIBLE with a lambda, so this template uses optimistic:true (the entity holds its own state) and no lambda.
- restore_value:true writes to NVS on every change (one flash write per change). NVS flash has limited write endurance - leave it "false" for values that change very often.
