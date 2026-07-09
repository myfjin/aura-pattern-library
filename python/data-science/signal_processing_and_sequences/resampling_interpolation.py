"""
Resampling and Interpolation.

Upsample or downsample a time series via interpolation.
Demonstrate linear interpolation and nearest-neighbor.
On smooth signals, linear should outperform nearest-neighbor (lower RMSE).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List


def linear_interpolation(signal: List[float], factor: int) -> List[float]:
    """
    Upsample signal by inserting `factor-1` interpolated points between each pair.
    Uses linear interpolation.
    """
    n = len(signal)
    upsampled = []

    for i in range(n - 1):
        upsampled.append(signal[i])
        for j in range(1, factor):
            t = j / factor  # Interpolation parameter [0, 1)
            interpolated = (1 - t) * signal[i] + t * signal[i + 1]
            upsampled.append(interpolated)

    upsampled.append(signal[-1])  # Add last point
    return upsampled


def nearest_neighbor_interpolation(signal: List[float], factor: int) -> List[float]:
    """
    Upsample signal by repeating each sample `factor` times (or nearest neighbor).
    """
    upsampled = []
    for i in range(len(signal) - 1):
        upsampled.append(signal[i])
        for _ in range(factor - 1):
            upsampled.append(signal[i])  # Repeat

    upsampled.append(signal[-1])
    return upsampled


def downsample(signal: List[float], factor: int) -> List[float]:
    """Downsample: take every `factor`-th sample."""
    return signal[::factor]


def rmse(x: List[float], y: List[float]) -> float:
    """RMSE between x and y (truncate to common length)."""
    min_len = min(len(x), len(y))
    return (sum((x[i] - y[i]) ** 2 for i in range(min_len)) / min_len) ** 0.5


if __name__ == "__main__":
    import random
    import math

    random.seed(42)

    # Create a smooth signal (sine wave)
    n = 50
    signal = [
        math.sin(2 * math.pi * t / 20) + random.gauss(0, 0.05) for t in range(n)
    ]

    upsample_factor = 3

    # Upsample with both methods
    linear_up = linear_interpolation(signal, upsample_factor)
    nearest_up = nearest_neighbor_interpolation(signal, upsample_factor)

    # Create true higher-resolution signal for comparison
    true_upsampled = [
        math.sin(2 * math.pi * t / (20 * upsample_factor))
        for t in range(len(linear_up))
    ]

    # Compute RMSE
    rmse_linear = rmse(linear_up, true_upsampled)
    rmse_nearest = rmse(nearest_up, true_upsampled)

    assert rmse_linear < rmse_nearest, (
        f"Linear interpolation did not outperform nearest-neighbor: "
        f"linear={rmse_linear:.4f}, nearest={rmse_nearest:.4f}"
    )

    # Downsample and check length
    downsampled = downsample(signal, upsample_factor)
    expected_length = (n - 1) // upsample_factor + 1

    assert len(downsampled) == expected_length, (
        f"Downsample length mismatch: {len(downsampled)} vs {expected_length}"
    )

    print(
        f"Original length: {n} | Upsampled: {len(linear_up)} | "
        f"Linear RMSE: {rmse_linear:.4f} | Nearest RMSE: {rmse_nearest:.4f} | "
        f"Improvement: {(1 - rmse_linear/rmse_nearest)*100:.1f}% | PASS"
    )
