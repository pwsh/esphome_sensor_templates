# Runtime Stats

Enables the runtime_stats component, which periodically logs per-component loop execution time (count, average, max, total) to the console. A debugging aid - it exposes no entities.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  runtime_stats: !include
    file: esphome_sensor_templates/templates/diagnostics/runtime_stats.yaml
    vars: { st_runtime_stats_log_interval: 60s }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  runtime_stats: github://OWNER/esphome_sensor_templates/templates/diagnostics/runtime_stats.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_runtime_stats_log_interval | `60s` | How often to print the runtime statistics report to the log |

## Notes

- This is a debugging tool. Collecting the stats adds overhead to every component execution, so remove this package once you have finished profiling rather than leaving it enabled long-term.
- Output goes to the logger at INFO level (there are no sensor entities). Watch it with `esphome logs` or the log viewer. A shorter log_interval means more log volume.
