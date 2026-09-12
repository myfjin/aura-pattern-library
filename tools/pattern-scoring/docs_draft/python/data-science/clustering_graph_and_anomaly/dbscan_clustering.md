# DBSCAN Clustering

**File:** `python/data-science/clustering_graph_and_anomaly/dbscan_clustering.py`
**Sphere:** Data Science — Clustering, Graph, and Anomaly Detection

---

## What it solves

**Find clusters of any shape, and spot the outliers.** K-means forces clusters into spheres; DBSCAN doesn't care. It groups points that are close together (within `eps` distance) and have at least `min_pts` neighbors. Points in sparse regions are labeled as noise. The algorithm grows clusters from dense points, merging overlapping regions — like oil drops on water coalescing.

**When to use:** Clusters have irregular shapes, density varies, or you need to identify outliers (noise points). Common in geospatial clustering, anomaly detection, and any domain where "round clusters" is a bad assumption.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `points` | list of `(float, ...)` tuples | empty → all noise |
| `eps` | > 0, neighborhood radius | 0 → all noise · too large → one cluster |
| `min_pts` | ≥ 1, density threshold | 1 → every point is its own cluster |

---

## How inputs shape the output

- **`eps` is the reach knob:** too small → everything is noise; too large → everything is one cluster. The demo's eps=1.0 with clusters centered at (2,2) and (8,8) cleanly separates them.
- **`min_pts` is the density threshold:** higher → only very dense regions form clusters; lower → looser groupings. The demo's min_pts=5 with 20 points per cluster works well.
- **Noise points are honest:** the 5 random uniform points in [0,10]² are correctly labeled as noise — they don't belong to either dense cluster.

---

## Worked example (real run)

```
$ python3 python/data-science/clustering_graph_and_anomaly/dbscan_clustering.py
dbscan_clustering.py: 2 clusters, 5 noise points PASS
```

**Reading the output:** 2 clusters found (the planted groups at (2,2) and (8,8)), 5 noise points (the uniform random points). The assert proves the algorithm correctly separates dense regions from sparse.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty points list | returns all -1 labels | correct but silent |
| eps=0 | all points are noise | correct but surprising |
| single point | labeled noise (no neighbors) | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
