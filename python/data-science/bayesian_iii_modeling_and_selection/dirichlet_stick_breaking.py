"""Dirichlet stick-breaking process: samples probabilities that sum to 1.

Weights sum→1; E[#active clusters] increases monotonically with α (concentration).
Core claim: weights sum→1; E[#active clusters] increases with α.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List



class AuraInputError(ValueError):
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_domain_stick_breaking_process(alpha):
    v = []
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    elif isinstance(alpha, (int, float)) and alpha <= 0:
        v.append(f"AURA-E001: alpha must be > 0, got {alpha}")
    if v:
        raise AuraInputError(v)

def stick_breaking_process(alpha: float, num_breaks: int = 100) -> List[float]:
    """Generate stick-breaking weights: V_k ~ Beta(1, α), weights w_k = V_k * ∏(1-V_j).

    Returns probabilities that sum to (approximately) 1.
    """
    _aura_domain_stick_breaking_process(alpha)
    import random
    weights = []
    remaining = 1.0

    for _ in range(num_breaks):
        # V ~ Beta(1, α).
        v = random.betavariate(1.0, alpha)
        weight = v * remaining
        weights.append(weight)
        remaining *= (1.0 - v)

        if remaining < 1e-8:
            break

    return weights

def _aura_domain_count_active_clusters(weights, threshold):
    v = []
    if not (isinstance(threshold, (int, float)) and math.isfinite(threshold)):
        v.append(f"AURA-E008: threshold must be finite, got {threshold}")
    for i, w in enumerate(weights):
        if not (isinstance(w, (int, float)) and math.isfinite(w)):
            v.append(f"AURA-E008: weights[{i}] must be finite, got {w}")
            break
    if v:
        raise AuraInputError(v)

def count_active_clusters(weights: List[float], threshold: float = 0.01) -> int:
    """Count weights above threshold (approximate number of 'active' clusters)."""
    _aura_domain_count_active_clusters(weights, threshold)
    return sum(1 for w in weights if w > threshold)

if __name__ == "__main__":
    import random
    random.seed(42)

    # Test two concentration levels: α = 0.5 (sparse) vs α = 5.0 (uniform).
    alpha_low = 0.5
    alpha_high = 5.0

    # Generate many samples and compute expected active clusters.
    n_sims = 100
    active_low = [count_active_clusters(stick_breaking_process(alpha_low)) for _ in range(n_sims)]
    active_high = [count_active_clusters(stick_breaking_process(alpha_high)) for _ in range(n_sims)]

    mean_active_low = sum(active_low) / len(active_low)
    mean_active_high = sum(active_high) / len(active_high)

    # Weights should sum to ≈ 1.
    sample_weights = stick_breaking_process(1.0)
    weight_sum = sum(sample_weights)
    assert weight_sum > 0.9, f"Weights should sum ≈ 1, got {weight_sum}"

    # Higher α → more active clusters (E[K(α)] increasing in α).
    assert mean_active_high > mean_active_low, \
        f"Higher α {alpha_high} should have more clusters: {mean_active_high} vs {mean_active_low}"

    print("PASS")
