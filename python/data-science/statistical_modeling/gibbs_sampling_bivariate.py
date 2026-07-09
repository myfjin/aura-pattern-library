"""
Gibbs Sampling for Bivariate Normal Distribution.

Alternately samples each variable from its conditional distribution.
Recovers correlation structure from a correlated bivariate normal.
Use when joint sampling is hard but conditionals are tractable.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def gibbs_bivariate_normal(
    rho: float,
    n_iter: int,
    initial_x: float = 0.0,
    initial_y: float = 0.0,
) -> Tuple[List[float], List[float]]:
    """
    Gibbs sample from bivariate normal N([0,0], [[1, rho], [rho, 1]]).

    Conditionals:
        X | Y ~ N(rho * Y, 1 - rho^2)
        Y | X ~ N(rho * X, 1 - rho^2)

    Args:
        rho: correlation coefficient
        n_iter: number of iterations
        initial_x, initial_y: starting values

    Returns:
        (x_samples, y_samples)
    """
    x_samples = []
    y_samples = []

    x = initial_x
    y = initial_y

    sd_cond = math.sqrt(1.0 - rho ** 2)

    for _ in range(n_iter):
        # Sample X | Y
        mean_x = rho * y
        x = random.gauss(mean_x, sd_cond)

        # Sample Y | X
        mean_y = rho * x
        y = random.gauss(mean_y, sd_cond)

        x_samples.append(x)
        y_samples.append(y)

    return x_samples, y_samples


def compute_correlation(x_samples: List[float], y_samples: List[float]) -> float:
    """Compute sample correlation coefficient."""
    n = len(x_samples)
    mean_x = sum(x_samples) / n
    mean_y = sum(y_samples) / n

    cov_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_samples, y_samples)) / n
    var_x = sum((x - mean_x) ** 2 for x in x_samples) / n
    var_y = sum((y - mean_y) ** 2 for y in y_samples) / n

    if var_x * var_y == 0:
        return 0.0

    return cov_xy / math.sqrt(var_x * var_y)


if __name__ == "__main__":
    random.seed(42)

    # Test with rho = 0.7
    true_rho = 0.7
    n_burn = 500
    n_samples = 3000

    x_samples, y_samples = gibbs_bivariate_normal(true_rho, n_burn + n_samples)

    # Discard burn-in
    x_keep = x_samples[n_burn:]
    y_keep = y_samples[n_burn:]

    # Recover correlation
    recovered_rho = compute_correlation(x_keep, y_keep)

    # Should be close to true_rho
    assert abs(recovered_rho - true_rho) < 0.1, f"Recovered {recovered_rho}, expected {true_rho}"

    # Verify marginal variances are ~1
    var_x = sum((x - sum(x_keep) / len(x_keep)) ** 2 for x in x_keep) / len(x_keep)
    var_y = sum((y - sum(y_keep) / len(y_keep)) ** 2 for y in y_keep) / len(y_keep)
    assert abs(var_x - 1.0) < 0.1, f"Var_x {var_x} should be ~1"
    assert abs(var_y - 1.0) < 0.1, f"Var_y {var_y} should be ~1"

    print(f"gibbs_sampling_bivariate.py: true_rho={true_rho}, recovered_rho={recovered_rho:.3f} PASS")
