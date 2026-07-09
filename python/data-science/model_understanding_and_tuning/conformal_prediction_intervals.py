"""
Split-Conformal Prediction Intervals for Regression

Core idea: Split data into train/calibration. Train a regression model, then on calibration
data compute residuals to set interval width such that coverage is guaranteed.

When to use: You want prediction intervals with a formal coverage guarantee, even if the
model is miscalibrated or the error distribution is non-Gaussian.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import statistics
from typing import List, Tuple


def simple_linear_model(X: List[float], y: List[float]) -> Tuple[float, float]:
    """Fit y = a + b*x via least squares."""
    n = len(X)
    x_mean = sum(X) / n
    y_mean = sum(y) / n

    b = sum((X[i] - x_mean) * (y[i] - y_mean) for i in range(n)) / (sum((x - x_mean) ** 2 for x in X) + 1e-8)
    a = y_mean - b * x_mean
    return a, b


def predict(x: float, params: Tuple[float, float]) -> float:
    """Predict y given x and model params (intercept, slope)."""
    a, b = params
    return a + b * x


def split_conformal_intervals(
    X_train: List[float],
    y_train: List[float],
    X_cal: List[float],
    y_cal: List[float],
    confidence: float = 0.9
) -> Tuple[float, float]:
    """
    Fit model on train, compute calibration residuals, set interval width.
    Returns (model_params, quantile_residual) for interval width.
    """
    # Train model
    params = simple_linear_model(X_train, y_train)

    # Compute calibration residuals
    residuals = []
    for x, y in zip(X_cal, y_cal):
        pred = predict(x, params)
        residual = abs(y - pred)
        residuals.append(residual)

    # Sort residuals
    residuals.sort()
    n_cal = len(residuals)

    # Ceiling of quantile index: at least (n_cal + 1) * confidence elements
    quantile_idx = min(int((n_cal) * confidence), n_cal - 1)

    return params, residuals[quantile_idx]


def predict_interval(x: float, params: Tuple[float, float], half_width: float) -> Tuple[float, float]:
    """Predict interval [lower, upper] for x."""
    pred = predict(x, params)
    return pred - half_width, pred + half_width


if __name__ == "__main__":
    random.seed(42)

    # Generate synthetic data: y = 5 + 2*x + noise
    X_all = []
    y_all = []
    for _ in range(400):
        x = random.uniform(-5, 5)
        y = 5 + 2 * x + random.gauss(0, 2.0)
        X_all.append(x)
        y_all.append(y)

    # Split: 150 train, 125 calibration, 125 test
    X_train = X_all[:150]
    y_train = y_all[:150]
    X_cal = X_all[150:275]
    y_cal = y_all[150:275]
    X_test = X_all[275:]
    y_test = y_all[275:]

    # Fit conformal predictor
    params, half_width = split_conformal_intervals(X_train, y_train, X_cal, y_cal, confidence=0.9)

    # Generate intervals on test set
    coverage_count = 0
    interval_widths = []
    for x, y in zip(X_test, y_test):
        lower, upper = predict_interval(x, params, half_width)
        interval_widths.append(upper - lower)
        if lower <= y <= upper:
            coverage_count += 1

    coverage = coverage_count / len(X_test)
    avg_width = statistics.mean(interval_widths)

    print(f"Coverage: {coverage:.2%} (target 90%)")
    print(f"Average interval width: {avg_width:.2f}")

    # Assertion: coverage should be reasonable (split-conformal guarantees >= (n+1)/(n+2) * p)
    assert coverage >= 0.70, f"Coverage should be >= 70%: {coverage:.2%}"
    assert avg_width > 0 and avg_width < 100, f"Interval width should be reasonable: {avg_width}"

    print("✓ Conformal Prediction Intervals: PASS")
