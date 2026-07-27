# supervised child

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

## What it does

supervised_child: spawn a child process; supervisor monitors and restarts on death.
Failure simulated: child process dies.
Recovery asserted: supervisor detects death and restarts; assert restart_count > 0.

## Guarantee

When it runs, supervised child guarantees supervisor.restart_count == expected_restarts; no_op_supervisor.restart_count == 0; supervisor.restart_count > no_op_supervisor.restart_count (proven by run).

**Checkable constraints:**

- `supervisor.restart_count == expected_restarts`
- `no_op_supervisor.restart_count == 0`
- `supervisor.restart_count > no_op_supervisor.restart_count`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
