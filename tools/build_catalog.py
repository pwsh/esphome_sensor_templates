#!/usr/bin/env python3
"""Catalog / docs generator for the ESPHome template library.

Parses the machine-readable metadata header of every templates/*/*.yaml file
(spec: CONVENTIONS.md, "Metadata header" section) and emits:

  * web/catalog.json  - machine-readable catalog (pretty, deterministic)
  * docs/<slug>.md    - one doc page per template (stale pages pruned)
  * README.md         - regenerated index between the GENERATED INDEX markers
  * web/index.html    - catalog injected into <script id="catalog"> IF present

Standard library only. Idempotent: safe to re-run.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "templates"
DOCS_DIR = ROOT / "docs"
WEB_DIR = ROOT / "web"
README = ROOT / "README.md"
CATALOG_JSON = WEB_DIR / "catalog.json"
INDEX_HTML = WEB_DIR / "index.html"

MIN_ESPHOME = "2026.5.0"
CATEGORIES = ["core", "diagnostics", "network", "controls", "inputs"]

REQUIRED_KEYS = ("template", "title", "category", "description",
                 "platforms", "requires", "entities")

# @var lines are '@var NAME [..]: desc' (no colon after 'var'); every other key
# is '@key: value'. Capture the key, then the remainder is normalized below.
HEADER_LINE_RE = re.compile(r"^#\s*@(\w+)(.*)$")
ENTITY_RE = re.compile(r'^(\w+)\s+"([^"]+)"(?:\s+\((.*)\))?$')
DEFAULTS_KEY_RE = re.compile(r"^  (\w+):")
ID_RE = re.compile(r"^\s*(?:- )?id: (st_[a-z0-9_]+)$")

BEGIN_MARK = "<!-- BEGIN GENERATED INDEX -->"
END_MARK = "<!-- END GENERATED INDEX -->"
CATALOG_SCRIPT_RE = re.compile(
    r'(<script id="catalog" type="application/json">)(.*?)(</script>)',
    re.DOTALL,
)


class ParseError(Exception):
    pass


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

def split_header_body(text):
    """Return (header_lines, body_text).

    Header = leading run of '#' comment lines. Body = everything from the first
    non-'#', non-empty line onward, verbatim.
    """
    lines = text.splitlines(keepends=True)
    body_start = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "":
            continue
        if stripped.startswith("#"):
            continue
        body_start = i
        break
    if body_start is None:
        header_lines = [ln for ln in lines if ln.strip().startswith("#")]
        return header_lines, ""
    header_lines = [ln for ln in lines[:body_start] if ln.strip().startswith("#")]
    body = "".join(lines[body_start:])
    return header_lines, body


def parse_var(val):
    """Parse the value portion of a '@var' line: 'name [default]: description'."""
    open_idx = val.find("[")
    if open_idx == -1:
        raise ParseError(f"@var line has no '[default]': {val!r}")
    sep = val.find("]: ", open_idx)
    if sep == -1:
        raise ParseError(f"@var line has no ']: ' separator: {val!r}")
    name = val[:open_idx].strip()
    default = val[open_idx + 1:sep]
    description = val[sep + 3:].strip()
    required = default == "(required)"
    if required:
        default = ""
    secret = "!secret" in description
    return {
        "name": name,
        "default": default,
        "required": required,
        "secret": secret,
        "description": description,
    }


def parse_entities(val):
    """Parse a '@entities' value into a list of {domain, name[, extra]}."""
    if val.startswith("none"):
        return []
    entities = []
    for chunk in val.split("; "):
        chunk = chunk.strip()
        m = ENTITY_RE.match(chunk)
        if not m:
            raise ParseError(f"unparseable @entities item: {chunk!r}")
        entity = {"domain": m.group(1), "name": m.group(2)}
        if m.group(3):
            entity["extra"] = m.group(3)
        entities.append(entity)
    return entities


def parse_requires(val):
    if val == "none":
        return []
    return val.split(", ")


def parse_defaults_keys(body):
    """Minimal indent-based scan of the 'defaults:' block (no PyYAML)."""
    keys = []
    in_block = False
    for line in body.splitlines():
        if not in_block:
            if line.rstrip() == "defaults:":
                in_block = True
            continue
        if line.strip() == "":
            continue
        if not line[:1].isspace():  # next top-level key -> block ended
            break
        if line.lstrip().startswith("#"):
            continue
        m = DEFAULTS_KEY_RE.match(line)
        if m:
            keys.append(m.group(1))
    return keys


def parse_file(path):
    text = path.read_text(encoding="utf-8")
    header_lines, body = split_header_body(text)

    single = {}
    var_vals = []
    notes = []
    for raw in header_lines:
        m = HEADER_LINE_RE.match(raw.strip())
        if not m:
            continue
        key, rest = m.group(1), m.group(2)
        if rest.startswith(":"):  # '@key: value' form
            rest = rest[1:]
        val = rest.strip()
        if key == "var":
            var_vals.append(val)
        elif key == "note":
            notes.append(val)
        else:
            single[key] = val

    rel = path.relative_to(ROOT).as_posix()

    missing = [k for k in REQUIRED_KEYS if k not in single]
    if missing:
        raise ParseError(f"{rel}: missing required header keys: {', '.join(missing)}")

    slug = single["template"]
    category = single["category"]

    vars_parsed = [parse_var(v) for v in var_vals]
    defaults_keys = parse_defaults_keys(body)

    entry = {
        "slug": slug,
        "title": single["title"],
        "category": category,
        "description": single["description"],
        "platforms": single["platforms"].split(", "),
        "requires": parse_requires(single["requires"]),
        "entities": parse_entities(single["entities"]),
        "vars": vars_parsed,
        "notes": notes,
        "path": rel,
        "body": body,
    }
    entry["_defaults_keys"] = defaults_keys  # internal, stripped before emit
    return entry


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------

def validate(entries):
    errors = []
    slugs = {}
    for e in entries:
        rel = e["path"]
        # slug matches filename
        expected_slug = Path(rel).stem
        if e["slug"] != expected_slug:
            errors.append(f"{rel}: @template '{e['slug']}' != filename '{expected_slug}'")
        # category matches directory
        parent = Path(rel).parent.name
        if e["category"] != parent:
            errors.append(f"{rel}: @category '{e['category']}' != directory '{parent}'")
        if e["category"] not in CATEGORIES:
            errors.append(f"{rel}: unknown category '{e['category']}'")
        # slug uniqueness
        if e["slug"] in slugs:
            errors.append(f"{rel}: duplicate slug '{e['slug']}' (also in {slugs[e['slug']]})")
        else:
            slugs[e["slug"]] = rel
        # defaults keys vs @var names. Required vars (secrets/pins) have no
        # default by convention, so they are exempt from the defaults: block.
        all_vars = {v["name"] for v in e["vars"]}
        non_required = {v["name"] for v in e["vars"] if not v["required"]}
        def_set = set(e["_defaults_keys"])
        for k in sorted(def_set - all_vars):
            errors.append(f"{rel}: '{k}' in defaults: but has no matching @var line")
        for k in sorted(non_required - def_set):
            errors.append(f"{rel}: @var '{k}' has no matching key in defaults:")

    # global id uniqueness (regex across raw file bodies)
    id_owners = {}
    for e in entries:
        for line in e["body"].splitlines():
            m = ID_RE.match(line)
            if m:
                id_owners.setdefault(m.group(1), set()).add(e["path"])
    for st_id, owners in sorted(id_owners.items()):
        if len(owners) > 1:
            errors.append(f"id collision '{st_id}' shared by: {', '.join(sorted(owners))}")

    return errors


# --------------------------------------------------------------------------
# Emitters
# --------------------------------------------------------------------------

def public_entry(e):
    """Entry with internal fields stripped, keys in a stable order."""
    return {
        "slug": e["slug"],
        "title": e["title"],
        "category": e["category"],
        "description": e["description"],
        "platforms": e["platforms"],
        "requires": e["requires"],
        "entities": e["entities"],
        "vars": e["vars"],
        "notes": e["notes"],
        "path": e["path"],
        "body": e["body"],
    }


def build_catalog(entries):
    ordered = sorted(entries, key=lambda e: (e["category"], e["slug"]))
    return {
        "min_esphome": MIN_ESPHOME,
        "categories": CATEGORIES,
        "templates": [public_entry(e) for e in ordered],
    }


def snippet_value(v):
    """Value shown for a var in the local include snippet."""
    if v["secret"]:
        name = v["name"]
        short = name[3:] if name.startswith("st_") else name
        return f"!secret {short}"
    if v["required"]:
        return "<value>"
    return v["default"] if v["default"] != "" else '""'


def snippet_vars(entry):
    """Ordered mapping for the local snippet: first var + all required vars."""
    pairs = {}
    if entry["vars"]:
        first = entry["vars"][0]
        pairs[first["name"]] = snippet_value(first)
    for v in entry["vars"]:
        if v["required"]:
            pairs[v["name"]] = snippet_value(v)
    return pairs


def render_doc(entry):
    slug = entry["slug"]
    cat = entry["category"]
    L = []
    L.append(f"# {entry['title']}")
    L.append("")
    L.append(entry["description"])
    L.append("")
    L.append("**Platforms:** " + " ".join(f"`{p}`" for p in entry["platforms"]))
    L.append("")
    req = ", ".join(entry["requires"]) if entry["requires"] else "none"
    L.append(f"**Requires:** {req}")
    L.append("")

    # Entities
    L.append("## Entities")
    L.append("")
    if entry["entities"]:
        L.append("| Domain | Name |")
        L.append("|---|---|")
        for ent in entry["entities"]:
            name = ent["name"]
            if ent.get("extra"):
                name = f"{name} ({ent['extra']})"
            L.append(f"| `{ent['domain']}` | {name} |")
    else:
        L.append("_No Home Assistant entities (preset / firmware-only)._")
    L.append("")

    # Usage
    L.append("## Usage")
    L.append("")
    L.append("Local include (repo checked out beside your config):")
    L.append("")
    L.append("```yaml")
    L.append("packages:")
    pairs = snippet_vars(entry)
    if pairs:
        L.append(f"  {slug}: !include")
        L.append(f"    file: esphome_sensor_templates/templates/{cat}/{slug}.yaml")
        inline = ", ".join(f"{k}: {v}" for k, v in pairs.items())
        L.append(f"    vars: {{ {inline} }}")
    else:
        L.append(f"  {slug}: !include esphome_sensor_templates/templates/{cat}/{slug}.yaml")
    L.append("```")
    L.append("")
    L.append("Remote include (pulled straight from GitHub):")
    L.append("")
    L.append("```yaml")
    L.append("packages:")
    L.append(f"  {slug}: github://OWNER/esphome_sensor_templates/templates/{cat}/{slug}.yaml@main")
    L.append("```")
    L.append("")
    L.append("> Replace `OWNER` with the GitHub owner/repo that hosts this library.")
    L.append("")

    # Variables
    if entry["vars"]:
        L.append("## Variables")
        L.append("")
        L.append("| Variable | Default | Description |")
        L.append("|---|---|---|")
        for v in entry["vars"]:
            if v["required"]:
                name = f"**{v['name']}**"
                default = "**(required)**"
            else:
                name = v["name"]
                default = f"`{v['default']}`" if v["default"] != "" else "`\"\"`"
            L.append(f"| {name} | {default} | {v['description']} |")
        L.append("")

    # Notes
    if entry["notes"]:
        L.append("## Notes")
        L.append("")
        for n in entry["notes"]:
            L.append(f"- {n}")
        L.append("")

    return "\n".join(L).rstrip() + "\n"


def write_docs(entries):
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    slugs = set()
    written = []
    for e in entries:
        slugs.add(e["slug"])
        path = DOCS_DIR / f"{e['slug']}.md"
        path.write_text(render_doc(e), encoding="utf-8")
        written.append(path)
    # prune stale docs
    deleted = []
    for md in DOCS_DIR.glob("*.md"):
        if md.stem not in slugs:
            md.unlink()
            deleted.append(md)
    return written, deleted


def render_readme_index(entries):
    L = [BEGIN_MARK]
    by_cat = {c: [] for c in CATEGORIES}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)
    for cat in CATEGORIES:
        items = sorted(by_cat.get(cat, []), key=lambda e: e["slug"])
        if not items:
            continue
        L.append("")
        L.append(f"### {cat.capitalize()}")
        L.append("")
        L.append("| Template | Description | Entities |")
        L.append("|---|---|---|")
        for e in items:
            count = len(e["entities"])
            ent = str(count) if count else "preset"
            L.append(f"| [{e['title']}](docs/{e['slug']}.md) | {e['description']} | {ent} |")
    L.append("")
    L.append(END_MARK)
    return "\n".join(L)


def update_readme(entries):
    text = README.read_text(encoding="utf-8")
    if BEGIN_MARK not in text or END_MARK not in text:
        raise ParseError("README.md is missing the GENERATED INDEX markers")
    new_block = render_readme_index(entries)
    pattern = re.compile(re.escape(BEGIN_MARK) + r".*?" + re.escape(END_MARK), re.DOTALL)
    updated = pattern.sub(lambda m: new_block, text, count=1)
    README.write_text(updated, encoding="utf-8")


def inject_index_html(catalog):
    if not INDEX_HTML.exists():
        print("note: web/index.html not found - skipping catalog injection (step 6)")
        return False
    text = INDEX_HTML.read_text(encoding="utf-8")
    compact = json.dumps(catalog, ensure_ascii=False, separators=(",", ":"))
    if not CATALOG_SCRIPT_RE.search(text):
        print("note: web/index.html has no <script id=\"catalog\"> element - skipping injection")
        return False
    updated = CATALOG_SCRIPT_RE.sub(
        lambda m: m.group(1) + compact + m.group(3), text, count=1)
    INDEX_HTML.write_text(updated, encoding="utf-8")
    return True


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    files = sorted(TEMPLATES_DIR.glob("*/*.yaml"))
    if not files:
        print("error: no template files found under templates/*/", file=sys.stderr)
        return 1

    entries = []
    parse_errors = []
    for path in files:
        try:
            entries.append(parse_file(path))
        except ParseError as exc:
            parse_errors.append(str(exc))

    errors = parse_errors + validate(entries)
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    # Write catalog.json
    catalog = build_catalog(entries)
    WEB_DIR.mkdir(parents=True, exist_ok=True)
    CATALOG_JSON.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Docs
    written_docs, deleted_docs = write_docs(entries)

    # README index
    update_readme(entries)

    # index.html injection
    injected = inject_index_html(catalog)

    # Summary
    per_cat = {c: 0 for c in CATEGORIES}
    for e in entries:
        per_cat[e["category"]] = per_cat.get(e["category"], 0) + 1
    print(f"Parsed {len(entries)} templates.")
    print("Per-category counts:")
    for c in CATEGORIES:
        print(f"  {c}: {per_cat[c]}")
    print("Files written:")
    print(f"  {CATALOG_JSON.relative_to(ROOT)}")
    print(f"  {len(written_docs)} docs/*.md" +
          (f" ({len(deleted_docs)} stale removed)" if deleted_docs else ""))
    print(f"  {README.relative_to(ROOT)} (index between markers)")
    print(f"  web/index.html: {'injected' if injected else 'skipped'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
