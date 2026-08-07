# consistent hash ring

**Language:** Python · **Oracle sphere:** rust (this file is the Python twin) · **Category:** distributed

## What it does

Consistent Hash Ring Implementation

This module provides a consistent hash ring implementation that distributes
keys across nodes in a way that minimizes redistribution when nodes are
added or removed.

## Guarantee

When it runs, consistent hash ring guarantees assert!(new_loc == 1 || new_loc == 2, "node-3 key {i} moved to {new_loc}, not a survivor") (proven by rustc-run on the RUST original).

**Checkable constraints:**

- `assert!(count_1 > 100 && count_1 < 600, "node 1 should have a reasonable fraction of keys")`
- `assert!(new_loc == 1 || new_loc == 2, "node-3 key {i} moved to {new_loc}, not a survivor")`
- `assert!(moved_set.contains(&i), "node-3 key {i} must be reported as moved")`
- `assert_eq!(new_loc as usize, initial_dist[i as usize], "key {i} moved but shouldn't have")`
- `assert!(!moved_set.contains(&i), "non-node-3 key {i} must not be reported moved")`
- `assert_eq!(moved_keys.len(), node3_keys, "moved count must equal exactly node-3's key count")`
- `assert_eq!(node3_keys, count_3, "node-3 key count must match the initial distribution")`
- `assert!(moved_keys.len() < 500, "a correct ring moves only ~1/N, never a majority")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
