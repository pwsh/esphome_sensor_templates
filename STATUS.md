# Project Status

_Last updated: 2026-07-11 (ESPHome 2026.6.5)._

## What exists

- **74 templates** across **12 categories** (counts from the generated catalog):
  core 14 · diagnostics 16 · network 7 · lighting 5 · audio 4 · environment 5 · presence 2 ·
  bluetooth 2 · remote 4 · peripherals 4 · controls 6 · inputs 5.
- **Web config builder** at <https://pwsh.github.io/esphome_sensor_templates/> — board/variant
  picker (all 10 ESP32 variants), device identity + network + timezone panel, per-template
  variable editors with enum/boolean dropdowns, requirements advisor with one-click fixes,
  multi-instance support, three output modes (remote github://, local vendored, inline YAML),
  substitutions hoisting for multi-device reuse, annotated output, secrets checklist.
- **Generated docs** — one page per template in `docs/`, README index, `web/catalog.json`.
- **Examples** — `minimal` (C3), `full_diagnostics` (ESP32, global-override demo),
  `all_templates` (S3 kitchen sink, the merge proof), `peripherals_esp32` (camera/IR/RF/LD2450,
  identity fully package-sourced).

## Verification state

- All four example configs pass `esphome config` on 2026.6.5 (run `tools/validate.sh`).
- Real firmware compiled for: the 19-template diagnostics set (incl. NVS/WiFi-channel IDF
  lambdas), the hardware-info + all-lighting set, and the peripherals set (camera, IR/RF,
  LD2450, syslog, device_base) — all `esp32dev`/ESP-IDF.
- Six builder-generated acceptance configs (full device DHCP/static, timezone local + inline,
  generic-C6 variant, P4) pass `esphome config`; the builder's generator functions run under a
  Node smoke harness (~190 assertions across 7 suites).

## Verified platform facts the design rests on

- Package `defaults:` beat top-level `substitutions:`; package `substitutions:` blocks merge
  and are overridden by the main config (empirically proven; see ARCHITECTURE.md). The shared
  global knobs work **because** they live in `substitutions:` blocks.
- Re-declaring an id across packages is a hard error; `!extend` is the only cross-package
  attachment mechanism. Only one SNTP instance is allowed per config.
- ESPHome lambdas see no IDF headers by default (`nvs.h`, `esp_wifi.h`, `esp_chip_info.h`…);
  templates force-include what they need via `build_src_flags`. Only a real compile catches
  violations.
- ESP32-H2 and ESP32-P4 have no WiFi radio (a `wifi:` block fails validation); the builder
  suppresses the network surface for them.
- `syslog`, `runtime_stats`, and `ld2450` are official components (2026.6); the third-party
  syslog external component is archived and Arduino-only.

## Known limitations

- **Platform audit**: templates declare `@platforms` for esp32/s2/s3/c3/c6. The other variants
  (c2, c5, c61, h2, p4) are selectable in the builder but marked "unaudited" — most templates
  should work where the hardware supports them, but nobody has verified each one.
- **Duplicate entity names**: stacking several temperature/humidity templates on one device
  needs distinct `st_name_prefix` values per include (ESPHome rejects duplicate names);
  `examples/all_templates.yaml` shows the pattern. The builder does not yet auto-prefix.
- **micro_wake_word** downloads its model at compile time; it is config-validated but has not
  been through a full compile in this repo.
- **Inline output mode** drops most comments from template bodies and requires hand-merging if
  your config already defines the same top-level keys (the output warns about both).
- The wifi_quality template's internal RSSI helper keeps the platform-default
  `state_class: measurement`; it is `internal: true` so HA never sees it.

## Possible next steps

- Platform audit for the five unaudited variants (then lift the amber badges).
- CI job running `tools/validate.sh` on pull requests (currently deploy-only).
- Auto name-prefixing in the builder when entity-name collisions are predictable.
- A full `esphome compile` matrix (S3/C3) in CI, cached, for the lambda-bearing templates.
