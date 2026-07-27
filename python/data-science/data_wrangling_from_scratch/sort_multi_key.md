# sort multi key

**Language:** Python · **Sphere:** data-science · **Category:** Data Wrangling From Scratch

**Signature:** `(records: List[Dict[str, Any]], keys: List[tuple]) → List[Dict[str, Any]]`

## What it does

Multi-Key Sorting with Mixed Order (asc/desc).

Sort records by multiple keys, each asc or desc.
We verify STABILITY: records with equal keys stay in original order.

## Guarantee

When it runs, sort multi key guarantees sorted_categories == ['A', 'A', 'A', 'B', 'B']; a_values == [20, 20, 10]; a_20_orders == [2, 4] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `sorted_categories == ['A', 'A', 'A', 'B', 'B']`
- `a_values == [20, 20, 10]`
- `a_20_orders == [2, 4]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def multi_key_sort(records: List[Dict[str, Any]], keys: List[tuple]) -> List[Dict[str, Any]]:`, `def sort_key(record):`
**Valid input:** `records` non-empty; each `key` tuple is `(key_name: str, is_asc: bool)`; sortable values for the requested keys.
**Core:** Stable multi-key sort with per-key ascending/descending direction. Uses Python's `sorted` with a generated sort key.
**Assert:** On planted records with ties, sorting by `(category, asc)` then `(value, desc)` yields categories [A, A, A, B, B], A values [20, 20, 10], and tied rows preserve their original order (stability check: A/20 records keep order [2, 4]).
**⚠️ Defect:** For descending string keys, the sort key is `(1, val)`, which does **not** reverse string order — the leading `1` is constant for all strings, so comparison falls back to ascending string order. Only descending numeric keys work correctly because they are negated. The demo uses a descending numeric key, so the string bug is hidden. Also `sort_key` is exposed as a module-level function despite being an internal helper.

---
*△ AURA Pattern Library — © Reality Optimizer*
