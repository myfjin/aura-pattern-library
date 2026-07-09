"""
Discrete Fourier Transform (DFT) from Scratch.

Convert time-domain signal to frequency-domain via DFT.
DFT[k] = Σ x[n] * exp(-2πi*k*n/N).
We plant known frequencies in a signal and verify DFT recovers them.
Also verify Parseval's theorem: sum of squared signal = sum of squared DFT magnitudes / N.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple


def dft(signal: List[float]) -> List[Tuple[float, float]]:
    """
    Compute DFT of a real signal.
    Returns list of (real, imag) tuples for each frequency bin.
    """
    N = len(signal)
    result = []

    for k in range(N):
        real_part = 0.0
        imag_part = 0.0

        for n in range(N):
            angle = -2 * math.pi * k * n / N
            real_part += signal[n] * math.cos(angle)
            imag_part += signal[n] * math.sin(angle)

        result.append((real_part, imag_part))

    return result


def magnitude(complex_num: Tuple[float, float]) -> float:
    """Magnitude of a complex number."""
    real, imag = complex_num
    return math.sqrt(real**2 + imag**2)


if __name__ == "__main__":
    import random

    random.seed(42)

    # Create signal with known frequencies: 5 Hz and 12 Hz
    fs = 100  # Sampling frequency (Hz)
    duration = 2.0  # seconds
    N = int(fs * duration)  # Number of samples

    freq1, freq2 = 5.0, 12.0
    signal = [
        math.sin(2 * math.pi * freq1 * t / fs)
        + 0.5 * math.sin(2 * math.pi * freq2 * t / fs)
        + random.gauss(0, 0.1)
        for t in range(N)
    ]

    # Compute DFT
    dft_result = dft(signal)

    # Find peaks in magnitude spectrum (only positive/Nyquist frequencies)
    magnitudes = [magnitude(c) for c in dft_result]
    nyquist_idx = N // 2

    # Check specific bins for our expected frequencies
    bin_freq1 = int(round(freq1 * N / fs))  # Bin for 5 Hz
    bin_freq2 = int(round(freq2 * N / fs))  # Bin for 12 Hz

    mag_freq1 = magnitudes[bin_freq1] if bin_freq1 < len(magnitudes) else 0
    mag_freq2 = magnitudes[bin_freq2] if bin_freq2 < len(magnitudes) else 0

    # Check: magnitudes at expected frequency bins should be high
    assert mag_freq1 > 20, f"Magnitude at {freq1} Hz (bin {bin_freq1}): {mag_freq1:.1f}"
    assert mag_freq2 > 10, f"Magnitude at {freq2} Hz (bin {bin_freq2}): {mag_freq2:.1f}"

    # Verify Parseval's theorem: sum(x^2) = sum(|X[k]|^2) / N
    signal_energy = sum(s**2 for s in signal)
    dft_energy = sum(magnitude(c) ** 2 for c in dft_result) / N

    parseval_error = abs(signal_energy - dft_energy) / signal_energy

    assert parseval_error < 0.05, (
        f"Parseval violation: signal_energy={signal_energy:.2f}, "
        f"dft_energy={dft_energy:.2f}, error={parseval_error:.2%}"
    )

    print(
        f"Bin {bin_freq1}: {mag_freq1:.1f} ({freq1} Hz) | "
        f"Bin {bin_freq2}: {mag_freq2:.1f} ({freq2} Hz) | "
        f"Parseval error: {parseval_error:.2%} | PASS"
    )
