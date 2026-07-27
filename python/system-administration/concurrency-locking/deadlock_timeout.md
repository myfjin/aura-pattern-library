# deadlock timeout

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(lock1: TimeoutLock, lock2: TimeoutLock, lock_order: List[int], results: dict, thread_id: str, timeout: float, barrier: Barrier) → ?`

## What it does

deadlock_timeout: detect and break potential deadlocks with a timeout mechanism.
Failure simulated: two threads try to acquire locks in opposite order (A: lock1→lock2,
B: lock2→lock1), creating a cycle. Without timeouts, this deadlocks forever. With timeouts,
the second-to-acquire times out and backs off.
Recovery asserted: at least one thread times out (detecting the deadlock cycle) and retreats,
allowing both threads to finish. A no-op timeout would hang forever.

## Guarantee

When it runs, deadlock timeout guarantees timed_out_count > 0; not t_a.is_alive(); not t_b.is_alive() (weak-grade: directional, proven by run).

**Checkable constraints:**

- `timed_out_count > 0`
- `not t_a.is_alive()`
- `not t_b.is_alive()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class TimeoutLock:`, `def __init__(self):`, `def acquire(self, timeout=None):`, `def release(self):`, `def acquirer(lock1, lock2, lock_order, results, thread_id, timeout, barrier):`
**Valid input:** `timeout` is a non-negative number or `None`; locks are `TimeoutLock` instances; two threads use opposite lock orders to create a cycle.
**Core:** Condition-variable-based lock with timed `acquire`. If the lock is not available within `timeout`, returns `False` instead of blocking forever, allowing the caller to back off and break deadlock.
**Assert:** Two threads acquiring two locks in opposite order produce at least one timeout, and neither thread hangs.
**⚠️ Defect:** `release` does not verify that the calling thread owns the lock, so a thread can release a lock it never acquired. There is no deadlock *detection* (cycle detection), only timeout-and-backoff, so the same cycle can recur.

---
*△ AURA Pattern Library — © Reality Optimizer*
