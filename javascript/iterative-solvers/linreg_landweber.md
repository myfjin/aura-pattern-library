# linreg landweber

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Landweber iteration.

## Guarantee

When it runs, linreg landweber guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_landweber.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `landweberRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of Landweber iterations.
**Core:** Gradient descent on the OLS objective with a fixed step `alpha = 0.9 / frobSq` where `frobSq` is the squared Frobenius norm of `A`. Each step: `r = A*theta - y; grad = A^T * r; theta -= alpha * grad`.
**Assert:** Expected: `[1.9999999999999727, 2.9999999999999862]`, bias `0.5000000000000021` at 1e-9.
**⚠️ Defect:** The step size `alpha = 0.9 / frobSq` is a conservative bound that guarantees convergence for any matrix (the spectral norm is bounded by the Frobenius norm). This is the only solver in the batch that explicitly estimates a spectral bound. However, the Frobenius norm is a loose upper bound on the spectral norm — the step is smaller than necessary, so convergence is slower than optimal. The `lr` parameter is unused.

---
*△ AURA Pattern Library — © Reality Optimizer*
