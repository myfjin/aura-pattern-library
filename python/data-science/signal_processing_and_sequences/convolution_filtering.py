"""
Convolution and Filtering.

Convolve a signal with a kernel via discrete convolution: y[n] = Σ x[k] * h[n-k].
Demonstrate smoothing (moving average kernel) and edge detection (difference kernel).
Verify that smoothing reduces noise and difference kernel detects transitions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List


def convolve(signal: List[float], kernel: List[float]) -> List[float]:
    """
    Discrete convolution (full mode): output length = len(signal) + len(kernel) - 1.
    Pad signal with zeros as needed.
    """
    n = len(signal)
    m = len(kernel)
    output = [0.0] * (n + m - 1)

    for i in range(n + m - 1):
        for j in range(m):
            signal_idx = i - j
            if 0 <= signal_idx < n:
                output[i] += signal[signal_idx] * kernel[j]

    return output


def moving_average_kernel(window_size: int) -> List[float]:
    """Moving average kernel."""
    return [1.0 / window_size] * window_size


def difference_kernel() -> List[float]:
    """Difference (edge detection) kernel: [1, -1]."""
    return [1.0, -1.0]


def mse(x: List[float], y: List[float]) -> float:
    """Mean squared error."""
    min_len = min(len(x), len(y))
    return sum((x[i] - y[i]) ** 2 for i in range(min_len)) / min_len


if __name__ == "__main__":
    import random

    random.seed(42)

    # Create a smooth signal with noise
    n = 50
    true_signal = [5 * (i / 10) for i in range(n)]  # Linear trend
    noisy_signal = [true_signal[i] + random.gauss(0, 2) for i in range(n)]

    # Smooth via moving average convolution
    ma_kernel = moving_average_kernel(5)
    smoothed = convolve(noisy_signal, ma_kernel)
    smoothed = smoothed[:n]  # Trim to original length

    # MSE: smoothed should be closer to true signal than noisy
    mse_noisy = mse(true_signal, noisy_signal)
    mse_smoothed = mse(true_signal, smoothed)

    assert mse_smoothed < mse_noisy, (
        f"Smoothing did not reduce MSE: "
        f"noisy={mse_noisy:.2f}, smoothed={mse_smoothed:.2f}"
    )

    # Edge detection: create a step signal and convolve with difference kernel
    step_signal = [1.0] * 25 + [5.0] * 25
    diff_kernel = difference_kernel()
    edges = convolve(step_signal, diff_kernel)

    # The maximum edge should occur at the step transition (index ~25)
    max_edge_idx = edges.index(max(edges))
    edge_is_near_transition = 20 <= max_edge_idx <= 30

    assert edge_is_near_transition, (
        f"Edge detection did not find transition at index 25, "
        f"found max at {max_edge_idx}"
    )

    print(
        f"Noisy MSE: {mse_noisy:.2f} | Smoothed MSE: {mse_smoothed:.2f} | "
        f"MSE reduction: {(1 - mse_smoothed / mse_noisy) * 100:.1f}% | "
        f"Edge at index: {max_edge_idx} (expected ~25) | PASS"
    )
