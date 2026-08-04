# statistics naive sos

**Language:** JavaScript · **Sphere:** javascript · **Category:** Summary Statistics

**Signature:** `(X, y, lr, iters) → object`

## What it does

Naive sum-of-squares formula for mean and population variance.

## Guarantee

When it runs, statistics naive sos guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `result.statsX && typeof result.statsX === 'object' && isFinite(result.statsX.mean) && isFinite(result.statsX.variance)`
- `result.statsY && typeof result.statsY === 'object' && isFinite(result.statsY.mean) && isFinite(result.statsY.variance)`
- `typeof result.correlation === 'number' && isFinite(result.correlation)`
- `typeof result.covariance === 'number' && isFinite(result.covariance)`
- `approxEqual(result.statsX, expectedStatsX, 1e-9)`
- `approxEqual(result.statsY, expectedStatsY, 1e-9)`
- `approxEqual(result.correlation, expectedCorrelation, 1e-9)`
- `approxEqual(result.covariance, expectedCovariance, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node statistics_naive_sos.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `naiveVariance(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array where `X[i][0]` is the i-th data point. `y` is the target vector. `lr` and `iters` are unused.
**Core:** Computes `sum = Σx` and `sumSq = Σx²` in a single pass, then returns `variance = sumSq/n - (sum/n)²`. This is the textbook formula that catastrophically cancels when variance is small compared to the data magnitude.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The docstring honestly presents this as "the numerically weakest method... included only as a pedagogical baseline; a careful implementation should prefer Welford or Kahan." This is the only pattern in the batch whose self-test actually tests what the pattern is supposed to demonstrate — but only because the harness data happens to be well-conditioned enough that even the bad formula works. On data where `sumSq ≈ (sum)²/n` (e.g., xs = [1e12, 1e12 + 1, 1e12 + 2]), this formula would return variance ≈ 0 while the true variance is ~1.

**Shared with every pattern in its family:**

- **`lr` and `iters` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but variance computation has no use for a learning rate or iteration count. `X` is used (mapped to `xs` via `X.map(row => row[0])`), and `y` is used as the target vector for the Y statistics. `lr` and `iters` are dead parameters.
- **The self-test does not exercise the instability any of these patterns exist to fix.** All 10 use the same harness data: 30 points in [-1, 1] with variance ~0.37 (xs) and ~2.0 (ys). These are small, well-conditioned values where even the naive `sumSq/n - mean²` formula produces the correct answer to 1e-9. A Kahan summation verified on this data proves nothing about Kahan summation — the compensation path is never tested against a case where it would matter. The self-test passes for reasons unrelated to each pattern's purpose.
- **`k=3` is not relevant here** (these are statistics, not clustering), but the harness contract still forces the `(X, y, lr, iters)` signature.

---
*△ AURA Pattern Library — © Reality Optimizer*
