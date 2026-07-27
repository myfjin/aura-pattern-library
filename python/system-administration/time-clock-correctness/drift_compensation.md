# drift compensation

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 11 · Time, clock & correctness

**Signature:** `(real_time: float, clock_time: float) → ?`

## What it does

Compensate for clock drift (clock running fast or slow).

## Guarantee

When it runs, drift compensation guarantees corrected == expected; corrected == expected; error == 20.0 (proven by run).

**Checkable constraints:**

- `corrected == expected`
- `corrected == expected`
- `error == 20.0`
- `real_elapsed == 100.0`
- `uncorrected_elapsed == 115.0`
- `uncorrected_elapsed != real_elapsed`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
