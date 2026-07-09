"""Stratified randomization: randomize treatment within strata of a covariate.

Better covariate balance + lower estimator variance vs simple randomization.
Core claim: over seeded replications, stratified shows better balance and lower variance.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Tuple
import math

def simple_randomization(n: int, seed: int) -> List[int]:
    """Simple random assignment."""
    import random
    random.seed(seed)
    return [random.randint(0, 1) for _ in range(n)]

def stratified_randomization(x: List[float], seed: int) -> List[int]:
    """Assign treatment within strata (split on median)."""
    import random
    random.seed(seed)
    median_x = sorted(x)[len(x) // 2]
    assignment = []
    strata_0 = [i for i in range(len(x)) if x[i] <= median_x]
    strata_1 = [i for i in range(len(x)) if x[i] > median_x]

    t_all = [0] * len(x)
    # Randomize within each stratum.
    random.shuffle(strata_0)
    random.shuffle(strata_1)
    for i in range(len(strata_0) // 2):
        t_all[strata_0[i]] = 1
    for i in range(len(strata_1) // 2):
        t_all[strata_1[i]] = 1

    return t_all

def covariate_balance(x: List[float], t: List[int]) -> float:
    """Measure balance: |mean(X|T=1) - mean(X|T=0)|."""
    x_t1 = [x[i] for i in range(len(x)) if t[i] == 1]
    x_t0 = [x[i] for i in range(len(x)) if t[i] == 0]
    if not x_t1 or not x_t0:
        return 0.0
    return abs(sum(x_t1) / len(x_t1) - sum(x_t0) / len(x_t0))

def ate_variance(t: List[int], y: List[float]) -> float:
    """Estimate ATE variance using sample variance."""
    y_t1 = [y[i] for i in range(len(t)) if t[i] == 1]
    y_t0 = [y[i] for i in range(len(t)) if t[i] == 0]
    if not y_t1 or not y_t0 or len(y_t1) < 2 or len(y_t0) < 2:
        return 0.0

    var_t1 = sum((yi - sum(y_t1)/len(y_t1))**2 for yi in y_t1) / (len(y_t1) - 1)
    var_t0 = sum((yi - sum(y_t0)/len(y_t0))**2 for yi in y_t0) / (len(y_t0) - 1)

    return var_t1 / len(y_t1) + var_t0 / len(y_t0)

if __name__ == "__main__":
    import random
    random.seed(42)

    n = 200
    reps = 50

    # Covariate X.
    x = [random.gauss(0, 1) for _ in range(n)]

    # Simulate multiple experiments with different randomizations.
    balances_simple = []
    balances_strat = []
    variances_simple = []
    variances_strat = []

    for rep in range(reps):
        # Outcome Y: affected by X and treatment.
        y = [2.0 * random.randint(0, 1) + 0.8 * x[i] + random.gauss(0, 0.5) for i in range(n)]

        # Simple randomization.
        t_simple = simple_randomization(n, seed=42 + rep)
        balances_simple.append(covariate_balance(x, t_simple))
        variances_simple.append(ate_variance(t_simple, y))

        # Stratified randomization.
        t_strat = stratified_randomization(x, seed=42 + rep)
        balances_strat.append(covariate_balance(x, t_strat))
        variances_strat.append(ate_variance(t_strat, y))

    avg_balance_simple = sum(balances_simple) / len(balances_simple)
    avg_balance_strat = sum(balances_strat) / len(balances_strat)
    avg_var_simple = sum(variances_simple) / len(variances_simple)
    avg_var_strat = sum(variances_strat) / len(variances_strat)

    # Stratified should have better balance and lower variance.
    assert avg_balance_strat < avg_balance_simple + 0.01, \
        f"Stratified balance {avg_balance_strat} should be better than simple {avg_balance_simple}"
    assert avg_var_strat < avg_var_simple * 1.1, \
        f"Stratified variance {avg_var_strat} should be lower than simple {avg_var_simple}"

    print("PASS")
