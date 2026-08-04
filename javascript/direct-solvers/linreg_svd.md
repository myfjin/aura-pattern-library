# linreg svd

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via one-sided Jacobi SVD / Moore-Penrose pseudoinverse.

## Guarantee

When it runs, linreg svd guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_svd.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `svdRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused. Handles rank-deficient matrices (returns the minimum-norm solution).
**Core:** Computes the thin SVD of `A` by applying Jacobi rotations to orthogonalise the columns. Uses the pseudoinverse: `theta = V * S^+ * U^T * y`. Singular values are checked: `s[j] > 1e-12 ? ... : 0.0` before division.
**Assert:** Expected: `[1.9999999999999998, 2.999999999999999]`, bias `0.5` at 1e-9.
**⚠️ Defect:** The singular value check `s[j] > 1e-12` is a partial singularity guard — small singular values are clamped to zero (the standard pseudoinverse approach). This is the most robust singularity handling in the batch. However, the Jacobi SVD with `maxSweeps = 50` may not converge for ill-conditioned matrices.

---
*△ AURA Pattern Library — © Reality Optimizer*
