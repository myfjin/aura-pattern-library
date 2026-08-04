# statistics shifted

**Language:** JavaScript · **Sphere:** javascript · **Category:** Summary Statistics

**Signature:** `(X, y, lr, iters) → object`

## What it does

Shifted (compensated) one-pass variance: subtract a shift constant to reduce

## Guarantee

When it runs, statistics shifted guarantees its self-test assertions hold on the harness fixture
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

- **Green-run:** ✓ passes (`node statistics_shifted.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `shiftedVariance(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array where `X[i][0]` is the i-th data point. `y` is the target vector. `lr` and `iters` are unused.
**Core:** Subtracts the first data point as a shift constant: `d = xs[i] - shift; sum += d; sumSq += d²`. Then computes `mean = shift + sum/n` and `variance = (sumSq - sum²/n) / n`. The shift reduces the magnitude of the values, making the `sumSq - sum²/n` cancellation less severe.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The variance formula is still `sumSq - sum²/n` — the same cancellation-prone form as naive_sos, just applied to shifted data. The shift helps when all values are large and close together (e.g., [1e12, 1e12+1, 1e12+2] shifted by 1e12 becomes [0, 1, 2]), but the cancellation is reduced, not eliminated. The choice of `xs[0]` as the shift is arbitrary — a better shift would be the mean or median. For the harness data (values in [-1, 1]), the shift has no effect because the values are already small.

**Shared with every pattern in its family:**

- **`lr` and `iters` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but variance computation has no use for a learning rate or iteration count. `X` is used (mapped to `xs` via `X.map(row => row[0])`), and `y` is used as the target vector for the Y statistics. `lr` and `iters` are dead parameters.
- **The self-test does not exercise the instability any of these patterns exist to fix.** All 10 use the same harness data: 30 points in [-1, 1] with variance ~0.37 (xs) and ~2.0 (ys). These are small, well-conditioned values where even the naive `sumSq/n - mean²` formula produces the correct answer to 1e-9. A Kahan summation verified on this data proves nothing about Kahan summation — the compensation path is never tested against a case where it would matter. The self-test passes for reasons unrelated to each pattern's purpose.
- **`k=3` is not relevant here** (these are statistics, not clustering), but the harness contract still forces the `(X, y, lr, iters)` signature.

---
*△ AURA Pattern Library — © Reality Optimizer*
