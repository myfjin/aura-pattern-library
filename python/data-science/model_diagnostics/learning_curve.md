# learning curve

**Language:** Python · **Sphere:** data-science · **Category:** Model Diagnostics

**Signature:** `(n: int, seed: int) → List[Tuple[float, float]]`

## What it does

Learning Curve Analysis

Plots error vs training set size to assess model stability and data hunger.
Verifies that training error increases and validation error decreases as training data grows,
indicating the model has capacity to benefit from more data without overfitting.

Use this to diagnose high bias (both curves high and flat) vs high variance (training low, validation high).

## Guarantee

When it runs, learning curve guarantees len(y_true) == len(y_pred); n > 0; train_errors[-1] < 2.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(y_true) == len(y_pred)`
- `n > 0`
- `train_errors[-1] < 2.0`
- `val_errors[0] > train_errors[0]`
- `val_errors[-1] < val_errors[0]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `learning_curve_analysis()` — no return, prints PASS.
**Valid input:** Uses internal `generate_linear_data(200, seed=42)`.
**Core:** Fit linear model on increasing training set sizes (10, 30, 50, 80, 120, 150). Training error should be low and stable. Validation error should start high and decrease with more data, demonstrating the learning curve pattern.
**Assert:** On 150 train + 50 validation points (y = 2x + N(0,1)): final training error < 2.0, validation error > training error at smallest size, validation error decreases with more data.
**⚠️ Defect:** The test asserts `val_errors[-1] < val_errors[0]` (validation error decreases), but this is a monotonicity check that can fail due to random variation in the data split. With only 50 validation points, the validation error at size 150 could be slightly higher than at size 10 by chance. A statistical test or averaging over multiple splits would be more robust.

---
*△ AURA Pattern Library — © Reality Optimizer*
