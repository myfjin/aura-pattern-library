# monotonic vs wall

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 11 · Time, clock & correctness

**Signature:** `(clock: ClockMock, start_wall: float, start_mono: float) → ?`

## What it does

Monotonic clock immune to wall-clock backward jumps.

## Guarantee

When it runs, monotonic vs wall guarantees elapsed_mono == 5.0; elapsed_mono == 5.0; was_skew is True (proven by run).

**Checkable constraints:**

- `elapsed_mono == 5.0`
- `was_skew is True`
- `elapsed_mono == 5.0`
- `was_skew is False`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
