"""
Theil-Sen Median-of-Slopes Estimator.

Theil-Sen fits a line by computing slopes between all pairs of points and
taking the median slope (robust to outliers). The intercept is the median
of residuals after subtracting the slope. This non-parametric method is
more robust than OLS under outliers.

Use when: non-parametric robust regression, known outliers, distribution-free estimation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple

def theil_sen_estimator(X: List[float], y: List[float]) -> Tuple[float, float]:
    """
    Theil-Sen: compute median slope from all pairs, then median intercept.

    Args:
        X: x coordinates
        y: y coordinates

    Returns:
        (m, b) for line y = mx + b
    """
    n = len(X)

    if n < 2:
        return 0.0, 0.0 if n == 0 else y[0]

    # Compute all pairwise slopes
    slopes = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = X[j] - X[i]
            dy = y[j] - y[i]
            if abs(dx) > 1e-10:
                slope = dy / dx
                slopes.append(slope)

    if not slopes:
        # All x values are identical
        return 0.0, sum(y) / n

    # Median slope
    slopes_sorted = sorted(slopes)
    m = slopes_sorted[len(slopes_sorted) // 2]

    # Compute intercepts for each point, then take median
    intercepts = [y[i] - m * X[i] for i in range(n)]
    intercepts_sorted = sorted(intercepts)
    b = intercepts_sorted[len(intercepts_sorted) // 2]

    return m, b

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

    # Generate regression data with outliers
    # True line: y = 1.5*x + 2
    n_inliers = 50
    X = []
    y = []

    # Inliers on true line with small noise
    for i in range(n_inliers):
        x = random.uniform(0, 10)
        true_y = 1.5 * x + 2.0
        y_noisy = true_y + random.gauss(0, 0.5)
        X.append(x)
        y.append(y_noisy)

    # Add outliers (25% of data)
    n_outliers = n_inliers // 4
    for i in range(n_outliers):
        x = random.uniform(0, 10)
        y_outlier = random.uniform(-20, 40)  # Extreme outliers
        X.append(x)
        y.append(y_outlier)

    # Fit with OLS
    m_ols, b_ols = ordinary_least_squares(X, y)

    # Fit with Theil-Sen
    m_ts, b_ts = theil_sen_estimator(X, y)

    # Ground truth
    true_m = 1.5
    true_b = 2.0

    # Measure error in slope recovery
    ols_error = abs(m_ols - true_m)
    ts_error = abs(m_ts - true_m)

    # Theil-Sen should recover slope closer to truth
    assert ts_error < ols_error, \
        f"Theil-Sen slope error {ts_error:.3f} should be < OLS {ols_error:.3f}"
    print(f"theil_sen_estimator: ols_slope_error={ols_error:.4f}, ts_slope_error={ts_error:.4f} PASS")
