import math
"""
Rolling Z-Score Anomaly Detection

Detect anomalies using rolling-window z-scores. For each point, compute
the z-score within a rolling window: z = (x - window_mean) / window_std.
Flag points where |z| exceeds a threshold (e.g., 3) as anomalies.
Use for detecting sudden spikes or drops in streaming data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_rolling_zscore(threshold):
    v = []
    if isinstance(threshold, (int, float)) and not math.isfinite(threshold):
        v.append(f"AURA-E008: threshold must be finite, got {threshold}")
    if v:
        raise AuraInputError(v)

def rolling_zscore(series: List[float], window: int, threshold: float = 3.0) -> Tuple[List[float], List[int]]:
    """
    Compute rolling z-scores and detect anomalies.
    window: size of rolling window for mean/std
    threshold: |z-score| above this triggers anomaly flag
    Returns (z_scores, anomaly_indices)
    """
    _aura_validate_rolling_zscore(threshold)
    if window < 2 or window > len(series):
        raise ValueError("window must be between 2 and len(series)")

    z_scores = []
    anomaly_indices = []

    for i in range(len(series)):
        # Determine window boundaries
        start = max(0, i - window + 1)
        end = i + 1
        window_data = series[start:end]

        # Compute mean and std
        mean_val = sum(window_data) / len(window_data)
        variance = sum((x - mean_val) ** 2 for x in window_data) / len(window_data)
        std_val = variance ** 0.5

        # Compute z-score
        if std_val < 1e-10:
            z_score = 0.0
        else:
            z_score = (series[i] - mean_val) / std_val

        z_scores.append(z_score)

        # Flag anomaly
        if abs(z_score) > threshold:
            anomaly_indices.append(i)

    return z_scores, anomaly_indices


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate series with injected spikes
    series = [random.gauss(10, 1) for _ in range(100)]

    # Inject clear spikes at specific indices
    spike_indices = [20, 45, 75]
    for idx in spike_indices:
        series[idx] += 10  # Add large spike

    # Run detector
    z_scores, anomalies = rolling_zscore(series, window=10, threshold=2.5)

    # Check that we detected all spikes
    assert len(anomalies) > 0, "Should detect spikes"

    # Check that detected anomalies are close to injected spikes
    for spike_idx in spike_indices:
        # Allow a small window around the spike
        nearby_anomalies = [a for a in anomalies if abs(a - spike_idx) <= 2]
        assert len(nearby_anomalies) > 0, f"Should detect spike near index {spike_idx}"

    # Verify that most normal points have low z-scores
    normal_z_scores = [
        z_scores[i] for i in range(len(series)) if i not in anomalies
    ]
    avg_normal_z = sum(abs(z) for z in normal_z_scores) / len(normal_z_scores)
    assert avg_normal_z < 1.5, f"Normal points should have low z-scores, got avg {avg_normal_z}"

    # Verify that anomalies have high z-scores
    anomaly_z_scores = [z_scores[i] for i in anomalies]
    avg_anomaly_z = sum(abs(z) for z in anomaly_z_scores) / len(anomaly_z_scores)
    assert avg_anomaly_z > 2.0, f"Anomalies should have high z-scores, got avg {avg_anomaly_z}"

    print("rolling_zscore_anomaly.py PASS")
