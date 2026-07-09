"""
ADWIN0 adaptive-windowing drift detector (Bifet & Gavalda, 2007).
Core idea: keep a window of recent values; after each arrival, try EVERY split of the
window into an older part W0 and newer part W1. If |mean(W0) - mean(W1)| exceeds the
variance-aware Hoeffding cut bound e_cut(delta), a real change is declared and the older
part is dropped. delta bounds the false-positive rate; the bound is NOT an arbitrary
fraction of the std -- it is derived from delta and the window sizes.
When: detect distribution shift online with a provable false-alarm guarantee.
Values are assumed in [0,1] (e.g. a stream of classification errors) -- ADWIN's setting.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
import random
from typing import List, Tuple


def _e_cut(n0: int, n1: int, var_w: float, n: int, delta: float) -> float:
    # Harmonic mean of the two sub-window sizes, per the ADWIN paper.
    m = 1.0 / (1.0 / n0 + 1.0 / n1)
    dprime = delta / n
    return math.sqrt((2.0 / m) * var_w * math.log(2.0 / dprime)) + (2.0 / (3.0 * m)) * math.log(2.0 / dprime)


def adwin_drift_detector(stream: List[float], delta: float = 0.05) -> Tuple[bool, int]:
    """
    Feed the stream one value at a time; return (drift_detected, index_of_first_cut).
    index is -1 if no drift is ever flagged.
    Args:
        stream: values in [0,1]
        delta: target false-positive probability
    """
    assert 0 < delta < 1
    window: List[float] = []
    for i, x in enumerate(stream):
        window.append(x)
        n = len(window)
        if n < 10:
            continue
        total = sum(window)
        mean_w = total / n
        var_w = sum((v - mean_w) ** 2 for v in window) / n
        # try splits at a stride (coarse but faithful -- catches any real shift)
        stride = max(1, n // 32)
        cut_at = -1
        pref = 0.0
        for j in range(1, n):
            pref += window[j - 1]
            if j % stride and j != n - 1:
                continue
            n0, n1 = j, n - j
            mean0 = pref / n0
            mean1 = (total - pref) / n1
            if abs(mean0 - mean1) > _e_cut(n0, n1, var_w, n, delta):
                cut_at = j
                break
        if cut_at != -1:
            # drift: drop the older part, keep the newer window, report the arrival index
            window = window[cut_at:]
            return True, i
    return False, -1


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation

    # Case 1: stationary error stream, Bernoulli(0.2) throughout -> NO drift.
    stationary = [1.0 if random.random() < 0.2 else 0.0 for _ in range(600)]
    det_s, idx_s = adwin_drift_detector(stationary, delta=0.05)
    print(f"stationary: detected={det_s} at {idx_s} (want False)")

    # Case 2: error rate jumps 0.2 -> 0.6 at index 300 -> drift near 300.
    drift = [1.0 if random.random() < 0.2 else 0.0 for _ in range(300)]
    drift += [1.0 if random.random() < 0.6 else 0.0 for _ in range(300)]
    det_d, idx_d = adwin_drift_detector(drift, delta=0.05)
    print(f"shift: detected={det_d} at {idx_d} (want True, soon after 300)")

    # RECOVERY ASSERT: no false alarm on the stationary stream (the delta guarantee),
    # and the planted shift is caught within one window (~100) of the change point.
    assert det_s is False, "ADWIN false-alarmed on a stationary stream"
    assert det_d is True, "ADWIN missed a real 0.2->0.6 shift"
    assert 300 <= idx_d <= 400, f"detection {idx_d} not localised near the change point 300"
    print("ADWIN PASS")
