# linreg adagrad

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Batch AdaGrad for linear regression.

## Guarantee

When it runs, linreg adagrad guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_adagrad.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `adaGradRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` controls the number of outer epochs (internally multiplied by 250).
**Core:** Accumulates squared gradients per coordinate: `g2 += grad²; theta -= lr * grad / (sqrt(g2) + eps)`. Uses `iters * 250` internal iterations (50,000 at harness default) because AdaGrad's per-coordinate scaling converges slowly on well-conditioned data.
**Assert:** Expected: `[1.999999999999937, 2.9999999999997904]`, bias `0.5000000000000228` at 1e-9.
**⚠️ Defect:** The internal iteration multiplier of 250 is documented in the docstring but is a large hidden constant. The adaptive mechanism IS exercised — the expected weights differ from plain GD — but the accumulator `g2` grows monotonically, so the effective learning rate decreases over time. On well-conditioned data this is unnecessary overhead.

---
*△ AURA Pattern Library — © Reality Optimizer*
