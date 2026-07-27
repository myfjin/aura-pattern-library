# ransac robust regression

**Language:** Python · **Sphere:** data-science · **Category:** Ensembles & Robust Methods

**Signature:** `(p1: Tuple[float, float], p2: Tuple[float, float]) → Tuple[float, float]`

## What it does

RANSAC (Random Sample Consensus) for Robust Regression.

RANSAC iteratively selects random minimal subsets of data, fits models,
and counts inliers (points close to the model). The model with the most
inliers is returned, robustly ignoring gross outliers.

Use when: data with severe outliers, unknown noise distribution, automatic outlier detection.

## Guarantee

When it runs, ransac robust regression guarantees ransac_error < ols_error (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ransac_error < ols_error`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
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
