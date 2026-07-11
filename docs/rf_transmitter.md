# 433 MHz RF Transmitter (RC Switch)

433 MHz RF transmitter hub (FS1000A / ASK class) plus a demo template button that sends a sample RC Switch code. Learn codes with rf_receiver, then replay them from here.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `button` | RF Test |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  rf_transmitter: !include
    file: esphome_sensor_templates/templates/remote/rf_transmitter.yaml
    vars: { st_name_prefix: "", st_rf_tx_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  rf_transmitter: github://OWNER/esphome_sensor_templates/templates/remote/rf_transmitter.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| **st_rf_tx_pin** | **(required)** | GPIO driving the transmitter DATA pin |
| st_rf_tx_id | `st_rf_tx` | Base id for the demo button (button id is ${st_rf_tx_id}_test) |
| st_rf_tx_name | `RF Test` | Name of the demo button (after st_name_prefix) |
| st_rf_test_code | `000000000001010100010001` | RC Switch binary code string the demo button transmits |
| st_rf_test_protocol | `1` | RC Switch protocol number for the demo code |

## Notes

- carrier_duty_percent is 100% - the documented value for RF. 433 MHz ASK transmitters have NO subcarrier, so the output must stay on for the whole mark (an IR-style 50% duty would halve the signal). IR transmitters use 50%; see ir_transmitter.yaml.
- The demo button sends an RC Switch raw code via remote_transmitter.transmit_rc_switch_raw (code + protocol). Learn your real codes with rf_receiver.yaml (they print to the log), then set st_rf_test_code / st_rf_test_protocol, or add buttons via !extend using transmit_rc_switch_a/_b/_c/_d for typed dip-switch/button remotes.
- The bare FS1000A needs a 17.3 cm wire antenna and ideally >3.3 V on VCC for real range; many run it off 5 V with the DATA pin still driven from a 3.3 V GPIO.
