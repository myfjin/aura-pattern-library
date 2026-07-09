"""
OPTIMIZATION: Newton's Method for 1D Minimization

Core idea: Use second-order (curvature) information via the Hessian to take
smarter steps than gradient descent. Newton's method quadratically converges
near the optimum, often faster than first-order methods on well-conditioned problems.

When to use: 1D or small-scale smooth optimization where second derivatives are
available; faster convergence than GD on strongly convex objectives, but can diverge
if not near optimum or if Hessian is singular.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import Tuple, Callable


def quadratic_function(x: float) -> float:
    """f(x) = 3*x^2 - 12*x + 10. Minimum at x=2, f(2)=-2."""
    return 3 * x**2 - 12 * x + 10


def gradient(x: float) -> float:
    """df/dx = 6*x - 12."""
    return 6 * x - 12


def hessian(x: float) -> float:
    """d²f/dx² = 6 (constant)."""
    return 6.0


def newton_method(
    x_init: float, tolerance: float = 1e-10, max_iters: int = 100
) -> Tuple[int, float]:
    """
    Newton's method for 1D minimization.
    x_new = x_old - f'(x) / f''(x)
    Returns (iterations, final_x).
    """
    x = x_init

    for i in range(max_iters):
        grad = gradient(x)

        if abs(grad) < tolerance:
            return i, x

        hess = hessian(x)
        if abs(hess) < 1e-12:
            raise ValueError("Hessian near zero, cannot proceed")

        x_new = x - grad / hess
        x = x_new

    return max_iters, x


def gradient_descent(
    x_init: float, learning_rate: float = 0.1, tolerance: float = 1e-10, max_iters: int = 1000
) -> Tuple[int, float]:
    """
    Gradient descent for comparison.
    Returns (iterations, final_x).
    """
    x = x_init

    for i in range(max_iters):
        grad = gradient(x)

        if abs(grad) < tolerance:
            return i, x

        x -= learning_rate * grad

    return max_iters, x


if __name__ == "__main__":
    # Minimize f(x) = 3*x^2 - 12*x + 10
    # True minimum at x = 2, f(2) = -2

    x_init = 0.0

    iters_newton, x_newton = newton_method(x_init, tolerance=1e-10)
    iters_gd, x_gd = gradient_descent(x_init, learning_rate=0.1, tolerance=1e-10)

    # Verify both methods found the minimum
    assert abs(x_newton - 2.0) < 1e-8, f"Newton did not find minimum: x={x_newton}"
    assert abs(x_gd - 2.0) < 1e-6, f"GD did not converge to minimum: x={x_gd}"

    # Newton should require significantly fewer iterations
    assert (
        iters_newton < iters_gd
    ), f"Newton ({iters_newton} iters) not faster than GD ({iters_gd} iters)"

    f_newton = quadratic_function(x_newton)
    f_gd = quadratic_function(x_gd)

    assert abs(f_newton - (-2.0)) < 1e-8, f"Newton function value wrong: {f_newton}"
    assert abs(f_gd - (-2.0)) < 1e-6, f"GD function value wrong: {f_gd}"

    print(
        f"newton_method_optimization.py: newton_iters={iters_newton} gd_iters={iters_gd} PASS"
    )
