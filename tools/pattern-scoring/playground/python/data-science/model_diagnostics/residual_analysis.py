"""
Residual Analysis

Fits a linear model to data with a planted quadratic term.
Inspects residuals for structure (correlation with x^2 or runs test).

Use this to detect model misspecification: if residuals correlate with the omitted feature,
you've found a missing term in your specification.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def generate_quadratic_data(n: int, seed: int) -> List[Tuple[float, float]]:
    """Generate y = 1 + 0.5*x + 0.3*x^2 + noise."""
    random.seed(seed)
    data = []
    for _ in range(n):
        x = random.uniform(-4, 4)
        y = 1.0 + 0.5 * x + 0.3 * x * x + random.gauss(0, 0.3)
        data.append((x, y))
    return data


def fit_linear_model(x_list: List[float], y_list: List[float]) -> Tuple[float, float]:
    """Fit linear model y = a + b*x."""
    n = len(x_list)
    x_mean = sum(x_list) / n
    y_mean = sum(y_list) / n

    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_list, y_list))
    den = sum((x - x_mean) ** 2 for x in x_list)

    if den == 0:
        return y_mean, 0.0

    b = num / den
    a = y_mean - b * x_mean
    return a, b


def fit_quadratic_model(
    x_list: List[float], y_list: List[float]
) -> Tuple[float, float, float]:
    """Fit quadratic model y = a + b*x + c*x^2."""
    n = len(x_list)

    sx0 = n
    sx1 = sum(x_list)
    sx2 = sum(x * x for x in x_list)
    sx3 = sum(x * x * x for x in x_list)
    sx4 = sum(x * x * x * x for x in x_list)
    sy = sum(y_list)
    sxy = sum(x * y for x, y in zip(x_list, y_list))
    sx2y = sum(x * x * y for x, y in zip(x_list, y_list))

    # Solve 3x3 normal equations
    det = (sx0 * (sx2 * sx4 - sx3 * sx3) -
           sx1 * (sx1 * sx4 - sx3 * sx2) +
           sx2 * (sx1 * sx3 - sx2 * sx2))

    if abs(det) < 1e-10:
        return 0, 0, 0

    a = (sy * (sx2 * sx4 - sx3 * sx3) -
         sxy * (sx1 * sx4 - sx3 * sx2) +
         sx2y * (sx1 * sx3 - sx2 * sx2)) / det

    b = (sx0 * (sxy * sx4 - sx3 * sx2y) -
         sy * (sx1 * sx4 - sx3 * sx2) +
         sx2y * (sx1 * sx3 - sx2 * sx2)) / det

    c = (sx0 * (sx2 * sx2y - sx3 * sxy) -
         sx1 * (sx1 * sx2y - sx3 * sy) +
         sy * (sx1 * sx3 - sx2 * sx2)) / det

    return a, b, c


def compute_residuals(
    x_list: List[float], y_list: List[float], a: float, b: float
) -> List[float]:
    """Compute residuals for linear model."""
    return [y - (a + b * x) for x, y in zip(x_list, y_list)]


def pearson_correlation(u: List[float], v: List[float]) -> float:
    """Compute Pearson correlation coefficient."""
    assert len(u) == len(v)
    n = len(u)

    u_mean = sum(u) / n
    v_mean = sum(v) / n

    num = sum((ui - u_mean) * (vi - v_mean) for ui, vi in zip(u, v))
    u_var = sum((ui - u_mean) ** 2 for ui in u)
    v_var = sum((vi - v_mean) ** 2 for vi in v)

    if u_var == 0 or v_var == 0:
        return 0.0

    return num / math.sqrt(u_var * v_var)


def residual_analysis_test() -> None:
    """
    Fit linear model to quadratic data, check that residuals correlate with x^2.
    Then fit quadratic model and verify residuals no longer show structure.
    """
    random.seed(42)
    data = generate_quadratic_data(100, seed=42)
    x_list = [x for x, y in data]
    y_list = [y for x, y in data]

    # Fit linear model (misspecified)
    a_lin, b_lin = fit_linear_model(x_list, y_list)
    residuals_lin = compute_residuals(x_list, y_list, a_lin, b_lin)

    # Compute x^2 for each point
    x_squared = [x * x for x in x_list]

    # Check correlation between residuals and x^2
    # If significant, the quadratic term was omitted
    corr_lin = pearson_correlation(residuals_lin, x_squared)
    assert abs(corr_lin) > 0.5, f"Linear residuals should correlate with x^2: {corr_lin}"

    # Fit quadratic model (correctly specified)
    a_quad, b_quad, c_quad = fit_quadratic_model(x_list, y_list)
    residuals_quad = [y - (a_quad + b_quad * x + c_quad * x * x) for x, y in zip(x_list, y_list)]

    # Check correlation between quadratic residuals and x^2
    # Should be much lower (just noise)
    corr_quad = pearson_correlation(residuals_quad, x_squared)
    assert (
        abs(corr_quad) < abs(corr_lin) * 0.3
    ), f"Quadratic residuals should not correlate with x^2: {corr_quad} vs {corr_lin}"

    print("residual_analysis.py: PASS")


if __name__ == "__main__":
    residual_analysis_test()
