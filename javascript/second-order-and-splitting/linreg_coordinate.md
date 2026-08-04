# linreg coordinate

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Coordinate descent for linear regression.

## Guarantee

When it runs, linreg coordinate guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_coordinate.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `coordinateDescentRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of full passes over coordinates.
**Core:** Alternates between a closed-form bias update and closed-form weight updates. Each weight is updated by solving `w_j = (Σ x_ij * (y_i - bias - Σ_{k≠j} w_k * x_ik)) / Σ x_ij²`. The denominator is cached as `colSq[j]`. The `lr` parameter is unused.
**Assert:** Expected: `[2.0000000000000004, 3.000000000000001]`, bias `0.5` at 1e-9.
**⚠️ Defect:** No precondition needed (coordinate descent works on any convex quadratic). The closed-form update for each coordinate is exact for the OLS objective. The `lr` parameter is unused. This is one of the few patterns in the batch with no hidden assumptions.

---
*△ AURA Pattern Library — © Reality Optimizer*
