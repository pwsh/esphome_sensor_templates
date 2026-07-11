# HA-Controlled Deep Sleep

The classic Home Assistant-controlled deep sleep pattern. The device sleeps between runs but honors an HA input_boolean that can hold it awake for OTA/config.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** api, HA input_boolean helper named by st_prevent_sleep_entity

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  deep_sleep_control: !include
    file: esphome_sensor_templates/templates/inputs/deep_sleep_control.yaml
    vars: { st_sleep_duration: 10min }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  deep_sleep_control: github://OWNER/esphome_sensor_templates/templates/inputs/deep_sleep_control.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_sleep_duration | `10min` | How long the device stays asleep between runs |
| st_run_duration | `60s` | How long the device stays awake each run before sleeping |
| st_prevent_sleep_entity | `input_boolean.prevent_deep_sleep` | HA entity that, when ON, prevents sleep |

## Notes

- SINGLE-INSTANCE - this file uses fixed ids (st_deep_sleep, st_prevent_sleep). Include it exactly ONCE.
- Requires an active api: connection - the homeassistant binary_sensor platform reads the toggle over the API.
- The device can only see the toggle WHILE AWAKE. Flip the HA input_boolean ON *before* the next wake so the device catches it during its brief run_duration window (that window is your OTA opportunity).
- When the toggle goes back OFF (on_release), deep_sleep.allow re-arms sleep and restarts the run_duration timer, so the device stays awake for a fresh run_duration before sleeping again.
- Create the helper in HA: Settings > Devices & Services > Helpers > Toggle, matching st_prevent_sleep_entity.
