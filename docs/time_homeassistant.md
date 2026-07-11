# Home Assistant Time

Time source synced from Home Assistant. Provides the time: component other templates (daily_restart, last_boot) require.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** api

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  time_homeassistant: !include esphome_sensor_templates/templates/core/time_homeassistant.yaml
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  time_homeassistant: github://OWNER/esphome_sensor_templates/templates/core/time_homeassistant.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Notes

- Timezone auto-syncs from Home Assistant unless you set it in YAML - override with "time: - id: !extend st_time_ha / timezone: Europe/Berlin".
- Do not include together with time_sntp.yaml unless you want two time sources.
