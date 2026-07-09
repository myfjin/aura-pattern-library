"""
Exponentially-decayed streaming mean/variance (Welford-style, decay-weighted).
Core idea: maintain a decay-weighted running mean and M2 so recent samples dominate. On a
stream whose level shifts, the decayed mean tracks the RECENT level while the plain global
mean lags halfway between old and new. The demo plants a clean level shift and asserts the
decayed mean recovers the post-shift level -- and beats the global mean at it.
When: track mean/variance on non-stationary streams (concept drift, regime change).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
from typing import Tuple


def welford_decayed_moments(stream: list, decay: float = 0.98) -> Tuple[float, float]:
    """
    Decay-weighted streaming mean and variance.
    Args:
        stream: input sequence
        decay: 0<decay<1; weight of a sample t steps in the past is decay**t
    Returns:
        (decayed_mean, decayed_variance)
    """
    assert 0 < decay < 1.0
    mean = 0.0
    M2 = 0.0
    weight_sum = 0.0
    for x in stream:
        # age all prior mass by `decay`, then add this sample with weight 1
        weight_sum = weight_sum * decay + 1.0
        delta = x - mean
        mean += delta / weight_sum
        delta2 = x - mean
        M2 = M2 * decay + delta * delta2
    variance = M2 / weight_sum
    return mean, variance


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation
    # Plant a clean level shift: first half ~N(0,1), second half ~N(10,1).
    first = [random.gauss(0.0, 1.0) for _ in range(500)]
    second = [random.gauss(10.0, 1.0) for _ in range(500)]
    stream = first + second

    decayed_mean, decayed_var = welford_decayed_moments(stream, decay=0.95)
    global_mean = sum(stream) / len(stream)          # ~5 (lags between regimes)
    recent_level = sum(second) / len(second)         # ~10 (the current truth)
    print(f"decayed_mean={decayed_mean:.3f}  global_mean={global_mean:.3f}  recent={recent_level:.3f}")

    # RECOVERY ASSERT 1: the decayed mean recovers the CURRENT level (~10) closely.
    assert abs(decayed_mean - recent_level) < 1.0, \
        f"decayed mean {decayed_mean:.3f} failed to track recent level {recent_level:.3f}"

    # RECOVERY ASSERT 2: it beats the plain global mean at tracking the current level by
    # a wide margin (the reason to decay at all). global_mean sits ~5 units off.
    assert abs(decayed_mean - recent_level) < abs(global_mean - recent_level) - 3.0, \
        "decayed mean must beat the global mean at tracking the current regime"

    # RECOVERY ASSERT 3: decayed variance reflects the recent regime (~1), not the huge
    # cross-regime spread (~25 for the pooled data).
    assert decayed_var < 4.0, f"decayed variance {decayed_var:.3f} not tracking recent regime"
    print("Welford decayed moments PASS")
