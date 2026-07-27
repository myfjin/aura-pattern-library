# refuse start on invalid

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(config_file: str, required_fields: List[str]) → ?`

## What it does

Refuse start on invalid config: raise PRECISE error with field name, never silent default.
Failure simulated: invalid config provided; code silently defaults instead of refusing.
Asserts: exact field name in error; startup blocks; valid config allows start.

## Guarantee

When it runs, refuse start on invalid guarantees config['port'] == 8080; config['timeout'] == 30.0; config['host'] == 'localhost' (proven by run).

**Checkable constraints:**

- `config['host'] == 'localhost'`
- `config['port'] == 8080`
- `config['timeout'] == 30.0`
- `'port' in str(e).lower()`
- `'refuse' in str(e).lower()`
- `'port' in str(e).lower()`
- `'int' in str(e).lower()`
- `'port' in str(e).lower()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def validate_and_load_config(config_file, required_fields):`
**Valid input:** `config_file` is a JSON file; `required_fields` is a list of top-level keys; when present, `port` must be an int in 1–65535 and `timeout` must be a positive number.
**Core:** Loads JSON config and validates required fields plus hardcoded semantic checks for `port` and `timeout`. Raises precise `ValueError` messages prefixed with "REFUSE START".
**Assert:** Valid config loads; missing required field, wrong port type, out-of-range port, negative timeout, missing file, and invalid JSON are all rejected with descriptive errors.
**⚠️ Defect:** Validation rules for `port` and `timeout` are hardcoded, so the function cannot validate arbitrary config schemas. It does not return the loaded config in a structured way; callers must parse the returned dict themselves.

---
*△ AURA Pattern Library — © Reality Optimizer*
