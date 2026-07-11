# 433 MHz RF Receiver (RC Switch)

433 MHz RF receiver hub (RXB6 / superheterodyne class) that decodes RC Switch codes from cheap wall plugs and remotes and prints them to the log. Filter/idle/tolerance are pre-tuned for noisy 433 MHz receivers.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  rf_receiver: !include
    file: esphome_sensor_templates/templates/remote/rf_receiver.yaml
    vars: { st_rf_rx_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  rf_receiver: github://OWNER/esphome_sensor_templates/templates/remote/rf_receiver.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_rf_rx_pin** | **(required)** | GPIO wired to the receiver DATA pin |
| st_rf_dump | `rc_switch` | Which decoded protocol(s) to print to the log One of: `rc_switch`, `raw`, `all`. |
| st_rf_tolerance | `60%` | Timing tolerance - 60% is the doc-recommended value for noisy 433 MHz receivers |
| st_rf_filter | `4us` | Ignore pulses shorter than this (de-noises the cheap AGC front-end) |
| st_rf_idle | `4ms` | Gap that marks the end of a transmission |

## Notes

- The filter 4us / idle 4ms / tolerance 60% values are the ESPHome-documented rc_switch tuning for noisy 433 MHz receivers; leave them unless you have a clean signal.
- READ CODES FROM THE LOG - press a 433 MHz remote near the receiver and the decoded code prints at INFO, e.g. "Received RCSwitch Raw: protocol=1 data=0x151151". Copy the binary code and protocol into rf_transmitter.yaml to replay it.
- ADD A REMOTE BUTTON via !extend (not shipped, codes are device-specific). Example:
- Cheap 433 MHz receivers are noisy; a proper antenna (17.3 cm wire) and a superheterodyne module (RXB6) decode far more reliably than the tiny green boards.
