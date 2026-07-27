# named mutex

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(mutex_name: ?, results_dict: ?, worker_id: ?, hold_time: ?) → ?`

## What it does

named_mutex: a named mutex using filesystem locking (tempfile-based).
Failure simulated: two processes try to acquire the same named mutex at the same time.
Recovery asserted: (1) both acquire and release successfully in sequence (one blocks until
the other releases), (2) the execution times show clear serialization (each holds for ~0.3s,
total time ~0.6s, not concurrent). A no-op mutex would allow both to enter "critical section"
at once, violating the mutex invariant.

## Guarantee

When it runs, named mutex guarantees results.get(f'worker_{i}_acquired'); held >= hold_time - 0.05; total_time >= 2 * hold_time - 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `results.get(f'worker_{i}_acquired')`
- `held >= hold_time - 0.05`
- `total_time >= 2 * hold_time - 0.1`
- `total_time < 2 * hold_time + 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class NamedMutex:`, `def __init__(self, name):`, `def acquire(self, timeout=None):`, `def release(self):`, `def __enter__(self):`, `def __exit__(self, *args):`, `def critical_section(mutex_name, results_dict, worker_id, hold_time):`
**Valid input:** `name` is a string usable in a filename; `timeout` is `None` or a positive number; workers run in separate processes.
**Core:** Named mutex backed by a temp-directory lockfile. `acquire` uses `os.open(O_CREAT | O_EXCL)`; if the file exists it polls until timeout. Context-manager support is provided.
**Assert:** Two workers each hold a 0.3 s critical section; total wall time is at least ~0.6 s, proving serialization.
**⚠️ Defect:** The mutex is *not* robust: if a worker crashes while holding the lock, the lockfile remains and blocks all future acquirers forever (no heartbeat or stale-lock detection). `release` swallows all exceptions, hiding failures.

---
*△ AURA Pattern Library — © Reality Optimizer*
