"""
Elbow Method + K-Means from scratch.

K-means: iterative clustering that minimizes within-cluster inertia. Elbow method:
plot inertia vs. k and find the knee (largest drop in inertia). Core idea: inertia
decreases as k increases, but the rate of decrease flattens at the "true" k.

Use when: choosing optimal k for k-means clustering without labels.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple

def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
    """Compute Euclidean distance between two points."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def kmeans(
    points: List[Tuple[float, ...]],
    k: int,
    max_iterations: int = 100,
    seed: int = 42
) -> Tuple[List[int], List[Tuple[float, ...]], float]:
    """
    K-means clustering.

    Args:
        points: List of points
        k: Number of clusters
        max_iterations: Max iterations
        seed: Random seed for reproducibility

    Returns:
        (cluster labels, centroids, inertia)
    """
    random.seed(seed)
    n_points = len(points)
    point_dim = len(points[0])

    # K-means++: probabilistic initialization
    centroids = [random.choice(points)]
    for _ in range(k - 1):
        # For each point, compute distance to nearest centroid
        distances = [
            min(euclidean_distance(p, c) for c in centroids) ** 2
            for p in points
        ]
        total_dist = sum(distances)
        if total_dist > 0:
            probabilities = [d / total_dist for d in distances]
            # Choose next centroid with probability proportional to distance squared
            cumsum = 0.0
            r = random.random() * total_dist
            for i, p in enumerate(points):
                cumsum += distances[i]
                if cumsum >= r:
                    centroids.append(p)
                    break
        else:
            centroids.append(random.choice(points))

    for _ in range(max_iterations):
        old_centroids = [c for c in centroids]

        # Assign points to nearest centroid
        labels = [
            min(range(k), key=lambda j: euclidean_distance(p, centroids[j]))
            for p in points
        ]

        # Update centroids
        new_centroids = []
        for cluster_id in range(k):
            cluster_points = [points[i] for i in range(n_points) if labels[i] == cluster_id]
            if cluster_points:
                new_centroid = tuple(
                    sum(p[d] for p in cluster_points) / len(cluster_points)
                    for d in range(point_dim)
                )
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(centroids[cluster_id])

        centroids = new_centroids

        # Check convergence
        if all(euclidean_distance(c1, c2) < 1e-6 for c1, c2 in zip(old_centroids, centroids)):
            break

    # Compute inertia
    inertia = sum(
        euclidean_distance(points[i], centroids[labels[i]]) ** 2
        for i in range(n_points)
    )

    return labels, centroids, inertia

def elbow_knee(inertias: List[float]) -> int:
    """
    Find the knee in the inertia curve using second derivative heuristic.

    Args:
        inertias: Inertia values for k=1,2,3,...

    Returns:
        Index of knee (k value - 1)
    """
    if len(inertias) < 3:
        return 0

    # Compute differences between consecutive inertias
    diffs = [inertias[i] - inertias[i + 1] for i in range(len(inertias) - 1)]

    # Compute second differences (acceleration)
    second_diffs = [diffs[i] - diffs[i + 1] for i in range(len(diffs) - 1)]

    # Find the largest change in acceleration (biggest negative jump means knee)
    knee_idx = second_diffs.index(max(second_diffs)) + 1

    return knee_idx

if __name__ == "__main__":
    random.seed(42)

    # Plant three well-separated clusters
    cluster1 = [(random.gauss(0.0, 0.4), random.gauss(0.0, 0.4)) for _ in range(20)]
    cluster2 = [(random.gauss(6.0, 0.4), random.gauss(6.0, 0.4)) for _ in range(20)]
    cluster3 = [(random.gauss(12.0, 0.4), random.gauss(0.0, 0.4)) for _ in range(20)]
    points = cluster1 + cluster2 + cluster3

    # Compute inertia for k=1 to 6
    inertias = []
    for k in range(1, 7):
        _, _, inertia = kmeans(points, k, max_iterations=50, seed=42)
        inertias.append(inertia)

    # Find elbow
    knee_idx = elbow_knee(inertias)
    detected_k = knee_idx + 1

    # Verify: knee should be at k=3 (since we planted 3 clusters)
    # The inertia drop from k=2 to k=3 should be larger than from k=3 to k=4
    assert detected_k == 3, f"Expected knee at k=3, got k={detected_k}"
    assert inertias[1] - inertias[2] > inertias[2] - inertias[3], \
        "Drop from k=2 to k=3 should be larger than k=3 to k=4"

    print(f"elbow_method_kmeans.py: knee detected at k={detected_k} PASS")
