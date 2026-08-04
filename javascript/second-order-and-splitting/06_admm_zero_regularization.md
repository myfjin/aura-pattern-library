# 06 admm zero regularization

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

ADMM for linear regression with zero regularisation.

## Guarantee

When it runs, 06 admm zero regularization guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 06_admm_zero_regularization.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `admmZeroRegularization(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of ADMM iterations.
**Core:** Splits the OLS problem with an augmented Lagrangian. The x-update solves `(AtA + rho*I) * x = Aty + rho*(z - u)`. The z-update with zero regularisation is `z = x + u` (identity prox). The dual update is `u += x - z`. With zero regularisation, the z-update is an identity — ADMM reduces to a sequence of regularised least-squares solves that converge to the OLS solution.
**Assert:** Expected: `[2, 3]`, bias `0.5` at 1e-9.
**⚠️ Defect:** With zero regularisation, the z-update `z = x + u` is an identity operation — it does nothing because `x + u` is immediately undone by the dual update `u += x - z = u + x - (x + u) = 0`. The method reduces to repeatedly solving `(AtA + rho*I) * x = Aty` with a shifted right-hand side that converges to the unregularised solution. The `rho = 1.0` is hardcoded. The `lr` parameter is unused.

---
*△ AURA Pattern Library — © Reality Optimizer*
