# linreg polyak sgd

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Polyak-averaged stochastic gradient descent.

## Guarantee

When it runs, linreg polyak sgd guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_polyak_sgd.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `polyakSgdRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` controls the number of SGD epochs.
**Core:** Runs SGD with Fisher-Yates shuffle per epoch (seeded LCG, seed 12345). Accumulates the running sum of all iterates and returns the average: `theta_avg = sum(theta_t) / T`. This reduces variance compared to the last iterate of plain SGD.
**Assert:** Expected: `[1.9737396844814927, 2.96950662507312]`, bias `0.5016051217615838` at 1e-9.
**⚠️ Defect:** The expected weights are closer to the true values `[2, 3, 0.5]` than plain GD but not identical. Polyak averaging reduces but does not eliminate the bias from the last iterate. The averaging is correctly implemented — every step's weights are accumulated, not just the final epoch.

---
*△ AURA Pattern Library — © Reality Optimizer*
