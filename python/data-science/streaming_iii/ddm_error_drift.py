"""
DDM -- Drift Detection Method (Gama, Medas, Castillo, Rodrigues 2004).
Core idea: as a classifier's binary error stream arrives, track p_i (running error rate)
and s_i = sqrt(p_i(1-p_i)/i). Keep the minimum of (p_i + s_i) ever seen (p_min, s_min):
that marks the best the model has been. Signal WARNING at p_i+s_i >= p_min+2*s_min and
DRIFT at p_i+s_i >= p_min+3*s_min -- a statistical control chart, not "later > earlier".
When: detect that a classifier's error rate has significantly worsened, online.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
import math
from typing import List, Tuple


def ddm_error_drift(error_stream: List[int], min_samples: int = 30) -> Tuple[bool, int]:
    """
    Returns (drift_detected, index_of_drift). index is -1 if never.
    Args:
        error_stream: 0/1 errors (1 = misclassification)
        min_samples: warm-up before the chart is armed
    """
    assert min_samples > 0
    n_err = 0
    p_min = float("inf")
    s_min = float("inf")
    for i, e in enumerate(error_stream):
        n_err += e
        n = i + 1
        p = n_err / n
        s = math.sqrt(p * (1 - p) / n)
        if n < min_samples:
            continue
        if p + s < p_min + s_min:          # new best-so-far => update the control baseline
            p_min, s_min = p, s
        if p + s >= p_min + 3 * s_min:     # DDM drift level
            return True, i
    return False, -1


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation

    # Stationary: Bernoulli(0.15) error throughout -> the chart must NOT fire.
    stationary = [1 if random.random() < 0.15 else 0 for _ in range(600)]
    det_s, idx_s = ddm_error_drift(stationary, min_samples=30)
    print(f"stationary: detected={det_s} at {idx_s} (want False)")

    # Drift: error jumps 0.10 -> 0.40 at index 400 -> drift caught soon after.
    drift = [1 if random.random() < 0.10 else 0 for _ in range(400)]
    drift += [1 if random.random() < 0.40 else 0 for _ in range(300)]
    det_d, idx_d = ddm_error_drift(drift, min_samples=30)
    print(f"drift: detected={det_d} at {idx_d} (want True, after 400)")

    # RECOVERY ASSERT: no false alarm on a stationary error stream, and the real error
    # increase is flagged strictly AFTER the change point (the 3*sigma control level did
    # the work -- the old code's dead control_limit loop is now the live mechanism).
    assert det_s is False, "DDM false-alarmed on stationary errors"
    assert det_d is True and idx_d >= 400, f"DDM missed/mistimed the drift (idx={idx_d})"
    print("DDM PASS")
