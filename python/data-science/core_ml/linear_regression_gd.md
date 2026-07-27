# linear regression gd

**Language:** Python · **Sphere:** data-science · **Category:** Core ML

**Signature:** `(X: List[List[float]], y: List[float], learning_rate: float, iterations: int) → Tuple[List[float], float]`

## What it does

Linear Regression via Batch Gradient Descent (from scratch).

Core idea: Given labeled training data (X, y), fit a linear model y = Xw + b
by iteratively updating weights w and bias b to minimize mean squared error.
Gradient descent computes ∂loss/∂w and ∂loss/∂b each iteration and moves opposite
the gradient to reduce loss.

When to use: Continuous target prediction; interpretable model; small to medium datasets.

## Guarantee

When it runs, linear regression gd guarantees abs(weights[0] - 2.0) < 0.5; abs(weights[1] - 3.0) < 0.5; r2 > 0.8 (proven by run).

**Checkable constraints:**

- `r2 > 0.8`
- `abs(weights[0] - 2.0) < 0.5`
- `abs(weights[1] - 3.0) < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — invariant, metamorphic, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `linear_regression_gd(X, y, learning_rate=0.01, iterations=100) → (weights, bias)`
**Valid input:** `X: List[List[float]]` non-empty, all same length. `y: List[float]` same length as X. `learning_rate > 0`.
**Core:** Batch gradient descent for linear regression. Initialize w=0, b=0. Each iteration: compute predictions ŷ = Xw + b, MSE loss, gradients dw = (1/n) Σ (ŷᵢ - yᵢ) xᵢ, db = (1/n) Σ (ŷᵢ - yᵢ), update w ← w - lr·dw, b ← b - lr·db.
**Assert:** On y = 2·x₁ + 3·x₂ + N(0,0.5) with 30 samples, 200 iterations, R² > 0.8, |w₀ - 2| < 0.5, |w₁ - 3| < 0.5.
**⚠️ Defect:** Fixed iteration count with no convergence check. If learning rate is too high, it may diverge; if too low, it may not converge in 100 iterations. No early stopping on gradient norm or loss plateau. The caller must tune lr and iterations together.

---
*△ AURA Pattern Library — © Reality Optimizer*
