# kd tree

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

## What it does

A complete k-d tree implementation for 2D points with insert, nearest neighbor,
and range search functionality.

## Guarantee

When it runs, kd tree guarantees abs(d_got - d_true) < 1e-09; tree.nearest_neighbor(points[17]) == points[17]; got == want (proven by run).

**Checkable constraints:**

- `tree.nearest_neighbor(points[17]) == points[17]`
- `abs(d_got - d_true) < 1e-09`
- `got == want`
- `len(tree.range_search((0, 0), (100, 100))) == 200`
- `tree.range_search((200, 200), (300, 300)) == []`
- `KDTree().nearest_neighbor((1, 1)) is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
