# 08 gauss newton

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Gauss-Newton for linear regression.

## Guarantee

When it runs, 08 gauss newton guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 08_gauss_newton.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `gaussNewtonRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused (Gauss-Newton converges in one step on a linear model).
**Core:** For a linear model, the Gauss-Newton Hessian approximation `J^T J` equals the exact Hessian `A^T A`. The method converges in one step from any starting point. This implementation performs exactly that single step by solving `AtA * theta = Aty` via Gaussian elimination. `lr` and `iters` are unused.
**Assert:** Expected: `[2, 2.9999999999999996]`, bias `0.5` at 1e-9.
**⚠️ Defect:** Same as Newton — this is a direct solve wearing Gauss-Newton's name. On a linear problem, Gauss-Newton is identical to Newton, and both are identical to solving the normal equations. The docstring honestly documents this degeneracy. No precondition check on `AtA`.

---
*△ AURA Pattern Library — © Reality Optimizer*
