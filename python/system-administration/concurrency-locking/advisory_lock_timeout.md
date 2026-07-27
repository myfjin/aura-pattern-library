# advisory lock timeout

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(filename: ?, timeout_sec: ?) → ?`

## What it does

advisory_lock_timeout: Non-blocking (LOCK_NB) advisory lock with timeout fallback.
Failure simulated: launch two processes; first acquires and holds, second tries non-blocking
acquire, gets EWOULDBLOCK, then waits with a timeout. Recovery asserted: the non-blocking
attempt fails (EAGAIN), then with a timeout wait it succeeds after the holder releases.
A no-op timeout that doesn't actually wait would fail this test (would return immediately).

## Guarantee

When it runs, advisory lock timeout guarantees results.get('holder_acquired'); results.get('holder_released'); results.get('waiter_acquired') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `results.get('holder_acquired')`
- `results.get('holder_released')`
- `results.get('waiter_acquired')`
- `waiter_elapsed >= 0.25`
- `waiter_elapsed < hold_time + 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def advisory_lock_with_timeout(filename, timeout_sec):`, `def holder(filename, results_dict, hold_time):`, `def waiter_with_timeout(filename, results_dict, timeout_val):`
**Valid input:** `filename` is a writable lockfile path; `timeout_sec` and `hold_time` are positive numbers; the waiter starts after a short delay.
**Core:** Non-blocking advisory lock via `fcntl.flock(LOCK_EX | LOCK_NB)`. If the lock is held, the caller polls every 10 ms until `timeout_sec` elapses, then returns `False`.
**Assert:** Holder acquires and releases; waiter eventually acquires after blocking for at least 0.25 s while the holder holds the lock for 0.5 s.
**⚠️ Defect:** The polling loop is a busy-wait (10 ms sleep) rather than an event-driven wakeup, so it wastes CPU under contention. It does not handle `EINTR` or unexpected `IOError` errno values; any non-EAGAIN error is re-raised.

---
*△ AURA Pattern Library — © Reality Optimizer*
