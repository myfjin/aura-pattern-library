# 04 randomized kaczmarz

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Randomized Kaczmarz for linear regression.

## Guarantee

When it runs, 04 randomized kaczmarz guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 04_randomized_kaczmarz.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `randomizedKaczmarzRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of row projections.
**Core:** Same row-action projection as cyclic Kaczmarz, but selects rows with probability proportional to their squared norm. Uses a seeded PRNG (seed `20240811`) and a binary search over a CDF for row selection. This is structurally different from the cyclic variant and has provably faster expected convergence.
**Assert:** Expected: `[2, 2.9999999999999996]`, bias `0.4999999999999997` at 1e-9.
**⚠️ Defect:** The randomized selection is deterministic (seeded PRNG), so the same row sequence is produced every run. The CDF-based sampling via binary search is correct. No precondition check needed (Kaczmarz works on any consistent system). The `lr` parameter is unused.

---
*△ AURA Pattern Library — © Reality Optimizer*
