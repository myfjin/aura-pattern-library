"""
Exponentially Weighted Moving Average (EWMA) for streaming metrics.

EWMA smooths noisy streaming data while reacting quickly to level shifts.
Each new observation is weighted inversely to its age (older = lower weight).
More responsive than simple moving average, smoother than raw values.

Use: real-time monitoring, anomaly detection, adaptive thresholds.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math


class EWMAMetric:
    """Online EWMA tracker for a single metric."""

    def __init__(self, alpha: float = 0.3):
        """
        Initialize EWMA.
        alpha: smoothing factor [0, 1]. Higher = more responsive to new values.
        """
        self.alpha = alpha
        self.value = None
        self.count = 0

    def update(self, x: float) -> float:
        """Add observation x, return updated EWMA."""
        self.count += 1

        if self.value is None:
            self.value = x
        else:
            self.value = self.alpha * x + (1 - self.alpha) * self.value

        return self.value


class SMAMetric:
    """Online Simple Moving Average tracker (for comparison)."""

    def __init__(self, window_size: int = 10):
        """Initialize SMA with a window size."""
        self.window_size = window_size
        self.values = []

    def update(self, x: float) -> float:
        """Add observation, return moving average."""
        self.values.append(x)
        if len(self.values) > self.window_size:
            self.values.pop(0)

        return sum(self.values) / len(self.values)


if __name__ == "__main__":
    import random
    random.seed(42)

    print("EWMA vs Simple Moving Average for streaming metrics")
    print()

    # Scenario: baseline level at 100, then shift to 120 at step 30
    # Track how quickly EWMA and SMA react

    baseline = 100
    shift_step = 30
    new_level = 120

    data = []
    ewma_values = []
    sma_values = []

    ewma = EWMAMetric(alpha=0.3)
    sma = SMAMetric(window_size=10)

    for step in range(1, 51):
        # True value: baseline until shift_step, then new_level with noise
        if step < shift_step:
            true_val = baseline + random.gauss(0, 2)
        else:
            true_val = new_level + random.gauss(0, 2)

        data.append(true_val)

        # Update estimators
        ewma_val = ewma.update(true_val)
        sma_val = sma.update(true_val)

        ewma_values.append(ewma_val)
        sma_values.append(sma_val)

    # Print phase transition
    print("Phase 1 (stable baseline, steps 1-29):")
    print(f"  Raw values avg:  {sum(data[:29])/29:.2f}")
    print(f"  EWMA avg:        {sum(ewma_values[:29])/29:.2f}")
    print(f"  SMA avg:         {sum(sma_values[:29])/29:.2f}")
    print()

    print("Phase 2 (after shift, steps 30-50):")
    print(f"  Raw values avg:  {sum(data[29:])/21:.2f}")
    print(f"  EWMA avg:        {sum(ewma_values[29:])/21:.2f}")
    print(f"  SMA avg:         {sum(sma_values[29:])/21:.2f}")
    print()

    # Measure: how far from new level is each estimator at step 35 (5 steps after shift)?
    target_step = 34  # 0-indexed, so step 35
    ewma_at_35 = ewma_values[target_step]
    sma_at_35 = sma_values[target_step]
    raw_at_35 = data[target_step]

    gap_ewma = abs(ewma_at_35 - new_level)
    gap_sma = abs(sma_at_35 - new_level)
    gap_raw = abs(raw_at_35 - new_level)

    print(f"At step 35 (5 steps after shift to {new_level}):")
    print(f"  Raw value:       {raw_at_35:.2f} (gap: {gap_raw:.2f})")
    print(f"  EWMA:            {ewma_at_35:.2f} (gap: {gap_ewma:.2f})")
    print(f"  SMA:             {sma_at_35:.2f} (gap: {gap_sma:.2f})")
    print()

    # Measure smoothness: variance of derivatives
    ewma_deltas = [abs(ewma_values[i] - ewma_values[i-1]) for i in range(1, len(ewma_values))]
    sma_deltas = [abs(sma_values[i] - sma_values[i-1]) for i in range(1, len(sma_values))]
    raw_deltas = [abs(data[i] - data[i-1]) for i in range(1, len(data))]

    ewma_smoothness = sum(d**2 for d in ewma_deltas) / len(ewma_deltas)
    sma_smoothness = sum(d**2 for d in sma_deltas) / len(sma_deltas)
    raw_smoothness = sum(d**2 for d in raw_deltas) / len(raw_deltas)

    print(f"Smoothness (MSE of step changes):")
    print(f"  Raw:  {raw_smoothness:.2f}")
    print(f"  EWMA: {ewma_smoothness:.2f} (smoother than raw)")
    print(f"  SMA:  {sma_smoothness:.2f}")
    print()

    # Assertions
    # 1. EWMA should react faster than SMA (closer to new level at step 35)
    assert gap_ewma < gap_sma, \
        f"EWMA gap {gap_ewma:.2f} should be < SMA gap {gap_sma:.2f} (faster reaction)"

    # 2. EWMA should be smoother than raw values
    assert ewma_smoothness < raw_smoothness, \
        f"EWMA smoothness {ewma_smoothness:.2f} should be < raw {raw_smoothness:.2f}"

    # 3. Both EWMA and SMA should have lower variance than raw
    assert sma_smoothness < raw_smoothness, \
        f"SMA smoothness {sma_smoothness:.2f} should be < raw {raw_smoothness:.2f}"

    print("Verification:")
    print(f"  EWMA reacts faster than SMA: ✓")
    print(f"  EWMA smoother than raw:      ✓")
    print(f"  SMA smoother than raw:       ✓")

    print("\newma_streaming_metrics.py PASS")
