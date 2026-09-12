"""
Silhouette Score from scratch.

Measure of clustering quality: how similar a point is to its own cluster vs. other
clusters. Score ranges from -1 (wrong cluster) to 1 (well-clustered). Computed per point
as (b-a)/max(a,b), where a=avg distance to cluster members, b=min avg distance to other clusters.

Use when: evaluating cluster quality or choosing optimal k for k-means.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple

def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
    """Compute Euclidean distance between two points."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def silhouette_score(
    points: List[Tuple[float, ...]],
    labels: List[int]
) -> float:
    """
    Compute average silhouette score for a clustering.

    Args:
        points: List of points
        labels: Cluster label for each point

    Returns:
        Average silhouette coefficient (higher is better)
    """
    unique_labels = set(labels)
    num_clusters = len(unique_labels)

    if num_clusters < 2:
        return 0.0  # Can't compute for single cluster

    silhouette_scores = []

    for i, point in enumerate(points):
        current_cluster = labels[i]

        # a: average distance to points in same cluster
        same_cluster_indices = [j for j, l in enumerate(labels) if l == current_cluster]
        if len(same_cluster_indices) > 1:
            a = sum(
                euclidean_distance(point, points[j])
                for j in same_cluster_indices
                if j != i
            ) / (len(same_cluster_indices) - 1)
        else:
            a = 0.0

        # b: minimum average distance to points in other clusters
        b = float("inf")
        for cluster_id in unique_labels:
            if cluster_id == current_cluster:
                continue
            other_cluster_indices = [j for j, l in enumerate(labels) if l == cluster_id]
            avg_dist = sum(
                euclidean_distance(point, points[j])
                for j in other_cluster_indices
            ) / len(other_cluster_indices)
            b = min(b, avg_dist)

        # Silhouette coefficient
        if max(a, b) > 0:
            s = (b - a) / max(a, b)
        else:
            s = 0.0

        silhouette_scores.append(s)

    return sum(silhouette_scores) / len(silhouette_scores)

if __name__ == "__main__":
    import random
    random.seed(42)

    # Plant two well-separated clusters
    cluster1 = [(random.gauss(0.0, 0.4), random.gauss(0.0, 0.4)) for _ in range(15)]
    cluster2 = [(random.gauss(5.0, 0.4), random.gauss(5.0, 0.4)) for _ in range(15)]
    points = cluster1 + cluster2

    # Correct clustering
    correct_labels = [0] * 15 + [1] * 15
    correct_score = silhouette_score(points, correct_labels)

    # Wrong clustering (swap some labels)
    wrong_labels = [1] * 15 + [0] * 15
    wrong_score = silhouette_score(points, wrong_labels)

    # Correct score should be higher (or equal for symmetric case)
    assert correct_score >= 0.5, f"Correct clustering should have high score, got {correct_score}"
    assert correct_score > 0.0, "Correct clustering should be positive"

    # Both should be the same due to symmetry, but let's check they're both high
    assert wrong_score >= 0.5, f"Symmetric wrong clustering should also be high"

    # Test with scrambled labels (should be low)
    random.shuffle(correct_labels)
    scrambled_score = silhouette_score(points, correct_labels)
    assert scrambled_score < 0.5, f"Scrambled labels should have low score, got {scrambled_score}"

    print(f"silhouette_score.py: correct={correct_score:.3f}, wrong={wrong_score:.3f}, scrambled={scrambled_score:.3f} PASS")
