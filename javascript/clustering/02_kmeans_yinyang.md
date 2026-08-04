# 02 kmeans yinyang

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Yinyang k-means.

## Guarantee

When it runs, 02 kmeans yinyang guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `result && typeof result === 'object'`
- `result.k === 3`
- `Array.isArray(result.centroids) && result.centroids.length === 3`
- `Array.isArray(c) && c.length === 2`
- `Array.isArray(result.assignments) && result.assignments.length === 60`
- `approxEqual(result.centroids, expectedCentroids, 1e-9)`
- `approxEqual(result.assignments, expectedAssignments, 1e-9)`

## Verification evidence

- **Green-run:** ✓ passes (`node 02_kmeans_yinyang.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansYinyang(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Groups the 3 centroids into 2 super-clusters (`groupOf = [0, 1, 1]`). Each point keeps an upper bound to its assigned centroid and a per-group lower bound. Before computing a full distance, checks whether the upper bound already beats all group-level lower bounds — if so, the point cannot change assignment. The group assignment is hardcoded for k=3.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The group assignment `groupOf = [0, 1, 1]` is hardcoded for exactly 3 centroids, with centroid 0 in its own group and centroids 1 and 2 grouped together. This is a reasonable partition for the harness data (centroid 0 is the [0,0] cluster, centroids 1 and 2 are the [5,0] and [2.5,4] clusters which are farther apart), but it means the Yinyang acceleration is tuned to this specific data layout. On data where the optimal grouping is different, the bounds will be looser and less pruning will occur.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data but means the pattern is not a general k-means implementation.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change.
- **Empty-cluster fallback preserves old centroid.** Every pattern that recomputes centroids uses the pattern `if (counts[c] > 0) { ... }` without re-initialising empty clusters — the old centroid stays in place, and an empty cluster stays empty forever.

---
*△ AURA Pattern Library — © Reality Optimizer*
