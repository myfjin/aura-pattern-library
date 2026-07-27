# pidfile singleton

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 1 · Process Supervision & Immortality

**Signature:** `(pidfile: str) → ?`

## What it does

pidfile_singleton: prevent multiple instances via pidfile; if pidfile exists and pid alive, refuse start.
Failure simulated: second instance attempts to start.
Recovery asserted: second instance is blocked; assert exception raised or lock_acquired == False.

## Guarantee

When it runs, pidfile singleton guarantees exit_code == expected_exit_code; acquired_1 is True; acquired_1 is True (proven by run).

**Checkable constraints:**

- `acquired_1 is True`
- `exit_code == expected_exit_code`
- `acquired_1 is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
