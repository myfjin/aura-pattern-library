# leap safe interval

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 11 · Time, clock & correctness

**Signature:** `(time_a: float, time_b: float) → ?`

## What it does

Compute time intervals correctly across leap second insertions.

## Guarantee

When it runs, leap safe interval guarantees elapsed == 100.0; elapsed == 99.0; elapsed == 98.0 (proven by run).

**Checkable constraints:**

- `elapsed == 100.0`
- `elapsed == 99.0`
- `elapsed == 98.0`
- `elapsed == 99.0`
- `elapsed2 == 100.0`
- `elapsed1 == elapsed2 == 99.0`
- `elapsed == 97.0`
- `raw_diff == 100.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
