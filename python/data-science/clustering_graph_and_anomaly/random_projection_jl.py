"""
Random Projection: Johnson-Lindenstrauss Lemma from scratch.

Dimensionality reduction via random projection: project high-dimensional points onto
a random subspace. Johnson-Lindenstrauss guarantees: pairwise distances are approximately
preserved (within factor 1±epsilon) with high probability. Core idea: random gaussian
matrix of size target_dim × original_dim.

Use when: fast approximate dimensionality reduction without computing data-dependent structure.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_random_projection_matrix(original_dim):
    v = []
    if isinstance(original_dim, (int, float)) and original_dim <= 0:
        v.append(f"AURA-E009: original_dim must be > 0, got {original_dim}")
    if v:
        raise AuraInputError(v)

def random_projection_matrix(
    original_dim: int,
    target_dim: int,
    seed: int = 42
) -> List[List[float]]:
    """
    Generate random projection matrix (Gaussian).

    Args:
        original_dim: Original dimension
        target_dim: Target dimension (< original_dim)
        seed: Random seed

    Returns:
        Matrix of shape (target_dim, original_dim)
    """
    _aura_validate_random_projection_matrix(original_dim)
    random.seed(seed)
    # Generate gaussian random matrix
    matrix = []
    for i in range(target_dim):
        row = [random.gauss(0.0, 1.0) for _ in range(original_dim)]
        matrix.append(row)

    # Normalize rows
    for i in range(target_dim):
        norm = math.sqrt(sum(x ** 2 for x in matrix[i]))
        if norm > 1e-10:
            matrix[i] = [x / norm for x in matrix[i]]

    return matrix

def project_point(point: Tuple[float, ...], projection_matrix: List[List[float]]) -> Tuple[float, ...]:
    """Project a single point using projection matrix."""
    target_dim = len(projection_matrix)
    projected = []
    for i in range(target_dim):
        proj_val = sum(projection_matrix[i][j] * point[j] for j in range(len(point)))
        projected.append(proj_val)
    return tuple(projected)

def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
    """Compute Euclidean distance."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

if __name__ == "__main__":
    random.seed(42)

    # Generate CLUSTERED high-dimensional points. (iid gaussian points would make
    # all pairwise distances concentrate around the same value — concentration of
    # measure — leaving no distance structure to preserve, and the correlation
    # check would measure noise. Planted clusters give real structure.)
    original_dim = 50
    target_dim = 20
    num_points = 42

    centers = [tuple(random.gauss(0.0, 6.0) for _ in range(original_dim)) for _ in range(3)]
    points = [tuple(c + random.gauss(0.0, 1.0) for c in centers[k % 3])
              for k in range(num_points)]

    # Compute all pairwise distances in original space
    original_distances = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            dist = euclidean_distance(points[i], points[j])
            original_distances.append((i, j, dist))

    # Project to lower dimension
    projection_matrix = random_projection_matrix(original_dim, target_dim, seed=42)
    projected_points = [project_point(p, projection_matrix) for p in points]

    # Compute pairwise distances in projected space
    projected_distances = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            dist = euclidean_distance(projected_points[i], projected_points[j])
            projected_distances.append((i, j, dist))

    # Verify distances are approximately preserved (rank correlation)
    original_dists = [d[2] for d in original_distances]
    projected_dists = [d[2] for d in projected_distances]

    # Check if distances are correlated (Spearman-style): correlation coefficient
    mean_original = sum(original_dists) / len(original_dists)
    mean_projected = sum(projected_dists) / len(projected_dists)

    cov = sum((original_dists[i] - mean_original) * (projected_dists[i] - mean_projected) for i in range(len(original_dists)))
    var_original = sum((d - mean_original) ** 2 for d in original_dists)
    var_projected = sum((d - mean_projected) ** 2 for d in projected_dists)

    if var_original > 0 and var_projected > 0:
        correlation = cov / math.sqrt(var_original * var_projected)
    else:
        correlation = 0.0

    # JL with adequate target dims must preserve real distance structure STRONGLY
    assert correlation > 0.9, f"Distance correlation too low: {correlation}"
    assert correlation < 1.1, "Distance correlation should be <= 1"

    print(f"random_projection_jl.py: distance correlation {correlation:.3f} PASS")
