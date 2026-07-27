# hierarchical agglomerative

**Language:** Python · **Sphere:** data-science · **Category:** Clustering, Graph & Anomaly

**Signature:** `(points: List[Tuple[float, ...]], linkage: str) → Tuple[List[List[int]], List[Tuple[int, int, float]]]`

## What it does

Hierarchical Agglomerative Clustering from scratch.

Bottom-up merging of clusters using distance linkage (single or complete). Produces a
dendrogram (tree structure) of nested partitions. Cut at height k to get k clusters.
Core idea: repeatedly merge two closest clusters until one remains.

Use when: you want a hierarchy of clusters or need to explore multiple granularities.

## Guarantee

When it runs, hierarchical agglomerative guarantees all((l in range(3) for l in labels)) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(unique_labels) == 3`
- `all((l in range(3) for l in labels))`
- `len(set(c1_labels)) <= 2`
- `len(set(c2_labels)) <= 2`
- `len(set(c3_labels)) <= 2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `hierarchical_agglomerative(points, linkage="complete") → (clusters, merge_history)`, `cut_dendrogram(points, k, linkage="complete") → List[int]`
**Valid input:** `points: List[Tuple[float, ...]]` — at least 2 points. `linkage` in {"single", "complete"}.
**Core:** Bottom-up hierarchical clustering. Start with each point as its own cluster. Repeatedly merge the two closest clusters (single/min or complete/max linkage). Cut dendrogram at k clusters. Tested on 3 well-separated Gaussian clusters (10 pts each).
**Assert:** On 3 clusters (10 pts each at (0,0), (5,5), (10,0), σ=0.5): cut at k=3 produces exactly 3 clusters, each original cluster is at most 2-way fragmented.
**⚠️ Defect:** The algorithm is O(n³) due to recomputing all pairwise cluster distances at each merge step. For n=30 points, this is fine (~4,000 distance computations per merge × 29 merges). For n > 1,000, this becomes prohibitive. A proper implementation would use a distance matrix with lazy updates (Lance-Williams formula). Also, the `cluster_distance` function recomputes all pairwise distances between clusters each time, with no caching.

---
*△ AURA Pattern Library — © Reality Optimizer*
