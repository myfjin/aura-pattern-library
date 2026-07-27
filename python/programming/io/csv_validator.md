# csv validator

**Language:** Python · **Sphere:** programming · **Category:** Io

**Signature:** `(csv_data: str, schema: List[FieldSchema], delimiter: str) → Dict[str, Union[List[Dict[str, Any]], List[ValidationError]]]`

## What it does

CSV Validator and Transformer Module

This module provides classes for validating and transforming CSV data based on a schema.

## Guarantee

When it runs, csv validator guarantees john['age'] == 30; john['salary'] == 50000.5 and isinstance(john['salary'], float); charlie['salary'] == 70000.25 (proven by run).

**Checkable constraints:**

- `john['id'] == 1 and isinstance(john['id'], int)`
- `john['age'] == 30`
- `john['salary'] == 50000.5 and isinstance(john['salary'], float)`
- `john['active'] is True`
- `jane['active'] is True`
- `charlie['active'] is True`
- `charlie['salary'] == 70000.25`
- `len(salary_errors) == 1 and salary_errors[0].row_index == 3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
