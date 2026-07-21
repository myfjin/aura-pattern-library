"""
Quantile Regression via Pinball Loss and Gradient Descent.

Estimates conditional quantiles (e.g., median, 90th percentile) by minimizing
the pinball (check) loss: L_tau(y, pred) = (tau - 1)*min(y-pred,0) + tau*max(y-pred,0).
Use when you need robust estimates of specific quantiles instead of the mean.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


def pinball_loss(y: float, pred: float, tau: float) -> float:
    """Pinball loss for quantile tau."""
    residual = y - pred
    if residual >= 0:
        return tau * residual
    else:
        return (tau - 1) * residual




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_count_below_line(a, b):
    v = []
    if isinstance(a, (int, float)) and not math.isfinite(a):
        v.append(f"AURA-E008: a must be finite, got {a}")
    if isinstance(b, (int, float)) and not math.isfinite(b):
        v.append(f"AURA-E008: b must be finite, got {b}")
    if v:
        raise AuraInputError(v)

def _aura_validate_pinball_loss_gradient(y, pred):
    v = []
    if isinstance(y, (int, float)) and not math.isfinite(y):
        v.append(f"AURA-E008: y must be finite, got {y}")
    if isinstance(pred, (int, float)) and not math.isfinite(pred):
        v.append(f"AURA-E008: pred must be finite, got {pred}")
    if v:
        raise AuraInputError(v)

def _aura_validate_quantile_regression_linear(learning_rate, n_iter):
    v = []
    if isinstance(learning_rate, (int, float)) and learning_rate <= 0:
        v.append(f"AURA-E009: learning_rate must be > 0, got {learning_rate}")
    if isinstance(learning_rate, (int, float)) and learning_rate <= 0:
        v.append(f"AURA-E001: learning_rate must be > 0, got {learning_rate}")
    if isinstance(n_iter, (int, float)) and n_iter <= 0:
        v.append(f"AURA-E009: n_iter must be > 0, got {n_iter}")
    if v:
        raise AuraInputError(v)

def pinball_loss_gradient(y: float, pred: float, tau: float) -> float:
    """Gradient of pinball loss w.r.t. pred."""
    _aura_validate_pinball_loss_gradient(y, pred)
    residual = y - pred
    if residual >= 0:
        return -tau
    else:
        return -(tau - 1)


def quantile_regression_linear(
    x_vals: List[float],
    y_vals: List[float],
    tau: float,
    learning_rate: float = 0.01,
    n_iter: int = 1000,
) -> Tuple[float, float]:
    """
    Fit linear quantile regression: pred = a + b*x.

    Args:
        x_vals, y_vals: training data
        tau: quantile level (0 < tau < 1)
        learning_rate: step size
        n_iter: gradient descent iterations

    Returns:
        (intercept, slope)
    """
    _aura_validate_quantile_regression_linear(learning_rate, n_iter)
    n = len(x_vals)
    a, b = 0.0, 0.0  # intercept, slope

    for _ in range(n_iter):
        # Gradient w.r.t. a and b
        grad_a = 0.0
        grad_b = 0.0

        for xi, yi in zip(x_vals, y_vals):
            pred = a + b * xi
            grad = pinball_loss_gradient(yi, pred, tau)
            grad_a += grad
            grad_b += grad * xi

        # Update
        a -= learning_rate * grad_a / n
        b -= learning_rate * grad_b / n

    return a, b


def count_below_line(x_vals: List[float], y_vals: List[float], a: float, b: float) -> float:
    """Fraction of points below the fitted line."""
    _aura_validate_count_below_line(a, b)
    count = sum(1 for xi, yi in zip(x_vals, y_vals) if yi <= a + b * xi)
    return count / len(y_vals)


if __name__ == "__main__":
    random.seed(42)

    # Generate noisy data around y = 1 + 0.5*x
    n = 50
    x_vals = [i * 0.2 for i in range(n)]
    y_vals = [1.0 + 0.5 * x + random.gauss(0, 0.5) for x in x_vals]

    # Fit median (tau=0.5)
    a_median, b_median = quantile_regression_linear(x_vals, y_vals, tau=0.5, learning_rate=0.05, n_iter=5000)

    # Fit 90th percentile
    a_90, b_90 = quantile_regression_linear(x_vals, y_vals, tau=0.9, learning_rate=0.05, n_iter=5000)

    # For median: ~50% of points should be below the line
    frac_below_median = count_below_line(x_vals, y_vals, a_median, b_median)
    assert 0.35 < frac_below_median < 0.65, f"Median: {frac_below_median} should be ~0.5"

    # For 90th percentile: ~90% of points should be below the line
    frac_below_90 = count_below_line(x_vals, y_vals, a_90, b_90)
    assert 0.75 < frac_below_90 < 0.99, f"90th: {frac_below_90} should be ~0.9"

    # 90th line should be above median line (for most x)
    assert a_90 + b_90 * 0.5 > a_median + b_median * 0.5, "90th line should be above median"

    print(f"quantile_regression_pinball.py: frac_below_median={frac_below_median:.3f}, frac_below_90={frac_below_90:.3f} PASS")
