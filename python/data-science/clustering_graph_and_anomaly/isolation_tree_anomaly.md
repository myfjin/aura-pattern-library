# isolation tree anomaly

**Language:** Python · **Sphere:** data-science · **Category:** Clustering, Graph & Anomaly

**Signature:** `(points: List[Tuple[float, ...]], indices: List[int], depth: int, max_depth: int) → IsolationNode`

## What it does

Isolation Forest (Lite) Anomaly Detection from scratch.

Ensemble of random isolation trees: points requiring fewer splits to isolate are likely
anomalies (short average path length). Core idea: anomalies are isolated easily; normals
require many splits. Anomaly score = average path length across trees (lower = anomaly).

Use when: detecting outliers/anomalies without computing distances to all points.

## Guarantee

When it runs, isolation tree anomaly guarantees avg_outlier < avg_normal; avg_normal > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `avg_outlier < avg_normal`
- `avg_normal > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `isolation_forest_anomaly_score(points, num_trees=50, seed=42) → List[float]`
**Valid input:** `points: List[Tuple[float, ...]]` — at least 2 points. `num_trees ≥ 1`.
**Core:** Isolation forest for anomaly detection. Build ensemble of random isolation trees: randomly select feature and split value, recurse until single point or max depth. Anomaly score = average path length across trees (shorter = more anomalous). Tested on 100 normal points (Gaussian cluster) + 5 outliers.
**Assert:** On 100 normal + 5 outlier points: average outlier path length < average normal path length, all scores positive.
**⚠️ Defect:** The `build_isolation_tree` function returns a leaf node when `min_val == max_val` (can't split), but this check is done AFTER selecting the split feature. If all points have the same value for the randomly selected feature but differ on other features, the algorithm gives up instead of trying another feature. Also, the max_depth of 10 is hardcoded and may be too shallow for large datasets (the expected path length for n=100 is ~log₂(100) ≈ 7, so 10 is adequate here).

---
*△ AURA Pattern Library — © Reality Optimizer*
