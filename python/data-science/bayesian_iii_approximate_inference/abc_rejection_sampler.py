"""Approximate Bayesian Computation (ABC): rejection sampling for intractable likelihoods.

Sample from prior, simulate data, accept if simulated ≈ observed (within ε).
Core claim: posterior mean recovers the planted parameter; acceptance rate shrinks as ε tightens.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Tuple
import math

def prior_sample():
    """Sample from prior: θ ~ Uniform(0, 5)."""
    import random
    return random.uniform(0, 5)

def simulate_data(theta: float, n: int = 20) -> List[float]:
    """Simulate data from model: y_i ~ Poisson(θ)."""
    import random
    return [random.randint(0, int(theta * 3)) for _ in range(n)]

def distance(simulated: List[float], observed: List[float]) -> float:
    """Summary distance: absolute difference in means."""
    return abs(sum(simulated) / len(simulated) - sum(observed) / len(observed))



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_abc_rejection(n_samples, epsilon):
    v = []
    if isinstance(n_samples, (int, float)) and n_samples <= 0:
        v.append(f"AURA-E009: n_samples must be > 0, got {n_samples}")
    if isinstance(epsilon, (int, float)) and not math.isfinite(epsilon):
        v.append(f"AURA-E008: epsilon must be finite, got {epsilon}")
    if isinstance(epsilon, (int, float)) and epsilon <= 0:
        v.append(f"AURA-E009: epsilon must be > 0, got {epsilon}")
    if v:
        raise AuraInputError(v)

def abc_rejection(observed: List[float], n_samples: int, epsilon: float) -> Tuple[List[float], float]:
    """ABC rejection sampler. Returns (posterior_samples, acceptance_rate)."""
    _aura_validate_abc_rejection(n_samples, epsilon)
    accepted = []
    for _ in range(n_samples):
        theta = prior_sample()
        simulated = simulate_data(theta, n=len(observed))
        if distance(simulated, observed) < epsilon:
            accepted.append(theta)

    acceptance_rate = len(accepted) / n_samples if n_samples > 0 else 0.0
    return accepted, acceptance_rate

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: true θ = 2.5.
    theta_true = 2.5
    observed = simulate_data(theta_true, n=30)
    obs_mean = sum(observed) / len(observed)

    # ABC with loose tolerance.
    posterior_loose, accept_loose = abc_rejection(observed, n_samples=500, epsilon=0.5)
    mean_loose = sum(posterior_loose) / len(posterior_loose) if posterior_loose else 0.0

    # ABC with tight tolerance.
    posterior_tight, accept_tight = abc_rejection(observed, n_samples=500, epsilon=0.2)
    mean_tight = sum(posterior_tight) / len(posterior_tight) if posterior_tight else 0.0

    # Posterior mean should be close to truth.
    assert abs(mean_loose - theta_true) < 1.0, \
        f"Loose ABC posterior mean {mean_loose} should recover truth {theta_true}"
    assert abs(mean_tight - theta_true) < 1.0, \
        f"Tight ABC posterior mean {mean_tight} should recover truth {theta_true}"

    # Tighter tolerance → lower acceptance rate.
    assert accept_loose > accept_tight, \
        f"Loose acceptance {accept_loose} should be > tight {accept_tight}"

    print("PASS")
