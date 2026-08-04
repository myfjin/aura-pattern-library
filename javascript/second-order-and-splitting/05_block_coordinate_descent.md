# 05 block coordinate descent

**Language:** JavaScript · **Sphere:** javascript · **Category:** Second-Order & Splitting

**Signature:** `(X, y, lr, iters) → object`

## What it does

Block coordinate descent for linear regression.

## Guarantee

When it runs, 05 block coordinate descent guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 05_block_coordinate_descent.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `blockCoordinateDescentRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of block sweeps.
**Core:** Splits parameters into a bias block and a weights block. Updates the bias with a closed-form mean, then solves the normal equations for the weights block using a 2×2 solver (or general GE for nf > 2). The 2×2 solver checks `Math.abs(det) < 1e-14` before dividing.
**Assert:** Expected: `[2.0000000000000004, 3.0000000000000004]`, bias `0.5` at 1e-9.
**⚠️ Defect:** The determinant check `Math.abs(det) < 1e-14` is a partial precondition check — if the weights block is singular, the solver returns `[0, 0]` instead of failing. The `lr` parameter is unused. For nf=2, the block update is exact in one pass, so `iters` beyond 1 are redundant.

---
*△ AURA Pattern Library — © Reality Optimizer*
