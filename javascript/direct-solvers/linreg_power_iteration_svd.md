# linreg power iteration svd

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via power-iteration SVD.

## Guarantee

When it runs, linreg power iteration svd guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_power_iteration_svd.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `powerIterationSvdRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused. Handles rank-deficient matrices (returns the minimum-norm solution).
**Core:** Computes the thin SVD of `A` by repeated power iteration with deflation. For each of the m singular vectors, runs 100 power iterations, then deflates `B -= sigma * u * v^T`. Uses the pseudoinverse: `theta = V * S^+ * U^T * y`. Singular values are checked: `sigmas[j] > 1e-12 ? ... : 0.0`.
**Assert:** Expected: `[2.0000000000006097, 2.999999999996634]`, bias `0.5000000000004455` at 1e-9.
**⚠️ Defect:** The singular value check is the same partial guard as the Jacobi SVD. The power iteration with 100 steps may not have converged for closely-spaced singular values — the deflation process accumulates error from each previous singular vector. The `lr` and `iters` parameters are unused.

---
*△ AURA Pattern Library — © Reality Optimizer*
