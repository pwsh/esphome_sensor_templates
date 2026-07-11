# I2S Amplifier / DAC Speaker

An I2S class-D amplifier or DAC (MAX98357A class) on its own I2S bus, exposed as an ESPHome speaker component for media_player / voice_assistant audio output.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** none

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  speaker_i2s: !include
    file: esphome_sensor_templates/templates/audio/speaker_i2s.yaml
    vars: { st_spk_lrclk: <value>, st_spk_bclk: <value>, st_spk_dout: <value> }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  speaker_i2s: github://OWNER/esphome_sensor_templates/templates/audio/speaker_i2s.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| **st_spk_lrclk** | **(required)** | GPIO for the I2S word-select / LR clock (LRC on the amp) |
| **st_spk_bclk** | **(required)** | GPIO for the I2S bit clock (BCLK on the amp) |
| **st_spk_dout** | **(required)** | GPIO for the I2S data output (DIN on the amp) |
| st_spk_dac_type | `external` | DAC type - external for an outboard I2S amp/DAC like the MAX98357A One of: `external`. |
| st_spk_channel | `mono` | Output channel mapping (MAX98357A is a single mono amp -> mono) One of: `left`, `right`, `mono`, `stereo`. |
| st_spk_bits_per_sample | `16bit` | I2S word width sent to the amp One of: `8bit`, `16bit`, `24bit`, `32bit`. |
| st_spk_sample_rate | `16000` | Sample rate in Hz (16000 matches voice_assistant TTS; raise to 44100/48000 for music) |

## Notes

- This template owns its own i2s_audio bus (id st_i2s_spk_bus). Single-I2S chips (ESP32-C3/C6) have only ONE I2S peripheral, so a speaker and a microphone CANNOT run at the same time on them - use an ESP32 or ESP32-S3 (two I2S peripherals) to run speaker_i2s.yaml and microphone_i2s.yaml together.
- The MAX98357A output volume/gain is set in HARDWARE by the GAIN pin strapping, not in ESPHome - there is no software gain key on this platform.
