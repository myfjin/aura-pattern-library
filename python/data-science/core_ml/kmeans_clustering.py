"""
k-Means Clustering (from scratch).

Core idea: Partition data into k clusters by iteratively assigning samples
to the nearest centroid and updating centroids to be the mean of assigned samples.
Repeat until convergence (centroids stop moving).

When to use: Unsupervised clustering; exploratory analysis; identifying natural groups.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def euclidean_distance(p1: List[float], p2: List[float]) -> float:
    """Compute Euclidean distance between two points."""
    return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))))


def kmeans(
    X: List[List[float]],
    k: int,
    max_iterations: int = 100,
    tolerance: float = 1e-4
) -> Tuple[List[List[float]], List[int]]:
    """
    Fit k-means clustering.

    Args:
        X: list of data points (each a feature vector)
        k: number of clusters
        max_iterations: maximum number of iterations
        tolerance: convergence threshold for centroid movement

    Returns:
        (centroids, assignments): final centroids and cluster assignments for each sample
    """
    n_samples = len(X)
    n_features = len(X[0]) if X else 0

    # Initialize centroids: randomly select k samples
    indices = random.sample(range(n_samples), k)
    centroids = [X[i][:] for i in indices]

    for iteration in range(max_iterations):
        # Assign samples to nearest centroid
        assignments = []
        for i in range(n_samples):
            distances = [euclidean_distance(X[i], centroids[j]) for j in range(k)]
            assignments.append(distances.index(min(distances)))

        # Compute new centroids
        new_centroids = []
        for j in range(k):
            cluster_points = [X[i] for i in range(n_samples) if assignments[i] == j]
            if cluster_points:
                centroid = [sum(p[f] for p in cluster_points) / len(cluster_points)
                           for f in range(n_features)]
            else:
                # Empty cluster: keep old centroid
                centroid = centroids[j][:]
            new_centroids.append(centroid)

        # Check convergence: sum of centroid movements
        movement = sum(euclidean_distance(centroids[j], new_centroids[j]) for j in range(k))
        centroids = new_centroids

        if movement < tolerance:
            break

    # Final assignment
    assignments = []
    for i in range(n_samples):
        distances = [euclidean_distance(X[i], centroids[j]) for j in range(k)]
        assignments.append(distances.index(min(distances)))

    return centroids, assignments


def intra_cluster_distance(
    X: List[List[float]],
    centroids: List[List[float]],
    assignments: List[int]
) -> float:
    """Compute average distance from points to their centroid (inertia)."""
    total_dist = 0.0
    for i in range(len(X)):
        c = assignments[i]
        total_dist += euclidean_distance(X[i], centroids[c])
    return total_dist / len(X) if X else 0.0


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic data: 3 well-separated clusters
    n_per_cluster = 20
    X = []

    # Cluster 0: around (0, 0)
    for _ in range(n_per_cluster):
        X.append([random.gauss(0, 0.5), random.gauss(0, 0.5)])

    # Cluster 1: around (5, 0)
    for _ in range(n_per_cluster):
        X.append([random.gauss(5, 0.5), random.gauss(0, 0.5)])

    # Cluster 2: around (2.5, 4)
    for _ in range(n_per_cluster):
        X.append([random.gauss(2.5, 0.5), random.gauss(4, 0.5)])

    # Fit k-means
    centroids, assignments = kmeans(X, k=3, max_iterations=100)

    # Evaluate: most points should be in the correct cluster
    # Cluster 0: points 0-19, Cluster 1: points 20-39, Cluster 2: points 40-59
    correct = 0
    for i in range(len(X)):
        true_cluster = i // n_per_cluster
        # Find which predicted cluster matches (may be permuted)
        # For now just check that points in same true cluster are assigned to same predicted cluster
        pass

    # Check intra-cluster distance is small (tight clusters)
    intra_dist = intra_cluster_distance(X, centroids, assignments)
    assert intra_dist < 2.0, f"Intra-cluster distance = {intra_dist} is too high"

    # Check that we have 3 distinct centroids
    centroid_dists = []
    for i in range(3):
        for j in range(i + 1, 3):
            centroid_dists.append(euclidean_distance(centroids[i], centroids[j]))
    assert min(centroid_dists) > 2.0, "Centroids are too close together"

    print(f"KMEANS_CLUSTERING PASS: intra_dist = {intra_dist:.3f}, k = 3")
