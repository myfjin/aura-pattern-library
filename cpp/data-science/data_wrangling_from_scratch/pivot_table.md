# pivot table

**Language:** C++ · **Sphere:** data-science · **Category:** Data Wrangling From Scratch

**Signature:** `(records: List[Dict[str, Any]], row_key: str, col_key: str, val_key: str, agg_func: str) → Dict[Any, Dict[Any, float]]`

## What it does

pivot_table.cpp
Long to wide pivot table with margins.

## Guarantee

When it runs, pivot table guarantees pivot['A']['US'] == 150; pivot['B']['EU'] == 125; row_totals['A'] == 225 (proven by run on the PY original).

**Checkable constraints:**

- `total_from_rows == total_from_records`
- `total_from_cols == total_from_records`
- `pivot['A']['US'] == 150`
- `pivot['B']['EU'] == 125`
- `row_totals['A'] == 225`
- `row_totals['B'] == 155`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def pivot_table(records: List[Dict[str, Any]], row_key: str, col_key: str, val_key: str, agg_func: str = "sum") -> Dict[Any, Dict[Any, float]]:`, `def compute_margins(pivot: Dict[Any, Dict[Any, float]]) -> Dict[str, Dict[Any, float]]:`
**Valid input:** `records` non-empty; `row_key`, `col_key`, `val_key` exist; `val_key` values are numeric; `agg_func` is `"sum"` or `"count"`.
**Core:** Pivot long-format records into a wide table, supporting sum and count aggregation, plus row and column margin totals.
**Assert:** On planted records, pivot cells match hand-computed values (A/US = 150, B/EU = 125), row totals equal the record sum, and column totals equal the record sum.
**⚠️ Defect:** For any `agg_func` other than `"sum"` or `"count"` (e.g., `"mean"`, `"min"`, `"max"`), `pivot_table` stores values in a list but never computes the final aggregation, returning a list in the cell instead of a float. This is a silent failure for unsupported aggregations. The docstring does not warn that only sum and count are implemented.

---
*△ AURA Pattern Library — © Reality Optimizer*
