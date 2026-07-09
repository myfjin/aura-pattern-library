"""
FEATURE SCALING: Min-Max, Z-Score, Robust Scaling

Core idea: Different scaling methods normalize features to comparable ranges.
Min-max scales to [0, 1]; z-score centers to mean=0, std=1; robust uses median/IQR
to resist outliers. Choose based on data distribution and algorithm requirements.

When to use: KNN, SVM, neural networks, or any algorithm sensitive to feature magnitude.
Verify output properties (bounds, mean, std) match expectations.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple


def min_max_scale(data: List[float]) -> Tuple[List[float], float, float]:
    """
    Min-max scaling: (x - min) / (max - min) -> range [0, 1]
    Returns (scaled_data, min_val, max_val)
    """
    if len(data) == 0:
        return [], 0.0, 0.0

    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val

    if range_val == 0:
        # All values identical
        return [0.0] * len(data), min_val, max_val

    scaled = [(x - min_val) / range_val for x in data]
    return scaled, min_val, max_val


def z_score_scale(data: List[float]) -> Tuple[List[float], float, float]:
    """
    Z-score (standardization): (x - mean) / std -> mean=0, std=1
    Returns (scaled_data, mean, std)
    """
    if len(data) == 0:
        return [], 0.0, 0.0

    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std = math.sqrt(variance)

    if std == 0:
        # All values identical
        return [0.0] * len(data), mean, std

    scaled = [(x - mean) / std for x in data]
    return scaled, mean, std


def robust_scale(data: List[float]) -> Tuple[List[float], float, float]:
    """
    Robust scaling: (x - median) / IQR
    Resistant to outliers. IQR = Q3 - Q1 (interquartile range)
    Returns (scaled_data, median, iqr)
    """
    if len(data) == 0:
        return [], 0.0, 0.0

    sorted_data = sorted(data)
    n = len(sorted_data)

    # Compute median
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2.0

    # Compute Q1 (25th percentile)
    q1_idx = n // 4
    q1 = sorted_data[q1_idx]

    # Compute Q3 (75th percentile)
    q3_idx = (3 * n) // 4
    q3 = sorted_data[q3_idx]

    iqr = q3 - q1

    if iqr == 0:
        # All quartiles identical
        return [0.0] * len(data), median, iqr

    scaled = [(x - median) / iqr for x in data]
    return scaled, median, iqr


def verify_properties(scaled: List[float], name: str, target_mean: float = 0.0, target_std: float = 1.0, allow_mean_tol: float = 1e-10, allow_std_tol: float = 0.05):
    """
    Verify scaling properties (for test assertions).
    """
    if len(scaled) == 0:
        return True

    actual_mean = sum(scaled) / len(scaled)
    actual_variance = sum((x - actual_mean) ** 2 for x in scaled) / len(scaled)
    actual_std = math.sqrt(actual_variance)

    mean_ok = abs(actual_mean - target_mean) < allow_mean_tol
    std_ok = abs(actual_std - target_std) < allow_std_tol

    return mean_ok and std_ok


if __name__ == "__main__":
    import random

    random.seed(42)

    # Test data: mix of normal values and an outlier
    data = [10.0, 12.0, 11.0, 13.0, 14.0, 100.0]  # 100 is an outlier

    # Test 1: Min-max scaling
    scaled_minmax, min_val, max_val = min_max_scale(data)
    assert min(scaled_minmax) >= 0.0, "Min-max scaled value below 0"
    assert max(scaled_minmax) <= 1.0, "Min-max scaled value above 1"
    assert abs(min(scaled_minmax) - 0.0) < 1e-10, "Min-max min not 0"
    assert abs(max(scaled_minmax) - 1.0) < 1e-10, "Min-max max not 1"

    # Test 2: Z-score scaling
    scaled_zscore, mean, std = z_score_scale(data)
    actual_mean = sum(scaled_zscore) / len(scaled_zscore)
    actual_std = math.sqrt(sum((x - actual_mean) ** 2 for x in scaled_zscore) / len(scaled_zscore))
    assert abs(actual_mean - 0.0) < 1e-10, f"Z-score mean not 0: {actual_mean}"
    assert abs(actual_std - 1.0) < 1e-10, f"Z-score std not 1: {actual_std}"

    # Test 3: Robust scaling
    scaled_robust, median, iqr = robust_scale(data)
    # Robust scaling doesn't guarantee zero mean/unit std, but should be finite
    assert all(math.isfinite(x) for x in scaled_robust), "Robust scaling produced non-finite values"

    # Test 4: Outlier effect
    # Z-score will be heavily influenced by outlier (100)
    zscore_outlier = scaled_zscore[5]  # The 100 value
    # Robust should treat it less extremely
    robust_outlier = scaled_robust[5]

    # The outlier will have larger z-score than robust score (in absolute terms depends on IQR)
    # Both should at least identify it as unusual (far from center)
    assert abs(zscore_outlier) > 1.0, "Z-score didn't identify outlier as unusual"
    assert abs(robust_outlier) > 0.0, "Robust scaling collapsed"

    # Test 5: Scaling is invertible (for min-max and z-score)
    # Inverse min-max: x_orig = x_scaled * range + min
    reconstructed_minmax = [x * (max_val - min_val) + min_val for x in scaled_minmax]
    for orig, recon in zip(data, reconstructed_minmax):
        assert abs(orig - recon) < 1e-10, f"Min-max not invertible: {orig} != {recon}"

    # Inverse z-score: x_orig = x_scaled * std + mean
    reconstructed_zscore = [x * std + mean for x in scaled_zscore]
    for orig, recon in zip(data, reconstructed_zscore):
        assert abs(orig - recon) < 1e-10, f"Z-score not invertible: {orig} != {recon}"

    print("feature_scaling_toolkit.py: minmax_bounds zscore_properties robust_finite PASS")
