# linreg nesterov

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Nesterov accelerated gradient descent for linear regression.

## Guarantee

When it runs, linreg nesterov guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_nesterov.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `nesterovGdRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` controls the number of iterations.
**Core:** Computes the gradient at the lookahead point `theta + beta * v` rather than the current point. The lookahead is computed explicitly each iteration: `aheadWeights[k] = weights[k] + beta * vWeights[k]`. This is the correct Nesterov formulation.
**Assert:** Expected: `[2.0000030077696156, 2.9999947574111663]`, bias `0.500000536697103` at 1e-9.
**⚠️ Defect:** The lookahead is computed correctly — the gradient is evaluated at `theta + beta * v`, not at `theta`. This is a genuine Nesterov implementation and differs from momentum (the expected weights differ from momentum's).

---
*△ AURA Pattern Library — © Reality Optimizer*
