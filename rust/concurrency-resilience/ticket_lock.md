# ticket lock

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `() → u64`

## What it does

ticket_lock — a fair ticket lock with atomic next-ticket and now-serving.

Core idea: each thread acquires a ticket (via atomic fetch_add on next-ticket),
then spins until now-serving matches its ticket. Fairness is guaranteed: FIFO.
THE ONE LAW: N threads contend for the lock; their acquire order must match ticket
order (provable by observing the sequence of release-to-acquire transitions).
When to use: when lock fairness (no starvation) is critical under high contention.

## Guarantee

When it runs, ticket lock guarantees assert_eq!(final_count as usize, n_threads * increments, "lost updates or double-counting under ticket lock") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(final_count as usize, n_threads * increments, "lost updates or double-counting under ticket lock")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
