# linreg bfgs

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via BFGS quasi-Newton optimization.

## Guarantee

When it runs, linreg bfgs guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_bfgs.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `bfgsRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of BFGS iterations.
**Core:** Maintains a dense 3×3 inverse-Hessian approximation `H`, initialised to identity. Each iteration: computes the gradient, computes the search direction `p = -H * g`, performs exact line search for the quadratic objective, then updates `H` with the BFGS formula. The curvature condition `s·y` is checked: `if (Math.abs(ys) < 1e-18) break;` — if the condition is not met, the update is skipped.
**Assert:** Expected: `[1.9999999999999996, 2.999999999999999]`, bias `0.4999999999999992` at 1e-9.
**⚠️ Defect:** The curvature condition `s·y > 0` is checked before the BFGS update — this is a partial precondition check. However, the check is `Math.abs(ys) < 1e-18` which tests for near-zero, not for positivity. If `s·y` is negative (which would make the Hessian approximation indefinite), the check passes and the update proceeds with a negative `rho = 1/ys`, which can destroy the positive-definiteness of `H`. The correct check is `ys > 1e-18`, not `Math.abs(ys) < 1e-18`.

---
*△ AURA Pattern Library — © Reality Optimizer*
