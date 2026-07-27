# interval tree

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

## What it does

Augmented BST of intervals — each node caches its subtree's maximum endpoint —
for efficient overlap queries.

Use to insert and delete intervals and find all that overlap a query interval;
the max_end augmentation prunes subtrees that cannot contain a hit. Touching
endpoints count as an overlap (start <= end).

Guarantees (self-test): overlap results match a brute-force oracle across hundreds
of queries and through 40 deletes (max_end recomputed on the way up), inorder is
sorted by start, and non-Interval or inverted arguments are refused.

## Guarantee

When it runs, interval tree guarantees sum((h.start for h in tree.query_overlap(Interval(-10, 100)))) == 16; sorted((h.data for h in hits)) == ['a', 'b']; [h.data for h in tree.query_overlap(Interval(9, 9))] == [] (proven by run).

**Checkable constraints:**

- `sorted((h.data for h in hits)) == ['a', 'b']`
- `[h.data for h in tree.query_overlap(Interval(9, 9))] == []`
- `sorted((h.data for h in tree.query_overlap(Interval(5, 6)))) == ['b', 'c']`
- `sorted((h.data for h in tree.query_overlap(Interval(-10, 100)))) == list('abcd')`
- `tree.delete(b) is True`
- `tree.delete(b) is False`
- `sorted((h.data for h in tree.query_overlap(Interval(2, 3)))) == ['a']`
- `len(tree.inorder_traversal()) == 3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
