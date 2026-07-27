# fenwick tree

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

**Signature:** `() → None`

## What it does

Fenwick Tree (Binary Indexed Tree) implementation with comprehensive functionality.
Supports point updates and prefix/range sum queries in O(log n) time.

## Guarantee

When it runs, fenwick tree guarantees ft.prefix_sum(5) == 28; ft.range_sum(1, 3) == 16; ft.range_sum(0, 0) == 2 and ft.range_sum(5, 5) == 8 (proven by run).

**Checkable constraints:**

- `ft.prefix_sum(5) == 28`
- `ft.range_sum(1, 3) == 16`
- `ft.range_sum(0, 0) == 2 and ft.range_sum(5, 5) == 8`
- `ft.prefix_sum(9) == 28`
- `ft.range_sum(3, 3) == 0 and ft.prefix_sum(9) == 20`
- `fresh.prefix_sum(idx) == sum(arr[:idx + 1])`
- `fresh.range_sum(left, right) == sum(arr[left:right + 1])`
- `fresh.prefix_sum(i) == sum(arr[:i + 1])`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
