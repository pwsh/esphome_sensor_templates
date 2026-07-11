# Generic Select Input

A user-adjustable template select (dropdown), surfaced in HA as a config control. Use it to pick a mode/profile and read the choice elsewhere via id(...).state.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `select` | Mode |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  generic_select: !include
    file: esphome_sensor_templates/templates/inputs/generic_select.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  generic_select: github://OWNER/esphome_sensor_templates/templates/inputs/generic_select.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_select_id | `st_generic_select` | Entity id - MUST be overridden on every extra include (see notes) |
| st_select_name | `Mode` | Entity name (after st_name_prefix) |
| st_select_options | `["Option A", "Option B"]` | List of options - pass a YAML list in vars: |
| st_select_initial | `Option A` | Option selected before anything is restored/set |
| st_select_restore | `true` | Persist the selection across reboots (C++ literal "true"/"false") |

## Notes

- MULTI-INSTANCE - include this file more than once to get several selects. Each extra include MUST override BOTH st_select_id AND st_select_name; duplicate ids are a hard "ID redefined!" compile error.
- st_select_options is a LIST-valued substitution. Pass it exactly like any other var, but as a YAML list, e.g. vars: { st_select_options: ["Eco", "Comfort", "Boost"] }.
- st_select_initial MUST be one of st_select_options, otherwise config validation fails.
- On a template select, restore_value is INCOMPATIBLE with a lambda, so this template uses optimistic:true (the entity holds its own state) and no lambda.
- restore_value:true writes to NVS on every change (one flash write per change) - NVS flash has limited write endurance.
