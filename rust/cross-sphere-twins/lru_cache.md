# lru cache

**Language:** Rust · **Sphere:** rust · **Category:** cross-sphere-twins

**Signature:** `(key: u32, value: u32) → ?`

## What it does

lru_cache — LRU eviction; exact eviction order vs brute-force reference.

Core idea: cache with fixed size. On insertion when full, evict the least-recently-used.
THE LAW: execute an access trace, track eviction order, and assert it matches a
brute-force reference implementation that replays the entire trace.
When to use: memory-constrained caches, page replacement, working-set management.

## Guarantee

When it runs, lru cache guarantees assert_eq!(cache.data, expected, "cache state matches") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(cache.data, expected, "cache state matches")`
- `assert!(!cache2.data.contains_key(&2), "2 was evicted")`
- `assert!(cache2.data.contains_key(&1), "1 is still cached")`
- `assert!(!cache3.data.contains_key(&1))`
- `assert_eq!(cache3.get(2), Some(20))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
