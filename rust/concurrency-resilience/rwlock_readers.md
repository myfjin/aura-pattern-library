# rwlock readers

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

## What it does

rwlock_readers — multiple readers coexist; writer is exclusive and blocks readers.

Core idea: std::sync::RwLock allows many readers or one writer, never both.
THE ONE LAW: spawn R reader threads and W writer threads. Measure concurrent reader
count; it must be > 1 (readers truly run in parallel) and 0 whenever a writer holds
the lock (exclusivity). A broken lock allows readers during writes or writer stalls.
When to use: protecting read-heavy shared state.

## Guarantee

When it runs, rwlock readers guarantees assert_eq!(reader_count, 0, "writer held lock while {} readers active", reader_count) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(reader_count, 0, "writer held lock while {} readers active", reader_count)`
- `assert!(max_read > 1, "readers never ran concurrently (max concurrent: {})", max_read)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
