# idempotent once guard

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(.0: range_iterator) → ?`

## What it does

idempotent_once_guard: ensure an idempotent action runs exactly once, even if called
from multiple processes concurrently. Failure simulated: two processes call the action
at the same time; only one should succeed and modify the shared state, the other should
skip (already done). Recovery asserted: (1) the action ran exactly once (counter=1), (2)
both processes completed, (3) the second process detected "already done" and returned False.
A no-op guard would allow the action to run twice (or more), violating "exactly once".

## Guarantee

When it runs, idempotent once guard guarantees ran_count == 1; already_done_count == 1; counter_value == 1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ran_count == 1`
- `already_done_count == 1`
- `counter_value == 1`
- `os.path.exists(marker_file)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def idempotent_action_once(marker_file, results_dict, caller_id):`
**Valid input:** `marker_file` is a writable path; `caller_id` is an identifier; two callers start concurrently.
**Core:** Marker-file guard. Uses `fcntl.flock` to serialize a check-and-run: if the marker file exists, the action is already done; otherwise it increments a counter and writes the marker.
**Assert:** Exactly one caller runs the action (counter == 1); the other caller detects "already done".
**⚠️ Defect:** The marker file is written after the counter increment, so a crash between counter write and marker write would allow a second caller to re-run the action. The marker stores only the PID, not a completion timestamp or checksum.

---
*△ AURA Pattern Library — © Reality Optimizer*
