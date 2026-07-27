# group by aggregate

**Language:** Python · **Sphere:** data-science · **Category:** Data Wrangling From Scratch

**Signature:** `(records: List[Dict[str, Any]], group_keys: List[str], agg_col: str, agg_func: str) → Dict[tuple, float]`

## What it does

Group-By Aggregation (Multi-Key).

Group records by one or more keys, then aggregate (sum, mean, count, min, max).
We verify against a brute-force nested-loop computation on the same data.

## Guarantee

When it runs, group by aggregate guarantees result_sum == brute_sum; result_mean == brute_mean; result_count == brute_count (weak-grade: directional, proven by run).

**Checkable constraints:**

- `result_sum == brute_sum`
- `result_mean == brute_mean`
- `result_count == brute_count`
- `result_min == brute_min`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def group_by_aggregate(records: List[Dict[str, Any]], group_keys: List[str], agg_col: str, agg_func: str) -> Dict[tuple, float]:`, `def brute_force_aggregate(records: List[Dict[str, Any]], group_keys: List[str], agg_col: str, agg_func: str) -> Dict[tuple, float]:`
**Valid input:** `records` non-empty; `group_keys` and `agg_col` exist in every record; `agg_func` is one of `"sum"`, `"mean"`, `"count"`, `"min"`, `"max"`.
**Core:** Multi-key group-by aggregation. Collects values per group key tuple and applies the requested aggregation function. A brute-force reference implementation is provided for parity checks.
**Assert:** On planted records grouped by `(category, region)` and `(category)`, the function matches the brute-force reference for sum, mean, count, and min.
**⚠️ Defect:** `group_by_aggregate` silently returns `None` for every group if `agg_func` is not one of the five supported strings, instead of raising an error. It also does not validate that `group_keys` or `agg_col` exist in a record, so a missing key raises an unhelpful `KeyError` only at access time. The return type claims `Dict[tuple, float]`, but for unsupported functions the values are lists or `None`.

---
*△ AURA Pattern Library — © Reality Optimizer*
