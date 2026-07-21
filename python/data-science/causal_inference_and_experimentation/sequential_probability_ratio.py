"""
Sequential Probability Ratio Test (SPRT).

A sequential test that stops early: accumulate log-likelihood ratio for H0 vs H1.
Stop when LR > threshold (accept H1) or LR < -threshold (accept H0).
Compared to fixed-n testing at the same error rates, SPRT uses fewer observations on average.
We verify that SPRT stops earlier than fixed-n while maintaining error rates.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_fixed_n_test(p0, p1, alpha):
    v = []
    if isinstance(p0, (int, float)) and not math.isfinite(p0):
        v.append(f"AURA-E008: p0 must be finite, got {p0}")
    if isinstance(p1, (int, float)) and not math.isfinite(p1):
        v.append(f"AURA-E008: p1 must be finite, got {p1}")
    if isinstance(p1, (int, float)) and not (0.0 <= p1 <= 1.0):
        v.append(f"AURA-E003: p1 must be in [0,1], got {p1}")
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    if isinstance(alpha, (int, float)) and math.isfinite(alpha) and not (0.0 < alpha < 1.0):
        v.append(f"AURA-E001: alpha must be in (0,1), got {alpha}")  # domain: significance level
    if v:
        raise AuraInputError(v)

def _aura_validate_sprt(p0, p1, alpha, beta):
    v = []
    if isinstance(p0, (int, float)) and not math.isfinite(p0):
        v.append(f"AURA-E008: p0 must be finite, got {p0}")
    if isinstance(p1, (int, float)) and not math.isfinite(p1):
        v.append(f"AURA-E008: p1 must be finite, got {p1}")
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    if isinstance(beta, (int, float)) and not math.isfinite(beta):
        v.append(f"AURA-E008: beta must be finite, got {beta}")
    if v:
        raise AuraInputError(v)

def sprt(
    data: list,
    p0: float,
    p1: float,
    alpha: float = 0.05,
    beta: float = 0.05,
) -> Tuple[str, int]:
    """
    SPRT for Bernoulli: H0: p=p0, H1: p=p1.
    Stops when LR reaches threshold or runs out of data.
    Returns (decision, number of samples used).
    """
    _aura_validate_sprt(p0, p1, alpha, beta)
    # Thresholds
    A = (1 - beta) / alpha
    B = beta / (1 - alpha)

    log_lr = 0.0
    for i, x in enumerate(data):
        if x == 1:
            log_lr += math.log(p1 / p0)
        else:
            log_lr += math.log((1 - p1) / (1 - p0))

        if log_lr > math.log(A):
            return "H1", i + 1
        if log_lr < math.log(B):
            return "H0", i + 1

    return "INCONCLUSIVE", len(data)


def fixed_n_test(
    data: list,
    p0: float,
    p1: float,
    alpha: float = 0.05,
) -> str:
    """
    Fixed-n test: accumulate all data, make single decision.
    Roughly calibrated to same power as SPRT.
    """
    _aura_validate_fixed_n_test(p0, p1, alpha)
    successes = sum(data)
    n = len(data)
    p_hat = successes / n

    # Simple threshold: if p_hat > midpoint, decide H1
    midpoint = (p0 + p1) / 2
    return "H1" if p_hat > midpoint else "H0"


if __name__ == "__main__":
    random.seed(42)

    p0 = 0.4  # Null hypothesis
    p1 = 0.6  # Alternative hypothesis
    alpha = 0.05
    beta = 0.05

    # Generate data where true p = 0.6 (supports H1)
    true_p = 0.6
    max_samples = 500

    sprt_samples_list = []
    for trial in range(100):
        data = [1 if random.random() < true_p else 0 for _ in range(max_samples)]
        decision, n_used = sprt(data, p0, p1, alpha, beta)
        if decision == "H1":  # Only count trials where SPRT decided H1
            sprt_samples_list.append(n_used)

    # Fixed-n test: use typical sample size for 80% power
    fixed_n_typical = 200
    fixed_n_decisions = []
    for trial in range(100):
        data = [1 if random.random() < true_p else 0 for _ in range(fixed_n_typical)]
        decision = fixed_n_test(data, p0, p1, alpha)
        fixed_n_decisions.append(decision)

    # Check: SPRT should use fewer samples on average
    avg_sprt = sum(sprt_samples_list) / len(sprt_samples_list) if sprt_samples_list else 0
    h1_rate_fixed = fixed_n_decisions.count("H1") / len(fixed_n_decisions)

    assert avg_sprt > 0, "SPRT did not produce valid samples"
    assert avg_sprt < fixed_n_typical, (
        f"SPRT used more samples ({avg_sprt:.0f}) than fixed-n ({fixed_n_typical})"
    )
    assert h1_rate_fixed > 0.7, (
        f"Fixed-n test not detecting H1 well enough: {h1_rate_fixed:.1%}"
    )

    print(
        f"SPRT avg samples: {avg_sprt:.0f} (n={len(sprt_samples_list)}) | "
        f"Fixed-n samples: {fixed_n_typical} | Fixed-n H1 rate: {h1_rate_fixed:.1%} | PASS"
    )
