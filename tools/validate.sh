#!/usr/bin/env bash
# Validate every example config (and through them, every template file) with
# `esphome config`. Catches YAML errors, unresolved substitutions, ID collisions,
# and schema violations. Pass --compile to additionally build examples/minimal.yaml
# (slow; proves the C++ lambdas actually compile on ESP-IDF).
set -euo pipefail
cd "$(dirname "$0")/.."

VENV=.venv
if [ ! -x "$VENV/bin/esphome" ]; then
  echo "== Creating venv and installing esphome (one-time) =="
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install --quiet --upgrade pip esphome
fi
ESPHOME="$VENV/bin/esphome"
echo "== Using $("$ESPHOME" version) =="

# Dummy secrets for validation only (examples/secrets.yaml is gitignored).
if [ ! -f examples/secrets.yaml ]; then
  cat > examples/secrets.yaml <<'SECRETS'
# Auto-generated dummy secrets for `esphome config` validation. NOT real.
wifi_ssid: "example-ssid"
wifi_password: "example-password"
api_encryption_key: "MDEyMzQ1Njc4OWFiY2RlZjAxMjM0NTY3ODlhYmNkZWY="
ota_password: "example-ota-password"
web_password: "example-web-password"
mqtt_password: "example-mqtt-password"
ap_password: "example-ap-password"
SECRETS
fi

fail=0
for cfg in examples/*.yaml; do
  case "$cfg" in *secrets*) continue ;; esac
  echo "== esphome config $cfg =="
  if ! "$ESPHOME" config "$cfg" > /dev/null; then
    echo "!! VALIDATION FAILED: $cfg"
    fail=1
  fi
done

if [ "${1:-}" = "--compile" ]; then
  echo "== esphome compile examples/minimal.yaml (this takes a while) =="
  "$ESPHOME" compile examples/minimal.yaml || fail=1
fi

if [ "$fail" -ne 0 ]; then
  echo "== FAILED =="
  exit 1
fi
echo "== All configs valid =="
