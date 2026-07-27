# segment tree

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

## What it does

Pointer-based segment tree over a fixed-length numeric array supporting range-sum
and range-min queries with point updates.

Use for O(log n) range aggregate queries on mutable data; each node caches the sum
and min of its span, refreshed along the root-to-leaf path on update.

Guarantees (self-test): planted sums/mins exact, a point update propagates to both
aggregates, a 600-op fuzz agrees with a plain-list oracle, and inverted or
out-of-bounds ranges and empty construction are refused.

## Guarantee

When it runs, segment tree guarantees st.range_sum(0, 9) == 55; st.range_sum(10, 19) == 155; st.range_sum(0, 99) == 5050 (proven by run).

**Checkable constraints:**

- `st.range_sum(0, 9) == 55`
- `st.range_sum(10, 19) == 155`
- `st.range_sum(0, 99) == 5050`
- `st.range_min(0, 9) == 1`
- `st.range_min(10, 19) == 11`
- `st.range_min(50, 99) == 51`
- `st.range_sum(0, 4) == 15`
- `st.range_sum(0, 4) == 112`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
