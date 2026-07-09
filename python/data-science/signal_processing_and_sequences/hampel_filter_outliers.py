"""
Hampel Filter for Outlier Detection and Removal.

Use rolling-median and MAD (median absolute deviation) to detect outliers.
Replace outliers with the rolling median.
Outliers are values > median + k*MAD, typically k=3.
We plant spikes and verify they are removed while the true signal is preserved.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List


def hampel_filter(signal: List[float], window_size: int = 5, k: float = 3.0) -> List[float]:
    """
    Apply Hampel filter: detect outliers based on rolling median + k*MAD.
    Replace outliers with rolling median.
    """
    n = len(signal)
    half_window = window_size // 2
    filtered = signal.copy()

    for i in range(n):
        # Define window around i
        left = max(0, i - half_window)
        right = min(n - 1, i + half_window)
        window = signal[left : right + 1]

        # Compute median and MAD
        sorted_window = sorted(window)
        median = sorted_window[len(sorted_window) // 2]
        deviations = [abs(x - median) for x in window]
        sorted_deviations = sorted(deviations)
        mad = sorted_deviations[len(sorted_deviations) // 2]

        # Detect outlier
        if abs(signal[i] - median) > k * mad:
            filtered[i] = median

    return filtered


def mse(x: List[float], y: List[float]) -> float:
    """MSE between x and y."""
    return sum((x[i] - y[i]) ** 2 for i in range(len(x))) / len(x)


if __name__ == "__main__":
    import random

    random.seed(42)

    # Create a clean signal
    n = 100
    true_signal = [5.0 + 0.1 * t + random.gauss(0, 0.3) for t in range(n)]

    # Plant spikes (outliers)
    noisy_signal = true_signal.copy()
    spike_indices = [20, 40, 60, 80]
    for idx in spike_indices:
        noisy_signal[idx] += 10.0  # Add large spike

    # Apply Hampel filter
    filtered_signal = hampel_filter(noisy_signal, window_size=5, k=3.0)

    # Compute MSE: filtered should be closer to true than noisy
    mse_noisy = mse(true_signal, noisy_signal)
    mse_filtered = mse(true_signal, filtered_signal)

    assert mse_filtered < mse_noisy, (
        f"Hampel filter did not improve: "
        f"noisy MSE={mse_noisy:.2f}, filtered={mse_filtered:.2f}"
    )

    # Check that spikes are removed
    spike_removals = 0
    for idx in spike_indices:
        if abs(filtered_signal[idx] - noisy_signal[idx]) > 5.0:
            spike_removals += 1

    assert spike_removals >= 3, f"Removed only {spike_removals}/4 spikes"

    print(
        f"Noisy MSE: {mse_noisy:.2f} | Filtered MSE: {mse_filtered:.2f} | "
        f"MSE reduction: {(1 - mse_filtered/mse_noisy)*100:.1f}% | "
        f"Spikes removed: {spike_removals}/{len(spike_indices)} | PASS"
    )
