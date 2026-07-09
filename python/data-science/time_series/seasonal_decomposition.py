"""
Seasonal Decomposition (Naive Additive)

Decompose a time series into trend, seasonal, and residual components using
naive additive decomposition: y_t = trend_t + seasonal_t + residual_t.
Trend extracted via centered moving average; seasonal via period-wise means.
Use to understand and remove seasonal patterns from data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple
from collections import defaultdict


def centered_moving_average(series: List[float], window: int) -> List[float]:
    """Centered moving average with NaN handling (return None for edges)."""
    result = [None] * len(series)
    half_w = window // 2
    for i in range(half_w, len(series) - half_w):
        result[i] = sum(series[i - half_w : i + half_w + 1]) / window
    return result


def naive_seasonal_decomposition(
    series: List[float], period: int
) -> Tuple[List[float], List[float], List[float]]:
    """
    Naive additive decomposition.
    trend = centered MA with window = period
    seasonal = mean residual for each season
    residual = series - trend - seasonal
    Returns (trend, seasonal, residual) lists; trend/seasonal may have None values.
    """
    if period < 2 or period > len(series) // 2:
        raise ValueError("period must be >= 2 and <= len(series)/2")

    # Extract trend via centered MA
    trend = centered_moving_average(series, period)

    # Detrend
    detrended = [
        series[i] - trend[i] if trend[i] is not None else None
        for i in range(len(series))
    ]

    # Extract seasonal: mean of each season
    seasonal_values = defaultdict(list)
    for i, dt in enumerate(detrended):
        if dt is not None:
            seasonal_values[i % period].append(dt)

    seasonal_means = {}
    for season in range(period):
        if season in seasonal_values:
            seasonal_means[season] = sum(seasonal_values[season]) / len(
                seasonal_values[season]
            )
        else:
            seasonal_means[season] = 0.0

    # Full seasonal component
    seasonal = [seasonal_means[i % period] for i in range(len(series))]

    # Residual
    residual = []
    for i in range(len(series)):
        if trend[i] is not None:
            residual.append(series[i] - trend[i] - seasonal[i])
        else:
            residual.append(None)

    return trend, seasonal, residual


def compute_variance_excluding_none(values: List[float]) -> float:
    """Compute variance, ignoring None values."""
    clean = [v for v in values if v is not None]
    if len(clean) < 2:
        return 0.0
    mean = sum(clean) / len(clean)
    return sum((v - mean) ** 2 for v in clean) / len(clean)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate series with trend + seasonal pattern
    trend_vals = [10 + 0.1 * i for i in range(120)]
    seasonal_vals = [5 * (1 if (i % 12) < 6 else -1) for i in range(120)]
    noise = [random.gauss(0, 0.5) for _ in range(120)]
    series = [t + s + n for t, s, n in zip(trend_vals, seasonal_vals, noise)]

    # Decompose
    trend, seasonal, residual = naive_seasonal_decomposition(series, period=12)

    # Check lengths
    assert len(trend) == len(series)
    assert len(seasonal) == len(series)
    assert len(residual) == len(series)

    # Trend should be smoother than original (lower variance on non-None values)
    trend_var = compute_variance_excluding_none(trend)
    series_var = sum((x - sum(series) / len(series)) ** 2 for x in series) / len(series)
    assert trend_var < series_var, f"Trend should be smoother: {trend_var} vs {series_var}"

    # Seasonal should exhibit periodicity: check that same-season indices are similar
    season_groups = defaultdict(list)
    for i, s in enumerate(seasonal):
        season_groups[i % 12].append(s)
    within_season_var = sum(
        sum((v - sum(season_groups[i]) / len(season_groups[i])) ** 2
            for v in season_groups[i]) / len(season_groups[i])
        for i in range(12)
    ) / 12
    between_season_var = sum(
        (sum(season_groups[i]) / len(season_groups[i]) - sum(seasonal) / len(seasonal)) ** 2
        for i in range(12)
    ) / 12
    assert between_season_var > 0, "Seasonal component should show variation between seasons"

    # Residual should be much smaller than original
    residual_var = compute_variance_excluding_none(residual)
    assert residual_var < series_var, "Residual variance should be less than series variance"

    print("seasonal_decomposition.py PASS")
