# Generic Text Input

A user-editable template text field, surfaced in HA as a config control. Use it for free-form notes, labels, or short config strings - read it via id(...).state.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `text` | Note |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  generic_text: !include
    file: esphome_sensor_templates/templates/inputs/generic_text.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  generic_text: github://OWNER/esphome_sensor_templates/templates/inputs/generic_text.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_text_id | `st_generic_text` | Entity id - MUST be overridden on every extra include (see notes) |
| st_text_name | `Note` | Entity name (after st_name_prefix) |
| st_text_max_length | `64` | Maximum number of characters allowed |
| st_text_restore | `false` | Persist the text across reboots (C++ literal "true"/"false") |

## Notes

- MULTI-INSTANCE - include this file more than once to get several text fields. Each extra include MUST override BOTH st_text_id AND st_text_name; duplicate ids are a hard "ID redefined!" compile error.
- On a template text, restore_value is INCOMPATIBLE with a lambda, so this template uses optimistic:true (the entity holds its own state) and no lambda.
- Text values eat NVS space (a whole string per write, one flash write per change), so restore_value defaults to "false" here. Turn it "true" only when persistence is genuinely needed.
