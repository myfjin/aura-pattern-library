# treap

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

## What it does

Treap — a randomized balanced BST that is a search tree on values and a max-heap
on random priorities — with insert, erase-one, membership, and order statistics.

Use as an ordered multiset with expected-O(log n) operations and kth-smallest
queries via subtree-size augmentation.

Guarantees (self-test): inorder equals the sorted input, the heap invariant on
priorities holds, kth equals the sorted rank for every k, erase removes exactly
one duplicate, and a 500-op fuzz agrees with a sorted-list oracle.

## Guarantee

When it runs, treap guarantees t.size() == 10; t.size() == 11 and t.to_list().count(7) == 2; t.size() == 10 (proven by run).

**Checkable constraints:**

- `t.to_list() == sorted(values)`
- `t.size() == 10`
- `_check_heap(t.root)`
- `t.kth(k) == truth[k]`
- `t.find(7) is True and t.find(9) is False`
- `t.size() == 11 and t.to_list().count(7) == 2`
- `t.erase(7) is True`
- `t.to_list().count(7) == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
