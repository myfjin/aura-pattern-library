# linreg momentum

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Momentum-accelerated batch gradient descent for linear regression.

## Guarantee

When it runs, linreg momentum guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_momentum.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `momentumGdRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` controls the number of iterations.
**Core:** Maintains a velocity vector `v = beta * v - lr * grad; theta += v` with `beta = 0.9`. The velocity accumulates gradient in directions of consistent descent and dampens oscillations.
**Assert:** Expected: `[2.0000730731960927, 2.9999834362294107]`, bias `0.49998761287729787` at 1e-9.
**⚠️ Defect:** The momentum update is correct. The expected weights are close to the true values `[2, 3, 0.5]` but not identical — momentum overshoots slightly and has not fully settled after 200 iterations. A longer run would converge closer.

---
*△ AURA Pattern Library — © Reality Optimizer*
