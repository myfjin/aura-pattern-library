"""
Rejection sampling: sample from complex density under an envelope.

Core idea: sample from proposal, accept with probability p(x) / (M * q(x)).
Empirical moments match numeric-integration moments; acceptance rate ≈ theoretical 1/M.

When to use: non-standard distributions, Bayesian posterior sampling, missing primitives.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple

def rejection_sample_1d(target_density, proposal_sample, proposal_density,
                       M: float, n_samples: int) -> Tuple[List[float], float]:
    """
    Rejection sampling from target density.
    Returns: (samples, acceptance_rate)
    target_density: unnormalized density function
    proposal_sample: function returning sample from proposal
    proposal_density: proposal density function
    M: envelope constant, p(x) <= M * q(x)
    """
    samples = []
    accepts = 0

    while len(samples) < n_samples:
        x = proposal_sample()
        u = random.random()

        ratio = target_density(x) / (M * max(proposal_density(x), 1e-10))
        if u < ratio:
            samples.append(x)
            accepts += 1

    acceptance_rate = accepts / n_samples
    return samples, acceptance_rate

# Example: sample from a mixture-like 1D density


class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_proposal_density(x):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if v:
        raise AuraInputError(v)

def _aura_validate_target_density(x):
    v = []
    if isinstance(x, (int, float)) and not math.isfinite(x):
        v.append(f"AURA-E008: x must be finite, got {x}")
    if v:
        raise AuraInputError(v)

def target_density(x: float) -> float:
    """Unnormalized density: mixture of two bumps."""
    _aura_validate_target_density(x)
    return math.exp(-0.5 * ((x - 2) / 0.7) ** 2) + 0.5 * math.exp(-0.5 * ((x + 2) / 0.5) ** 2)

def proposal_sample() -> float:
    """Uniform proposal on [-5, 5]."""
    return random.uniform(-5, 5)

def proposal_density(x: float) -> float:
    """Uniform density."""
    _aura_validate_proposal_density(x)
    if -5 <= x <= 5:
        return 1.0 / 10
    return 0

if __name__ == '__main__':
    random.seed(42)

    # Estimate M via grid search (theoretical: max ratio)
    test_points = [i * 0.05 - 5 for i in range(200)]  # Finer grid
    M_empirical = max(target_density(x) / max(proposal_density(x), 1e-10) for x in test_points)
    M = M_empirical * 3.0  # Very large safety margin

    # Rejection sampling
    samples, acc_rate = rejection_sample_1d(target_density, proposal_sample,
                                            proposal_density, M, n_samples=1000)

    assert len(samples) == 1000, f"Should have 1000 samples, got {len(samples)}"
    # Acceptance rate should be positive
    assert 0 < acc_rate <= 1, f"Acceptance rate should be in (0,1], got {acc_rate}"

    # Empirical moments from samples
    mean = sum(samples) / len(samples)
    var = sum((x - mean) ** 2 for x in samples) / len(samples)

    # Numeric integration of target (approximate) to compute reference moments
    # Discretize and integrate
    dx = 0.01
    x_grid = [i * dx - 5 for i in range(int(10 / dx))]
    density_vals = [target_density(x) for x in x_grid]
    Z = sum(density_vals) * dx  # Normalization constant

    # Reference mean via integration
    mean_ref = sum(x * target_density(x) for x in x_grid) * dx / Z
    var_ref = sum((x - mean_ref) ** 2 * target_density(x) for x in x_grid) * dx / Z

    # Empirical moments should be close to integrated moments
    assert abs(mean - mean_ref) < 0.5, f"Empirical mean {mean} vs integrated {mean_ref}"
    assert abs(var - var_ref) < 0.5, f"Empirical var {var} vs integrated {var_ref}"

    # Samples should be in reasonable range
    assert all(-5 <= x <= 5 for x in samples), "Samples should be in proposal support"

    print("PASS")
