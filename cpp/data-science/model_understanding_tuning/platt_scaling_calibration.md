# platt scaling calibration

**Language:** C++ · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(z: float) → float`

## What it does

platt_scaling_calibration.cpp
Platt scaling for probability calibration.

## Guarantee

When it runs, platt scaling calibration guarantees baseline_brier > calibrated_brier; calibrated_brier < 0.25 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `baseline_brier > calibrated_brier`
- `calibrated_brier < 0.25`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
