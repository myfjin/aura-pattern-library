# linreg gauss seidel

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Gauss-Seidel iteration on the normal equations for linear regression.

## Guarantee

When it runs, linreg gauss seidel guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_gauss_seidel.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `gaussSeidelRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of Gauss-Seidel passes.
**Core:** Same structure as Jacobi, but updates coordinates in-place: `theta[i] = (Aty[i] - Σ_{j≠i} AtA[i][j] * theta[j]) / AtA[i][i]`. Because each coordinate uses the newest values of the others, Gauss-Seidel converges in fewer passes than Jacobi.
**Assert:** Expected: `[2, 3]`, bias `0.5` at 1e-9 — exact true weights.
**⚠️ Defect:** Gauss-Seidel converges for SPD or diagonally dominant matrices, and there is no check for either. It is measurably more robust than Jacobi in practice: it converged on all four inputs that made Jacobi diverge (uncentred, correlated, wildly scaled, near-collinear), because the in-place update propagates each correction immediately. That is empirical evidence from four fixtures, NOT a guarantee — on a genuinely non-SPD system Gauss-Seidel diverges silently exactly as Jacobi does. The convergence is iteration-capped with no tolerance-based early exit.

---
*△ AURA Pattern Library — © Reality Optimizer*
