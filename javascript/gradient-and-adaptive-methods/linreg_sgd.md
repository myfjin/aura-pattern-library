# linreg sgd

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Stochastic gradient descent for linear regression.

## Guarantee

When it runs, linreg sgd guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_sgd.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `sgdRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` controls the number of steps (internally multiplied by 10).
**Core:** Uses a seeded LCG to select one random sample per step. Runs `iters * 10` steps (2000 steps at the harness default). Each step updates weights from a single sample's error. The stochastic approximation converges to the true weights `[2, 3, 0.5]` rather than the plain-GD fixed point.
**Assert:** Asserts 2 weights and a finite bias. Expected: `[1.9999999999975537, 2.999999999998561]`, bias `0.5000000000003587` at 1e-9.
**⚠️ Defect:** The internal step multiplier (`iters * 10`) is undocumented in the function signature — a caller who passes `iters=1` gets 10 steps, not 1. The seeded LCG makes the sample order deterministic, so this is actually a fixed-sequence SGD, not a stochastic one.

---
*△ AURA Pattern Library — © Reality Optimizer*
