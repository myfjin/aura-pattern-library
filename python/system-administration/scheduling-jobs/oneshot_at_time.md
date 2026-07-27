# oneshot at time

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(job_key: str, target_time: float, callback: Callable) → ?`

## What it does

Oneshot scheduler: fire a job exactly once at a specified time.
Failure simulated: oneshot is submitted multiple times; assert it fires exactly once.

## Guarantee

When it runs, oneshot at time guarantees fire_count[0] == 3; fire_count[0] == 1; scheduler.get_count('job1') == 1 (proven by run).

**Checkable constraints:**

- `fire_count[0] == 1`
- `scheduler.get_count('job1') == 1`
- `fire_count[0] == 1`
- `scheduler.get_count('job2') == 1`
- `fire_count[0] == 3`
- `scheduler.get_count('job3a') == 1`
- `scheduler.get_count('job3b') == 1`
- `scheduler.get_count('job3c') == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
