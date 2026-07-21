"""
Metropolis-Hastings MCMC Sampling.

Samples from a target distribution using a random-walk proposal.
Accepts/rejects proposals based on the Metropolis-Hastings ratio.
Use when you need posterior samples from a complex distribution.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Callable, Tuple


def metropolis_hastings(
    target_pdf: Callable[[float], float],
    proposal_sd: float,
    n_samples: int,
    initial_x: float = 0.0,
) -> Tuple[List[float], float]:
    """
    Metropolis-Hastings sampler.

    Args:
        target_pdf: unnormalized target density function
        proposal_sd: standard deviation of random-walk proposal
        n_samples: number of iterations
        initial_x: starting value

    Returns:
        (samples, acceptance_rate)
    """
    samples = []
    x = initial_x
    n_accept = 0

    for _ in range(n_samples):
        # Propose
        x_prop = x + random.gauss(0, proposal_sd)

        # Metropolis-Hastings ratio
        log_ratio = math.log(target_pdf(x_prop)) - math.log(target_pdf(x))
        log_ratio = min(0.0, log_ratio)  # Clamp to avoid overflow

        # Accept/reject
        if math.log(random.random()) < log_ratio:
            x = x_prop
            n_accept += 1

        samples.append(x)

    acceptance_rate = n_accept / n_samples
    return samples, acceptance_rate




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_mixture_target(x):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if v:
        raise AuraInputError(v)

def mixture_target(x: float) -> float:
    """
    Bimodal target: 0.5 * N(x; -2, 1) + 0.5 * N(x; 2, 1).
    """
    _aura_validate_mixture_target(x)
    def gauss(x, mu, sd):
        return math.exp(-0.5 * ((x - mu) / sd) ** 2)

    return 0.5 * gauss(x, -2.0, 1.0) + 0.5 * gauss(x, 2.0, 1.0)


if __name__ == "__main__":
    random.seed(42)

    # Sample from bimodal mixture
    n_burn = 1000
    n_samples = 5000

    samples, acc_rate = metropolis_hastings(mixture_target, proposal_sd=2.5, n_samples=n_burn + n_samples, initial_x=0.0)

    # Discard burn-in
    samples_keep = samples[n_burn:]

    # Compute statistics
    mean_samples = sum(samples_keep) / len(samples_keep)
    var_samples = sum((x - mean_samples) ** 2 for x in samples_keep) / len(samples_keep)
    sd_samples = math.sqrt(var_samples)

    # Target has modes at ±2, variance ~1 each, mixture variance ~5 overall
    # Expected mean ≈ 0 (symmetric), expected variance ≈ 5
    expected_mean = 0.0
    expected_var = 5.0

    assert abs(mean_samples - expected_mean) < 0.5, f"Mean {mean_samples} far from {expected_mean}"
    assert abs(var_samples - expected_var) < 1.0, f"Variance {var_samples} far from {expected_var}"
    assert 0.2 < acc_rate < 0.7, f"Acceptance rate {acc_rate} outside reasonable band"

    print(f"metropolis_hastings_mcmc.py: mean={mean_samples:.3f}, sd={sd_samples:.3f}, acc_rate={acc_rate:.3f} PASS")
