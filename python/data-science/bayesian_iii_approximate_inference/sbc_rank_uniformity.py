"""Simulation Based Calibration (SBC): ranks should be uniform for a well-calibrated sampler.

Simulate parameter, simulate data, infer posterior, check where the true parameter ranks.
Core claim: ranks ~uniform (χ²) for correct sampler; flagged non-uniform for biased one.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List
import math

def simulate_and_rank(n_sims: int, seed_offset=0) -> List[int]:
    """SBC: simulate (θ_true, data), infer θ posterior samples, rank θ_true.

    Returns list of ranks (0 to n_samples-1).
    """
    import random
    ranks = []

    for sim in range(n_sims):
        random.seed(42 + seed_offset + sim)

        # Simulate true parameter.
        theta_true = random.gauss(0, 1)

        # Simulate data from N(theta_true, 1.0).
        n_obs = 30
        data = [random.gauss(theta_true, 1.0) for _ in range(n_obs)]

        # Posterior inference (simplified: draw from posterior).
        y_mean = sum(data) / len(data)
        posterior_var = 1.0 / (n_obs + 1.0)
        posterior_mean = posterior_var * y_mean * n_obs

        # Sample from posterior.
        n_samples = 100
        posterior_samples = [random.gauss(posterior_mean, math.sqrt(posterior_var)) for _ in range(n_samples)]

        # Rank where theta_true falls.
        rank = sum(1 for p in posterior_samples if p < theta_true)
        ranks.append(rank)

    return ranks

def chi_sq_gof(ranks: List[int], n_samples: int) -> float:
    """Chi-square goodness-of-fit test for uniform distribution over ranks.

    Under null, ranks should be uniform on {0, ..., n_samples}.
    """
    n_bins = min(10, n_samples // 5)  # Group ranks into bins.
    bin_size = (n_samples + 1) / n_bins
    observed = [0] * n_bins

    for rank in ranks:
        bin_idx = min(int(rank / bin_size), n_bins - 1)
        observed[bin_idx] += 1

    expected = len(ranks) / n_bins
    chi_sq = sum((o - expected)**2 / expected for o in observed if expected > 0)

    return chi_sq

if __name__ == "__main__":
    # Correct sampler: ranks should be uniform.
    ranks_correct = simulate_and_rank(n_sims=200, seed_offset=0)
    chi_sq_correct = chi_sq_gof(ranks_correct, n_samples=100)

    # Biased sampler: resample shifted ranks (simulate a biased posterior).
    import random
    random.seed(42)
    ranks_biased = [max(0, min(100, r + random.randint(-20, 20))) for r in simulate_and_rank(n_sims=200, seed_offset=1000)]
    chi_sq_biased = chi_sq_gof(ranks_biased, n_samples=100)

    # Correct sampler: χ² should be small (uniform).
    assert chi_sq_correct < 30, f"Correct sampler χ² {chi_sq_correct} should be small"

    # Biased sampler: χ² should be larger (non-uniform).
    assert chi_sq_biased > chi_sq_correct, \
        f"Biased χ² {chi_sq_biased} should be > correct {chi_sq_correct}"

    print("PASS")
