# rwlock cache

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(key: u64) → u64`

## What it does

rwlock_cache — a read-through cache guarded by a std `RwLock`, single-fill on miss.

Core idea: many concurrent readers share the read lock; a miss upgrades to the write
lock and fills EXACTLY once (double-checked under the write lock). THE ONE LAW: fire a
concurrent herd of lookups of the same missing key and assert the expensive loader ran
exactly once and every reader saw the same value — a cache without the write-guard
re-check would run the loader many times (thundering herd), which the load-count assert
catches. When to use: read-heavy caches with costly misses.

## Guarantee

When it runs, rwlock cache guarantees assert_eq!(loads, 1, "loader ran {loads} times (herd not suppressed)") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(loads, 1, "loader ran {loads} times (herd not suppressed)")`
- `assert!(results.iter().all(|&v| v == key * 10), "readers disagreed on cached value")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
