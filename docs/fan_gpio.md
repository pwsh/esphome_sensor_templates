# On/Off Fan (GPIO)

Simple on/off fan switched through a relay or MOSFET on a GPIO output. No speed control. Multi-instance via id/name vars.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `fan` | Fan |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  fan_gpio: !include
    file: esphome_sensor_templates/templates/peripherals/fan_gpio.yaml
    vars: { st_name_prefix: "", st_fan_gpio_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  fan_gpio: github://OWNER/esphome_sensor_templates/templates/peripherals/fan_gpio.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_fan_gpio_id | `st_fan_gpio` | Entity id - MUST be overridden on every extra include (see notes) |
| st_fan_gpio_name | `Fan` | Entity name (after st_name_prefix) |
| **st_fan_gpio_pin** | **(required)** | GPIO driving the relay/MOSFET control input |

## Notes

- MULTI-INSTANCE - include more than once for several fans. Each extra include MUST override st_fan_gpio_id, st_fan_gpio_name AND st_fan_gpio_pin; duplicate ids or shared pins are errors. The GPIO output id is derived as ${st_fan_gpio_id}_out.
- Size the relay/MOSFET for the fan's stall current, not its running current. A DC fan is an inductive load - add a flyback diode across the fan (or use a relay module with one built in) so the back-EMF spike does not destroy the switching device. For a bare MOSFET, use a logic-level part switching the fan's ground.
