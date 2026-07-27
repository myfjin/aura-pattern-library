# skip list

**Language:** Python · **Sphere:** rust · **Category:** data structures

**Signature:** `() → usize`

## What it does

Probabilistic skip list mapping int keys to values with randomized level
promotion, giving expected O(log n) search, insert, and delete.

Use as an ordered map with sorted iteration and range queries, without the
rotation machinery of a balanced tree.

Guarantees (self-test): iteration stays sorted after shuffled inserts, range
queries return exact contiguous slices, insert on an existing key updates in
place, delete reports honestly, and a 600-op fuzz agrees with a dict oracle.

## Guarantee

When it runs, skip list guarantees assert_eq!(SkipList::new(1).iter_sorted().len(), 0, "empty skip list") (proven by rustc-run on the RUST original).

**Checkable constraints:**

- `assert_eq!(sl.iter_sorted(), sorted, "skip-list iteration must match BTreeSet order")`
- `assert_eq!(sl.search(v), reference.contains(&v), "search({v}) must match reference")`
- `assert!(sl.max_level_used() > 1, "a real skip list builds >1 level, got {}", sl.max_level_used())`
- `assert!(has_express, "at least one node must have an express-lane link above level 0")`
- `assert_eq!(sl.iter_sorted().len(), vals.len(), "duplicate insert does not grow the set")`
- `assert_eq!(SkipList::new(1).iter_sorted().len(), 0, "empty skip list")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
