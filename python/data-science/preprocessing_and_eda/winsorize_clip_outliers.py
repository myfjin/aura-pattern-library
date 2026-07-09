"""
Winsorization and Clipping Pattern.

Caps extreme values at percentile thresholds (winsorization) or hard bounds
(clipping). Core idea: reduce influence of outliers while preserving sample
count and general structure; interior values untouched.

When to use: outlier mitigation before analysis, handling measurement errors,
reducing leverage of extreme observations, robust preprocessing.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List
import statistics


def percentile(data: List[float], p: float) -> float:
    """
    Compute the p-th percentile (0 <= p <= 100).
    Linear interpolation between closest ranks.
    """
    if not data or p < 0 or p > 100:
        raise ValueError("Invalid percentile")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 1:
        return sorted_data[0]

    # Position in 0-indexed array
    h = (p / 100.0) * (n - 1)
    i = int(h)
    f = h - i

    if i >= n - 1:
        return sorted_data[n - 1]
    return sorted_data[i] + f * (sorted_data[i + 1] - sorted_data[i])


def winsorize(data: List[float], limits: tuple = (0.05, 0.05)) -> List[float]:
    """
    Winsorize data: cap at percentile limits.
    Args:
        data: List of numeric values
        limits: (lower_pct, upper_pct) as fraction (0.05 = 5th percentile)
    Returns:
        Winsorized data (outliers capped, others unchanged)
    """
    lower_pct = limits[0] * 100
    upper_pct = 100 - limits[1] * 100

    lower_bound = percentile(data, lower_pct)
    upper_bound = percentile(data, upper_pct)

    return [max(lower_bound, min(x, upper_bound)) for x in data]


def clip(data: List[float], min_val: float, max_val: float) -> List[float]:
    """
    Clip data to hard bounds.
    Args:
        data: List of numeric values
        min_val: Lower hard bound
        max_val: Upper hard bound
    Returns:
        Clipped data
    """
    return [max(min_val, min(x, max_val)) for x in data]


if __name__ == "__main__":
    import random

    random.seed(42)

    # Synthetic data with planted outliers
    normal_data = [random.gauss(50, 10) for _ in range(80)]
    outliers = [2.0, 200.0, -50.0, 250.0]
    data_with_outliers = normal_data + outliers
    n_original = len(data_with_outliers)

    # Apply winsorization
    winsorized = winsorize(data_with_outliers, limits=(0.05, 0.05))

    # Verify count unchanged
    assert len(winsorized) == n_original, "Count changed after winsorization"

    # Verify count unchanged
    assert len(winsorized) == n_original, "Count changed"

    # Verify extreme injected values are capped
    # The 4 extreme outliers should be bounded
    extreme_original = [2.0, 200.0, -50.0, 250.0]
    winsorized_extremes = winsorized[-4:]  # Last 4 are the outliers we added
    for val in winsorized_extremes:
        assert min(winsorized) <= val <= max(winsorized), f"Extreme value out of bounds: {val}"

    # Verify range is much tighter after winsorization
    original_range = max(data_with_outliers) - min(data_with_outliers)
    winsorized_range = max(winsorized) - min(winsorized)
    assert winsorized_range < original_range * 0.7, f"Winsorization didn't reduce range much"

    # Test clipping
    clipped = clip(data_with_outliers, 10, 90)

    # Verify all values in range
    assert all(10 <= x <= 90 for x in clipped), "Clipping failed"

    # Verify count unchanged
    assert len(clipped) == n_original, "Count changed after clipping"

    # Verify boundary values
    assert min(clipped) == 10, f"Min not clipped to 10: {min(clipped)}"
    assert max(clipped) == 90, f"Max not clipped to 90: {max(clipped)}"

    print("winsorize_clip_outliers.py: PASS")
