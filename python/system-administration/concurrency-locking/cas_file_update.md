# cas file update

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(path: str) → ?`

## What it does

cas_file_update: optimistic compare-and-swap on a versioned file (read → compute → swap-if-
version-unchanged → retry on conflict). This is REAL CAS, not pessimistic whole-cycle locking:
the read and the (expensive) compute happen OUTSIDE any lock; only the atomic compare-and-swap
(re-read version, write iff it still matches) is guarded, and a losing writer RETRIES.
Failure simulated: two processes read the same version concurrently, both compute, then race to
swap. Recovery asserted: (1) final value == N (no lost update — the loser's stale swap is
REJECTED and it retries on the fresh value), (2) at least one real CONFLICT+RETRY occurred
(retries >= 1) — which a pessimistic full-lock could never produce, proving this is genuine CAS.

## Guarantee

When it runs, cas file update guarantees results.get(f'updater_{i}_ok'); final_value == num; final_version == num (weak-grade: directional, proven by run).

**Checkable constraints:**

- `results.get(f'updater_{i}_ok')`
- `final_value == num`
- `final_version == num`
- `total_retries >= 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def _read(path):`, `def cas_increment(path, lockfile, results_dict, updater_id, barrier):`
**Valid input:** `path` points to a JSON file containing `{"value": int, "version": int}`; `lockfile` exists; multiple updaters start together via the barrier.
**Core:** Optimistic compare-and-swap counter. Reads value+version outside the lock, computes new value, then under a brief `fcntl.flock` re-reads and writes only if the version is unchanged; otherwise retries.
**Assert:** With two concurrent updaters the final value and version are both 2, and at least one real conflict-retry occurred (proving it is CAS, not pessimistic locking).
**⚠️ Defect:** The compare-and-swap serializes under a global file lock, so it is not lock-free; it is optimistic only in the read/compute phase. The lockfile is opened in append mode but the lock is per-process file descriptor, not per-file, so a stale lock from a crashed process could block all future updaters.

---
*△ AURA Pattern Library — © Reality Optimizer*
