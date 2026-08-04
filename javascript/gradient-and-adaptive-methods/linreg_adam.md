# linreg adam

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Adam (adaptive moment estimation) batch gradient descent for linear regression.

## Guarantee

When it runs, linreg adam guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_adam.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `adamRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` controls the number of outer epochs (internally multiplied by 3).
**Core:** Maintains bias-corrected first moment (momentum) and second moment (RMSProp-style scaling): `m = beta1*m + (1-beta1)*grad; v = beta2*v + (1-beta2)*grad²; mHat = m/(1-beta1^t); vHat = v/(1-beta2^t); theta -= lr * mHat / (sqrt(vHat) + eps)`. Uses `iters * 3` internal iterations.
**Assert:** Expected: `[2.000000000000103, 3.000000000000291]`, bias `0.4999999999999489` at 1e-9.
**⚠️ Defect:** The bias correction is correctly implemented (`mHat = m / (1 - beta1^t)`). The internal multiplier of 3 is modest. The adaptive mechanism IS exercised.

---
*△ AURA Pattern Library — © Reality Optimizer*
