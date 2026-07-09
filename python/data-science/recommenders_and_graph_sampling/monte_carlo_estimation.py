"""Monte Carlo estimation: pi and definite integrals.

Core idea: estimate quantities via random sampling. For pi: sample points in
a unit square, count those inside the inscribed circle. For integrals: sample
from the domain and average the function values, scaled by volume.

When to use: for estimating integrals or geometric quantities where direct
computation is hard; error shrinks as O(1/sqrt(n)).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Callable, Tuple


def estimate_pi(num_samples: int) -> float:
    """Estimate pi by sampling points in [0,1]^2 and checking distance to origin."""
    count_inside = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            count_inside += 1
    # Area of quarter circle = pi/4, area of square = 1
    # pi/4 ≈ count_inside / num_samples
    return 4 * count_inside / num_samples


def estimate_integral(
    func: Callable[[float], float],
    a: float,
    b: float,
    num_samples: int,
) -> float:
    """
    Estimate integral of func from a to b via Monte Carlo.
    Sample uniformly from [a,b], average function values, multiply by interval width.
    """
    total = sum(func(random.uniform(a, b)) for _ in range(num_samples))
    return (b - a) * total / num_samples


if __name__ == "__main__":
    random.seed(42)

    # Test 1: Estimate pi
    pi_estimate_1000 = estimate_pi(1000)
    pi_estimate_10000 = estimate_pi(10000)

    # Error should shrink with more samples
    error_1000 = abs(pi_estimate_1000 - math.pi)
    error_10000 = abs(pi_estimate_10000 - math.pi)

    assert error_10000 < error_1000, \
        f"Error should decrease: 1000 samples error {error_1000:.4f}, 10000 error {error_10000:.4f}"

    # Test 2: Estimate integral of x^2 from 0 to 1 (true value = 1/3 ≈ 0.333)
    def quadratic(x: float) -> float:
        return x**2

    integral_1000 = estimate_integral(quadratic, 0, 1, 1000)
    integral_10000 = estimate_integral(quadratic, 0, 1, 10000)

    error_int_1000 = abs(integral_1000 - 1.0 / 3)
    error_int_10000 = abs(integral_10000 - 1.0 / 3)

    assert error_int_10000 < error_int_1000, \
        f"Integral error should decrease: 1000 {error_int_1000:.4f}, 10000 {error_int_10000:.4f}"

    # Both estimates should be reasonably close to true values
    assert abs(pi_estimate_10000 - math.pi) < 0.1, \
        f"Pi estimate {pi_estimate_10000} too far from {math.pi}"
    assert abs(integral_10000 - 1.0 / 3) < 0.05, \
        f"Integral estimate {integral_10000} too far from {1.0 / 3}"

    print(f"monte_carlo_estimation.py: pi_est={pi_estimate_10000:.4f}, int_est={integral_10000:.4f} PASS")
