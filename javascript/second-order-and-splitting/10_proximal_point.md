# 10 proximal point

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Proximal point method for linear regression.

## Guarantee

When it runs, 10 proximal point guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 10_proximal_point.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `proximalPointRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of proximal iterations.
**Core:** Each iteration solves `(AtA + lambda*I) * theta = Aty + lambda * theta_old`. The regularisation `lambda` starts at 1.0 and decays by factor 0.7 each iteration, with a floor of 1e-12. As `lambda` approaches zero, the iterates converge to the OLS solution.
**Assert:** Expected: `[1.9999999999999996, 3]`, bias `0.5` at 1e-9.
**⚠️ Defect:** The initial `lambda = 1.0`, decay `lambda *= 0.7`, and floor `lambda < 1e-12` are all hardcoded. The decay rate of 0.7 is tuned to this fixture — a different problem may need a different schedule. The `lr` parameter is unused. The regularisation makes the system always invertible, so no precondition check is needed.

---
*△ AURA Pattern Library — © Reality Optimizer*
