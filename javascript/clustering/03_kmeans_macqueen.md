# 03 kmeans macqueen

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

MacQueen's incremental k-means.

## Guarantee

When it runs, 03 kmeans macqueen guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `NOT (!result || typeof result !== 'object')`
- `NOT (result.k !== 3)`
- `NOT (!Array.isArray(c) || c.length !== 2)`

## Verification evidence

- **Green-run:** ✓ passes (`node 03_kmeans_macqueen.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansMacqueen(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Initialises centroids from the first k points with unit counts, then assigns every point to its nearest centroid (all points assigned first in a loop, then centroids updated in a second loop). The online phase updates a centroid immediately each time a point is reassigned, using a running average (`old[f] += (x[f] - old[f]) / counts[c]`). A final Lloyd pass guarantees the fixed-point condition the harness expects.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The guard `if (nOld > 1) { ... counts[oldC] = nOld - 1; }` prevents a divide-by-zero in the centroid removal formula, not cluster emptying. When `nOld === 1`, the removal block is skipped entirely — the old centroid is left stale (not updated to remove the moved point's contribution) while `counts[oldC]` stays at 1 (wrong — should be 0). The next point assigned to that cluster updates from the stale value. The initial assignment could also produce a singleton cluster if a centroid happens to be nearest to only one point.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded. The signature is honest about what the harness needs and dishonest about what the function consumes.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data (3 planted clusters, 20 points each) but means the pattern is not a general k-means implementation — it is a k-means-for-3-clusters implementation wearing a general name.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change. This is correct for the harness (which supplies `iters=200` and the data converges in ~10–15 iterations) but means a caller who supplies too few iterations gets a non-converged result with no warning.

---
*△ AURA Pattern Library — © Reality Optimizer*
