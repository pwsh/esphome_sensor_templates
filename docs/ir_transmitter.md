# IR Transmitter (LED)

Infrared transmitter hub driving an IR LED, plus a demo template button that sends a sample NEC code. Use ir_receiver to learn codes, then replay them from here.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `button` | IR Test |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  ir_transmitter: !include
    file: esphome_sensor_templates/templates/remote/ir_transmitter.yaml
    vars: { st_name_prefix: "", st_ir_tx_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  ir_transmitter: github://OWNER/esphome_sensor_templates/templates/remote/ir_transmitter.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| **st_ir_tx_pin** | **(required)** | GPIO driving the IR LED (via a transistor for range) |
| st_ir_tx_id | `st_ir_tx` | Base id for the demo button (button id is ${st_ir_tx_id}_test) |
| st_ir_tx_name | `IR Test` | Name of the demo button (after st_name_prefix) |
| st_ir_test_address | `0x1234` | 16-bit NEC address the demo button transmits |
| st_ir_test_command | `0x78` | 16-bit NEC command the demo button transmits |

## Notes

- carrier_duty_percent is 50% - the documented value for IR LEDs (the ~38 kHz carrier is on half the time). RF transmitters use 100%; see rf_transmitter.yaml.
- The demo button sends a NEC frame via remote_transmitter.transmit_nec. Learn your real codes with ir_receiver.yaml (they print to the log), then set st_ir_test_address / st_ir_test_command, or add more buttons via !extend using transmit_nec / transmit_sony / transmit_raw / transmit_pronto.
- An ESP32 GPIO sources only ~20 mA; for usable range drive the IR LED through a transistor/MOSFET rather than directly off the pin.
