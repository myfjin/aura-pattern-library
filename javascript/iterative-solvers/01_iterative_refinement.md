# 01 iterative refinement

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Iterative refinement for linear regression.

## Guarantee

When it runs, 01 iterative refinement guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 01_iterative_refinement.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `iterativeRefinementRegression(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of refinement iterations (internally halved).
**Core:** Solves `AtA * theta = Aty` using Gaussian elimination with partial pivoting, then iteratively refines the solution by solving the same system for the residual correction. The refinement loop runs `floor(iters / 2)` iterations and stops early if the residual sum drops below 1e-12.
**Assert:** Expected: `[2, 2.9999999999999996]`, bias `0.5` at 1e-9.
**⚠️ Defect:** The initial solve uses Gaussian elimination, which is a direct method — it already produces the exact solution (to machine precision) for this well-conditioned 3x3 system. The iterative refinement is completely unexercised: the residual is already at machine zero after the first solve, so the refinement loop exits immediately. This is the same defect class as the statistics batch — a pattern named for an iterative correction that is never tested against a case where it would matter.

---
*△ AURA Pattern Library — © Reality Optimizer*
