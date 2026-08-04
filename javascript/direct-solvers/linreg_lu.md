# linreg lu

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via LU decomposition with partial pivoting.

## Guarantee

When it runs, linreg lu guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_lu.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `luRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused. ⚠️ `AtA` must be invertible — on a singular matrix this returns NaN.
**Core:** Decomposes `AtA` into `L` (unit lower triangular) and `U` (upper triangular) with partial pivoting. Forward-substitutes `L * z = P * Aty`, then back-substitutes `U * theta = z`.
**Assert:** Expected: `[2, 3]`, bias `0.5` at 1e-9.
**⚠️ Defect:** No guard against zero pivot in either the LU factorisation or the back-substitution. The division `U[i][k] / U[k][k]` and `s / U[i][i]` will produce Inf/NaN on a singular matrix. This is the least guarded solver in the batch.

---
*△ AURA Pattern Library — © Reality Optimizer*
