# linreg nadam

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Nadam (Adam with Nesterov momentum).

## Guarantee

When it runs, linreg nadam guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_nadam.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `nadamRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` controls the number of outer epochs (internally multiplied by 3).
**Core:** Adam with Nesterov lookahead in the momentum term: `nesterov = beta1 * mHat + (1-beta1) * grad / (1-beta1^t)`. Uses `iters * 3` internal iterations.
**Assert:** Expected: `[2.0000000000000084, 3.0000000000000373]`, bias `0.4999999999999961` at 1e-9.
**⚠️ Defect:** The Nadam update is correctly implemented — the Nesterov lookahead is applied to the bias-corrected momentum. The expected weights differ from both Adam and Nesterov, confirming the combination is genuinely different.

---
*△ AURA Pattern Library — © Reality Optimizer*
