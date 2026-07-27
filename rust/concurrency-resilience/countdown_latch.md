# countdown latch

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

## What it does

countdown_latch — a latch that releases all waiters only when count reaches zero.

Core idea: a shared counter and Condvar. Tasks decrement the counter via count_down();
waiters call wait() and block until the counter hits 0. THE ONE LAW: spawn N workers
that count down on staggered delays; spawn M waiters. The instant a waiter unblocks it
asserts remaining() == 0 — proving no waiter is released before the count is fully spent.
A no-op (broken) latch releases a waiter while remaining() is still > 0, failing the
assertion. When to use: coordinating completion of a fixed number of tasks.

## Guarantee

When it runs, countdown latch guarantees assert_eq!(remaining, 0, "waiter released while {remaining} count remained") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(remaining, 0, "waiter released while {remaining} count remained")`
- `assert_eq!(completed, n_waiters, "not all waiters unblocked")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
