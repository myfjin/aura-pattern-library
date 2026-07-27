# ridge regression normal eq

**Language:** Python · **Sphere:** data-science · **Category:** Core ML

**Signature:** `(X: List[List[float]], y: List[float], lambda_reg: float) → List[float]`

## What it does

Ridge Regression via Normal Equations (from scratch).

Core idea: Linear regression with L2 regularization: minimize ||Xw - y||^2 + λ||w||^2.
Solved analytically via normal equations: w = (X^T X + λI)^(-1) X^T y.
Implement matrix operations (transpose, multiply, Gaussian elimination) from scratch.

When to use: Regression with collinearity; small to medium data; interpretable model.

## Guarantee

When it runs, ridge regression normal eq guarantees r2 > 0.8; all((abs(weights[i] - true_weights[i]) < 1.0 for i in range(n_features))) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `r2 > 0.8`
- `all((abs(weights[i] - true_weights[i]) < 1.0 for i in range(n_features)))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — invariant, metamorphic, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `ridge_regression_normal_eq(X, y, lambda_reg=0.01) → weights`
**Valid input:** `X: List[List[float]]` — n_samples × n_features. `y: List[float]` length n_samples. `lambda_reg ≥ 0`.
**Core:** Ridge regression (L2-regularized linear regression) solved via normal equations. Compute XᵀX + λI and Xᵀy, solve via Gaussian elimination with partial pivoting. Matrix ops (transpose, multiply, solve) implemented from scratch.
**Assert:** On y = 2·x₁ + 3·x₂ - 1·x₃ + N(0,0.5) with 30 samples, λ=0.01, R² > 0.8 and all weights within 1.0 of true.
**⚠️ Defect:** No bias/intercept term. The normal equations solve Xw = y without an augmented bias column. The return type is `List[float]` (weights only), not `(weights, bias)` as the docstring implies. This works when the true model has no intercept, but will produce biased estimates when one is needed.

---
*△ AURA Pattern Library — © Reality Optimizer*
