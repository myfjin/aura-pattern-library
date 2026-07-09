"""
Moving Average Smoothing

Smooth a noisy time series using simple and weighted moving averages.
Reduces short-term fluctuations while preserving trend; wider windows smooth
more but lag the signal. Use for noise reduction in raw sensor or market data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple


def simple_moving_average(series: List[float], window: int) -> List[float]:
    """Compute simple moving average with given window size."""
    if window < 1 or window > len(series):
        raise ValueError("window must be between 1 and series length")
    result = []
    for i in range(len(series)):
        if i < window - 1:
            # Not enough history; use available data
            result.append(sum(series[:i+1]) / (i + 1))
        else:
            result.append(sum(series[i-window+1:i+1]) / window)
    return result


def weighted_moving_average(series: List[float], window: int) -> List[float]:
    """Compute weighted moving average: most recent points get highest weight."""
    if window < 1 or window > len(series):
        raise ValueError("window must be between 1 and series length")
    weights = list(range(1, window + 1))
    weight_sum = sum(weights)
    result = []
    for i in range(len(series)):
        if i < window - 1:
            w = list(range(1, i + 2))
            ws = sum(w)
            result.append(sum(s * wt for s, wt in zip(series[:i+1], w)) / ws)
        else:
            result.append(sum(s * wt for s, wt in zip(series[i-window+1:i+1], weights)) / weight_sum)
    return result


def compute_variance(series: List[float]) -> float:
    """Compute sample variance."""
    if len(series) < 2:
        return 0.0
    mean = sum(series) / len(series)
    return sum((x - mean) ** 2 for x in series) / (len(series) - 1)


if __name__ == "__main__":
    random.seed(42)

    # Generate noisy signal with trend
    true_signal = [10 + 0.05 * i for i in range(100)]
    noise = [random.gauss(0, 2) for _ in range(100)]
    noisy_series = [s + n for s, n in zip(true_signal, noise)]

    # Apply smoothing
    sma = simple_moving_average(noisy_series, window=5)
    wma = weighted_moving_average(noisy_series, window=5)

    # Check that smoothing reduces variance
    raw_var = compute_variance(noisy_series)
    sma_var = compute_variance(sma)
    wma_var = compute_variance(wma)

    assert sma_var < raw_var, f"SMA should reduce variance: {sma_var} vs {raw_var}"
    assert wma_var < raw_var, f"WMA should reduce variance: {wma_var} vs {raw_var}"
    # Both methods reduce variance
    assert sma_var > 0 and wma_var > 0, "Variances should be positive"

    # Check length preservation
    assert len(sma) == len(noisy_series)
    assert len(wma) == len(noisy_series)

    print("moving_average_smoothing.py PASS")
