# silhouette score

**Language:** Python · **Sphere:** data-science · **Category:** Clustering, Graph & Anomaly

**Signature:** `(points: List[Tuple[float, ...]], labels: List[int]) → float`

## What it does

Silhouette Score from scratch.

Measure of clustering quality: how similar a point is to its own cluster vs. other
clusters. Score ranges from -1 (wrong cluster) to 1 (well-clustered). Computed per point
as (b-a)/max(a,b), where a=avg distance to cluster members, b=min avg distance to other clusters.

Use when: evaluating cluster quality or choosing optimal k for k-means.

## Guarantee

When it runs, silhouette score guarantees correct_score >= 0.5; correct_score > 0.0; wrong_score >= 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `correct_score >= 0.5`
- `correct_score > 0.0`
- `wrong_score >= 0.5`
- `scrambled_score < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `silhouette_score(points, labels) → float`
**Valid input:** `points: List[Tuple[float, ...]]` — at least 2 points. `labels: List[int]` — at least 2 unique labels.
**Core:** Silhouette score: for each point, a = mean distance to same-cluster points, b = min mean distance to other-cluster points. Score = (b-a)/max(a,b). Range [-1, 1]. Higher is better. Tested on 2 well-separated Gaussian clusters (15 pts each at (0,0) and (5,0), σ=0.4).
**Assert:** Correct clustering score ≥ 0.5 and > 0. Scrambled labels score < 0.5.
**⚠️ Defect:** The test asserts `wrong_score >= 0.5` for the "wrong" clustering (labels swapped), which is trivially true because swapping labels on symmetric clusters gives the same score. The test then shuffles labels and checks `scrambled_score < 0.5`, but `random.shuffle(correct_labels)` modifies the list in-place after it was already used for `correct_score`, so `correct_labels` is now the shuffled version. This means the "scrambled" test uses the shuffled labels, which is correct, but the variable name `correct_labels` is misleading after the shuffle.

---
*△ AURA Pattern Library — © Reality Optimizer*
