# ransac robust regression

**Language:** C++ · **Sphere:** data-science · **Category:** Ensembles & Robust Methods

**Signature:** `(p1: Tuple[float, float], p2: Tuple[float, float]) → Tuple[float, float]`

## What it does

ransac_robust_regression.cpp — RANSAC robust line fitting vs OLS.

## Guarantee

When it runs, ransac robust regression guarantees ransac_error < ols_error (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `ransac_error < ols_error`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `ransac_regression(X, y, n_iterations=100, threshold=1.0) → (m, b)`
**Valid input:** `X: List[float]` non-empty. `y: List[float]` same length. `n_iterations ≥ 1`. `threshold > 0`.
**Core:** RANSAC: randomly sample 2 points, fit line y = mx + b, count inliers (|y - (mx+b)| < threshold). Repeat n_iterations. Return model with most inliers. Robust to > 30% outliers.
**Assert:** On y = 2x + 1 with 50 inliers + 15 outliers (uniform ±[10,30]), RANSAC slope error < OLS slope error.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
