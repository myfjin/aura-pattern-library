# double launch block

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 3 · Concurrency & Locking

**Signature:** `(.0: range_iterator) → ?`

## What it does

double_launch_block: prevent launching the same service twice; a pidfile lock ensures
only one instance can run. Failure simulated: two processes try to start the same service
concurrently. Recovery asserted: (1) the first obtains the lock and starts, (2) the second
tries to acquire the lock, finds the pidfile held, and fails/returns False without starting,
(3) only the first writes to the output file (proving only one ran). A no-op launch guard
would allow both instances to start, corrupting shared state.

## Guarantee

When it runs, double launch block guarantees success_count == 1; fail_count == 1; reason == 'already_running' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `success_count == 1`
- `fail_count == 1`
- `reason == 'already_running'`
- `started_count == 1`
- `running_count == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class ServiceLauncher:`, `def __init__(self, service_name, tmpdir):`, `def try_launch(self):`, `def launcher_process(service_name, tmpdir, results_dict, launcher_id):`
**Valid input:** `service_name` and `tmpdir` are strings; two launcher processes contend for the same service.
**Core:** PID-file-style singleton launcher. Uses atomic `os.open(O_CREAT | O_EXCL)` to create a lockfile; if held, checks whether the holder PID is alive via `os.kill(pid, 0)`; breaks stale locks if the holder is dead; writes output entries to prove only one instance ran.
**Assert:** Exactly one of two concurrent launches succeeds; the other gets reason `already_running`; the output file contains exactly one "started" and one "running" line.
**⚠️ Defect:** Reading the holder PID from the lockfile is racy (a loop of retries is used, but not atomic with lock creation). `os.kill(pid, 0)` can succeed for a recycled PID, so a stale lock may be treated as live. The lockfile is removed in `finally`, so the singleton guarantee expires the moment the first instance finishes.

---
*△ AURA Pattern Library — © Reality Optimizer*
