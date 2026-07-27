# polynomial regression

**Language:** Python · **Sphere:** data-science · **Category:** Statistical Modeling

**Signature:** `(A: List[List[float]], b: List[float]) → List[float]`

## What it does

Polynomial Regression via Least Squares (Vandermonde Design Matrix).

A polynomial regression solver using Gaussian elimination on the Vandermonde matrix.
Fits a degree-d polynomial to (x, y) data by solving the normal equations directly.
Use when you need interpretable polynomial fit without external libraries.

## Guarantee

When it runs, polynomial regression guarantees abs(true_c - fit_c) < 0.2; mse_2 < mse_1 (proven by run).

**Checkable constraints:**

- `abs(true_c - fit_c) < 0.2`
- `mse_2 < mse_1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — invariant, metamorphic, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `fit_polynomial(x_vals, y_vals, degree) → List[float]`
**Valid input:** `x_vals, y_vals: List[float]` — same length. `degree ≥ 0`.
**Core:** Polynomial regression via normal equations on Vandermonde design matrix. Build V[i,j] = xᵢʲ, solve (VᵀV)c = Vᵀy via Gaussian elimination with partial pivoting. Evaluate polynomial via Horner-like power accumulation.
**Assert:** On quadratic y = 2 + 3x + 0.5x² + N(0,0.1) with 20 points, degree-2 fit recovers coefficients within 0.2 of true, and quadratic MSE < linear MSE.
**⚠️ Defect:** The Vandermonde matrix is notoriously ill-conditioned for high degrees or non-centered data. For degree 2 with x in [0, 9.5], it's fine, but for degree > 10 or large x ranges, the normal equations become numerically unstable. No centering/scaling of x values is performed.

---
*△ AURA Pattern Library — © Reality Optimizer*
