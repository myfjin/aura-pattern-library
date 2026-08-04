# linreg sherman morrison

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via Sherman-Morrison rank-1 updates to an inverse.

## Guarantee

When it runs, linreg sherman morrison guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_sherman_morrison.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `shermanMorrisonRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused. The initial regularisation `reg = 1e-4` biases the solution slightly.
**Core:** Starts from a regularised diagonal `invM = (1/reg) * I` with `reg = 1e-4`. For each row of `A`, applies the Sherman-Morrison formula: `invM -= invMu * invMu^T / (1 + u^T * invMu)`. After all 30 rows are absorbed, computes `theta = invM * Aty`. This is a genuine rank-1 update implementation.
**Assert:** Expected: `[1.9999732733407967, 2.9999688269931224]`, bias `0.5000013845975201` at 1e-9.
**⚠️ Defect:** The denominator check `if (Math.abs(denom) < 1e-24) { continue; }` skips updates that would cause numerical instability. The initial regularisation `reg = 1e-4` biases the solution — the expected weights are the least accurate in this batch (off by ~3e-5). The `lr` parameter is unused.

---
*△ AURA Pattern Library — © Reality Optimizer*
