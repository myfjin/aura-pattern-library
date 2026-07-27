# csv type inference

**Language:** Python · **Sphere:** data-science · **Category:** Data Wrangling From Scratch

**Signature:** `(value: str) → str`

## What it does

CSV Type Inference.

Read CSV and infer column types (int, float, date, str).
We verify every column against planted data with explicit types.

## Guarantee

When it runs, csv type inference guarantees types['id'] == 'int'; types['age'] == 'int'; types['salary'] == 'float' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `types['id'] == 'int'`
- `types['age'] == 'int'`
- `types['salary'] == 'float'`
- `types['date'] == 'date'`
- `types['name'] == 'str'`
- `'' in age_values`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def infer_type(value: str) -> str:`, `def infer_column_types(rows: List[Dict[str, str]]) -> Dict[str, str]:`
**Valid input:** `rows` is a non-empty list of dicts representing CSV rows. Values are strings.
**Core:** Infers a column type from the most common non-missing type among its string values: int (parses as int), float (parses as float), date (`YYYY-MM-DD`), or str (fallback). Missing/"none" values are ignored.
**Assert:** On planted rows with id→int, age→int (with one missing), salary→float, date→date, name→str, the inferred types match the planted expectations.
**⚠️ Defect:** `infer_type` tries `int()` before the date regex, so a column of ISO dates without hyphens (e.g., "20240115") or a column of integer-like IDs is inferred as int, not date. The date regex is strictly `YYYY-MM-DD` and ignores times, time zones, and other separators. `infer_column_types` assumes every row has exactly the keys of `rows[0]` and does not validate consistency; rows with missing or extra columns silently shift column inference.

---
*△ AURA Pattern Library — © Reality Optimizer*
