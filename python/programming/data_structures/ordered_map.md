# ordered map

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

## What it does

Sorted dictionary backed by an unbalanced binary search tree, implementing the
MutableMapping interface with ordered iteration and range/bound queries.

Use as a dict whose keys iterate in sorted order and that answers lower_bound
(smallest key >= k), upper_bound (smallest key > k), and half-open range(start,
end) queries.

Guarantees (self-test): keys iterate sorted, bounds are exact, range [3,7) yields
exactly 3,4,5,6 (the below-start leakage bug is pinned), all three BST delete
cases hold, and a 500-op fuzz agrees with a plain-dict oracle.

## Guarantee

When it runs, ordered map guarantees sum(omap.keys()) == 45; omap.lower_bound(4).key == 4; omap.upper_bound(4).key == 5 (proven by run).

**Checkable constraints:**

- `len(omap) == 9`
- `list(omap) == list(range(1, 10))`
- `omap[5] == 'five'`
- `sum(omap.keys()) == 45`
- `omap[5] == 'FIVE' and len(omap) == 9`
- `omap.lower_bound(4).key == 4`
- `omap.upper_bound(4).key == 5`
- `omap.lower_bound(10) is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
