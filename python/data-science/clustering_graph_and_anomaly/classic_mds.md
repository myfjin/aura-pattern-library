# classic mds

**Language:** Python · **Sphere:** data-science · **Category:** Clustering, Graph & Anomaly

**Signature:** `(p1: Tuple[float, ...], p2: Tuple[float, ...]) → float`

## What it does

Classical Multidimensional Scaling (MDS) from scratch.

Non-linear dimensionality reduction: embed points in lower-dimensional space preserving
pairwise distances. Core idea: convert distance matrix to inner-product matrix (double
centering), then use eigendecomposition to find optimal low-rank embedding.

Use when: visualizing high-dimensional data or embedding based on pairwise distances.

## Guarantee

When it runs, classic mds guarantees correlation > 0.3 or abs(correlation) < 0.1; len(embedded) == len(points); any((abs(e[0]) > 0.001 or abs(e[1]) > 0.001 for e in embedded)) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `correlation > 0.3 or abs(correlation) < 0.1`
- `len(embedded) == len(points)`
- `any((abs(e[0]) > 0.001 or abs(e[1]) > 0.001 for e in embedded))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `classical_mds_2d(points) → List[Tuple[float, float]]`
**Valid input:** `points: List[Tuple[float, ...]]` — at least 2 points, all same dimension.
**Core:** Classical MDS: compute centered Gram matrix from high-dimensional points, then approximate 2D embedding using the first two rows of the Gram matrix. Preserves pairwise distances approximately. Tested on 40 random 50D points.
**Assert:** On 40 points in 50D: embedding size matches input, embedding is not all zeros, distance correlation > 0.3 or < 0.1 (lenient threshold).
**⚠️ Defect:** This is NOT true classical MDS. True MDS requires eigendecomposition of the doubly-centered distance matrix. This implementation uses the Gram matrix of the original points (which requires the original coordinates, defeating the purpose of MDS) and a heuristic projection (G[i][0] ± G[i][1]) instead of proper eigendecomposition. The distance correlation assertion is extremely lenient (0.3) and the fallback `abs(correlation) < 0.1` means a correlation of 0.0 also passes.

---
*△ AURA Pattern Library — © Reality Optimizer*
