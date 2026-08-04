# linreg sor

**Language:** JavaScript · **Sphere:** javascript · **Category:** Iterative Solvers

**Signature:** `(X, y, lr, iters) → object`

## What it does

Linear regression via successive over-relaxation (SOR) on the normal

## Guarantee

When it runs, linreg sor guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `Array.isArray(result.weights) && result.weights.length === 2`
- `typeof result.bias === 'number' && isFinite(result.bias)`
- `approxEqual(result.weights, expectedWeights, 1e-9)`
- `approxEqual(result.bias, expectedBias, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node linreg_sor.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `successiveOverRelaxation(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` is the target vector. `lr` is unused. `iters` controls the number of SOR sweeps. ⚠️ `AtA` must be SPD and omega must be in (0, 2).
**Core:** Same structure as Gauss-Seidel, but applies relaxation: `newVal = s / AtA[i][i]; theta[i] = (1 - omega) * theta[i] + omega * newVal` with `omega = 1.5`.
**Assert:** Expected: `[2, 3]`, bias `0.5` at 1e-9 — exact true weights.
**⚠️ Defect:** SOR converges only for `0 < omega < 2` on SPD matrices, and there is no precondition check. `omega = 1.5` is hardcoded rather than a parameter. On the harness fixture the value is IRRELEVANT — swept across 0.5, 1.0, 1.3, 1.5, 1.7 the result is identical to machine precision, and only 1.9 shows any error (1.6e-9). The relaxation parameter — the entire point of SOR over Gauss-Seidel — is therefore UNEXERCISED by the self-test. On a real problem the optimal omega matters a great deal and 1.5 is an arbitrary starting point, not a tuned one.

---
*△ AURA Pattern Library — © Reality Optimizer*
