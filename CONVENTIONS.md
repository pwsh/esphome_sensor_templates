# Template Authoring Conventions

This file is the authoritative spec for every template file in this library. All templates MUST
follow it exactly — the docs generator, the web builder, and the validation harness all depend on it.

## Scope and target

- Target hardware: **ESP32 family only** (esp32, esp32s2, esp32s3, esp32c3, esp32c6) on the
  **ESP-IDF framework**. Lambdas may use ESP-IDF APIs directly (`nvs_get_stats`, `esp_partition_*`,
  etc.). Never use Arduino-only APIs (`WiFi.`, `ESP.`).
- Minimum ESPHome version: **2026.5.0** (first release where `!include vars` are visible inside a
  package's own `substitutions:`/`defaults:` block and inside `!lambda` bodies).

## File model

Each template file is a **self-contained ESPHome package**, included by users via:

```yaml
packages:
  uptime: !include esphome_sensor_templates/templates/diagnostics/uptime.yaml
  wifi_signal: !include
    file: esphome_sensor_templates/templates/network/wifi_signal.yaml
    vars: { st_update_interval: 5min }
```

Rules:

1. **Self-contained.** A file must validate when it is the only template included. Never reference
   an `id` defined in another template file. If an entity needs a source sensor (e.g. WiFi quality
   needs RSSI), declare that source inside the same file with `internal: true`.
2. **One include = one logical sensor.** A file may expose several entities only when they are
   intrinsically coupled (dBm + percent; temperature + overtemp warning).
3. **Top-level keys merge.** Files may declare `debug:`, `wifi:`, `esphome:`, `safe_mode:`,
   `globals:`, etc. — ESPHome deep-merges dicts key-by-key and concatenates lists across packages.
   Never declare a top-level scalar that would clobber the user's value (e.g. never set
   `esphome: name:` or `wifi: ssid:` in a template).
4. **No `!secret` in template files.** Remote packages cannot resolve secrets. Anything secret is a
   required var the user passes (they can use `!secret` in their own `vars:` block).

## Substitution variables

All vars are prefixed `st_`. There are TWO declaration mechanisms with different semantics —
verified empirically on 2026.6.5, do not trust older doc readings:

- **`defaults:`** — resolved AT INCLUDE TIME, file-locally. A value here BEATS the user's
  top-level `substitutions:` (only per-include `vars:` overrides it). Use for file-specific
  vars and for deliberate deviations from a shared-knob standard value.
- **`substitutions:`** — merged across all packages into the global substitution table; the
  user's top-level `substitutions:` overrides it, and per-include `vars:` still wins for that
  file alone (vars resolve at include time). Use for the shared knobs.

Effective precedence: CLI `-s` → include `vars:` → file's `defaults:` → user's top-level
`substitutions:` → file's `substitutions:`. A required var (absent from both blocks) is
resolvable by any of them.

### Shared knobs — declare in every file's `substitutions:` block, at EXACTLY these values

Because package `substitutions:` blocks merge into one table, every file must use identical
values — a deviation would leak to every other template (the generator enforces this). A file
that intentionally deviates (e.g. factory_reset ships disabled) puts that knob in `defaults:`
instead, accepting that it can then only be changed per-include via `vars:`.

| Var | Default | Applied to |
|---|---|---|
| `st_update_interval` | `60s` | every polled sensor/text_sensor `update_interval` |
| `st_name_prefix` | `""` | prepended to every entity `name` (`name: "${st_name_prefix}WiFi Signal dBm"`) |
| `st_disabled_by_default` | `"false"` | every non-internal entity |
| `st_internal` | `"false"` | every user-facing entity's `internal:` |
| `st_state_class` | `measurement` | every numeric, non-counter sensor (`state_class: "${st_state_class}"`); users set `""` globally to opt out of HA long-term statistics |

Exceptions: `st_state_class` is omitted where a fixed class is semantically required
(`total_increasing` for counters — hardcode it) or where no state_class applies (text/binary).
Files with no polled entity omit `st_update_interval`. Never apply `${st_internal}` to a helper
sensor that is always `internal: true`.

### File-specific vars

Named `st_<topic>_<param>` (e.g. `st_ntp_server`, `st_overtemp_threshold`, `st_web_username`,
`st_status_led_pin`). Give every var a sensible default unless a default is impossible (pins,
secrets) — those are "required vars" and MUST be listed with default `(required)` in the header.

Booleans substituted into C++ lambdas must be documented as C++ literals (`"true"`/`"false"`).

## IDs

- Every `id:` is prefixed `st_` and **unique across the whole library** (all packages merge into
  one namespace). Pattern: `st_<template>_<entity>`, e.g. `st_wifi_signal_dbm`,
  `st_boot_counter_value`. Check the ID registry section in the authoring task before choosing.
- Users override entities via `!extend st_<id>` / remove via `!remove` — always give every entity
  an `id`, even when not referenced, to make that possible.

## Entity metadata

- `entity_category: diagnostic` for read-only health/info entities; `config` for controls/inputs.
- Correct `device_class`, `unit_of_measurement`, `accuracy_decimals`, `icon` (mdi) on everything.
- text_sensor `device_class` may ONLY be `timestamp` or `date` — otherwise omit.
- Never set `force_update: true`.
- Lambdas returning floats must guard with `isnan()`; template text/binary lambdas return `{}` when
  the value is unknown rather than a wrong value.
- Keep execution lightweight: default `update_interval` 60s (30s only where genuinely useful),
  no busy work in `loop()`, `globals` with `restore_value: true` only where persistence is the
  point (NVS write on change — document it).

## Metadata header (machine-parsed — exact format)

Every file starts with this comment block, one `# @key:` per line, before any YAML:

```yaml
# @template: wifi_signal            <- unique slug, matches filename without .yaml
# @title: WiFi Signal Strength      <- short human title
# @category: core|diagnostics|network|lighting|audio|environment|presence|bluetooth|remote|peripherals|controls|inputs
# @description: One or two sentences: what it does and what it provides.
# @platforms: esp32, esp32s2, esp32s3, esp32c3, esp32c6   <- only chips it truly supports
# @requires: wifi                   <- comma list of config the USER must already have
#                                      (wifi, api, time, none) or another note like
#                                      "HA input_boolean helper"
# @entities: sensor "WiFi Signal dBm"; sensor "WiFi Signal %"   <- semicolon-separated,
#                                      format: <domain> "<default name>"
# @var st_update_interval [60s]: How often to sample RSSI
# @var st_status_led_pin [(required)]: GPIO for the LED
# @var st_log_level [INFO] {NONE|ERROR|WARN|INFO|DEBUG|VERBOSE|VERY_VERBOSE}: Log verbosity
# @note: Free-form caveat line. Repeatable, optional.
```

Rules: `@var` lines list EVERY var in `defaults:` (shared knobs included) with its default in
`[...]` and a description after `: `. Vars with a fixed set of valid values declare them as
`{A|B|C}` between the default and the colon — the web builder renders these as dropdowns (the
default MUST be one of the choices). Plain `"true"`/`"false"` vars need no `{...}`; the builder
auto-detects booleans. `@requires: none` when standalone. After the header, use plain `#`
comments generously — explain WHY (gotchas, IDF behavior), like the reference files do.

## Shared hardware buses

Templates that need a bus follow the daily_restart pattern — reference a shared resource by id
via a var instead of declaring a colliding duplicate:

- **I2C**: `core/i2c.yaml` provides the bus (id `st_i2c_bus`, pin vars). I2C sensor templates
  declare `@requires: i2c` and set `i2c_id: ${st_<tpl>_i2c_id}` with default `st_i2c_bus`.
  They never declare their own `i2c:` block.
- **UART**: each UART device template declares its OWN `uart:` entry (devices need distinct
  pins anyway) with a unique `st_<tpl>_uart` id and required pin vars. Note in the file that
  ESP32 has 3 hardware UARTs (C3/C6: 2, one often used by the logger).
- **I2S**: microphone and speaker templates declare their own `i2s_audio:` bus with unique
  `st_` ids; chips with a single I2S peripheral (C3) can only run one at a time — document it.
- **one_wire**: the DS18B20 template owns its `one_wire:` bus (only template using it).

## Lighting templates

- Lights are primary entities: no `entity_category`, and they are **multi-instance** — the entity
  `id` and `name` are vars (like the inputs category), so one file can be included several times
  with different pins.
- **Power caps are mandatory.** Defaults must be safe for a board powered from USB with no
  external supply: PWM-driven lights cap duty via the output's `max_power:`; addressable strips
  cap via `color_correct:` entries. Default caps stay conservative (≤ 0.5 for strips) and every
  file documents the math (a WS2812-class LED draws ~60 mA at full white; a 500 mA USB budget
  minus ~150 mA for the ESP32 leaves headroom for only ~5-8 LEDs at 100%). Raising the cap to
  1.0 is an explicit user action for externally-powered rigs.
- `restore_mode` defaults to `ALWAYS_OFF` (a light that restores ON at boot can brown-out a
  USB-powered board before WiFi even starts).

## Reference implementations

Match the style of these files exactly:
- `templates/diagnostics/nvs_usage.yaml` (lambda text sensor, IDF APIs)
- `templates/network/wifi_quality.yaml` (self-contained internal source sensor)
- `templates/core/time_sntp.yaml` (core preset with file-specific vars)
