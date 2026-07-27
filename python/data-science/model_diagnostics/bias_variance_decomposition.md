# bias variance decomposition

**Language:** Python · **Sphere:** data-science · **Category:** Model Diagnostics

**Signature:** `(n: int, seed: int) → List[Tuple[float, float]]`

## What it does

Bias-Variance Decomposition

Estimates bias and variance of a model using bootstrap resampling on synthetic data.
Compares three models: constant (high bias), linear (good), and high-degree polynomial (high variance).

Use this to diagnose whether poor performance is due to underfitting (high bias) or overfitting (high variance).

## Guarantee

When it runs, bias variance decomposition guarantees n > degree; bias_c > bias_l; bias_c > 0.25 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `n > degree`
- `bias_c > bias_l`
- `bias_c > 0.25`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `bootstrap_bias_variance(train_data, test_x, degree, n_bootstraps=100) → (bias, variance, mse)`
**Valid input:** `train_data: List[Tuple[float, float]]` — (x, y) pairs. `test_x: List[float]`. `degree` in {0, 1, 2}. `n_bootstraps ≥ 1`.
**Core:** Bootstrap bias-variance decomposition on synthetic data y = 0.5 + 0.1x² + N(0,0.2). For each bootstrap: resample training data, fit polynomial of given degree, predict on test grid. Bias² = E[(mean_pred - true)²], Variance = E[(pred - mean_pred)²]. Compares constant (high bias) vs linear (medium bias) models.
**Assert:** On 100 training samples, 50 test points, 50 bootstraps: constant model bias > linear model bias, and constant bias > 0.25.
**⚠️ Defect:** The `polyfit` function has hardcoded formulas for degrees 0, 1, 2 only. Degree 3 returns `[0,0,0,0]` (placeholder zeros). The test only uses degrees 0 and 1, so this is fine, but the function claims to support arbitrary degrees. Also, the test only checks bias, not variance — the "variance decomposition" part is computed but not asserted.

---
*△ AURA Pattern Library — © Reality Optimizer*
