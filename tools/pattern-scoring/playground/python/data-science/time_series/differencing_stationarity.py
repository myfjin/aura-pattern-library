"""
Differencing for Stationarity

First differencing transforms a non-stationary series (e.g., random walk)
into a stationary one. Differenced series: d_t = y_t - y_{t-1}.
Stationarity (constant mean, variance) enables forecasting with AR models.
Demonstrate that differencing reduces mean and variance drift in a trend.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple


def first_difference(series: List[float]) -> List[float]:
    """Compute first difference: d_t = y_t - y_{t-1}."""
    return [series[i] - series[i - 1] for i in range(1, len(series))]


def augmented_dickey_fuller_simple(series: List[float]) -> float:
    """
    Simple stationarity check: compare variance of first half vs. second half.
    If ratio is close to 1, series is more stationary.
    (Not true ADF test, just a diagnostic.)
    """
    n = len(series)
    half = n // 2
    first_half = series[:half]
    second_half = series[half:]

    mean1 = sum(first_half) / len(first_half)
    mean2 = sum(second_half) / len(second_half)
    var1 = sum((x - mean1) ** 2 for x in first_half) / len(first_half)
    var2 = sum((x - mean2) ** 2 for x in second_half) / len(second_half)

    if var1 < 1e-10 or var2 < 1e-10:
        return 0.0
    variance_ratio = var2 / var1
    return variance_ratio


def compute_mean_drift(series: List[float], window: int) -> float:
    """Compute drift as change in mean between first and last window."""
    if len(series) < 2 * window:
        raise ValueError("Series too short")
    first_mean = sum(series[:window]) / window
    last_mean = sum(series[-window:]) / window
    return abs(last_mean - first_mean)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate random walk (non-stationary)
    series_rw = [0.0]
    for _ in range(150):
        series_rw.append(series_rw[-1] + random.gauss(0, 1))

    # First difference it
    diff_rw = first_difference(series_rw)

    # Check stationarity: random walk should have high variance_ratio (drift)
    vr_rw = augmented_dickey_fuller_simple(series_rw)
    vr_diff = augmented_dickey_fuller_simple(diff_rw)

    # Differenced series should be more stationary (ratio closer to 1)
    assert vr_diff < vr_rw, f"Differenced should be more stationary: {vr_diff} vs {vr_rw}"

    # Generate linear trend (non-stationary)
    series_trend = [5 + 0.3 * i + random.gauss(0, 0.5) for i in range(150)]

    # Difference it
    diff_trend = first_difference(series_trend)

    # Mean drift in original should be large
    drift_orig = compute_mean_drift(series_trend, window=20)
    drift_diff = compute_mean_drift(diff_trend, window=20)

    assert drift_diff < drift_orig, f"Differencing should reduce mean drift: {drift_diff} vs {drift_orig}"

    # Differenced series should be shorter by 1
    assert len(diff_rw) == len(series_rw) - 1
    assert len(diff_trend) == len(series_trend) - 1

    # Check that differenced random walk has mean close to 0
    diff_mean = sum(diff_rw) / len(diff_rw)
    assert abs(diff_mean) < 1.0, f"Differenced RW mean should be ~0, got {diff_mean}"

    # Differenced trend should have much lower trend
    diff_trend_mean = sum(diff_trend) / len(diff_trend)
    assert abs(diff_trend_mean) < 0.5, f"Differenced trend mean should be low, got {diff_trend_mean}"

    print("differencing_stationarity.py PASS")
