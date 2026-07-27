# red black tree

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

**Signature:** `() → None`

## What it does

Red-Black tree with insert, delete, and a full property validator, kept balanced
by recoloring and rotations around a shared NIL sentinel.

Use as a self-balancing ordered set of ints with O(log n) insert/delete and
in-order iteration.

Guarantees (self-test): after 50 sequential inserts and after deletes every
Red-Black property holds (black root, no red-red edge, equal black heights),
inorder is sorted, and a 600-op fuzz re-validates the invariants against a set
oracle.

## Guarantee

When it runs, red black tree guarantees sum(traversal) == 1275; ok; traversal == list(range(1, 51)) (proven by run).

**Checkable constraints:**

- `ok`
- `traversal == list(range(1, 51))`
- `sum(traversal) == 1275`
- `ok`
- `remaining == [k for k in range(1, 51) if k % 10 != 0]`
- `len(remaining) == 45`
- `not rb.delete(100)`
- `len(rb.inorder_traversal()) == 45`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
