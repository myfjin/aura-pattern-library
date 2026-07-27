# job dedup

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(job_id: str, callback: Callable, timeout: float) → ?`

## What it does

Job dedup: ensure only one instance of a job runs at a time.
Failure simulated: launch same job twice concurrently; assert only one runs.

## Guarantee

When it runs, job dedup guarantees call_count[0] == 3; dedup4.get_count('job_seq') == 3; sum(exec_results) == 1 (proven by run).

**Checkable constraints:**

- `sum(exec_results) == 1`
- `exec_count[0] == 1`
- `dedup.get_count('job_a') == 1`
- `results['job_b'] == 1`
- `results['job_c'] == 1`
- `acquired_count[0] == 1`
- `blocked_count[0] >= 1`
- `result1 and result2 and result3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
