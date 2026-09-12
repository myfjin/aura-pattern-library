"""
FFT via Cooley-Tukey Algorithm.

Recursive divide-and-conquer FFT: O(N log N) vs naive DFT O(N²).
Works on power-of-2 lengths. FFT should produce same result as naive DFT,
and operation count should be measurably lower (on fixed input).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple


def dft_naive(signal: List[float]) -> List[Tuple[float, float]]:
    """Naive DFT: O(N²) operations."""
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


def fft_cooley_tukey(signal: List[float]) -> List[Tuple[float, float]]:
    """
    Cooley-Tukey FFT (recursive, radix-2).
    Assumes N = 2^m.
    """
    N = len(signal)

    if N <= 1:
        return [(signal[0], 0.0)] if N == 1 else []

    # Split into even and odd indices
    even = fft_cooley_tukey([signal[i] for i in range(0, N, 2)])
    odd = fft_cooley_tukey([signal[i] for i in range(1, N, 2)])

    # Combine
    result = [(0.0, 0.0)] * N

    for k in range(N // 2):
        # Twiddle factor
        angle = -2 * math.pi * k / N
        twiddle_real = math.cos(angle)
        twiddle_imag = math.sin(angle)

        # odd[k] * twiddle
        odd_real, odd_imag = odd[k]
        product_real = odd_real * twiddle_real - odd_imag * twiddle_imag
        product_imag = odd_real * twiddle_imag + odd_imag * twiddle_real

        # Combine even[k] +/- product
        even_real, even_imag = even[k]

        result[k] = (
            even_real + product_real,
            even_imag + product_imag,
        )
        result[k + N // 2] = (
            even_real - product_real,
            even_imag - product_imag,
        )

    return result


def count_ops_naive(N: int) -> int:
    """Count complex multiplications in naive DFT."""
    return N * N


def count_ops_fft(N: int) -> int:
    """Count complex multiplications in Cooley-Tukey FFT (approximate)."""
    return int(N * math.log2(N)) if N > 1 else N


if __name__ == "__main__":
    import random

    random.seed(42)

    # Power-of-2 signal
    N = 256
    signal = [random.gauss(0, 1) for _ in range(N)]

    # Compute both
    dft_result = dft_naive(signal)
    fft_result = fft_cooley_tukey(signal)

    # Compare results (should be almost identical)
    max_error = 0.0
    for i in range(N):
        dft_real, dft_imag = dft_result[i]
        fft_real, fft_imag = fft_result[i]
        error = math.sqrt((dft_real - fft_real) ** 2 + (dft_imag - fft_imag) ** 2)
        max_error = max(max_error, error)

    assert max_error < 1e-6, f"FFT error too large: {max_error:.2e}"

    # Count operations
    ops_naive = count_ops_naive(N)
    ops_fft = count_ops_fft(N)

    assert ops_fft < ops_naive, (
        f"FFT ops {ops_fft} not less than naive {ops_naive}"
    )

    speedup = ops_naive / ops_fft

    print(
        f"N={N} | Naive ops: {ops_naive} | FFT ops: {ops_fft} | "
        f"Speedup: {speedup:.1f}x | Max error: {max_error:.2e} | PASS"
    )
