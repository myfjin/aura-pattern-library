"""
OPTIMIZATION: Gradient Descent with Momentum

Core idea: Vanilla gradient descent oscillates in narrow valleys; momentum accumulates
velocity across iterations, smoothing the path and converging faster. Compare vanilla GD
vs momentum GD on a 2D quadratic bowl.

When to use: Convex optimization with non-isotropic (elongated) loss landscapes; standard
in neural network training to accelerate convergence and reduce oscillation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Tuple, List


def quadratic_bowl(x: float, y: float) -> float:
    """2D quadratic bowl: f(x,y) = 100*x^2 + y^2. Global minimum at (0, 0)."""
    return 100 * x**2 + y**2


def gradient_bowl(x: float, y: float) -> Tuple[float, float]:
    """Gradient of quadratic_bowl: (df/dx, df/dy)."""
    return (200 * x, 2 * y)




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_momentum_gd(learning_rate, momentum, tolerance):
    v = []
    if isinstance(learning_rate, (int, float)) and learning_rate <= 0:
        v.append(f"AURA-E009: learning_rate must be > 0, got {learning_rate}")
    if isinstance(learning_rate, (int, float)) and learning_rate <= 0:
        v.append(f"AURA-E001: learning_rate must be > 0, got {learning_rate}")
    if isinstance(momentum, (int, float)) and momentum <= 0:
        v.append(f"AURA-E009: momentum must be > 0, got {momentum}")
    if isinstance(tolerance, (int, float)) and not math.isfinite(tolerance):
        v.append(f"AURA-E008: tolerance must be finite, got {tolerance}")
    if isinstance(tolerance, (int, float)) and tolerance <= 0:
        v.append(f"AURA-E009: tolerance must be > 0, got {tolerance}")
    if v:
        raise AuraInputError(v)

def _aura_validate_vanilla_gd(learning_rate, tolerance):
    v = []
    if isinstance(learning_rate, (int, float)) and learning_rate <= 0:
        v.append(f"AURA-E009: learning_rate must be > 0, got {learning_rate}")
    if isinstance(learning_rate, (int, float)) and learning_rate <= 0:
        v.append(f"AURA-E001: learning_rate must be > 0, got {learning_rate}")
    if isinstance(tolerance, (int, float)) and not math.isfinite(tolerance):
        v.append(f"AURA-E008: tolerance must be finite, got {tolerance}")
    if isinstance(tolerance, (int, float)) and tolerance <= 0:
        v.append(f"AURA-E009: tolerance must be > 0, got {tolerance}")
    if v:
        raise AuraInputError(v)

def vanilla_gd(
    x: float,
    y: float,
    learning_rate: float = 0.005,
    tolerance: float = 1e-6,
    max_iters: int = 10000,
) -> Tuple[int, float]:
    """
    Vanilla gradient descent.
    Returns (iterations to convergence, final function value).
    """
    _aura_validate_vanilla_gd(learning_rate, tolerance)
    for i in range(max_iters):
        fx = quadratic_bowl(x, y)
        if fx < tolerance:
            return i, fx

        gx, gy = gradient_bowl(x, y)
        x -= learning_rate * gx
        y -= learning_rate * gy

    return max_iters, quadratic_bowl(x, y)


def momentum_gd(
    x: float,
    y: float,
    learning_rate: float = 0.005,
    momentum: float = 0.9,
    tolerance: float = 1e-6,
    max_iters: int = 10000,
) -> Tuple[int, float]:
    """
    Gradient descent with momentum.
    Maintains velocity (vx, vy) accumulated from past gradients.
    Returns (iterations to convergence, final function value).
    """
    _aura_validate_momentum_gd(learning_rate, momentum, tolerance)
    vx, vy = 0.0, 0.0

    for i in range(max_iters):
        fx = quadratic_bowl(x, y)
        if fx < tolerance:
            return i, fx

        gx, gy = gradient_bowl(x, y)
        # Momentum update: v_new = momentum * v_old + lr * gradient
        vx = momentum * vx + learning_rate * gx
        vy = momentum * vy + learning_rate * gy
        x -= vx
        y -= vy

    return max_iters, quadratic_bowl(x, y)


if __name__ == "__main__":
    random.seed(42)

    # Start from same point for fair comparison
    x0, y0 = 10.0, 10.0

    iters_vanilla, fx_vanilla = vanilla_gd(x0, y0)
    iters_momentum, fx_momentum = momentum_gd(x0, y0)

    # Check convergence assertions
    assert fx_vanilla < 1e-6, f"Vanilla GD did not converge: {fx_vanilla}"
    assert fx_momentum < 1e-6, f"Momentum GD did not converge: {fx_momentum}"

    # Momentum should converge faster (fewer iterations)
    assert (
        iters_momentum < iters_vanilla
    ), f"Momentum ({iters_momentum}) not faster than vanilla ({iters_vanilla})"

    print(
        f"gradient_descent_momentum.py: vanilla_iters={iters_vanilla} momentum_iters={iters_momentum} PASS"
    )
