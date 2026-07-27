# group calibration audit

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

Group Calibration Audit: verify per-group reliability of predicted probabilities.

Creates two groups: one with well-calibrated predictions, one with miscalibrated.
Measures calibration via expected calibration error (ECE) for each group and asserts
that miscalibrated group is detected while well-calibrated group passes.

## Guarantee

When it runs, group calibration audit guarantees ece_good < 0.2; ece_bad > ece_good (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ece_good < 0.2`
- `ece_bad > ece_good`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
