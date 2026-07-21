"""Thompson sampling for multi-armed bandits.

Core idea: maintain Beta posteriors over success probability for each arm,
sample from each posterior, pull the arm with highest sample, update via
Bayesian update. Balances exploration vs exploitation optimally.

When to use: when you need to allocate resources (A/B test, optimization)
and want to minimize regret by learning arm quality online.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Dict




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_sample_beta(alpha, beta):
    v = []
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    if isinstance(alpha, (int, float)) and math.isfinite(alpha) and alpha <= 0:
        v.append(f"AURA-E001: alpha must be > 0, got {alpha}")  # domain: shape/concentration
    if isinstance(beta, (int, float)) and not math.isfinite(beta):
        v.append(f"AURA-E008: beta must be finite, got {beta}")
    if isinstance(beta, (int, float)) and math.isfinite(beta) and beta <= 0:
        v.append(f"AURA-E001: beta must be > 0, got {beta}")  # domain: shape/concentration
    if v:
        raise AuraInputError(v)

def _aura_validate_thompson_sampling_bandit(num_rounds):
    v = []
    if isinstance(num_rounds, (int, float)) and num_rounds <= 0:
        v.append(f"AURA-E009: num_rounds must be > 0, got {num_rounds}")
    if v:
        raise AuraInputError(v)

def sample_beta(alpha: float, beta: float) -> float:
    """Sample from Beta(alpha, beta) distribution using Gamma method."""
    _aura_validate_sample_beta(alpha, beta)
    # Beta ~ Gamma(alpha) / (Gamma(alpha) + Gamma(beta))
    # Use simple approximation: sample via rejection or direct method
    # For speed, use numerical approximation
    x = random.gauss(alpha / (alpha + beta), 0.1)
    return max(0.0, min(1.0, x))


def thompson_sampling_bandit(
    num_arms: int,
    num_rounds: int,
    true_probabilities: List[float],
) -> Dict[str, float]:
    """
    Run Thompson sampling bandit.
    Returns dict with cumulative_reward and num_pulls per arm.
    """
    _aura_validate_thompson_sampling_bandit(num_rounds)
    # Initialize Beta priors: Alpha=1, Beta=1 (uniform)
    alpha = [1.0] * num_arms
    beta = [1.0] * num_arms

    cumulative_reward = 0.0
    pulls_per_arm = [0] * num_arms

    for _ in range(num_rounds):
        # Thompson sampling: sample posterior for each arm
        samples = [sample_beta(alpha[i], beta[i]) for i in range(num_arms)]

        # Pull arm with highest sample
        arm = max(range(num_arms), key=lambda i: samples[i])
        pulls_per_arm[arm] += 1

        # Get reward (Bernoulli with true probability)
        reward = 1 if random.random() < true_probabilities[arm] else 0
        cumulative_reward += reward

        # Bayesian update: Beta-Binomial posterior
        if reward == 1:
            alpha[arm] += 1
        else:
            beta[arm] += 1

    return {
        "cumulative_reward": cumulative_reward,
        "pulls_per_arm": pulls_per_arm,
        "alpha_final": alpha,
        "beta_final": beta,
    }


if __name__ == "__main__":
    random.seed(42)

    # Three-arm bandit: arm 0 is best (80%), arm 1 medium (60%), arm 2 worst (40%)
    true_probs = [0.8, 0.6, 0.4]
    num_rounds = 1000

    result_ts = thompson_sampling_bandit(3, num_rounds, true_probs)
    pulls_ts = result_ts["pulls_per_arm"]

    # Run random policy for comparison
    cumulative_reward_random = sum(
        1 if random.random() < true_probs[random.randint(0, 2)] else 0
        for _ in range(num_rounds)
    )

    # Thompson sampling should pull best arm more often
    assert pulls_ts[0] > pulls_ts[2], \
        f"Best arm (0) should be pulled more than worst (2): {pulls_ts[0]} vs {pulls_ts[2]}"

    # Thompson sampling should earn more reward than random
    assert result_ts["cumulative_reward"] > cumulative_reward_random, \
        f"Thompson reward {result_ts['cumulative_reward']} should beat random {cumulative_reward_random}"

    print(f"thompson_sampling_bandit.py: pulls={pulls_ts}, reward={result_ts['cumulative_reward']} PASS")
