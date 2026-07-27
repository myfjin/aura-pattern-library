# semaphore limit

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

## What it does

semaphore_limit — counting semaphore from Mutex+Condvar; max in-flight never exceeds limit.

Core idea: implement a counting semaphore using std::sync::Mutex + CondVar. Tracks
in-flight permits and blocks acquires when exhausted. THE ONE LAW: spawn threads that
acquire/release permits, then assert the max concurrent in-flight never exceeds the
semaphore limit — an unguarded semaphore would allow unlimited in-flight.
When to use: resource pooling, connection limits, concurrency caps.

## Guarantee

When it runs, semaphore limit guarantees assert!(observed_max <= capacity, "max in-flight {} exceeded limit {}", observed_max, capacity); assert!(observed_max > 0, "nothing ran") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(observed_max <= capacity, "max in-flight {} exceeded limit {}", observed_max, capacity)`
- `assert!(observed_max > 0, "nothing ran")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
