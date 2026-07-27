# kswin drift

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[float], window_size: int, alpha: float) → bool`

## What it does

KSWIN (Kolmogorov-Smirnov Windowing) drift detector using KS test on sliding windows.
Core idea: maintain two windows; apply KS test to detect distribution shift.
When: detect concept drift via statistical test on sliding window with low false-alarm rate.

## Guarantee

When it runs, kswin drift guarantees not detected (weak-grade: directional, proven by run).

**Checkable constraints:**

- `detected`
- `not detected`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
