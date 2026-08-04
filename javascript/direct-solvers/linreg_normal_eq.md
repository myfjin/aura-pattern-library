# linreg normal eq

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Closed-form linear regression via normal equations. The implementation is a

## Guarantee

When it runs, linreg normal eq guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_normal_eq.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `normalEquationsRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused. ⚠️ `AtA` must be invertible — on a singular matrix this returns NaN.
**Core:** Forms `AtA` and `Aty`, then solves via Gaussian elimination with partial pivoting. This is the textbook OLS solution.
**Assert:** Expected: `[2, 2.9999999999999996]`, bias `0.5` at 1e-9.
**⚠️ Defect:** No guard against a zero pivot. If `AtA` is singular (rank-deficient data), the division `aug[col][j] /= piv` will produce Inf/NaN silently. The docstring does not mention that forming `AtA` squares the condition number, which is the standard reason to prefer QR over normal equations for ill-conditioned problems.

---
*△ AURA Pattern Library — © Reality Optimizer*
