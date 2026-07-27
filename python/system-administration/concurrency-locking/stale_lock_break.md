# stale lock break

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(lockfile: ?, pidfile: ?, results_dict: ?, ready_marker: ?) → ?`

## What it does

stale_lock_break: detect and break a stale lock when its holder dies.
Failure simulated: process A acquires a lock, then dies (SIGKILL) without releasing.
Process B detects the stale lock (holder is dead) and breaks it by waiting for it to be released.
Recovery asserted: (1) B detects the lock is held (not acquired without effort), (2) B reads
the holder pid, (3) after holder is killed, B acquires the now-released lock, (4) the pidfile
proves a real holder existed. A no-op stale-break would leave the lock held forever or fail
to detect the held lock.

## Guarantee

When it runs, stale lock break guarantees results.get('holder_acquired'); results.get('breaker_read_pid'); results.get('breaker_acquired') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `results.get('holder_acquired')`
- `results.get('breaker_read_pid')`
- `results.get('breaker_acquired')`
- `not results.get('breaker_got_lock_without_breaking')`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def acquire_and_hold_with_pidfile(lockfile, pidfile, results_dict, ready_marker):`, `def detector_and_breaker(lockfile, pidfile, results_dict, ready_marker):`
**Valid input:** `lockfile`, `pidfile`, and `ready_marker` are writable paths in the same temp directory; the holder process is killed with SIGKILL.
**Core:** Detects a stale advisory lock. A holder acquires `flock`, writes its PID, and hangs; a breaker tries non-blocking acquire, reads the PID, waits for the holder to die (which auto-releases the OS lock), and then acquires.
**Assert:** Holder acquires; breaker reads the holder PID and eventually acquires the lock after the holder is killed; breaker does not acquire before the lock is held.
**⚠️ Defect:** The breaker never actually *breaks* the lock; it simply waits for the OS to release it when the holder dies. There is no proactive stale-lock breaker that works when the holder is stuck but alive (e.g., hung in an infinite loop, not dead).

---

## Category: config-management

---
*△ AURA Pattern Library — © Reality Optimizer*
