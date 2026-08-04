# 06 kmeans kdtree

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

kd-tree accelerated k-means (blacklisting / filtering algorithm).

## Guarantee

When it runs, 06 kmeans kdtree guarantees its self-test assertions hold on the harness fixture
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

- **Green-run:** ✓ passes (`node 06_kmeans_kdtree.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansKdtree(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Builds an axis-aligned kd-tree over the data points once (median-split on alternating axes, leaf size 4). Each iteration, recursively assigns points in each tree node to the nearest centroid using cell-dominance pruning: a centroid is pruned from a node's candidate list if another centroid's **maximum** distance to the cell is less than its **minimum** distance. If only one candidate survives, all points in the node are assigned to it without further distance computation.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The kd-tree is built once and never rebuilt. This is correct for the data (which is static), but the cell bounds are computed from the data points, not the centroids — so the pruning effectiveness depends on how well the data partitions separate the clusters. For the harness data (3 well-separated spherical clusters), the kd-tree prunes aggressively. On data with overlapping clusters, the cell bounds will be large and little pruning will occur — the algorithm degrades to exact nearest-centroid for every point.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data but means the pattern is not a general k-means implementation.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change.
- **Empty-cluster fallback preserves old centroid.** Every pattern that recomputes centroids uses the pattern `if (counts[c] > 0) { ... }` without re-initialising empty clusters — the old centroid stays in place, and an empty cluster stays empty forever.

---
*△ AURA Pattern Library — © Reality Optimizer*
