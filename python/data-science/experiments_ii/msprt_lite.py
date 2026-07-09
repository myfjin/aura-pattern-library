"""mSPRT (mixture Sequential Probability Ratio Test): an always-valid test.

Under continuous peeking a fixed-α test inflates type-I badly. The mixture SPRT (Robbins)
mixes the likelihood ratio over a normal prior on the effect, giving a statistic whose
type-I error is controlled UNIFORMLY over all sample sizes (Ville's inequality): you may
peek after every observation and reject the first time Λ_n ≥ 1/α.
Core claim: naive peeking inflates type-I; mSPRT holds type-I under peeking, with power.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import Callable

def msprt_reject(diff_gen: Callable[[], float], alpha: float, tau2: float, v: float, max_n: int) -> bool:
    """Sequential test on a stream of paired differences d ~ N(delta, v).

    Mixture LR with prior N(0, tau2):
        Λ_n = sqrt(v/(v+n·tau2)) · exp( tau2·S_n² / (2·v·(v+n·tau2)) ),   S_n = Σ dᵢ.
    Reject the first time Λ_n ≥ 1/alpha (valid at every peek).
    """
    s = 0.0
    for n in range(1, max_n + 1):
        s += diff_gen()
        lam = math.sqrt(v / (v + n * tau2)) * math.exp(tau2 * s * s / (2 * v * (v + n * tau2)))
        if lam >= 1.0 / alpha:
            return True
    return False

def naive_peek_reject(diff_gen: Callable[[], float], alpha: float, v: float, max_n: int) -> bool:
    """Fixed-alpha z-test peeked after every observation (invalid)."""
    s = 0.0
    for n in range(1, max_n + 1):
        s += diff_gen()
        if n >= 2:
            z = s / math.sqrt(v * n)
            p = math.erfc(abs(z) / math.sqrt(2))
            if p < alpha:
                return True
    return False

if __name__ == "__main__":
    import random

    alpha = 0.05
    sigma2 = 1.0
    v = 2 * sigma2   # variance of a paired difference of two N(·, sigma2) streams
    tau2 = 1.0
    max_n = 200
    reps = 1000

    # Type-I under the NULL (delta = 0), peeking every step.
    random.seed(42)
    msprt_typeI = sum(msprt_reject(lambda: random.gauss(0.0, math.sqrt(v)), alpha, tau2, v, max_n)
                      for _ in range(reps)) / reps
    random.seed(42)
    naive_typeI = sum(naive_peek_reject(lambda: random.gauss(0.0, math.sqrt(v)), alpha, v, max_n)
                      for _ in range(reps)) / reps

    # Power under a real effect (delta = 0.4).
    random.seed(7)
    msprt_power = sum(msprt_reject(lambda: random.gauss(0.4, math.sqrt(v)), alpha, tau2, v, max_n)
                      for _ in range(reps)) / reps

    # Defining property: mSPRT controls type-I under peeking; naive peeking blows it up;
    # and mSPRT still has power. Measured: mSPRT type-I≈0.032, naive≈0.41, power≈0.87.
    assert msprt_typeI <= 0.06, f"mSPRT type-I {msprt_typeI} should stay ≤ α under peeking"
    assert naive_typeI > 0.20, f"Naive peeking type-I {naive_typeI} should be badly inflated"
    assert msprt_power > 0.5, f"mSPRT power {msprt_power} should detect a real effect"

    print("PASS")
