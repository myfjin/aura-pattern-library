# heartbeat liveness

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

**Signature:** `(heartbeat_timeout: float) → ?`

## What it does

heartbeat_liveness: periodic heartbeat from a process; detector marks dead if none arrive by deadline.
Failure simulated: heartbeat stops; deadline passes.
Recovery asserted: detector marks dead; assert liveness_flag == False after timeout.

## Guarantee

When it runs, heartbeat liveness guarantees actual_transitions == expected_transitions; state_transitions[0] == ('alive', 'dead'); is_alive is False (proven by run).

**Checkable constraints:**

- `actual_transitions == expected_transitions`
- `state_transitions[0] == ('alive', 'dead')`
- `is_alive is False`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
