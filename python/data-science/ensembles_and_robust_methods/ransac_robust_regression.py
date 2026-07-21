"""
RANSAC (Random Sample Consensus) for Robust Regression.

RANSAC iteratively selects random minimal subsets of data, fits models,
and counts inliers (points close to the model). The model with the most
inliers is returned, robustly ignoring gross outliers.

Use when: data with severe outliers, unknown noise distribution, automatic outlier detection.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple

def fit_line_2point(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
    """Fit line through two points: y = mx + b."""
    x1, y1 = p1
    x2, y2 = p2

    if abs(x2 - x1) < 1e-10:
        # Vertical line; use large slope
        return 1e6, y1
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return m, b

def predict_line(x: float, m: float, b: float) -> float:
    """Predict with linear model."""
    return m * x + b

def residual_distance(y_true: float, y_pred: float) -> float:
    """Residual distance (absolute error)."""
    return abs(y_true - y_pred)



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_ransac_regression(n_iterations, threshold):
    v = []
    if isinstance(n_iterations, (int, float)) and n_iterations <= 0:
        v.append(f"AURA-E009: n_iterations must be > 0, got {n_iterations}")
    if isinstance(threshold, (int, float)) and not math.isfinite(threshold):
        v.append(f"AURA-E008: threshold must be finite, got {threshold}")
    if v:
        raise AuraInputError(v)

def ransac_regression(X: List[float], y: List[float], n_iterations: int = 100,
                      threshold: float = 1.0) -> Tuple[float, float]:
    """
    RANSAC: fit line by selecting random 2-point samples and counting inliers.

    Args:
        X: x coordinates
        y: y coordinates
        n_iterations: number of random samples to try
        threshold: distance threshold for inliers

    Returns:
        (m, b) for best fit y = mx + b
    """
    _aura_validate_ransac_regression(n_iterations, threshold)
    n = len(X)
    best_m = 0.0
    best_b = 0.0
    best_inlier_count = 0

    for iteration in range(n_iterations):
        # Random sample 2 points
        if n < 2:
            break

        idx1, idx2 = random.sample(range(n), 2)
        p1 = (X[idx1], y[idx1])
        p2 = (X[idx2], y[idx2])

        # Fit line
        m, b = fit_line_2point(p1, p2)

        # Count inliers
        inlier_count = 0
        for i in range(n):
            y_pred = predict_line(X[i], m, b)
            dist = residual_distance(y[i], y_pred)
            if dist <= threshold:
                inlier_count += 1

        # Update best model
        if inlier_count > best_inlier_count:
            best_inlier_count = inlier_count
            best_m = m
            best_b = b

    return best_m, best_b

def ordinary_least_squares(X: List[float], y: List[float]) -> Tuple[float, float]:
    """Fit line via OLS (susceptible to outliers)."""
    n = len(X)
    mean_x = sum(X) / n
    mean_y = sum(y) / n

    numerator = sum((X[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((X[i] - mean_x) ** 2 for i in range(n))

    if denominator < 1e-10:
        return 0.0, mean_y
    else:
        m = numerator / denominator
        b = mean_y - m * mean_x
        return m, b

if __name__ == "__main__":
    random.seed(42)

    # Generate regression data: true line y = 2*x + 1
    n_inliers = 50
    X = []
    y = []

    # Generate inliers on true line with small noise
    for i in range(n_inliers):
        x = random.uniform(0, 10)
        true_y = 2.0 * x + 1.0
        y_noisy = true_y + random.gauss(0, 0.5)
        X.append(x)
        y.append(y_noisy)

    # Add outliers (30% of data)
    n_outliers = int(0.3 * n_inliers)
    for i in range(n_outliers):
        x = random.uniform(0, 10)
        y_outlier = random.uniform(-10, 30)  # Gross outlier
        X.append(x)
        y.append(y_outlier)

    # Fit with OLS (will be pulled by outliers)
    m_ols, b_ols = ordinary_least_squares(X, y)

    # Fit with RANSAC
    m_ransac, b_ransac = ransac_regression(X, y, n_iterations=200, threshold=1.0)

    # Ground truth: m=2, b=1
    true_m = 2.0
    true_b = 1.0

    # Measure error in slope recovery
    ols_error = abs(m_ols - true_m)
    ransac_error = abs(m_ransac - true_m)

    # RANSAC should recover slope closer to truth despite outliers
    assert ransac_error < ols_error, \
        f"RANSAC slope error {ransac_error:.3f} should be < OLS {ols_error:.3f}"
    print(f"ransac_robust_regression: ols_slope_error={ols_error:.4f}, ransac_slope_error={ransac_error:.4f} PASS")
