# IR Receiver (TSOP)

Infrared remote receiver hub for a TSOP-class demodulating IR sensor. Decodes received remote codes and prints them to the log so you can copy them into an ir_transmitter template.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  ir_receiver: !include
    file: esphome_sensor_templates/templates/remote/ir_receiver.yaml
    vars: { st_ir_rx_pin: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  ir_receiver: github://OWNER/esphome_sensor_templates/templates/remote/ir_receiver.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_ir_rx_pin** | **(required)** | GPIO wired to the TSOP data/OUT pin |
| st_ir_dump | `all` | Which decoded protocol(s) to print to the log; "all" dumps every known protocol One of: `all`, `nec`, `sony`, `rc5`, `rc6`, `samsung`, `samsung36`, `lg`, `panasonic`, `jvc`, `pronto`, `coolix`, `midea`, `rc_switch`, `raw`. |

## Notes

- TSOP-class receivers (TSOP38238 etc.) have an open-collector output that idles HIGH and pulls LOW on a carrier burst, so the pin is configured inverted:true with an internal pull-up. If your module has its own pull-up you can drop the pullup via !extend.
- READ CODES FROM THE LOG - point a remote at the receiver and the decoded code prints at INFO level, e.g. "Received NEC: address=0x1234, command=0x0078". Copy those values into ir_transmitter.yaml (st_ir_test_address / st_ir_test_command) to replay the button.
- dump also accepts a LIST - to dump several specific protocols instead of one, override via !extend: "remote_receiver: - id: !extend st_ir_receiver / dump: [nec, sony, rc5]".
- ADD A BUTTON BINARY_SENSOR via !extend (not shipped, codes are device-specific). Example - a "Power" button on a NEC remote:
