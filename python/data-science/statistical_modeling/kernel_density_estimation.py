"""
Kernel Density Estimation (KDE) with Gaussian Kernel & Silverman Bandwidth.

Non-parametric density estimation via kernel smoothing.
Bandwidth chosen by Silverman's rule: h = (4/(3*n))^(1/5) * sigma.
Use for smooth density estimates from raw samples.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List


def silverman_bandwidth(samples: List[float]) -> float:
    """Compute Silverman bandwidth for Gaussian KDE."""
    n = len(samples)
    if n < 2:
        return 1.0

    # Compute sample SD
    mean = sum(samples) / n
    var = sum((x - mean) ** 2 for x in samples) / n
    sigma = math.sqrt(var)

    # Silverman: h = (4 / (3*n))^(1/5) * sigma
    h = (4.0 / (3.0 * n)) ** (1.0 / 5.0) * sigma
    return h




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_gaussian_kernel_density(x, h):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if isinstance(h, (int, float)) and not math.isfinite(h):
        v.append(f"AURA-E008: h must be finite, got {h}")
    if v:
        raise AuraInputError(v)

def gaussian_kernel_density(samples: List[float], x: float, h: float) -> float:
    """Evaluate KDE at x using Gaussian kernel with bandwidth h."""
    _aura_validate_gaussian_kernel_density(x, h)
    n = len(samples)
    if n == 0:
        return 0.0

    # f(x) = (1 / (n * h)) * sum_i K((x - X_i) / h)
    # where K(u) = (1/sqrt(2*pi)) * exp(-u^2 / 2)
    density = 0.0
    normalizer = 1.0 / math.sqrt(2.0 * math.pi)

    for xi in samples:
        u = (x - xi) / h
        kernel_val = normalizer * math.exp(-0.5 * u ** 2)
        density += kernel_val

    return density / (n * h)


def numeric_integral_kde(samples: List[float], x_min: float, x_max: float, n_grid: int) -> float:
    """Numerically integrate KDE over [x_min, x_max]."""
    h = silverman_bandwidth(samples)
    dx = (x_max - x_min) / n_grid
    total = 0.0

    for i in range(n_grid):
        x = x_min + (i + 0.5) * dx
        total += gaussian_kernel_density(samples, x, h) * dx

    return total


if __name__ == "__main__":
    import random
    random.seed(42)

    # Sample from mixture of two Gaussians: 0.5*N(-2, 0.5) + 0.5*N(2, 0.5)
    n1 = 40
    n2 = 40
    samples = ([random.gauss(-2, 0.5) for _ in range(n1)] +
               [random.gauss(2, 0.5) for _ in range(n2)])

    h = silverman_bandwidth(samples)

    # Check that KDE integrates to ~1 over a wide range
    integral = numeric_integral_kde(samples, -5, 5, 500)
    assert abs(integral - 1.0) < 0.05, f"Integral {integral} not close to 1"

    # Check that density peaks near the planted modes
    density_at_minus2 = gaussian_kernel_density(samples, -2.0, h)
    density_at_0 = gaussian_kernel_density(samples, 0.0, h)
    density_at_2 = gaussian_kernel_density(samples, 2.0, h)

    assert density_at_minus2 > density_at_0, "KDE should be higher near mode -2 than at center"
    assert density_at_2 > density_at_0, "KDE should be higher near mode 2 than at center"

    print(f"kernel_density_estimation.py: integral={integral:.4f}, density_at_-2={density_at_minus2:.4f}, density_at_2={density_at_2:.4f} PASS")
