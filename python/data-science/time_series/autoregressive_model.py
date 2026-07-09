"""
Autoregressive (AR) Model

Fit an AR(p) model by regressing y_t on its p lagged values using least squares.
Solves the normal equations directly (no external libraries). Produces one-step-ahead
forecasts. Use for univariate time series prediction when past values predict the future.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple


def solve_2x2(a: float, b: float, c: float, d: float, e: float, f: float) -> Tuple[float, float]:
    """Solve 2x2 linear system: a*x + b*y = e, c*x + d*y = f."""
    det = a * d - b * c
    if abs(det) < 1e-10:
        raise ValueError("Singular matrix")
    x = (e * d - b * f) / det
    y = (a * f - e * c) / det
    return x, y


def ar_fit(series: List[float], p: int) -> List[float]:
    """
    Fit AR(p) model: y_t = c + phi_1*y_{t-1} + ... + phi_p*y_{t-p} + noise
    Returns coefficients [c, phi_1, ..., phi_p]
    Uses least squares by solving normal equations.
    For simplicity, we implement p=1 and p=2 explicitly.
    """
    if p < 1 or p >= len(series):
        raise ValueError("p must be 1 <= p < len(series)")

    # Center the series
    mean = sum(series) / len(series)
    centered = [y - mean for y in series]

    if p == 1:
        # y_t = phi_1 * y_{t-1} + noise (centered)
        # Minimize sum((y_t - phi_1 * y_{t-1})^2)
        # Normal eq: phi_1 * sum(y_{t-1}^2) = sum(y_{t-1} * y_t)
        sum_y2_prev = sum(centered[i] ** 2 for i in range(len(centered) - 1))
        sum_prod = sum(centered[i] * centered[i + 1] for i in range(len(centered) - 1))
        if abs(sum_y2_prev) < 1e-10:
            phi_1 = 0.0
        else:
            phi_1 = sum_prod / sum_y2_prev
        return [mean, phi_1]

    elif p == 2:
        # y_t = phi_1 * y_{t-1} + phi_2 * y_{t-2} + noise
        # Normal equations (2x2 system)
        n = len(centered)
        sum_y1_sq = sum(centered[i] ** 2 for i in range(n - 2))
        sum_y2_sq = sum(centered[i] ** 2 for i in range(n - 2))
        sum_y1_y2 = sum(centered[i] * centered[i + 1] for i in range(n - 2))
        sum_y1_y = sum(centered[i] * centered[i + 2] for i in range(n - 2))
        sum_y2_y = sum(centered[i + 1] * centered[i + 2] for i in range(n - 2))

        # [sum_y1_sq   sum_y1_y2] [phi_1]   [sum_y1_y]
        # [sum_y1_y2   sum_y2_sq] [phi_2] = [sum_y2_y]
        phi_1, phi_2 = solve_2x2(
            sum_y1_sq, sum_y1_y2, sum_y1_y2, sum_y2_sq, sum_y1_y, sum_y2_y
        )
        return [mean, phi_1, phi_2]

    else:
        raise NotImplementedError("Only p=1 and p=2 implemented")


def ar_forecast_one_step(series: List[float], coeffs: List[float]) -> List[float]:
    """One-step-ahead forecasts: y_hat_t = c + phi_1*y_{t-1} + ... """
    p = len(coeffs) - 1
    mean = coeffs[0]
    phis = coeffs[1:]
    forecasts = []
    for t in range(p, len(series)):
        yhat = mean
        for i in range(p):
            yhat += phis[i] * series[t - i - 1]
        forecasts.append(yhat)
    return forecasts


def compute_mae(actual: List[float], predicted: List[float]) -> float:
    """Mean absolute error."""
    if len(actual) != len(predicted):
        raise ValueError("Length mismatch")
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate AR(1) series: y_t = 0.7 * y_{t-1} + noise
    series = [10.0]
    for _ in range(100):
        series.append(0.7 * series[-1] + random.gauss(0, 1))

    # Fit AR(1)
    coeffs_1 = ar_fit(series, p=1)
    assert len(coeffs_1) == 2, "AR(1) should have 2 coefficients"
    # Estimated phi should be close to 0.7
    assert 0.5 < coeffs_1[1] < 0.9, f"Expected phi ~ 0.7, got {coeffs_1[1]}"

    # One-step forecasts
    fcst_1 = ar_forecast_one_step(series, coeffs_1)
    assert len(fcst_1) == len(series) - 1

    # Naive baseline: predict mean
    mean_series = sum(series) / len(series)
    naive_fcst = [mean_series] * len(fcst_1)
    actual_values = series[1:]

    mae_ar = compute_mae(actual_values, fcst_1)
    mae_naive = compute_mae(actual_values, naive_fcst)
    assert mae_ar < mae_naive, f"AR should beat naive mean: {mae_ar} vs {mae_naive}"

    # Fit AR(2)
    coeffs_2 = ar_fit(series, p=2)
    assert len(coeffs_2) == 3, "AR(2) should have 3 coefficients"
    fcst_2 = ar_forecast_one_step(series, coeffs_2)
    assert len(fcst_2) == len(series) - 2

    print("autoregressive_model.py PASS")
