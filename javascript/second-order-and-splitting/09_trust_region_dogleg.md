# 09 trust region dogleg

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Trust-region / dogleg method for linear regression.

## Guarantee

When it runs, 09 trust region dogleg guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 09_trust_region_dogleg.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `trustRegionDoglegRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused (the full Gauss-Newton step is taken).
**Core:** Solves `AtA * theta = Aty` via Gaussian elimination and returns the result as the dogleg step. The docstring notes that on a linear least-squares problem, the trust-region constraint is inactive at the OLS solution, so the full Gauss-Newton step is taken. `lr` and `iters` are unused.
**Assert:** Expected: `[2, 2.9999999999999996]`, bias `0.5` at 1e-9.
**⚠️ Defect:** There is no trust-region radius update, no dogleg path computation, and no acceptance/rejection logic. The implementation solves the normal equations and returns the result — it is a direct solve, not a trust-region method. The docstring honestly documents this, but the name "trust-region dogleg" promises a method that is not implemented. No precondition check.

---
*△ AURA Pattern Library — © Reality Optimizer*
