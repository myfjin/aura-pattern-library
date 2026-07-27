# zombie reaper

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

**Signature:** `(signum: int, frame: frame) → ?`

## What it does

zombie_reaper: spawn child; when child exits, reap it via SIGCHLD handler to prevent zombie.
Failure simulated: spawn child, let it exit, parent doesn't wait immediately.
Recovery asserted: SIGCHLD handler reaps child; assert no zombie remains (exitcode collected).

## Guarantee

When it runs, zombie reaper guarantees actual_reaped_count == expected_reaped_count; child_pid in reaped_pids; reaped_pids[0] == child_pid (proven by run).

**Checkable constraints:**

- `child_pid in reaped_pids`
- `actual_reaped_count == expected_reaped_count`
- `reaped_pids[0] == child_pid`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
