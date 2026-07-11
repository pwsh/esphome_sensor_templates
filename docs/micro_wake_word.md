# microWakeWord Detector

On-device wake-word detection (microWakeWord) that listens on an I2S microphone and pulses a template binary sensor when the chosen wake word is heard.

**Platforms:** `esp32` `esp32s3` `esp32c3` `esp32c6`

**Requires:** microphone (audio/microphone_i2s.yaml)

## Entities

| Domain | Name |
|---|---|
| `binary_sensor` | Wake Word Detected |

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  micro_wake_word: !include
    file: esphome_sensor_templates/templates/audio/micro_wake_word.yaml
    vars: { st_name_prefix: "" }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  micro_wake_word: github://OWNER/esphome_sensor_templates/templates/audio/micro_wake_word.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_name_prefix | `""` | Prefix prepended to the entity name |
| st_disabled_by_default | `false` | Ship the entity disabled in HA |
| st_internal | `false` | Hide the entity from HA/web entirely |
| st_wake_word_model | `okay_nabu` | Which officially hosted microWakeWord model to load One of: `okay_nabu`, `hey_jarvis`, `hey_mycroft`, `alexa`. |
| st_mww_microphone_id | `st_microphone` | id of the microphone component to listen on (default matches microphone_i2s.yaml) |

## Notes

- REQUIRES a microphone - include audio/microphone_i2s.yaml (which provides microphone id st_microphone) alongside this file. The mic must be 16 kHz.
- Model files are downloaded at COMPILE time from the esphome/micro-wake-word-models repo (github:// source) - the build host needs internet access; nothing is fetched at runtime.
- microWakeWord runs a TensorFlow-Lite-Micro model and is memory hungry - an ESP32-S3 with PSRAM is the recommended target. It will validate on plain ESP32/C3/C6 but may not have the RAM to run reliably.
- stop_after_detection is set false so the detector keeps listening (and the binary sensor keeps pulsing) without a voice_assistant to restart it.
