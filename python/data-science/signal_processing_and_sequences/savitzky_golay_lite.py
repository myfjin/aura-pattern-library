import math
"""
Savitzky-Golay Filter (Local Polynomial Smoothing).

Fit a low-order polynomial (e.g., quadratic) to a rolling window.
Smoother than moving-average and preserves peak heights better than moving-average.
We verify that SG filter preserves peak heights while moving-average attenuates them.
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

def _aura_validate_fit_polynomial_window(poly_order):
    v = []
    if isinstance(poly_order, (int, float)) and poly_order <= 0:
        v.append(f"AURA-E009: poly_order must be > 0, got {poly_order}")
    if v:
        raise AuraInputError(v)

def _aura_validate_moving_average_filter(window_size):
    v = []
    if isinstance(window_size, (int, float)) and window_size <= 0:
        v.append(f"AURA-E009: window_size must be > 0, got {window_size}")
    if v:
        raise AuraInputError(v)

def _aura_validate_savitzky_golay_filter(window_size):
    v = []
    if isinstance(window_size, (int, float)) and window_size <= 0:
        v.append(f"AURA-E009: window_size must be > 0, got {window_size}")
    if v:
        raise AuraInputError(v)

def fit_polynomial_window(
    window: List[float], poly_order: int = 2
) -> Tuple[float, float, float]:
    """
    Fit polynomial y = a + b*x + c*x^2 to a window via least-squares.
    x values are 0, 1, ..., len(window)-1.
    Returns (a, b, c).
    """
    _aura_validate_fit_polynomial_window(poly_order)
    n = len(window)
    x_vals = list(range(n))

    # Design matrix for y = a + b*x + c*x^2
    sum_x = sum(x_vals)
    sum_x2 = sum(x**2 for x in x_vals)
    sum_x3 = sum(x**3 for x in x_vals)
    sum_x4 = sum(x**4 for x in x_vals)
    sum_y = sum(window)
    sum_xy = sum(x_vals[i] * window[i] for i in range(n))
    sum_x2y = sum(x_vals[i] ** 2 * window[i] for i in range(n))

    # Normal equations
    xtx = [
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4],
    ]

    xty = [sum_y, sum_xy, sum_x2y]

    # Solve 3x3 system via Cramer's rule (for simplicity)
    det = (
        xtx[0][0] * (xtx[1][1] * xtx[2][2] - xtx[1][2] * xtx[2][1])
        - xtx[0][1] * (xtx[1][0] * xtx[2][2] - xtx[1][2] * xtx[2][0])
        + xtx[0][2] * (xtx[1][0] * xtx[2][1] - xtx[1][1] * xtx[2][0])
    )

    if abs(det) < 1e-10:
        return 0.0, 0.0, 0.0

    det_a = (
        xty[0] * (xtx[1][1] * xtx[2][2] - xtx[1][2] * xtx[2][1])
        - xtx[0][1] * (xty[1] * xtx[2][2] - xtx[1][2] * xty[2])
        + xtx[0][2] * (xty[1] * xtx[2][1] - xtx[1][1] * xty[2])
    )

    det_b = (
        xtx[0][0] * (xty[1] * xtx[2][2] - xtx[1][2] * xty[2])
        - xty[0] * (xtx[1][0] * xtx[2][2] - xtx[1][2] * xtx[2][0])
        + xtx[0][2] * (xtx[1][0] * xty[2] - xty[1] * xtx[2][0])
    )

    det_c = (
        xtx[0][0] * (xtx[1][1] * xty[2] - xty[1] * xtx[2][1])
        - xtx[0][1] * (xtx[1][0] * xty[2] - xty[1] * xtx[2][0])
        + xty[0] * (xtx[1][0] * xtx[2][1] - xtx[1][1] * xtx[2][0])
    )

    a = det_a / det
    b = det_b / det
    c = det_c / det

    return a, b, c


def savitzky_golay_filter(signal: List[float], window_size: int = 5) -> List[float]:
    """
    Apply Savitzky-Golay filter: fit local polynomial and use center value.
    """
    _aura_validate_savitzky_golay_filter(window_size)
    n = len(signal)
    half_window = window_size // 2
    filtered = []

    for i in range(n):
        left = max(0, i - half_window)
        right = min(n - 1, i + half_window)
        window = signal[left : right + 1]

        # Adjust x values for polynomial fit (center at 0)
        a, b, c = fit_polynomial_window(window)
        center_idx = i - left
        smoothed_value = a + b * center_idx + c * center_idx**2

        filtered.append(smoothed_value)

    return filtered


def moving_average_filter(signal: List[float], window_size: int = 5) -> List[float]:
    """Moving average filter for comparison."""
    _aura_validate_moving_average_filter(window_size)
    n = len(signal)
    half_window = window_size // 2
    filtered = []

    for i in range(n):
        left = max(0, i - half_window)
        right = min(n - 1, i + half_window)
        window = signal[left : right + 1]
        filtered.append(sum(window) / len(window))

    return filtered


if __name__ == "__main__":
    import random
    import math

    random.seed(42)

    # Create a signal with a SMOOTH peak (gaussian, a few samples wide).
    # SG's peak-preservation claim is about smooth band-limited peaks — a
    # local quadratic fits them. A single-sample spike is statistically an
    # OUTLIER (that's hampel_filter_outliers.py's job to REMOVE, not SG's
    # job to preserve) and would test the claim on its weakest signal class.
    n = 50
    peak_idx, height, width = 25, 8.0, 2.0
    clean = [1.0 + 0.01 * t + height * math.exp(-((t - peak_idx) ** 2) / (2 * width ** 2))
             for t in range(n)]
    signal = [s + random.gauss(0, 0.3) for s in clean]

    # Apply filters
    sg_filtered = savitzky_golay_filter(signal, window_size=5)
    ma_filtered = moving_average_filter(signal, window_size=5)

    # Check peak preservation against the NOISELESS truth at the peak center
    true_peak = clean[peak_idx]
    sg_peak = sg_filtered[peak_idx]
    ma_peak = ma_filtered[peak_idx]

    sg_peak_error = abs(sg_peak - true_peak)
    ma_peak_error = abs(ma_peak - true_peak)

    # Real preservation, not just "slower destruction": SG must hold the
    # smooth peak to within ~11% of its height, MA must visibly clip it,
    # and SG must clearly beat MA — all three, with margins.
    assert sg_peak_error < 0.9, f"SG should preserve a smooth peak: error {sg_peak_error:.2f}"
    assert ma_peak_error > 1.1, f"MA should visibly clip the peak: error {ma_peak_error:.2f}"
    assert sg_peak_error < 0.7 * ma_peak_error, (
        f"SG did not clearly beat MA: "
        f"SG error={sg_peak_error:.2f}, MA error={ma_peak_error:.2f}"
    )

    print(
        f"True peak: {true_peak:.2f} | SG filtered peak: {sg_peak:.2f} (error={sg_peak_error:.2f}) | "
        f"MA filtered peak: {ma_peak:.2f} (error={ma_peak_error:.2f}) | "
        f"SG improvement: {(1 - sg_peak_error/ma_peak_error)*100:.1f}% | PASS"
    )
