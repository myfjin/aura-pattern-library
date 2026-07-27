# flock singleton

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(filename: ?, results_dict: ?) → ?`

## What it does

flock_singleton: two processes contend for the same fcntl.flock(LOCK_EX) on a file.
Failure simulated: launch a holder and a blocker AT THE SAME TIME; the blocker attempts the
exclusive lock while the holder holds it. Recovery asserted: the blocker's acquire happens
strictly AFTER the holder's release (event ordering via shared-clock epoch timestamps), and its
wait was ~the hold time — proving it genuinely blocked. A no-op lock lets the blocker acquire
immediately (before the holder released) → the ordering assert fails.

## Guarantee

When it runs, flock singleton guarantees results.get('holder_released_at'); results.get('blocker_acquired_at'); blk_acquire >= held_release - 0.005 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `results.get('holder_released_at')`
- `results.get('blocker_acquired_at')`
- `blk_acquire >= held_release - 0.005`
- `blk_wait > 0.25`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def holder_then_releaser(filename, results_dict):`, `def blocker(filename, results_dict):`
**Valid input:** `filename` is a writable lockfile path; holder and blocker run in separate processes.
**Core:** Demonstrates that `fcntl.flock(LOCK_EX)` genuinely blocks: the holder acquires, sleeps 0.5 s, then releases; the blocker calls `flock` and records the acquisition time.
**Assert:** The blocker acquires only after the holder releases (event ordering); the blocker's relative wait is > 0.25 s, proving it blocked rather than acquiring immediately.
**⚠️ Defect:** This is a demo, not a reusable class. The lock is not tied to any resource or critical section beyond time measurement. `flock` locks are advisory, so any process that ignores them can access the guarded resource anyway.

---
*△ AURA Pattern Library — © Reality Optimizer*
