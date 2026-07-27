# atomic spinlock

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

## What it does

atomic_spinlock — a spinlock built from AtomicBool::compare_exchange.

Core idea: an AtomicBool holds the lock state (false=free, true=locked). To acquire,
spin via CAS until the lock transitions from false→true. THE ONE LAW: N threads each
increment a shared counter under the spinlock. If the lock doesn't work, increments race
and we lose updates. The final count must equal N × increments_per_thread (exact, no loss).
When to use: a minimal synchronization primitive when Mutex overhead is unwelcome.

## Guarantee

When it runs, atomic spinlock guarantees assert_eq!(final_count, expected, "spinlock lost updates under contention") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(final_count, expected, "spinlock lost updates under contention")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
