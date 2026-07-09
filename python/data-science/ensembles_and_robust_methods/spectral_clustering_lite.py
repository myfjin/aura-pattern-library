"""
Spectral Clustering Lite.

Spectral clustering constructs a graph Laplacian from pairwise affinities,
computes its eigenvector (via power iteration), and clusters by the sign of
the Fiedler vector. It recovers non-convex clusters (e.g., two moons) where
k-means fails.

Use when: non-convex cluster shapes, graph-based clustering, manifold structure.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple

def euclidean_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Euclidean distance between two 2D points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def build_affinity_matrix(X: List[Tuple[float, float]], sigma: float = 1.0) -> List[List[float]]:
    """
    Build affinity (adjacency) matrix using RBF kernel.
    W[i,j] = exp(-distance(X[i], X[j])^2 / (2*sigma^2))
    """
    n = len(X)
    W = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                W[i][j] = 0.0  # No self-loop
            else:
                dist = euclidean_distance(X[i], X[j])
                W[i][j] = math.exp(-dist * dist / (2 * sigma * sigma))

    return W

def compute_degree_matrix_diag(W: List[List[float]]) -> List[float]:
    """Compute diagonal of degree matrix: D[i,i] = sum_j W[i,j]."""
    n = len(W)
    degree = [sum(W[i]) for i in range(n)]
    return degree

def graph_laplacian(W: List[List[float]]) -> List[List[float]]:
    """Compute graph Laplacian: L = D - W."""
    n = len(W)
    degree = compute_degree_matrix_diag(W)

    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                L[i][j] = degree[i]
            else:
                L[i][j] = -W[i][j]

    return L

def power_iteration(L: List[List[float]], num_iter: int = 300) -> List[float]:
    """
    Fiedler vector (eigenvector of the SECOND-smallest Laplacian eigenvalue)
    via shifted power iteration. Plain power iteration on L converges to the
    LARGEST eigenvalue's eigenvector — the wrong one. So iterate on (cI - L),
    whose dominant eigenvector is L's smallest; and deflate the trivial
    all-ones eigenvector (λ=0) by re-centering to mean zero each step, which
    leaves the Fiedler vector as the dominant direction.
    """
    n = len(L)
    c = 2.0 * max(L[i][i] for i in range(n)) + 1.0   # Gershgorin: c > λ_max(L)

    v = [random.gauss(0, 1) for _ in range(n)]
    mean = sum(v) / n
    v = [x - mean for x in v]
    norm = math.sqrt(sum(x * x for x in v)) or 1.0
    v = [x / norm for x in v]

    for _ in range(num_iter):
        # w = (cI - L) v
        w = [c * v[i] - sum(L[i][j] * v[j] for j in range(n)) for i in range(n)]
        mean = sum(w) / n
        w = [x - mean for x in w]        # deflate the all-ones eigenvector
        norm = math.sqrt(sum(x * x for x in w))
        if norm > 1e-12:
            v = [x / norm for x in w]

    return v

def knn_sparsify(W: List[List[float]], k: int = 6) -> List[List[float]]:
    """Keep only each point's k strongest affinities, symmetrized (max).
    A fully-connected RBF graph quietly bridges nearby manifolds; the kNN
    graph is what lets the Laplacian see the moons as two components."""
    n = len(W)
    S = [[0.0] * n for _ in range(n)]
    for i in range(n):
        top = sorted(range(n), key=lambda j: -W[i][j])[:k]
        for j in top:
            S[i][j] = max(S[i][j], W[i][j])
            S[j][i] = max(S[j][i], W[i][j])
    return S


def spectral_cluster_two_moons(X: List[Tuple[float, float]]) -> List[int]:
    """
    Spectral clustering for 2-cluster partition.
    Uses Fiedler vector sign to assign clusters.
    """
    # Build affinity matrix, then sparsify to a kNN graph
    W = build_affinity_matrix(X, sigma=0.5)
    W = knn_sparsify(W, k=6)

    # Graph Laplacian
    L = graph_laplacian(W)

    # Power iteration to get Fiedler vector
    fiedler = power_iteration(L, num_iter=150)

    # Cluster by sign of Fiedler vector
    clusters = [1 if fiedler[i] >= 0 else 0 for i in range(len(X))]

    return clusters

def kmeans_baseline(X: List[Tuple[float, float]], k: int = 2, n_iter: int = 20) -> List[int]:
    """K-means baseline for comparison."""
    n = len(X)

    # Initialize centroids randomly
    centroids = [X[random.randint(0, n-1)] for _ in range(k)]

    for iteration in range(n_iter):
        # Assign to nearest centroid
        assignments = []
        for x in X:
            distances = [euclidean_distance(x, c) for c in centroids]
            assignments.append(distances.index(min(distances)))

        # Update centroids
        new_centroids = []
        for cluster_idx in range(k):
            members = [X[i] for i in range(n) if assignments[i] == cluster_idx]
            if members:
                cx = sum(p[0] for p in members) / len(members)
                cy = sum(p[1] for p in members) / len(members)
                new_centroids.append((cx, cy))
            else:
                new_centroids.append(centroids[cluster_idx])

        centroids = new_centroids

    return assignments

if __name__ == "__main__":
    random.seed(42)

    # Classic INTERLEAVED two moons (sklearn-style, scaled): the lower moon
    # curls back under the upper one, so any convex/centroid split fails.
    n_per_crescent = 40
    X = []
    y_true = []

    for i in range(n_per_crescent):          # upper moon
        t = math.pi * i / (n_per_crescent - 1)
        X.append((2 * math.cos(t) + random.gauss(0, 0.12),
                  2 * math.sin(t) + random.gauss(0, 0.12)))
        y_true.append(0)

    for i in range(n_per_crescent):          # lower moon, interleaved
        t = math.pi * i / (n_per_crescent - 1)
        X.append((2 - 2 * math.cos(t) + random.gauss(0, 0.12),
                  1 - 2 * math.sin(t) + random.gauss(0, 0.12)))
        y_true.append(1)

    def clustering_accuracy(pred: List[int], truth: List[int]) -> float:
        """Best accuracy over the two GLOBAL label permutations. (A per-point
        'pred==y or flipped==y' check is a tautology for binary labels —
        it scores 1.0 for any clustering whatsoever.)"""
        direct = sum(1 for p, t in zip(pred, truth) if p == t) / len(truth)
        flipped = sum(1 for p, t in zip(pred, truth) if 1 - p == t) / len(truth)
        return max(direct, flipped)

    kmeans_pred = kmeans_baseline(X, k=2, n_iter=30)
    kmeans_correct = clustering_accuracy(kmeans_pred, y_true)

    spectral_pred = spectral_cluster_two_moons(X)
    spectral_correct = clustering_accuracy(spectral_pred, y_true)

    # Spectral must genuinely recover the moons AND clearly beat k-means —
    # a tie would mean the data wasn't non-convex enough to need spectral.
    assert spectral_correct >= 0.95, \
        f"Spectral should recover interleaved moons: got {spectral_correct:.3f}"
    assert spectral_correct >= kmeans_correct + 0.05, \
        f"Spectral {spectral_correct:.3f} should clearly beat k-means {kmeans_correct:.3f}"
    print(f"spectral_clustering_lite: kmeans_acc={kmeans_correct:.4f}, spectral_acc={spectral_correct:.4f} PASS")
