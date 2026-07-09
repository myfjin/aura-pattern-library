"""
KSWIN (Kolmogorov-Smirnov Windowing) drift detector using KS test on sliding windows.
Core idea: maintain two windows; apply KS test to detect distribution shift.
When: detect concept drift via statistical test on sliding window with low false-alarm rate.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
import math
from typing import List

def kswin_drift(stream: List[float], window_size: int = 100, alpha: float = 0.05) -> bool:
    """
    KSWIN drift detector: KS test on two sliding windows.
    Args:
        stream: input sequence
        window_size: size of each window for KS test
        alpha: significance level
    Returns:
        True if drift detected (KS test rejects H0 of same distribution).
    """
    random.seed(42)
    assert window_size > 0 and 0 < alpha < 1

    if len(stream) < 2 * window_size:
        return False

    # Plant shift: first window from one distribution, second from another
    window1 = sorted(stream[:window_size])
    window2 = sorted(stream[-window_size:])

    # KS statistic: max absolute difference in empirical CDFs
    def ks_statistic(w1: List[float], w2: List[float]) -> float:
        n, m = len(w1), len(w2)
        i = j = 0
        d_max = 0.0
        while i < n and j < m:
            d = abs(i / n - j / m)
            d_max = max(d_max, d)
            if w1[i] <= w2[j]:
                i += 1
            else:
                j += 1
        d_max = max(d_max, abs((n - i) / n))  # Remaining elements
        return d_max

    ks_stat = ks_statistic(window1, window2)

    # Critical value (approximate for Kolmogorov distribution)
    n = len(window1)
    critical_value = math.sqrt(-0.5 * math.log(alpha / 2) / n)

    detected = ks_stat > critical_value

    # RECOVERY ASSERT: detect planted shift, stable on stationary
    # Compute true means of windows
    mean1 = sum(window1) / len(window1)
    mean2 = sum(window2) / len(window2)
    true_shift = abs(mean2 - mean1)

    if true_shift > 2.0:
        assert detected, f"KSWIN failed to detect shift of {true_shift:.4f}"
    else:
        assert not detected, f"KSWIN false positive on shift of {true_shift:.4f}"

    return detected


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation
    # Stationary
    stationary = [random.gauss(50, 5) for _ in range(300)]
    result1 = kswin_drift(stationary, window_size=100, alpha=0.05)
    print(f"KSWIN on stationary: {result1} (should be False)")

    # Shifted
    shifted = [random.gauss(50, 5) for _ in range(150)] + [random.gauss(65, 5) for _ in range(150)]
    result2 = kswin_drift(shifted, window_size=100, alpha=0.05)
    print(f"KSWIN on shifted: {result2} (should be True)")
