# 09 kmeans random partition

**Language:** JavaScript · **Sphere:** javascript · **Category:** Clustering

**Signature:** `(X, y, lr, iters) → object`

## What it does

Random-partition initialization followed by Lloyd's algorithm.

## Guarantee

When it runs, 09 kmeans random partition guarantees its self-test assertions hold on the harness fixture
(weak-grade: regression-locked, proven by run under `node`).

**Checkable constraints:**

- `NOT (!result || typeof result !== 'object')`
- `NOT (result.k !== 3)`
- `NOT (!Array.isArray(c) || c.length !== 2)`

## Verification evidence

- **Green-run:** ✓ passes (`node 09_kmeans_random_partition.js` exits 0)
- **Constraint strength:** weak (regression-locked to an oracle-validated baseline)
- **Independent oracle:** ✓ **consensus** — three-engine agreement (V8 / JavaScriptCore / QuickJS)
  at staging, plus a self-test proven to fail under mutation. This establishes the code still
  computes what those engines agreed it did — **not that it is correct**.
- **Peer review:** ver-corroborated (code-verified 2026-08-04)

## Detail (audited)

*Audited 2026-08-04. Written by 6E, code-verified by Ver.*

**Entry fn:** `kmeansRandomPartition(X, y, lr, iters)`
**Valid input:** `X` must be a 2D array of numbers. `y` and `lr` are unused. `iters` should be at least 10.
**Core:** Uses a seeded PRNG (seed `20240804`) to assign each point to a random cluster (0, 1, or 2). Computes initial centroids as the means of these random partitions. Then runs standard Lloyd iterations. If a cluster empties during Lloyd, it is re-initialised from a random data point.
**Assert:** Same shape and value checks as #1, with centroids in a different order (random partition produces a different initialisation than first-k or k-means++).
**⚠️ Defect:** The empty-cluster re-initialisation picks a random data point using the seeded PRNG, which is deterministic for the harness. But the re-initialised centroid is a single data point, not the mean of any group — it may be an outlier. This is a valid approach (the next Lloyd iteration will move it toward its assigned points) but means the first iteration after re-initialisation has a centroid that is not the mean of its cluster.

**Shared with every pattern in its family:**

- **`y` and `lr` are silently ignored.** Every function takes `(X, y, lr, iters)` because that is the Forge Gate harness contract, but k-means has no use for a target vector or a learning rate. A caller who passes meaningful values gets no warning that they were discarded. The signature is honest about what the harness needs and dishonest about what the function consumes.
- **`k=3` is hardcoded.** Every pattern fixes the number of clusters at 3. This matches the harness test data (3 planted clusters, 20 points each) but means the pattern is not a general k-means implementation — it is a k-means-for-3-clusters implementation wearing a general name.
- **Iteration-capped convergence.** Every pattern uses `iters` as a hard iteration limit rather than a tolerance-based convergence check. The loop runs for up to `iters` passes and stops early only if no assignments change. This is correct for the harness (which supplies `iters=200` and the data converges in ~10–15 iterations) but means a caller who supplies too few iterations gets a non-converged result with no warning.

---
*△ AURA Pattern Library — © Reality Optimizer*
