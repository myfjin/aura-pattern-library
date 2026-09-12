"""
Empirical Bayes shrinkage (James-Stein style): shrink group means toward grand mean.

Core idea: estimate hyperparameter from data; shrink group means via Bayesian posterior.
Total squared error BEATS raw group means (Stein's paradox measured).

When to use: meta-analysis, small-group inference, estimation of many parameters.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple

def empirical_bayes_shrinkage(groups: List[List[float]]) -> Tuple[List[float], List[float], float]:
    """
    Shrink group means toward grand mean.
    Input: list of groups (each group is a list of observations)
    Output: (shrunken_means, raw_means, shrinkage_factor)
    """
    # Compute raw group means and grand mean
    group_means = [sum(g) / len(g) for g in groups]
    grand_mean = sum(group_means) / len(group_means)

    # Estimate variance within and between groups
    n_groups = len(groups)
    group_sizes = [len(g) for g in groups]
    avg_group_size = sum(group_sizes) / n_groups

    # Within-group variance (pooled)
    var_within = 0.0
    total_obs = 0
    for g in groups:
        gm = sum(g) / len(g)
        var_within += sum((x - gm) ** 2 for x in g)
        total_obs += len(g)
    if total_obs > n_groups:
        var_within /= (total_obs - n_groups)

    # Between-group variance
    var_between = sum((gm - grand_mean) ** 2 for gm in group_means) / (n_groups - 1)

    # Posterior weight on the OWN group mean: B = τ̂² / (τ̂² + σ²/n̄), where
    # τ̂² = max(0, var_between − σ²/n̄) — the variance of RAW means includes
    # sampling noise σ²/n̄, so subtract it (positive-part estimator). More
    # REAL heterogeneity → trust the group's own mean MORE. Inverting this
    # weight (an easy slip) over-shrinks and LOSES to raw means — that
    # inversion was this file's original bug, caught by actually asserting
    # the Stein paradox over replications.
    # POSITIVE-PART JAMES-STEIN (the provable dominator for K >= 4): common
    # own-weight B = max(0, 1 − (K−3)·(σ²/n̄)/S) with S = Σ(raw − grand)².
    # The (K−3) rule — not (K−1) — is exactly what makes total squared error
    # dominate raw means IN EXPECTATION when shrinking toward an estimated
    # grand mean; method-of-moments weights (τ̂²/(τ̂²+σ²/n̄)) win most
    # datasets yet can LOSE in aggregate through occasional large errors —
    # measured here before this line was corrected, twice.
    sampling_var = var_within / avg_group_size if avg_group_size > 0 else 0.0
    S = sum((gm - grand_mean) ** 2 for gm in group_means)
    shrinkage_factor = max(0.0, 1.0 - (n_groups - 3) * sampling_var / S) if S > 0 else 0.0

    # Shrunken means
    shrunken_means = [shrinkage_factor * gm + (1 - shrinkage_factor) * grand_mean
                      for gm in group_means]

    return shrunken_means, group_means, shrinkage_factor

if __name__ == '__main__':
    import random
    random.seed(42)

    # Generate data: K groups with different true means, small samples
    true_means = [1.0, 2.5, 1.8, 3.2, 2.0]
    K = len(true_means)
    groups = []
    for true_mu in true_means:
        group = [random.gauss(true_mu, 1.0) for _ in range(5)]
        groups.append(group)

    # Apply shrinkage
    shrunken_means, raw_means, shrinkage = empirical_bayes_shrinkage(groups)

    assert len(shrunken_means) == K, f"Should have {K} shrunken means, got {len(shrunken_means)}"
    assert 0 <= shrinkage <= 1, f"Shrinkage factor should be in [0,1], got {shrinkage}"

    # Shrunken means should be closer to grand mean than raw means
    grand_mean = sum(raw_means) / len(raw_means)
    for sm, rm in zip(shrunken_means, raw_means):
        dist_raw = abs(rm - grand_mean)
        dist_shrunken = abs(sm - grand_mean)
        # Shrunken should be pulled toward grand mean (not beyond, but closer)
        assert dist_shrunken <= dist_raw, f"Shrunken {sm} should be closer to grand mean {grand_mean} than raw {rm}"

    # THE STEIN PARADOX, actually measured: over many replicated datasets,
    # shrunken group means beat raw group means in TOTAL squared error vs the
    # true means — even though every individual mean gets biased. One dataset
    # proves nothing (the paradox is an expectation); 400 replications do.
    reps, wins, tot_raw, tot_shr = 400, 0, 0.0, 0.0
    for _ in range(reps):
        gs = [[random.gauss(mu, 1.0) for _ in range(5)] for mu in true_means]
        shr, raw, _ = empirical_bayes_shrinkage(gs)
        se_raw = sum((r - m) ** 2 for r, m in zip(raw, true_means))
        se_shr = sum((s - m) ** 2 for s, m in zip(shr, true_means))
        tot_raw += se_raw
        tot_shr += se_shr
        wins += se_shr < se_raw
    print(f"replications: {reps} · mean SE raw {tot_raw/reps:.3f} vs "
          f"shrunken {tot_shr/reps:.3f} · shrinkage wins {wins/reps:.0%}")
    assert tot_shr < tot_raw, "shrinkage must beat raw means in aggregate SE"
    assert wins / reps > 0.55, f"shrinkage should win most datasets: {wins/reps:.0%}"

    # Shrinkage factor should be positive if there's heterogeneity
    # (not necessarily true for this small sample, but worth checking)
    assert shrinkage >= 0, f"Shrinkage should be non-negative, got {shrinkage}"

    # Homogeneous groups (no real differences) must shrink HARDER than the
    # heterogeneous main data — the comparative property, which is what the
    # estimator actually guarantees. (JS(K−3) on pure-null data settles near
    # own-weight ~0.5, not ~0 — asserting near-zero would encode a different
    # estimator's intuition.)
    uniform_groups = [[2.0 + random.gauss(0, 0.1) for _ in range(20)] for _ in range(5)]
    shrunken_unif, raw_unif, shrink_unif = empirical_bayes_shrinkage(uniform_groups)
    print(f"own-weight: heterogeneous {shrinkage:.2f} vs homogeneous {shrink_unif:.2f}")
    assert shrink_unif < shrinkage - 0.1, (
        f"homogeneous data should shrink harder: {shrink_unif:.2f} vs {shrinkage:.2f}")

    print("PASS")
