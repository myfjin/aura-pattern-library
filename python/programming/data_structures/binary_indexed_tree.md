# binary indexed tree

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

**Signature:** `() → None`

## What it does

Binary Indexed Tree (Fenwick tree) for prefix sums with point updates, plus a
Query wrapper that turns raw delta-updates into set-value semantics.

Use for O(log n) prefix-sum and range-sum queries over a mutable 1-indexed array.
BinaryIndexedTree.update adds a delta; Query.update overwrites an index to an
exact value by computing the implied delta.

Guarantees (self-test): planted sums exact, set-vs-delta semantics distinguished,
an 800-op fuzz agrees with a plain-list oracle, and out-of-bounds or inverted
ranges raise IndexError / ValueError.

## Guarantee

When it runs, binary indexed tree guarantees q.prefix_sum(5) == 14; q.range_sum(2, 4) == 6; q.range_sum(1, 20) == 14 (proven by run).

**Checkable constraints:**

- `q.prefix_sum(5) == 14`
- `q.range_sum(2, 4) == 6`
- `q.range_sum(1, 20) == 14`
- `q.range_sum(3, 3) == 10`
- `q.prefix_sum(5) == 20`
- `bit.prefix_sum(20) == before + 5`
- `fresh.prefix_sum(i) == sum(oracle[1:i + 1])`
- `fresh.range_sum(l, r) == sum(oracle[l:r + 1])`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
