# 04 kmeans compare means

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Compare-means k-means.

## Guarantee

When it runs, 04 kmeans compare means guarantees its self-test assertions hold on the harness fixture
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

- **Green-run:** ✓ passes (`node 04_kmeans_compare_means.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansCompareMeans(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Builds an inter-centroid distance table each iteration. For each point, checks centroids in order and applies the prune `if (cd[0][c] > 0 && bestD < (cd[0][c] * cd[0][c]) / 4) continue;` — an inter-centroid triangle-inequality test taken against centroid 0. See the defect below: the compare-means rule requires this test against the current best centroid, not centroid 0.
**Assert:** Same shape and value checks as #1.
**⚠️ Defect:** The prune `if (cd[0][c] > 0 && bestD < (cd[0][c] * cd[0][c]) / 4) continue;` uses the distance from centroid **0**, but the triangle-inequality rule requires the distance from the **current best** centroid. The bound is therefore invalid whenever the best centroid is not centroid 0: the prune can skip a centroid that is genuinely closer, assigning the point to the wrong cluster. Measured: disabling only this prune line changes the resulting clustering on 5 of 60 random 3-cluster datasets. It does not fire on the harness fixture (centroid 0 happens to be the true nearest for most points), so the self-test passes despite the bug.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data but means the pattern is not a general k-means implementation.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change.
- **Empty-cluster fallback preserves old centroid.** Every pattern that recomputes centroids uses the pattern `if (counts[c] > 0) { ... }` without re-initialising empty clusters — the old centroid stays in place, and an empty cluster stays empty forever.

---
*△ AURA Pattern Library — © Reality Optimizer*
