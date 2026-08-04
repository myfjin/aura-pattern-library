# linreg minibatch

**Language:** JavaScript · **Sphere:** javascript · **Category:** Gradient & Adaptive Methods

**Signature:** `(X, y, lr, iters) → object`

## What it does

Mini-batch gradient descent for linear regression.

## Guarantee

When it runs, linreg minibatch guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_minibatch.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `minibatchGdRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is the learning rate. `iters` controls the number of epochs.
**Core:** Shuffles indices per epoch using a seeded LCG (seed 42), processes in batches of 5. Each batch computes the average gradient and applies `lr / batchSize` as the effective step. Runs `iters` epochs (200 at harness default).
**Assert:** Expected: `[1.9999998265678343, 2.999999911058384]`, bias `0.5000000152316448` at 1e-9.
**⚠️ Defect:** The batch size of 5 is hardcoded. For n=30, the last batch in each epoch has only 5 values (30 / 5 = 6 batches exactly), so there is no tail handling issue — but this is coincidental. The seeded LCG makes the shuffle deterministic, so the same 6 batches are produced every run.

---
*△ AURA Pattern Library — © Reality Optimizer*
