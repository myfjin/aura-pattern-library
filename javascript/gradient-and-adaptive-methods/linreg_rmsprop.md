# linreg rmsprop

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

RMSProp batch gradient descent for linear regression.

## Guarantee

When it runs, linreg rmsprop guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_rmsprop.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `rmspropRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` controls the number of iterations.
**Core:** Maintains an EMA of squared gradients: `v = beta * v + (1-beta) * grad²; theta -= lr * grad / (sqrt(v) + eps)` with `beta = 0.99`. Unlike AdaGrad, the EMA allows the scaling to adapt to changing gradient magnitudes.
**Assert:** Expected: `[1.9999999999997666, 2.9999999999988893]`, bias `0.5000000000001152` at 1e-9.
**⚠️ Defect:** The EMA decay `beta = 0.99` means the effective window is ~100 iterations. For 200 iterations at the harness default, the EMA has not fully stabilised. The adaptive mechanism IS exercised — the expected weights differ from plain GD.

---
*△ AURA Pattern Library — © Reality Optimizer*
