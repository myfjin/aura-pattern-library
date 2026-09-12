"""
OPTIMIZATION: Hill Climbing with Random Restarts

Core idea: Pure hill climbing gets stuck in local optima on rugged landscapes.
Random restarts re-initialize from different points and return the best result
found across all restarts, allowing escape from local optima.

When to use: Local search on landscapes with many local optima; simple, fast,
and effective when computational budget allows multiple independent runs.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import Tuple


def rugged_landscape(x: float, y: float) -> float:
    """
    Rugged landscape with multiple local optima.
    f(x,y) = sin(5*pi*x) * cos(5*pi*y) + 0.1*(x^2 + y^2)
    Multiple local peaks due to sine/cosine, slight quadratic bowl for tiebreaker.
    """
    return math.sin(5 * math.pi * x) * math.cos(5 * math.pi * y) + 0.1 * (
        x**2 + y**2
    )


def hill_climbing(
    x: float,
    y: float,
    step_size: float = 0.05,
    tolerance: float = 1e-4,
    max_iters: int = 1000,
) -> Tuple[float, float, float]:
    """
    Single run of hill climbing: greedily move uphill.
    Returns (best_x, best_y, best_value).
    """
    best_x, best_y = x, y
    best_value = rugged_landscape(x, y)

    for _ in range(max_iters):
        # Try four directions: +x, -x, +y, -y
        candidates = [
            (best_x + step_size, best_y),
            (best_x - step_size, best_y),
            (best_x, best_y + step_size),
            (best_x, best_y - step_size),
        ]

        improved = False
        for cx, cy in candidates:
            # Enforce bounds
            cx = max(-1.0, min(1.0, cx))
            cy = max(-1.0, min(1.0, cy))

            cv = rugged_landscape(cx, cy)
            if cv > best_value + tolerance:  # Maximizing
                best_x, best_y, best_value = cx, cy, cv
                improved = True
                break

        if not improved:
            # Local optimum reached
            break

    return best_x, best_y, best_value


def hill_climbing_with_restarts(
    num_restarts: int = 10,
    step_size: float = 0.05,
    bounds: Tuple[float, float] = (-1.0, 1.0),
) -> Tuple[float, float, float]:
    """
    Hill climbing with multiple random restarts.
    Returns (best_x, best_y, best_value) across all restarts.
    """
    global_best_x, global_best_y, global_best_value = None, None, -float("inf")

    for _ in range(num_restarts):
        x_init = random.uniform(bounds[0], bounds[1])
        y_init = random.uniform(bounds[0], bounds[1])

        x, y, value = hill_climbing(x_init, y_init, step_size=step_size)

        if value > global_best_value:
            global_best_x, global_best_y, global_best_value = x, y, value

    return global_best_x, global_best_y, global_best_value


if __name__ == "__main__":
    random.seed(42)

    # Test single hill climbing: should get stuck in a local optimum
    x_single, y_single, value_single = hill_climbing(0.2, 0.3, step_size=0.05)

    # Test hill climbing with restarts: should find a better (or equal) optimum
    x_restart, y_restart, value_restart = hill_climbing_with_restarts(
        num_restarts=20, step_size=0.05
    )

    # Restarts should find a solution at least as good as single run
    assert (
        value_restart >= value_single - 1e-4
    ), f"Restarts worse than single run: {value_restart} < {value_single}"

    # With multiple restarts on a rugged landscape, should find reasonably good peak
    # The true global max is around sin(5*pi*x)*cos(5*pi*y) ≈ 1, when both factors near ±1
    # We expect to find something in the range [0.5, 1.0] or so
    assert (
        value_restart > -0.5
    ), f"Restarts found very poor solution: {value_restart}"

    print(
        f"hill_climbing_restarts.py: single={value_single:.4f} restarts={value_restart:.4f} PASS"
    )
