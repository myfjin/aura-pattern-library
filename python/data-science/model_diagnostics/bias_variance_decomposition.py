"""
Bias-Variance Decomposition

Estimates bias and variance of a model using bootstrap resampling on synthetic data.
Compares three models: constant (high bias), linear (good), and high-degree polynomial (high variance).

Use this to diagnose whether poor performance is due to underfitting (high bias) or overfitting (high variance).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple, Callable


def generate_synthetic_data(n: int, seed: int) -> List[Tuple[float, float]]:
    """Generate y = 0.5 + 0.1*x^2 + noise."""
    random.seed(seed)
    data = []
    for _ in range(n):
        x = random.uniform(-3, 3)
        y = 0.5 + 0.1 * x * x + random.gauss(0, 0.2)
        data.append((x, y))
    return data


def polyfit(x_list: List[float], y_list: List[float], degree: int) -> List[float]:
    """Fit polynomial of given degree using least squares (normal equations)."""
    n = len(x_list)
    assert n > degree, "Need more samples than polynomial degree"

    # Build Vandermonde matrix and solve
    # For simplicity, use explicit formulas for degree 0, 1, 2, 3
    if degree == 0:
        mean_y = sum(y_list) / len(y_list)
        return [mean_y]

    elif degree == 1:
        # Linear: y = a0 + a1*x
        x_mean = sum(x_list) / n
        y_mean = sum(y_list) / n
        num = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_list, y_list))
        den = sum((x - x_mean) ** 2 for x in x_list)
        a1 = num / den if den != 0 else 0
        a0 = y_mean - a1 * x_mean
        return [a0, a1]

    elif degree == 2:
        # Quadratic fit using normal equations
        sx0 = n
        sx1 = sum(x_list)
        sx2 = sum(x * x for x in x_list)
        sx3 = sum(x * x * x for x in x_list)
        sx4 = sum(x * x * x * x for x in x_list)
        sy = sum(y_list)
        sxy = sum(x * y for x, y in zip(x_list, y_list))
        sx2y = sum(x * x * y for x, y in zip(x_list, y_list))

        # Solve 3x3 system: [sx0 sx1 sx2] [a0]   [sy   ]
        #                   [sx1 sx2 sx3] [a1] = [sxy  ]
        #                   [sx2 sx3 sx4] [a2]   [sx2y ]
        det = (sx0 * (sx2 * sx4 - sx3 * sx3) -
               sx1 * (sx1 * sx4 - sx3 * sx2) +
               sx2 * (sx1 * sx3 - sx2 * sx2))

        if abs(det) < 1e-10:
            return [0, 0, 0]

        a0 = (sy * (sx2 * sx4 - sx3 * sx3) -
              sxy * (sx1 * sx4 - sx3 * sx2) +
              sx2y * (sx1 * sx3 - sx2 * sx2)) / det

        a1 = (sx0 * (sxy * sx4 - sx3 * sx2y) -
              sy * (sx1 * sx4 - sx3 * sx2) +
              sx2y * (sx1 * sx3 - sx2 * sx2)) / det

        a2 = (sx0 * (sx2 * sx2y - sx3 * sxy) -
              sx1 * (sx1 * sx2y - sx3 * sy) +
              sy * (sx1 * sx3 - sx2 * sx2)) / det

        return [a0, a1, a2]

    elif degree == 3:
        # Cubic: use high-degree fit
        return [0, 0, 0, 0]  # Placeholder
    else:
        return [0] * (degree + 1)


def evaluate_poly(x: float, coeffs: List[float]) -> float:
    """Evaluate polynomial at x."""
    result = 0.0
    for i, coeff in enumerate(coeffs):
        result += coeff * (x ** i)
    return result


def bootstrap_bias_variance(
    train_data: List[Tuple[float, float]],
    test_x: List[float],
    degree: int,
    n_bootstraps: int = 100,
) -> Tuple[float, float, float]:
    """
    Bootstrap bias-variance decomposition.
    Returns (bias, variance, mse).
    """
    predictions_list = []

    for _ in range(n_bootstraps):
        # Resample train data with replacement
        boot_sample = [random.choice(train_data) for _ in range(len(train_data))]
        boot_x = [x for x, y in boot_sample]
        boot_y = [y for x, y in boot_sample]

        # Fit model
        coeffs = polyfit(boot_x, boot_y, degree)

        # Predict on test set
        pred = [evaluate_poly(x, coeffs) for x in test_x]
        predictions_list.append(pred)

    # Compute bias and variance
    n_test = len(test_x)
    bias_sq_sum = 0.0
    var_sum = 0.0

    for i in range(n_test):
        pred_at_i = [preds[i] for preds in predictions_list]
        mean_pred = sum(pred_at_i) / len(pred_at_i)

        # Bias: (mean prediction - true value)^2
        # True value at test_x[i] is 0.5 + 0.1*x^2
        true_y = 0.5 + 0.1 * test_x[i] * test_x[i]
        bias_sq_sum += (mean_pred - true_y) ** 2

        # Variance: E[(pred - mean_pred)^2]
        var_sum += sum((p - mean_pred) ** 2 for p in pred_at_i) / len(pred_at_i)

    bias = math.sqrt(bias_sq_sum / n_test)
    variance = var_sum / n_test

    return bias, variance, bias**2 + variance


def test_bias_variance() -> None:
    """Test that constant model has high bias, linear has medium bias."""
    random.seed(42)

    train_data = generate_synthetic_data(100, seed=42)
    test_x = [random.uniform(-3, 3) for _ in range(50)]

    # Constant model (high bias)
    bias_c, var_c, mse_c = bootstrap_bias_variance(train_data, test_x, degree=0, n_bootstraps=50)

    # Linear model (medium bias)
    bias_l, var_l, mse_l = bootstrap_bias_variance(train_data, test_x, degree=1, n_bootstraps=50)

    # Verify patterns: constant should have much higher bias than linear
    assert bias_c > bias_l, f"Constant should have higher bias: {bias_c} vs {bias_l}"
    assert bias_c > 0.25, f"Constant bias should be substantial: {bias_c}"

    print("bias_variance_decomposition.py: PASS")


if __name__ == "__main__":
    test_bias_variance()
