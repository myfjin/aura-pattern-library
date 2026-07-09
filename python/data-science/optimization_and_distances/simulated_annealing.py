"""
OPTIMIZATION: Simulated Annealing

Core idea: Mimic metallic annealing by accepting worse solutions with decreasing
probability as "temperature" cools. Escapes local optima by allowing uphill moves
early, becoming greedy as temperature drops.

When to use: Non-convex, multi-modal functions where gradient-based methods fail;
combinatorial optimization (TSP, scheduling) and black-box function minimization.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Tuple


def rastrigin_1d(x: float) -> float:
    """
    1D multi-modal Rastrigin function: f(x) = (x-3)^2 + 10*(1 - cos(2*pi*(x-3)))
    Global minimum at x=3, value=0. Multiple local minima due to oscillations.
    """
    return (x - 3) ** 2 + 10 * (1 - math.cos(2 * math.pi * (x - 3)))


def rastrigin_2d(x: float, y: float) -> float:
    """
    2D Rastrigin: sum of 1D Rastrigin per coordinate.
    Global minimum at (3, 3), value=0.
    """
    return rastrigin_1d(x) + rastrigin_1d(y)


def simulated_annealing(
    x_init: float,
    y_init: float,
    func,
    bounds: Tuple[float, float],
    initial_temp: float = 10.0,
    cooling_rate: float = 0.95,
    max_iters: int = 5000,
) -> Tuple[float, float, float]:
    """
    Simulated annealing minimization.
    Bounds apply to both x and y (symmetric).

    Returns (best_x, best_y, best_value).
    """
    x, y = x_init, y_init
    current_value = func(x, y)
    best_x, best_y, best_value = x, y, current_value
    temperature = initial_temp

    for iteration in range(max_iters):
        # Propose neighbor by adding Gaussian noise
        scale = 0.5 * temperature
        x_new = x + random.gauss(0, scale)
        y_new = y + random.gauss(0, scale)

        # Enforce bounds
        x_new = max(bounds[0], min(bounds[1], x_new))
        y_new = max(bounds[0], min(bounds[1], y_new))

        new_value = func(x_new, y_new)
        delta = new_value - current_value

        # Metropolis criterion: accept if better, or with probability exp(-delta/T)
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            x, y = x_new, y_new
            current_value = new_value

            if current_value < best_value:
                best_x, best_y, best_value = x, y, current_value

        # Cool temperature
        temperature *= cooling_rate

        if temperature < 1e-8:
            break

    return best_x, best_y, best_value


if __name__ == "__main__":
    random.seed(42)

    # Run simulated annealing on 2D Rastrigin
    x_init = 0.0
    y_init = 0.0
    bounds = (-5.0, 8.0)

    best_x, best_y, best_value = simulated_annealing(
        x_init,
        y_init,
        rastrigin_2d,
        bounds,
        initial_temp=20.0,
        cooling_rate=0.98,
        max_iters=5000,
    )

    # Global minimum is at (3, 3) with value 0
    # We allow some tolerance due to stochasticity
    tolerance = 2.0
    assert (
        best_value < tolerance
    ), f"SA did not find minimum: best_value={best_value}, tolerance={tolerance}"

    # Verify it found a point near the true minimum
    distance_from_optimum = math.sqrt((best_x - 3) ** 2 + (best_y - 3) ** 2)
    assert (
        distance_from_optimum < 2.0
    ), f"SA drifted far from optimum: distance={distance_from_optimum}"

    print(
        f"simulated_annealing.py: best_value={best_value:.6f} distance_from_opt={distance_from_optimum:.6f} PASS"
    )
