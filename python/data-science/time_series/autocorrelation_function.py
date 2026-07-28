"""
Autocorrelation Function (ACF)

Compute the autocorrelation of a time series at multiple lags.
ACF(k) = correlation between y_t and y_{t-k}.
Include simple significance bounds (±2/sqrt(n)) to identify significant lags.
Use to detect seasonality and memory in the data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_acf(nlags):
    v = []
    if isinstance(nlags, (int, float)) and nlags <= 0:
        v.append(f"AURA-E009: nlags must be > 0, got {nlags}")
    if v:
        raise AuraInputError(v)

def acf(series: List[float], nlags: int) -> List[float]:
    """
    Compute autocorrelation function at lags 0 to nlags.
    ACF(k) = cov(y_t, y_{t-k}) / var(y_t)
    """
    _aura_validate_acf(nlags)
    if nlags < 0 or nlags >= len(series):
        raise ValueError("nlags must be 0 <= nlags < len(series)")

    # Demean
    mean = sum(series) / len(series)
    centered = [y - mean for y in series]

    # Compute variance (lag 0 autocovariance)
    c0 = sum(x ** 2 for x in centered) / len(centered)
    if c0 < 1e-10:
        return [0.0] * (nlags + 1)

    acf_vals = [1.0]  # ACF at lag 0 is always 1

    for lag in range(1, nlags + 1):
        cov_lag = sum(centered[i] * centered[i + lag] for i in range(len(centered) - lag)) / len(centered)
        acf_vals.append(cov_lag / c0)

    return acf_vals


def significance_bounds(n: int) -> float:
    """Bartlett's approximate 95% confidence bound: ±2/sqrt(n)"""
    return 2.0 / (n ** 0.5)


def identify_significant_lags(acf_vals: List[float], n: int) -> List[int]:
    """Identify lags where |ACF| exceeds significance bounds."""
    bound = significance_bounds(n)
    return [lag for lag, val in enumerate(acf_vals) if abs(val) > bound and lag > 0]


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate AR(1) series with autocorrelation
    series = [0.0]
    for _ in range(200):
        series.append(0.6 * series[-1] + random.gauss(0, 1))

    # Compute ACF
    acf_vals = acf(series, nlags=20)

    # Check basic properties
    assert len(acf_vals) == 21
    assert acf_vals[0] == 1.0, "ACF at lag 0 should be 1.0"

    # For AR(1) with phi=0.6, ACF should decay exponentially
    # ACF(k) ≈ 0.6^k
    assert 0.4 < acf_vals[1] < 0.8, f"ACF at lag 1 should be close to 0.6, got {acf_vals[1]}"
    assert acf_vals[1] > acf_vals[2], "ACF should decay"
    assert acf_vals[2] > acf_vals[5], "ACF should continue decaying"

    # Test significance bounds
    bound = significance_bounds(len(series))
    assert bound > 0 and bound < 0.2, f"Bound should be small: {bound}"

    # Find significant lags
    sig_lags = identify_significant_lags(acf_vals, len(series))
    assert len(sig_lags) > 0, "Should have significant lags for AR series"

    # The first lag should be significant
    assert 1 in sig_lags, "Lag 1 should be significant for AR(1)"

    # Create white noise (no autocorrelation)
    white_noise = [random.gauss(0, 1) for _ in range(200)]
    acf_white = acf(white_noise, nlags=20)
    sig_white = identify_significant_lags(acf_white, len(white_noise))

    # White noise should have few significant lags (some may occur by chance)
    assert len(sig_white) < 5, f"White noise should have few sig lags, got {len(sig_white)}"

    print("autocorrelation_function.py PASS")
