# Using the templates in Home Assistant without GitHub

The builder's **Local** output mode (and the [Quick start](../README.md#quick-start-yaml-by-hand))
reference the templates with plain relative includes:

```yaml
packages:
  uptime: !include esphome_sensor_templates/templates/diagnostics/uptime.yaml
```

That works entirely offline once the library sits next to your device YAMLs. This page explains
where "next to" actually is on each kind of Home Assistant install, and how to get the files
there. (If you use the **Inline** output mode instead, the YAML is self-contained and none of
this applies.)

## Why vendor the files locally

Remote packages (`github://pwsh/esphome_sensor_templates/...@main`) are convenient, but they are
a real `git clone` into ESPHome's private cache with a refresh window (`refresh:`, typically a
day). Once the window lapses, ESPHome re-fetches — and if the fetch fails (offline LAN, GitHub
outage), it does **not** fall back to the stale cache: it deletes the checkout, retries once, and
then the build **fails outright**. A config that compiled yesterday can stop compiling today with
zero changes on your side. A vendored copy:

- builds with no network access, forever;
- is pinned — updates happen only when you deliberately copy in a new version;
- survives this repository moving or disappearing;
- lets you patch templates locally if you need to.

(If you do stay remote, `refresh: never` in the long-form package syntax pins the first clone and
never re-fetches.)

## Where the files go

**The `templates/` tree must sit in the same folder as the device YAML that includes it**, keeping
the `esphome_sensor_templates/templates/...` path used in the include lines. ESPHome resolves
`!include` paths relative to the file containing the include line (verified in ESPHome source,
stable across the current release line) — for a normal single-file device config, that means
relative to the device YAML itself.

| Install type | Device YAMLs live at | Put the library at |
|---|---|---|
| HA OS / Supervised (ESPHome Device Builder add-on) | `/config/esphome/` | `/config/esphome/esphome_sensor_templates/` |
| HA Container (separate ESPHome dashboard container) | the host folder you bind-mount to `/config` | `<that folder>/esphome_sensor_templates/` |
| Standalone CLI (`pip install esphome`) | wherever you keep your YAMLs | a sibling `esphome_sensor_templates/` folder |

Notes for the add-on case:

- The add-on maps Home Assistant's main **`/config`** directory — the one holding
  `configuration.yaml`. Your device YAMLs are at `/config/esphome/<device>.yaml`, and that is
  still true today: the ESPHome 2023.9 storage change only moved the hidden `.esphome`
  build-cache out of `/config/esphome/`, not your configs. The `/addon_configs/…_esphome`
  directory is **not** used by the official add-on — don't put the templates there.
- You only strictly need the `templates/` subfolder, but keep it wrapped in an
  `esphome_sensor_templates/` folder so the include paths match the builder output verbatim.

## Getting the files there

First grab the library: **Code → Download ZIP** on the GitHub page, or
`git clone https://github.com/pwsh/esphome_sensor_templates.git`. Then copy it in with whichever
of these your install has:

- **Samba share add-on** — browse to the **`config`** share
  (`\\homeassistant\config\esphome\`), drop the `esphome_sensor_templates` folder in. Easiest
  from a desktop OS.
- **Studio Code Server add-on** — opens `/config` directly and ships `git`: open its terminal and
  `cd esphome && git clone https://github.com/pwsh/esphome_sensor_templates.git`. Updating later
  is `git pull`. Best option for staying current.
- **SSH add-ons** (official "Terminal & SSH", or Advanced SSH & Web Terminal) — both map
  `/config` and include `git`, so the same clone/pull works over SSH. For `scp`/SFTP transfers
  note the Advanced add-on ships with SFTP **disabled** by default; enable `sftp: true` in its
  options first.
- **File editor add-on** — can create/edit files under `/config` but has no upload-a-folder
  flow; workable for spot-editing a vendored file, not for the initial copy. (It also has a
  built-in `git: true` option that can pull a repo.)
- **HA Container** — no add-ons exist; the ESPHome dashboard container bind-mounts a host
  folder to `/config` (e.g. `-v /home/you/esphome:/config`), so just copy or clone the library
  into that host folder directly.

## Checking it works

In the ESPHome Device Builder, open any device that uses the includes and hit **Validate** (or
run `esphome config <device>.yaml`). If the copy is in the wrong place you'll get a clear
`Error reading file esphome_sensor_templates/templates/...: No such file or directory` naming
the exact path it tried.

## Updating a vendored copy

Nothing updates automatically — that's the point. To update: `git pull` (Studio Code
Server/SSH), or re-download the ZIP and replace the folder over Samba. Skim the commit history /
release notes first, and re-validate your devices afterwards.
