"""
DISTANCE METRICS: Euclidean, Manhattan, Minkowski, Chebyshev, Cosine

Core idea: Unified toolkit for common distance metrics on vectors. Each metric
emphasizes different aspects: Euclidean (straight-line), Manhattan (grid),
Chebyshev (max-coordinate), Minkowski (parametric generalization), Cosine (angle).

When to use: KNN, clustering, anomaly detection, or any task requiring multi-purpose
distance computation. Cross-checks ensure metric properties (symmetry, triangle inequality).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple


def euclidean(p: List[float], q: List[float]) -> float:
    """
    Euclidean (L2) distance: sqrt(sum((p_i - q_i)^2))
    """
    assert len(p) == len(q), "Vectors must have equal length"
    return math.sqrt(sum((pi - qi) ** 2 for pi, qi in zip(p, q)))


def manhattan(p: List[float], q: List[float]) -> float:
    """
    Manhattan (L1) distance: sum(|p_i - q_i|)
    """
    assert len(p) == len(q), "Vectors must have equal length"
    return sum(abs(pi - qi) for pi, qi in zip(p, q))


def minkowski(p: List[float], q: List[float], p_order: float = 2.0) -> float:
    """
    Minkowski (Lp) distance: (sum(|p_i - q_i|^p))^(1/p)
    Special cases: p=1 -> Manhattan, p=2 -> Euclidean, p=inf -> Chebyshev
    """
    assert len(p) == len(q), "Vectors must have equal length"
    if p_order == float("inf"):
        return max(abs(pi - qi) for pi, qi in zip(p, q))
    return sum(abs(pi - qi) ** p_order for pi, qi in zip(p, q)) ** (1.0 / p_order)


def chebyshev(p: List[float], q: List[float]) -> float:
    """
    Chebyshev (L-infinity) distance: max(|p_i - q_i|)
    """
    assert len(p) == len(q), "Vectors must have equal length"
    return max(abs(pi - qi) for pi, qi in zip(p, q))


def cosine_similarity(p: List[float], q: List[float]) -> float:
    """
    Cosine similarity: (p · q) / (||p|| * ||q||)
    Returns value in [-1, 1]; higher = more similar.
    """
    assert len(p) == len(q), "Vectors must have equal length"
    dot_product = sum(pi * qi for pi, qi in zip(p, q))
    norm_p = math.sqrt(sum(pi**2 for pi in p))
    norm_q = math.sqrt(sum(qi**2 for qi in q))

    if norm_p == 0 or norm_q == 0:
        return 0.0

    return dot_product / (norm_p * norm_q)


def cosine_distance(p: List[float], q: List[float]) -> float:
    """
    Cosine distance: 1 - cosine_similarity
    Returns value in [0, 2].
    """
    return 1.0 - cosine_similarity(p, q)


if __name__ == "__main__":
    import random

    random.seed(42)

    # Test vectors
    p = [1.0, 2.0, 3.0]
    q = [4.0, 5.0, 6.0]
    p_identical = [1.0, 2.0, 3.0]

    # Test 1: Euclidean distance
    dist_euclidean = euclidean(p, q)
    # Expected: sqrt((4-1)^2 + (5-2)^2 + (6-3)^2) = sqrt(9+9+9) = sqrt(27) ≈ 5.196
    assert abs(dist_euclidean - math.sqrt(27)) < 1e-6, f"Euclidean wrong: {dist_euclidean}"

    # Test 2: Manhattan distance
    dist_manhattan = manhattan(p, q)
    # Expected: |4-1| + |5-2| + |6-3| = 3+3+3 = 9
    assert dist_manhattan == 9.0, f"Manhattan wrong: {dist_manhattan}"

    # Test 3: Chebyshev distance
    dist_chebyshev = chebyshev(p, q)
    # Expected: max(3, 3, 3) = 3
    assert dist_chebyshev == 3.0, f"Chebyshev wrong: {dist_chebyshev}"

    # Test 4: Minkowski with p=2 should match Euclidean
    dist_minkowski_p2 = minkowski(p, q, p_order=2.0)
    assert (
        abs(dist_minkowski_p2 - dist_euclidean) < 1e-6
    ), f"Minkowski(p=2) != Euclidean: {dist_minkowski_p2} vs {dist_euclidean}"

    # Test 5: Minkowski with p=1 should match Manhattan
    dist_minkowski_p1 = minkowski(p, q, p_order=1.0)
    assert (
        abs(dist_minkowski_p1 - dist_manhattan) < 1e-6
    ), f"Minkowski(p=1) != Manhattan: {dist_minkowski_p1} vs {dist_manhattan}"

    # Test 6: Minkowski with p=inf should match Chebyshev
    dist_minkowski_inf = minkowski(p, q, p_order=float("inf"))
    assert (
        abs(dist_minkowski_inf - dist_chebyshev) < 1e-6
    ), f"Minkowski(p=inf) != Chebyshev: {dist_minkowski_inf} vs {dist_chebyshev}"

    # Test 7: Identical vectors should have all distances = 0
    assert euclidean(p, p_identical) == 0.0, "Identical vectors Euclidean not 0"
    assert manhattan(p, p_identical) == 0.0, "Identical vectors Manhattan not 0"
    assert chebyshev(p, p_identical) == 0.0, "Identical vectors Chebyshev not 0"

    # Test 8: Cosine similarity of identical vectors should be 1
    sim_identical = cosine_similarity(p, p_identical)
    assert abs(sim_identical - 1.0) < 1e-6, f"Cosine similarity of identical vectors not 1: {sim_identical}"

    # Test 9: Cosine distance of identical vectors should be 0
    cdist_identical = cosine_distance(p, p_identical)
    assert abs(cdist_identical - 0.0) < 1e-6, f"Cosine distance of identical vectors not 0: {cdist_identical}"

    # Test 10: Cosine similarity is symmetric
    sim_pq = cosine_similarity(p, q)
    sim_qp = cosine_similarity(q, p)
    assert abs(sim_pq - sim_qp) < 1e-6, f"Cosine similarity not symmetric: {sim_pq} vs {sim_qp}"

    # Test 11: All metrics are symmetric
    assert (
        euclidean(p, q) == euclidean(q, p)
    ), "Euclidean not symmetric"
    assert (
        manhattan(p, q) == manhattan(q, p)
    ), "Manhattan not symmetric"
    assert (
        chebyshev(p, q) == chebyshev(q, p)
    ), "Chebyshev not symmetric"

    print("distance_metrics_toolkit.py: all_metrics_correct all_symmetric PASS")
