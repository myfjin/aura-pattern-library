"""Cluster randomization: treatment assigned at the cluster level, not the individual.

Intracluster correlation (ICC) means observations within a cluster are not independent, so
the naive per-observation SE is too small — its 95% CIs UNDER-cover the true effect.
Aggregating to cluster means and testing on those (n = #clusters) restores nominal coverage.
Core claim: over many cluster-randomized datasets, the naive 95% CI under-covers while the
cluster-level 95% CI covers at ~95%.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple

def _var(z: List[float]) -> float:
    n = len(z)
    if n < 2:
        return 0.0
    mu = sum(z) / n
    return sum((zi - mu)**2 for zi in z) / (n - 1)

def naive_ci_covers(t_obs: List[float], c_obs: List[float], true_effect: float) -> bool:
    """Per-observation 95% CI for the ATE — ignores clustering (under-covers)."""
    ate = sum(t_obs) / len(t_obs) - sum(c_obs) / len(c_obs)
    se = math.sqrt(_var(t_obs) / len(t_obs) + _var(c_obs) / len(c_obs))
    return abs(ate - true_effect) < 1.96 * se

def cluster_ci_covers(t_means: List[float], c_means: List[float], true_effect: float) -> bool:
    """Cluster-level 95% CI: test on cluster means (n = #clusters) — correct coverage."""
    ate = sum(t_means) / len(t_means) - sum(c_means) / len(c_means)
    se = math.sqrt(_var(t_means) / len(t_means) + _var(c_means) / len(c_means))
    return abs(ate - true_effect) < 1.96 * se

def make_dataset(seed: int, n_clusters: int, m: int, icc: float, true_effect: float) -> Tuple[list, list, list, list]:
    """One cluster-randomized dataset. Returns (t_obs, c_obs, t_means, c_means)."""
    import random
    random.seed(seed)

    def arm(base: float):
        obs, means = [], []
        for _ in range(n_clusters):
            cluster_effect = random.gauss(0, math.sqrt(icc))
            vals = [base + cluster_effect + random.gauss(0, math.sqrt(1 - icc)) for _ in range(m)]
            obs += vals
            means.append(sum(vals) / m)
        return obs, means

    t_obs, t_means = arm(true_effect)
    c_obs, c_means = arm(0.0)
    return t_obs, c_obs, t_means, c_means

if __name__ == "__main__":
    n_clusters, m, icc, true_effect = 10, 20, 0.3, 2.0
    n_datasets = 400

    naive_cov = cluster_cov = 0
    for s in range(n_datasets):
        t_obs, c_obs, t_means, c_means = make_dataset(s, n_clusters, m, icc, true_effect)
        naive_cov += naive_ci_covers(t_obs, c_obs, true_effect)
        cluster_cov += cluster_ci_covers(t_means, c_means, true_effect)

    naive_rate = naive_cov / n_datasets
    cluster_rate = cluster_cov / n_datasets

    # Defining property: naive CI under-covers (ICC ignored); cluster CI covers ~95%.
    # Measured (ICC=0.3): naive≈0.57, cluster≈0.96.
    assert naive_rate < 0.85, f"Naive 95% CI should UNDER-cover under clustering: {naive_rate}"
    assert cluster_rate > 0.90, f"Cluster-level 95% CI should cover ~0.95: {cluster_rate}"
    assert cluster_rate > naive_rate, "Cluster-adjusted coverage should beat naive"

    print("PASS")
