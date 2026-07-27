# interval scheduler

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(callback: Callable) → ?`

## What it does

Interval scheduler: fire a job at fixed intervals.
Failure simulated: verify job fires at each expected interval boundary, no missed runs.
Assert: execution times match expected interval schedule exactly.

## Guarantee

When it runs, interval scheduler guarantees fire_count[0] >= 4; drift < interval * 0.5; count_after_first >= 1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(exec_times) >= 4`
- `fire_count[0] >= 4`
- `drift < interval * 0.5`
- `count_after_first >= 1`
- `count_after_second > count_after_first`
- `fire_count[0] == final_count`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
