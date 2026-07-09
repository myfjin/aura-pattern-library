"""
Linear Discriminant Analysis (LDA) from scratch.

Two-class dimensionality reduction: find the linear projection that maximizes
between-class variance relative to within-class variance. Core idea: compute class
means, pooled within-class scatter, then solve generalized eigenvalue problem.

Use when: projecting high-dimensional data to lower dims while preserving class separability.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple

def matrix_inverse_2x2(m: List[List[float]]) -> List[List[float]]:
    """Invert a 2x2 matrix."""
    det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    if abs(det) < 1e-10:
        return [[1.0, 0.0], [0.0, 1.0]]  # Return identity if singular
    inv_det = 1.0 / det
    return [
        [inv_det * m[1][1], -inv_det * m[0][1]],
        [-inv_det * m[1][0], inv_det * m[0][0]],
    ]

def matrix_multiply_2x2(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Multiply two 2x2 matrices."""
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]

def power_iteration_2x2(m: List[List[float]], iterations: int = 100) -> Tuple[float, List[float]]:
    """Power iteration to find largest eigenvalue and eigenvector of 2x2 matrix."""
    v = [1.0, 1.0]  # Initial vector
    for _ in range(iterations):
        # Matrix-vector product
        new_v = [m[0][0] * v[0] + m[0][1] * v[1], m[1][0] * v[0] + m[1][1] * v[1]]

        # Normalize
        norm = math.sqrt(new_v[0] ** 2 + new_v[1] ** 2)
        if norm > 1e-10:
            new_v = [x / norm for x in new_v]
        else:
            break

        v = new_v

    # Compute eigenvalue: lambda = v^T A v
        eigenvalue = v[0] * (m[0][0] * v[0] + m[0][1] * v[1]) + v[1] * (m[1][0] * v[0] + m[1][1] * v[1])

    return eigenvalue, v

def lda_2d(
    points: List[Tuple[float, float]],
    labels: List[int]
) -> Tuple[List[float], float]:
    """
    Two-class LDA in 2D.

    Args:
        points: List of (x, y) coordinates
        labels: Binary class labels (0 or 1)

    Returns:
        (LDA weight vector, projection threshold)
    """
    # Separate by class
    class_0 = [p for p, l in zip(points, labels) if l == 0]
    class_1 = [p for p, l in zip(points, labels) if l == 1]

    # Compute class means
    mean_0 = (
        sum(p[0] for p in class_0) / len(class_0),
        sum(p[1] for p in class_0) / len(class_0),
    )
    mean_1 = (
        sum(p[0] for p in class_1) / len(class_1),
        sum(p[1] for p in class_1) / len(class_1),
    )

    # Compute within-class scatter matrices
    s_0 = [[0.0, 0.0], [0.0, 0.0]]
    for p in class_0:
        dx, dy = p[0] - mean_0[0], p[1] - mean_0[1]
        s_0[0][0] += dx * dx
        s_0[0][1] += dx * dy
        s_0[1][0] += dy * dx
        s_0[1][1] += dy * dy

    s_1 = [[0.0, 0.0], [0.0, 0.0]]
    for p in class_1:
        dx, dy = p[0] - mean_1[0], p[1] - mean_1[1]
        s_1[0][0] += dx * dx
        s_1[0][1] += dx * dy
        s_1[1][0] += dy * dx
        s_1[1][1] += dy * dy

    # Pooled within-class scatter
    s_w = [[s_0[i][j] + s_1[i][j] for j in range(2)] for i in range(2)]

    # Between-class scatter
    s_b = [[0.0, 0.0], [0.0, 0.0]]
    dm_0, dm_1 = mean_0[0] - mean_1[0], mean_0[1] - mean_1[1]
    s_b[0][0] = dm_0 * dm_0
    s_b[0][1] = dm_0 * dm_1
    s_b[1][0] = dm_1 * dm_0
    s_b[1][1] = dm_1 * dm_1

    # Solve S_w^{-1} S_b w = lambda w (use power iteration)
    s_w_inv = matrix_inverse_2x2(s_w)
    s_w_inv_s_b = matrix_multiply_2x2(s_w_inv, s_b)
    _, lda_weights = power_iteration_2x2(s_w_inv_s_b, iterations=50)

    # Threshold at midpoint of projected means
    proj_mean_0 = mean_0[0] * lda_weights[0] + mean_0[1] * lda_weights[1]
    proj_mean_1 = mean_1[0] * lda_weights[0] + mean_1[1] * lda_weights[1]
    threshold = (proj_mean_0 + proj_mean_1) / 2.0

    return lda_weights, threshold

if __name__ == "__main__":
    import random
    random.seed(42)

    # Plant two separable Gaussian classes
    class_0 = [(random.gauss(1.0, 0.5), random.gauss(1.0, 0.5)) for _ in range(30)]
    class_1 = [(random.gauss(4.0, 0.5), random.gauss(4.0, 0.5)) for _ in range(30)]

    points = class_0 + class_1
    labels = [0] * 30 + [1] * 30

    weights, threshold = lda_2d(points, labels)

    # Test accuracy on training set
    correct = 0
    for p, true_label in zip(points, labels):
        projection = p[0] * weights[0] + p[1] * weights[1]
        predicted_label = 1 if projection > threshold else 0
        if predicted_label == true_label:
            correct += 1

    accuracy = correct / len(points)
    assert accuracy >= 0.9, f"LDA accuracy too low: {accuracy}"
    assert weights[0] ** 2 + weights[1] ** 2 > 0, "Weights should not be zero"

    print(f"linear_discriminant_analysis.py: accuracy {accuracy:.1%} PASS")
