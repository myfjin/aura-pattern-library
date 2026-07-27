# work stealing deque

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `() → Steal`

## What it does

work_stealing_deque — a lock-free deque where the owner uses one end, stealers the other.

Core idea: the Chase-Lev work-stealing deque. A single owner thread pushes and pops at
`bottom` (LIFO, cache-friendly); any number of stealer threads take from `top` (FIFO).
There is NO lock — `top` and `bottom` are atomics, the buffer holds atomics, and the
only synchronization is a CAS on `top`. The subtle case is a single remaining element,
where the owner's pop and a steal both target it: exactly one wins the CAS on `top`.
THE ONE LAW: the owner pushes N items, then stealers steal concurrently while the owner
pops. Each item is taken exactly once (owner-popped + stolen sums to the planted total,
and no value is counted twice). A serialized-under-a-Mutex "deque" is not this pattern;
the concurrency here is genuine. When to use: task schedulers and parallel work loops.

## Guarantee

When it runs, work stealing deque guarantees assert_eq!(total_sum, expected_sum, "sum mismatch: items lost or double-counted") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(total_cnt, n_items, "item count mismatch: {total_cnt} taken, expected {n_items} (lost or duplicated)")`
- `assert_eq!(total_sum, expected_sum, "sum mismatch: items lost or double-counted")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
