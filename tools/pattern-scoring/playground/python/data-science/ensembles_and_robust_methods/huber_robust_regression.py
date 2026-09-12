"""
Huber Loss Robust Regression.

Huber loss is a hybrid of squared loss (for small residuals) and absolute
loss (for large residuals). It reduces sensitivity to outliers compared to
OLS while staying smooth. Coefficients estimated under Huber loss are closer
to ground truth under heavy-tailed noise.

Use when: data with heavy-tailed noise, outlier robustness, smooth gradients.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple

def huber_loss(residual: float, delta: float = 1.0) -> float:
    """Huber loss: smooth transition between L2 and L1."""
    abs_res = abs(residual)
    if abs_res <= delta:
        return 0.5 * residual ** 2
    else:
        return delta * (abs_res - 0.5 * delta)

def huber_gradient(residual: float, delta: float = 1.0) -> float:
    """Gradient of Huber loss w.r.t. residual."""
    abs_res = abs(residual)
    if abs_res <= delta:
        return residual
    else:
        return delta if residual > 0 else -delta

def fit_line_huber(X: List[float], y: List[float], delta: float = 1.5,
                   learning_rate: float = 0.05, iterations: int = 300) -> Tuple[float, float]:
    """
    Fit line y = m*x + b using gradient descent on Huber loss.

    Args:
        X: x coordinates
        y: y coordinates
        delta: Huber loss threshold
        learning_rate: step size for gradient descent
        iterations: number of gradient steps

    Returns:
        (m, b) coefficients
    """
    n = len(X)
    # Initialize with OLS as starting point
    mean_x = sum(X) / n
    mean_y = sum(y) / n
    num = sum((X[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denom = sum((X[i] - mean_x) ** 2 for i in range(n))
    m = num / denom if denom > 1e-10 else 0.0
    b = mean_y - m * mean_x

    for iteration in range(iterations):
        # Compute predictions and residuals
        residuals = [y[i] - (m * X[i] + b) for i in range(n)]

        # Gradient w.r.t. m and b
        grad_m = 0.0
        grad_b = 0.0

        for i in range(n):
            h_grad = huber_gradient(residuals[i], delta)
            grad_m -= X[i] * h_grad / n
            grad_b -= h_grad / n

        # Gradient step with adaptive learning rate
        step_size = learning_rate / (1.0 + iteration / 100.0)
        m -= step_size * grad_m
        b -= step_size * grad_b

    return m, b

def ordinary_least_squares(X: List[float], y: List[float]) -> Tuple[float, float]:
    """Fit line via OLS (susceptible to outliers)."""
    n = len(X)
    mean_x = sum(X) / n
    mean_y = sum(y) / n

    numerator = sum((X[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((X[i] - mean_x) ** 2 for i in range(n))

    if denominator < 1e-10:
        return 0.0, mean_y
    else:
        m = numerator / denominator
        b = mean_y - m * mean_x
        return m, b

def squared_loss_error(y_true: List[float], y_pred: List[float]) -> float:
    """Squared loss (MSE)."""
    return sum((y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true))) / len(y_true)

if __name__ == "__main__":
    random.seed(42)

    # Generate regression data with heavy-tailed noise
    # True line: y = 2*x + 1
    n_normal = 50
    X = []
    y = []

    # Normal points with small noise
    for i in range(n_normal):
        x = random.uniform(0, 10)
        true_y = 2.0 * x + 1.0
        # Heavy-tailed noise: mix of small and extreme values
        if random.random() < 0.8:
            y_noisy = true_y + random.gauss(0, 0.5)
        else:
            # Heavy tail: outliers occur 20% of time
            y_noisy = true_y + random.choice([1, -1]) * random.uniform(5, 20)
        X.append(x)
        y.append(y_noisy)

    # Fit with OLS
    m_ols, b_ols = ordinary_least_squares(X, y)

    # Fit with Huber
    m_huber, b_huber = fit_line_huber(X, y, delta=1.0, learning_rate=0.01, iterations=200)

    # Ground truth
    true_m = 2.0
    true_b = 1.0

    # Measure error in slope recovery
    ols_error = abs(m_ols - true_m)
    huber_error = abs(m_huber - true_m)

    # Huber should recover slope closer to truth
    assert huber_error < ols_error, \
        f"Huber slope error {huber_error:.3f} should be < OLS {ols_error:.3f}"
    print(f"huber_robust_regression: ols_slope_error={ols_error:.4f}, huber_slope_error={huber_error:.4f} PASS")
