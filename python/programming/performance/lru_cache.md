# lru cache

**Language:** Python · **Oracle sphere:** rust (this file is the Python twin) · **Category:** performance

## What it does

Thread-safe LRU cache with optional per-entry TTL expiry.

A fixed-capacity cache backed by an OrderedDict under an RLock: reads and
writes mark keys as recently used, the least-recently-used key is evicted at
capacity, and entries may carry a time-to-live after which get() returns None.
Use it as a bounded in-process cache where both recency eviction and freshness
matter. Guarantees (self-test oracle): LRU eviction order holds, get() refreshes
recency (a just-read key survives the next eviction), TTL expiry fires on a
fake clock, and concurrent writes from many threads are not lost or corrupted.

## Guarantee

When it runs, lru cache guarantees assert_eq!(cache.data, expected, "cache state matches") (proven by rustc-run on the RUST original).

**Checkable constraints:**

- `assert_eq!(cache.data, expected, "cache state matches")`
- `assert!(!cache2.data.contains_key(&2), "2 was evicted")`
- `assert!(cache2.data.contains_key(&1), "1 is still cached")`
- `assert!(!cache3.data.contains_key(&1))`
- `assert_eq!(cache3.get(2), Some(20))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
