# linreg adadelta

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via AdaDelta adaptive gradient descent.

## Guarantee

When it runs, linreg adadelta guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_adadelta.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `adaDeltaRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is a scale factor applied to updates (internally multiplied by 200). `iters` controls the number of outer epochs (internally multiplied by 3).
**Core:** Maintains EMAs of squared gradients (`Eg2`) and squared parameter updates (`Edx2`). The step is `dx = -sqrt(Edx2 + eps) / sqrt(Eg2 + eps) * grad`. Uses `rho = 0.99`, `eps = 1e-6`, `lrScale = 200.0`, and `iters * 3` internal iterations.
**Assert:** Expected: `[1.9999999999999998, 2.999999999999999]`, bias `0.5000000000000001` at 1e-9.
**⚠️ Defect:** Pure AdaDelta has NO learning rate — the step size is entirely determined by the ratio of RMS terms. This implementation multiplies the AdaDelta step by `lr * lrScale`, which is a learning rate. The docstring acknowledges this ("lr is accepted for signature compatibility and scaled internally") but the result is AdaDelta-with-a-learning-rate, not AdaDelta. The `lrScale = 200.0` is a large hidden constant that compensates for the fact that AdaDelta's native step size is too small for this objective.

---
*△ AURA Pattern Library — © Reality Optimizer*
