# schema validate

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(config: dict, schema: dict) → ?`

## What it does

Schema validation: reject invalid config keys/types, accept valid config.
Failure simulated: missing required key, wrong type.
Asserts: exact field name in error message; valid config loads without error.

## Guarantee

When it runs, schema validate guarantees schema_validate(valid, schema); 'timeout' in str(e); 'port' in str(e) and 'str' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `schema_validate(valid, schema)`
- `'timeout' in str(e)`
- `'port' in str(e) and 'str' in str(e)`
- `schema_validate(extra, schema)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def schema_validate(config, schema):`
**Valid input:** `config` is a dict; `schema` is a dict mapping required keys to expected type names as strings (e.g., `"str"`, `"int"`).
**Core:** Checks that every key in `schema` exists in `config` and that its value's `type().__name__` matches the expected type name.
**Assert:** Valid config passes; missing required key and wrong type are rejected with the field name in the error; extra keys are allowed.
**⚠️ Defect:** Type checking is string-name based, so legitimate subclasses or numeric compatibility (e.g., `bool` is a subclass of `int`) are not handled. Nested schemas, optional keys, and value-range constraints are unsupported.

---
*△ AURA Pattern Library — © Reality Optimizer*
