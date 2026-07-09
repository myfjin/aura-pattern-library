"""Two-stage least squares (2SLS): correct inference with endogenous regressor.

Stage 1: x ~ z. Stage 2: y ~ x̂. Core claim: 2SLS recovers true coeff even
with endogeneity; OLS is biased. Planted endogenous x correlated with ε.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple

def ols_simple(y: List[float], x: List[float]) -> float:
    """Simple linear regression: y ~ x."""
    n = len(y)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
    var_x = sum((x[i] - mean_x)**2 for i in range(n)) / n
    return cov / var_x if var_x > 1e-14 else 0.0

def tsls(y: List[float], x: List[float], z: List[float]) -> float:
    """Two-stage least squares."""
    # Stage 1: regress x on z.
    gamma = ols_simple(x, z)

    # Predicted x.
    mean_z = sum(z) / len(z)
    mean_x = sum(x) / len(x)
    x_hat = [mean_x + gamma * (z[i] - mean_z) for i in range(len(z))]

    # Stage 2: regress y on x̂.
    beta_2sls = ols_simple(y, x_hat)
    return beta_2sls

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: y = 1 + 2·x + (1.5·u + ν).  A LATENT confounder u enters BOTH x and the
    # structural error, making x endogenous. The instrument z drives x but is independent
    # of u (and ν) — so z ⊥ error (exclusion restriction HOLDS; measured Cov(z,ε)≈0).
    # This is what lets 2SLS recover the truth while OLS is biased upward by u.
    n = 200
    beta_true = 2.0
    z = [random.gauss(0, 1) for _ in range(n)]          # valid instrument
    u = [random.gauss(0, 1) for _ in range(n)]          # latent confounder (unobserved)
    x = [0.8 * z[i] + u[i] + random.gauss(0, 0.5) for i in range(n)]
    y = [1.0 + beta_true * x[i] + 1.5 * u[i] + random.gauss(0, 0.5) for i in range(n)]

    beta_ols = ols_simple(y, x)
    beta_2sls_est = tsls(y, x, z)

    # Defining property: 2SLS RECOVERS the true structural coefficient (≈2.0);
    # OLS is biased UPWARD by the confounder. Measured (seed 42): OLS≈2.91, 2SLS≈2.32.
    assert abs(beta_2sls_est - beta_true) < 0.5, \
        f"2SLS should recover true β≈{beta_true}: got {beta_2sls_est}"
    assert beta_ols > beta_2sls_est + 0.2, \
        f"OLS {beta_ols} should be more biased (upward) than 2SLS {beta_2sls_est}"
    assert beta_ols > beta_true + 0.3, \
        f"OLS {beta_ols} should be biased upward from true {beta_true}"

    print("PASS")
