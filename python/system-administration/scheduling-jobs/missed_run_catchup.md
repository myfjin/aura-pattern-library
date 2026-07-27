# missed run catchup

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(callback: Callable, current_time: int) → ?`

## What it does

Missed run catchup: detect and execute missed scheduled runs.
Failure simulated: job is paused for N intervals; assert all missed runs are caught up.

## Guarantee

When it runs, missed run catchup guarantees call_count[0] == 2; call_count[0] == 5; call_count[0] == 11 (proven by run).

**Checkable constraints:**

- `call_count[0] == 1`
- `call_count[0] == 2`
- `call_count[0] == 5`
- `len(log) == 5`
- `len(catchup_entries) == 4`
- `call_count[0] == 1`
- `call_count[0] == 1`
- `call_count[0] == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
