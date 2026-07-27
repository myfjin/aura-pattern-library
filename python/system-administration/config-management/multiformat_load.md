# multiformat load

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(filepath: str) → ?`

## What it does

Multiformat config loader: load json, ini, dotenv formats; reject syntax errors.
Failure simulated: invalid json/ini/dotenv syntax; malformed format.
Asserts: exact format error with file type; valid configs of each type load.

## Guarantee

When it runs, multiformat load guarantees result['port'] == 8080; result['host'] == 'localhost'; result['server']['host'] == 'localhost' (proven by run).

**Checkable constraints:**

- `result['host'] == 'localhost'`
- `result['port'] == 8080`
- `result['server']['host'] == 'localhost'`
- `result['database']['name'] == 'mydb'`
- `result['HOST'] == 'localhost'`
- `result['PORT'] == '8080'`
- `'JSON' in str(e)`
- `'INI' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def load_config(filepath):`
**Valid input:** `filepath` has a `.json`, `.ini`, or `.env` suffix and contains valid syntax for that format.
**Core:** Dispatches to `json.load`, `configparser.ConfigParser`, or a simple dotenv parser based on file extension.
**Assert:** Valid JSON, INI, and dotenv files load; invalid syntax for each format and unsupported extensions are rejected with format-specific error messages.
**⚠️ Defect:** INI values are returned as strings (configparser default), so type information is lost. The dotenv parser is duplicated from `dotenv_parse.py` and inherits its limitations. YAML/TOML are unsupported.

---
*△ AURA Pattern Library — © Reality Optimizer*
