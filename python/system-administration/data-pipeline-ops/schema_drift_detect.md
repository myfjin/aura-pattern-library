# schema drift detect

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 19 · Data pipeline ops

**Signature:** `(records: List[dict], schema_path: str) → ?`

## What it does

Schema Drift Detection Pattern
Track expected schema. Detect when records deviate:
- New fields added
- Fields removed
- Field types changed
Assert: drift is detected and named explicitly.

## Guarantee

When it runs, schema drift detect guarantees schema1 == {'id': 'str', 'name': 'str', 'age': 'int'}; 'email' in new_field_drifts[0]; 'age' in type_change_drifts[0] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(drifts1) == 0`
- `schema1 == {'id': 'str', 'name': 'str', 'age': 'int'}`
- `len(drifts2) > 0`
- `len(new_field_drifts) == 1`
- `'email' in new_field_drifts[0]`
- `len(type_change_drifts) == 1`
- `'age' in type_change_drifts[0]`
- `'int->float' in type_change_drifts[0]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def detect_schema_drift(records, schema_path):`, `def infer_schema(records):`, `class SchemaDriftError(Exception):`
**Valid input:** `records` is a non-empty list of dicts; `schema_path` is a writable JSON path.
**Core:** Infers a schema `{field: type_name}` from the records and stores it on first run; on subsequent runs, compares the current schema to the stored schema and reports new fields, removed fields, and type changes.
**Assert:** First run stores schema with no drift; adding `'email'` and changing `'age'` from int to float reports both a new-field and a type-change drift; removing `'ssn'` reports a removed-field drift.
**⚠️ Defect:** `SchemaDriftError` is defined but never raised; drift is returned as a plain list of strings. Schema inference marks a field as `'mixed'` if type conflicts occur within the same batch, but this mixed type is not explicitly reported as drift. The stored schema is always updated after each run, so drift is ephemeral unless captured by the caller.

---
*△ AURA Pattern Library — © Reality Optimizer*
