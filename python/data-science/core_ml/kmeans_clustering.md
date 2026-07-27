# kmeans clustering

**Language:** Python · **Sphere:** data-science · **Category:** Core ML

**Signature:** `(p1: List[float], p2: List[float]) → float`

## What it does

k-Means Clustering (from scratch).

Core idea: Partition data into k clusters by iteratively assigning samples
to the nearest centroid and updating centroids to be the mean of assigned samples.
Repeat until convergence (centroids stop moving).

When to use: Unsupervised clustering; exploratory analysis; identifying natural groups.

## Guarantee

When it runs, kmeans clustering guarantees intra_dist < 2.0; min(centroid_dists) > 2.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `intra_dist < 2.0`
- `min(centroid_dists) > 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — metamorphic, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `kmeans(X, k, max_iterations=100, tolerance=1e-4) → (centroids, assignments)`
**Valid input:** `X: List[List[float]]` — at least k samples, all same length. `k: int` ≥ 2. `max_iterations` ≥ 1.
**Core:** Standard k-means: randomly initialize k centroids from data, assign each point to nearest centroid (Euclidean), recompute centroids as cluster means, repeat until centroid movement < tolerance or max iterations. Returns final centroids and assignments.
**Assert:** On 3 synthetic Gaussian clusters (20 pts each, well-separated at (0,0), (5,0), (2.5,4) with σ=0.5), intra-cluster distance < 2.0 and min centroid distance > 2.0.
**⚠️ Defect:** The test computes `correct` (line 121) but never uses it — the `for` loop body is `pass`. The test only checks cluster tightness and separation, not whether points are assigned to the correct cluster. A degenerate solution (all points in one cluster) could pass if centroids happened to be far apart.

---
*△ AURA Pattern Library — © Reality Optimizer*
