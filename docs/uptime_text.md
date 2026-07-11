# Uptime (human-readable)

Reports device uptime as a human-readable string (e.g. "3d 4h 12m 5s") using the uptime platform's built-in formatting. Nicer to read on a dashboard than raw seconds.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

| Domain | Name |
|---|---|
| `text_sensor` | Uptime |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  uptime_text: !include
    file: esphome_sensor_templates/templates/diagnostics/uptime_text.yaml
    vars: { st_update_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  uptime_text: github://OWNER/esphome_sensor_templates/templates/diagnostics/uptime_text.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_update_interval | `60s` | How often to refresh the formatted string |
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |

## Notes

- Supersedes the old hand-rolled lambda approach - the uptime text_sensor platform now formats the string natively via the format: block.
