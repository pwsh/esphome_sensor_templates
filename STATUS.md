# Project Status

_Last updated: 2026-08-21 (validated against ESPHome 2026.8.0)._

## What exists

- **77 templates** across **12 categories** (counts from the generated catalog):
  core 14 · diagnostics 16 · network 7 · lighting 6 · audio 4 · environment 6 · presence 3 ·
  bluetooth 2 · remote 4 · peripherals 4 · controls 6 · inputs 5.
- **Web config builder** at <https://pwsh.github.io/esphome_sensor_templates/> — board/variant
  picker (all 10 ESP32 variants), device identity + network + timezone panel, per-template
  variable editors with enum/boolean dropdowns and a color picker for `*_color_r/_g/_b` var
  trios, requirements advisor with one-click fixes, multi-instance support, three output modes
  (remote github://, local vendored, inline YAML), substitutions hoisting for multi-device
  reuse, annotated output, secrets checklist.
- **Lighting**: every light template ships a curated effects list (pulse/strobe/flicker/random
  plus the addressable set on strips), and `lighting/boot_color.yaml` pairs with any library
  light to set a chosen power-on color (boot priority 600, verified against ESPHome setup
  priorities: lights at 799–800, WiFi at 250).
- **Generated docs** — one page per template in `docs/`, README index, `web/catalog.json`,
  plus the hand-written `docs/home_assistant.md` (vendoring the library into HA OS/Container
  installs so local includes build without GitHub).
- **Examples** — `minimal` (C3), `full_diagnostics` (ESP32, global-override demo),
  `all_templates` (S3 kitchen sink, the merge proof), `peripherals_esp32` (camera/IR/RF/LD2450,
  identity fully package-sourced).

## Changelog review (2026-08-21, ESPHome 2026.7/2026.8 + HA 2026.6-2026.8)

Full sweep of the ESPHome 2026.7.x/2026.8.0 changelogs and Home Assistant 2026.6-2026.8
release notes against the library's component inventory, plus an empirical pass (every example
run through `esphome config` on 2026.8.0, real compiles on both toolchains). Outcomes:

- **Fixed - toolchain flip broke IDF lambdas**: 2026.7 made native ESP-IDF the default ESP32
  toolchain, where `platformio_options: build_src_flags` is ignored — the five IDF-header
  templates (nvs_usage, chip_info, flash_info, memory_info, wifi_channel) failed real compiles
  on 2026.8.0. Migrated to `esphome: includes:` with `<header.h>` system entries (codegen'd
  `#include` in main.cpp), verified working on 2026.6.5, 2026.7.4 and 2026.8.0.
- **Adopted - web_server digest auth**: 2026.8 warns on configs without an explicit auth
  `type:`; the default flips basic→digest in 2027.1.0. web_server.yaml now emits
  `type: ${st_web_auth_scheme}` (default `digest`), raising that one file's floor to 2026.7.0.
  Verified in 2026.8 source that the boot-gate and empty-username fail-open are scheme-independent.
- **Deferred - strip channel_colors**: `rgb_order`/`is_rgbw` on esp32_rmt_led_strip are
  deprecated for `channel_colors:` (removed 2027.3.0), but the new key only exists on 2026.8.0+
  (2026.7.4 rejects it — probed). Both strip templates keep the old keys and ship the
  replacement as a ready-to-enable commented-out `channel_colors:` line next to them (the
  safe_mode `storage: rtc` and deep_sleep `on_wake` opt-ins ship the same way); each block was
  proven by uncommenting per its own instructions and passing `esphome config` + a real compile
  on 2026.8.0. Revisit before 2027.3.
- **Added - ld6002b**: new template for the HLK-LD6002B 60 GHz 3D presence radar (component
  added in 2026.8.0; that template requires 2026.8.0+).
- **Documented, no config change**: HA 2026.6 flipped bluetooth_proxy's default scan mode to
  Auto; 2026.8 fixed the ble_tracker scan window under WiFi coexistence; 2026.7+ safe_mode
  `storage: rtc` and 2026.8 deep_sleep `on_wake` are noted as opt-ins; 2026.8 fixed the P4
  production-silicon bootloader (builder hint updated).
- **Checked, not affected**: `packages:` bare-include removal (2026.7) — the library and all
  builder output use the mapping form; api password removal (2026.1) — encryption-only already;
  web_server v1 sunset (2027.1) — v3 already; light brightness-0 semantics change; new
  merge-key warnings; voc/nox renames (components not used).

## Verification state

- All four example configs pass `esphome config` on 2026.8.0 (run `tools/validate.sh`).
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
  templates inject them via `esphome: includes:` `<header.h>` system entries (codegen'd
  `#include` lines in main.cpp — toolchain-independent). Only a real compile catches
  violations. The old `build_src_flags` route silently broke when 2026.7 switched the default
  toolchain to native ESP-IDF.
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
