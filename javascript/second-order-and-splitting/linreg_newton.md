# linreg newton

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Newton's method for linear regression.

## Guarantee

When it runs, linreg newton guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_newton.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `newtonRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused (one Newton step from the origin gives the closed-form OLS solution).
**Core:** Precomputes `AtA` and `Aty`, then solves `AtA * theta = Aty` via Gaussian elimination with partial pivoting. The docstring correctly notes that one Newton step from the origin gives the closed-form OLS solution. `lr` and `iters` are unused.
**Assert:** Expected: `[2, 2.9999999999999996]`, bias `0.5` at 1e-9.
**⚠️ Defect:** Newton converges in one step because the OLS objective is exactly quadratic — this is not a demonstration of Newton's method, it is a direct solve wearing Newton's name. The Hessian `AtA` is not checked for singularity before inversion. If `AtA` is singular (rank-deficient data), the Gaussian elimination will divide by a zero pivot and produce Inf/NaN silently. No precondition check.

---
*△ AURA Pattern Library — © Reality Optimizer*
