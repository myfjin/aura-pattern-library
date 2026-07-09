"""
Autocovariance and Power Spectral Density (Periodogram).

Periodogram = DFT of autocovariance function.
For a signal with strong periodicity, the periodogram should show a peak at that frequency.
We plant a periodic signal and verify the periodogram peaks at the correct frequency.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple


def autocovariance(signal: List[float], max_lag: int) -> List[float]:
    """
    Compute autocovariance at lags 0, 1, ..., max_lag.
    """
    n = len(signal)
    mean_signal = sum(signal) / n

    acov = []
    for lag in range(max_lag + 1):
        cov = 0.0
        for i in range(n - lag):
            cov += (signal[i] - mean_signal) * (signal[i + lag] - mean_signal)
        acov.append(cov / n)

    return acov


def periodogram_from_acov(acov: List[float]) -> List[float]:
    """
    Compute periodogram via FFT of autocovariance.
    Periodogram[k] = |FFT(acov)[k]|.
    """
    m = len(acov)

    # Compute DFT of autocovariance
    periodogram = []
    for k in range(m // 2 + 1):
        real_part = 0.0
        imag_part = 0.0

        for n in range(m):
            angle = -2 * math.pi * k * n / m
            real_part += acov[n] * math.cos(angle)
            imag_part += acov[n] * math.sin(angle)

        magnitude = math.sqrt(real_part**2 + imag_part**2)
        periodogram.append(magnitude)

    return periodogram


if __name__ == "__main__":
    import random

    random.seed(42)

    # Create periodic signal: 10 Hz component
    fs = 100  # Sampling frequency
    duration = 1.0
    n_samples = int(fs * duration)

    freq = 10.0
    signal = [
        math.sin(2 * math.pi * freq * t / fs) + random.gauss(0, 0.1)
        for t in range(n_samples)
    ]

    # Compute autocovariance
    max_lag = 50
    acov = autocovariance(signal, max_lag)

    # Compute periodogram
    periodogram = periodogram_from_acov(acov)

    # Find peak (excluding very low frequencies which are DC)
    peak_idx = max(range(2, len(periodogram)), key=lambda i: periodogram[i])

    # Frequency mapping: index k corresponds to k * fs / len(periodogram) Hz
    # But acov-based periodogram: bin k <-> k * fs / (2 * max_lag) Hz
    freq_resolution = fs / len(acov)
    detected_freq = peak_idx * freq_resolution

    # Check: peak should be near the planted frequency
    freq_error = abs(detected_freq - freq)

    assert freq_error < 2.0, (
        f"Periodogram peak at {detected_freq:.1f} Hz, "
        f"expected {freq:.1f} Hz (error={freq_error:.1f} Hz)"
    )
    assert periodogram[peak_idx] > periodogram[peak_idx - 1], "Peak not local max"
    assert periodogram[peak_idx] > periodogram[peak_idx + 1], "Peak not local max"

    print(
        f"Planted frequency: {freq:.1f} Hz | "
        f"Detected frequency: {detected_freq:.1f} Hz | "
        f"Peak value: {periodogram[peak_idx]:.2f} | "
        f"Error: {freq_error:.2f} Hz | PASS"
    )
