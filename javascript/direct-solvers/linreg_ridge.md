# linreg ridge

**Language:** JavaScript · **Sphere:** javascript · **Category:** Direct Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Ridge regression solved via normal equations with tiny regularisation.

## Guarantee

When it runs, linreg ridge guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_ridge.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `ridgeRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` and `iters` are unused. The regularisation `lambda = 1e-8` is negligible — this reduces to OLS.
**Core:** Same as normal equations but adds `lambda * n` to the diagonal of `AtA` for the weight columns (bias is not regularised). `lambda = 1e-8` is chosen so the solution reduces to OLS on the harness data.
**Assert:** Expected: `[1.9999999194648366, 2.9999999051704695]`, bias `0.5000000092735459` at 1e-9.
**⚠️ Defect:** The docstring honestly says `lambda = 1e-8` is chosen so the solution reduces to OLS. The ridge regularisation is deliberately disabled — the pattern is named for a behaviour that is not exercised. Same defect class as the unexercised compensation in the statistics batch. The expected weights differ from OLS by ~1e-7, which is the regularisation bias.

---
*△ AURA Pattern Library — © Reality Optimizer*
