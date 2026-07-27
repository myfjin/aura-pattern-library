# theil sen estimator

**Language:** Python · **Sphere:** data-science · **Category:** Ensembles & Robust Methods

**Signature:** `(X: List[float], y: List[float]) → Tuple[float, float]`

## What it does

Theil-Sen Median-of-Slopes Estimator.

Theil-Sen fits a line by computing slopes between all pairs of points and
taking the median slope (robust to outliers). The intercept is the median
of residuals after subtracting the slope. This non-parametric method is
more robust than OLS under outliers.

Use when: non-parametric robust regression, known outliers, distribution-free estimation.

## Guarantee

When it runs, theil sen estimator guarantees ts_error < ols_error (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ts_error < ols_error`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `theil_sen_estimator(X, y) → (m, b)`
**Valid input:** `X: List[float]` non-empty. `y: List[float]` same length.
**Core:** Theil-Sen: compute slope mᵢⱼ = (yⱼ - yᵢ) / (xⱼ - xᵢ) for all i < j. Take median slope. Intercept = median(yᵢ - m·xᵢ). Non-parametric, robust to outliers (breakdown point ~29%).
**Assert:** On y = 1.5x + 2 with 50 inliers + 12 outliers (uniform ±[20,40]), Theil-Sen slope error < OLS slope error.
**⚠️ Defect:** O(n²) pairwise slope computation. For n=62 (50+12), that's ~1,891 pairs, which is fine. But the doc doesn't mention the O(n²) cost, which becomes prohibitive for n > 10,000. A production implementation would use the Kendall-Theil median polish or subsampling.

---
*△ AURA Pattern Library — © Reality Optimizer*
