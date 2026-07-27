# consistent hash ring

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(data: &[u8]) → u64`

## What it does

consistent_hash_ring — hash ring + vnodes; key moves minimally when a node leaves.

Core idea: consistent hashing distributes keys across nodes. When a node leaves,
only a small fraction of keys (≈1/N) should be reassigned. THE ONE LAW: plant a
hash ring with known nodes and keys, remove a node, measure key remapping, and
assert the count is minimal and remapped keys move ONLY to/from the affected node.
A broken hash or naive linear probing would cause many keys to move.
When to use: distributed caching, load balancing, consistent rebalancing.

## Guarantee

When it runs, consistent hash ring guarantees assert!(new_loc == 1 || new_loc == 2, "node-3 key {i} moved to {new_loc}, not a survivor") (proven by rustc-run).

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
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
