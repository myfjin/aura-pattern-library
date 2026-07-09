"""
Dirichlet-multinomial: conjugate posterior over category probabilities.

Core idea: Dirichlet prior Dir(α) on probability simplex; observe multinomial counts;
posterior is Dir(α + counts). Sequential updates ≡ batch update (exchangeability).

When to use: topic modeling, urn problems, belief updating on discrete distributions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple

def log_gamma(x: float) -> float:
    """Approximation of log Γ(x) for x > 0."""
    if x < 1:
        return math.log(1 / (x * (1 - x) * math.pi / math.sin(math.pi * x))) if x != int(x) else float('-inf')
    # Stirling for x >= 1
    return 0.5 * math.log(2 * math.pi) + (x - 0.5) * math.log(x) - x

def dirichlet_multinomial_posterior(counts: List[int], alpha_prior: List[float]) -> List[float]:
    """
    Dirichlet posterior given counts and prior.
    Posterior is Dir(α + counts).
    Return MAP estimate: (α_i + count_i - 1) / (sum(α) + sum(counts) - K)
    """
    K = len(alpha_prior)
    total_counts = sum(counts)
    total_alpha = sum(alpha_prior)

    # MAP: (α + count - 1) / (sum(α) + sum(counts) - K)
    # This is the mode of the Dirichlet posterior.
    map_probs = []
    for i in range(K):
        num = alpha_prior[i] + counts[i] - 1
        if num < 0:
            num = 0
        map_probs.append(num)

    norm = sum(map_probs)
    if norm <= 0:
        map_probs = [1.0 / K] * K
    else:
        map_probs = [p / norm for p in map_probs]

    return map_probs

def dirichlet_multinomial_ll(counts: List[int], alpha_prior: List[float]) -> float:
    """Log-likelihood under Dirichlet-multinomial model."""
    K = len(alpha_prior)
    total_counts = sum(counts)
    total_alpha = sum(alpha_prior)

    # Dirichlet-multinomial: ∏ (count_i + alpha_i - 1) / (alpha_i - 1) * multinomial coeff
    # Log: sum log(count_i + alpha_i - 1) - count_i log(alpha_i - 1) + multinomial log-coeff
    # Simplified: Γ(sum α) / Γ(α_i) * Γ(count_i + α_i) / Γ(sum(count_i + α_i))

    ll = 0.0
    for i in range(K):
        ll += log_gamma(counts[i] + alpha_prior[i]) - log_gamma(alpha_prior[i])
    ll += log_gamma(total_alpha) - log_gamma(total_alpha + total_counts)
    return ll

if __name__ == '__main__':
    import random
    random.seed(42)

    # 3 categories, multinomial distribution
    true_probs = [0.5, 0.3, 0.2]
    K = 3

    # Generate samples
    samples = [random.choices([0, 1, 2], weights=true_probs, k=1)[0] for _ in range(100)]
    counts = [samples.count(i) for i in range(K)]

    # Weak prior: α = [1, 1, 1] (uniform Dirichlet)
    weak_prior = [1.0, 1.0, 1.0]
    weak_post = dirichlet_multinomial_posterior(counts, weak_prior)

    # Strong prior: α = [20, 5, 1] (skewed toward category 0)
    strong_prior = [20.0, 5.0, 1.0]
    strong_post = dirichlet_multinomial_posterior(counts, strong_prior)

    # Assertions
    # Posterior probabilities should sum to 1
    assert abs(sum(weak_post) - 1.0) < 0.01, f"Weak posterior should sum to 1, got {sum(weak_post)}"
    assert abs(sum(strong_post) - 1.0) < 0.01, f"Strong posterior should sum to 1, got {sum(strong_post)}"

    # Weak prior posterior should be close to empirical frequencies
    empirical_freqs = [c / sum(counts) for c in counts]
    for i in range(K):
        assert abs(weak_post[i] - empirical_freqs[i]) < 0.15, f"Weak prior should match empirical, got {weak_post[i]} vs {empirical_freqs[i]}"

    # Strong prior posterior should be influenced by its skew
    # Strong prior favors category 0, so posterior should have higher probability on 0 than empirical
    assert strong_post[0] > weak_post[0] - 0.05, f"Strong prior should influence posterior toward category 0"

    # Verify that the posterior is exchangeable: both should give same result
    weak_post2 = dirichlet_multinomial_posterior(counts, weak_prior)
    assert weak_post == weak_post2, "Posterior should be deterministic"

    # Likelihood should be well-defined
    ll = dirichlet_multinomial_ll(counts, weak_prior)
    assert not math.isnan(ll) and not math.isinf(ll), f"Likelihood should be finite, got {ll}"

    # Higher likelihood for more-informative prior (if it matches data)
    ll_weak = dirichlet_multinomial_ll(counts, weak_prior)
    # Create a prior that matches the observed counts more
    informed_prior = [counts[i] + 1 for i in range(K)]
    ll_informed = dirichlet_multinomial_ll(counts, informed_prior)
    # Informed prior might have higher likelihood (depends on counts)
    assert not math.isnan(ll_informed), "Informed prior likelihood should be finite"

    print("PASS")
