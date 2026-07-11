# Web Server

Built-in web UI (v3) with HTTP basic auth and a boot-time gate that can disable auth without editing the config. Keeps the device usable standalone when Home Assistant is down.

**Platforms:** `esp32` `esp32s2` `esp32s3` `esp32c3` `esp32c6`

**Requires:** wifi

## Entities

_No Home Assistant entities (preset / firmware-only)._

## Usage

Local include (repo checked out beside your config):

```yaml
packages:
  web_server: !include
    file: esphome_sensor_templates/templates/core/web_server.yaml
    vars: { st_web_include_internal: true, st_web_password: !secret web_password }
```

Remote include (pulled straight from GitHub):

```yaml
packages:
  web_server: github://OWNER/esphome_sensor_templates/templates/core/web_server.yaml@main
```

> Replace `OWNER` with the GitHub owner/repo that hosts this library.

## Variables

| Variable | Default | Description |
|---|---|---|
| st_web_include_internal | `true` | Show internal: entities in the web UI too (C++ bool literal) |
| st_web_username | `admin` | HTTP basic auth username; MUST NOT be empty (see note) |
| **st_web_password** | **(required)** | HTTP basic auth password; pass via vars: { st_web_password: !secret web_password } |
| st_web_auth | `true` | Enable auth at boot - must be exactly "true" or "false", substituted as a C++ bool literal |

## Notes

- st_web_auth is injected raw into a lambda as a C++ bool literal, so it MUST be exactly "true" or "false" - not "1", "yes", or "True".
- WebServerBase::add_handler only wraps handlers in auth middleware when credentials are non-empty AT REGISTRATION TIME. web_server registers its handlers in setup() at priority ~249 (WIFI-1), so clearing the credentials in on_boot at priority 600 (which runs earlier) disables auth for the whole boot.
- st_web_username must NOT be empty - web_server_idf's authenticate() FAILS OPEN on an empty username (returns true for every request), silently disabling auth. Password-only auth is therefore not possible.
