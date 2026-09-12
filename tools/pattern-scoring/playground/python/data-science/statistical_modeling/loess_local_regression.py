"""
LOESS-Lite: Locally Weighted Linear Regression.

Fits a piecewise linear regression using tricube-weighted local neighborhoods.
Simple non-parametric smoothing for noisy signals.
Use for smooth, adaptive curve fitting without assuming global model form.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple


def tricube_weight(u: float) -> float:
    """Tricube kernel: (1 - |u|^3)^3 for |u| <= 1, else 0."""
    abs_u = abs(u)
    if abs_u > 1.0:
        return 0.0
    return (1.0 - abs_u ** 3) ** 3


def loess_point(
    x_vals: List[float],
    y_vals: List[float],
    x_target: float,
    frac_nearest: float = 0.3,
) -> float:
    """
    Fit local linear regression at x_target using nearby points.

    Args:
        x_vals, y_vals: training data
        x_target: point to estimate at
        frac_nearest: fraction of points to use (k-NN style)

    Returns:
        Predicted y at x_target
    """
    n = len(x_vals)
    k = max(1, int(n * frac_nearest))

    # Find k nearest neighbors
    dists = [(abs(x - x_target), i) for i, x in enumerate(x_vals)]
    dists.sort()
    nearest_indices = [i for _, i in dists[:k]]

    # Compute max distance (bandwidth)
    max_dist = dists[k - 1][0]
    if max_dist == 0:
        max_dist = 1.0

    # Compute weights
    weights = []
    for i in nearest_indices:
        u = abs(x_vals[i] - x_target) / max_dist
        w = tricube_weight(u)
        weights.append(w)

    # Weighted linear regression on neighbors
    sum_w = sum(weights)
    if sum_w == 0:
        return sum(y_vals) / n  # Fallback

    # Compute weighted mean
    sum_wy = sum(w * y_vals[i] for w, i in zip(weights, nearest_indices))
    sum_wx = sum(w * x_vals[i] for w, i in zip(weights, nearest_indices))

    mean_y_w = sum_wy / sum_w
    mean_x_w = sum_wx / sum_w

    # Weighted slope
    sum_wxy = sum(
        w * x_vals[i] * y_vals[i]
        for w, i in zip(weights, nearest_indices)
    )
    sum_wx2 = sum(w * x_vals[i] ** 2 for w, i in zip(weights, nearest_indices))

    denom = sum_wx2 - mean_x_w * sum_wx
    if abs(denom) < 1e-10:
        return mean_y_w

    slope = (sum_wxy - mean_x_w * sum_wy) / denom
    intercept = mean_y_w - slope * mean_x_w

    return intercept + slope * x_target


def loess_smooth(
    x_vals: List[float],
    y_vals: List[float],
    x_grid: List[float],
    frac_nearest: float = 0.3,
) -> List[float]:
    """Apply LOESS to a grid of x values."""
    return [loess_point(x_vals, y_vals, x, frac_nearest) for x in x_grid]


def mean_squared_error(y_true: List[float], y_pred: List[float]) -> float:
    """Compute MSE."""
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate noisy sine wave
    n = 60
    x_vals = [i * math.pi / 15.0 for i in range(n)]
    y_vals = [math.sin(x) + random.gauss(0, 0.3) for x in x_vals]

    # LOESS fit
    x_grid = [i * math.pi / 15.0 for i in range(n)]
    y_loess = loess_smooth(x_vals, y_vals, x_grid, frac_nearest=0.3)

    # Linear fit for comparison
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_xy = sum(x * y for x, y in zip(x_vals, y_vals))
    sum_x2 = sum(x ** 2 for x in x_vals)
    n_pts = len(x_vals)

    mean_x = sum_x / n_pts
    mean_y = sum_y / n_pts

    slope_lin = (sum_xy - mean_x * sum_y) / (sum_x2 - mean_x * sum_x)
    intercept_lin = mean_y - slope_lin * mean_x

    y_linear = [intercept_lin + slope_lin * x for x in x_vals]

    # LOESS should fit better than global linear
    mse_loess = mean_squared_error(y_vals, y_loess)
    mse_linear = mean_squared_error(y_vals, y_linear)

    assert mse_loess < mse_linear, f"LOESS MSE {mse_loess} should beat linear {mse_linear}"

    print(f"loess_local_regression.py: mse_loess={mse_loess:.4f}, mse_linear={mse_linear:.4f} PASS")
