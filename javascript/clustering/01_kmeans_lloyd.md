# 01 kmeans lloyd

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Lloyd's k-means clustering.

## Guarantee

When it runs, 01 kmeans lloyd guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `NOT (!result || typeof result !== 'object')`
- `NOT (result.k !== 3)`
- `NOT (!Array.isArray(c) || c.length !== 2)`

## Verification evidence

- **Green-run:** ✓ passes (`node 01_kmeans_lloyd.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansLloyd(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers (n × nf). `y` and `lr` are unused. `iters` should be at least 10 for the harness data (converges in ~10 iterations).
**Core:** Initialises centroids from the first k data points (relies on the harness data being ordered round-robin across clusters, so the first 3 points are one from each cluster). Then alternates between assigning every point to its nearest centroid and recomputing each centroid as the mean of its assigned points. Stops when no assignment changes or `iters` is exhausted. A final pass ensures every point is assigned to its true nearest centroid (the loop may have stopped with stale assignments).
**Assert:** Asserts `k === 3`, 3 centroids each of length 2, 60 assignments. Compares centroids and assignments against expected values at 1e-9 relative tolerance.
**⚠️ Defect:** First-k-points initialisation is only valid because the harness data is round-robin ordered. On arbitrary data, all three initial centroids could land in the same cluster, producing a degenerate partition. The empty-cluster fallback (`next[c] = centroids[c].slice()`) preserves the old centroid rather than re-initialising, so an empty cluster stays empty forever.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded. The signature is honest about what the harness needs and dishonest about what the function consumes.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data (3 planted clusters, 20 points each) but means the pattern is not a general k-means implementation — it is a k-means-for-3-clusters implementation wearing a general name.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change. This is correct for the harness (which supplies `iters=200` and the data converges in ~10–15 iterations) but means a caller who supplies too few iterations gets a non-converged result with no warning.

---
*△ AURA Pattern Library — © Reality Optimizer*
