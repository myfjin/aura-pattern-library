"""GARCH(1,1): volatility clustering via autoregressive conditional heteroskedasticity.

σ²_t = ω + α·ε²_{t-1} + β·σ²_{t-1}. The ARCH coefficient α measures how strongly a
large shock today raises tomorrow's variance — the signature of volatility clustering.
Core claim: fitting GARCH to clustered returns recovers a POSITIVE α (clustering
present); fitting to iid returns drives α→0 (no clustering). All three params (ω, α, β)
are estimated by coordinate ascent on the Gaussian log-likelihood.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple

def garch11_fit(returns: List[float], max_pass: int = 200) -> Tuple[float, float, float]:
    """Fit GARCH(1,1) by coordinate ascent on the log-likelihood.

    Returns: (omega, alpha, beta). All three parameters are updated (α+β<1 enforced
    for stationarity, ω>0, α,β≥0).
    """
    n = len(returns)
    v0 = sum(r**2 for r in returns) / n  # unconditional variance seed

    def neg_loglik(omega: float, alpha: float, beta: float) -> float:
        s2 = v0
        ll = 0.0
        for t in range(1, n):
            s2 = omega + alpha * returns[t - 1]**2 + beta * s2
            if s2 <= 1e-12:
                return 1e18
            ll += -0.5 * math.log(s2) - 0.5 * returns[t]**2 / s2
        return -ll

    omega, alpha, beta = 0.05 * v0, 0.05, 0.85
    step = {"omega": 0.02 * v0, "alpha": 0.05, "beta": 0.05}
    cur = neg_loglik(omega, alpha, beta)

    for _ in range(max_pass):
        improved = False
        for name in ("omega", "alpha", "beta"):
            for d in (step[name], -step[name]):
                no, na, nb = omega, alpha, beta
                if name == "omega":
                    no = max(1e-8, omega + d)
                elif name == "alpha":
                    na = min(0.999, max(0.0, alpha + d))
                else:
                    nb = min(0.999, max(0.0, beta + d))
                if na + nb < 0.999:
                    val = neg_loglik(no, na, nb)
                    if val < cur - 1e-9:
                        omega, alpha, beta, cur = no, na, nb, val
                        improved = True
        if not improved:
            for k in step:
                step[k] *= 0.5
            if all(step[k] < 1e-6 for k in step):
                break

    return omega, alpha, beta

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: iid returns (constant variance — NO clustering, true α=0).
    iid_returns = [random.gauss(0, 1) for _ in range(200)]

    # Planted: returns with volatility clustering (true α=0.10, β=0.85).
    cluster_returns = []
    sigma2 = 1.0
    for _ in range(200):
        sigma2 = 0.05 + 0.10 * cluster_returns[-1]**2 + 0.85 * sigma2 if cluster_returns else 1.0
        cluster_returns.append(random.gauss(0, math.sqrt(sigma2)))

    omega_iid, alpha_iid, beta_iid = garch11_fit(iid_returns)
    omega_cluster, alpha_cluster, beta_cluster = garch11_fit(cluster_returns)

    # Defining property: the ARCH coefficient α separates clustered from iid.
    # Measured (seed 42): α_iid ≈ 0.000, α_cluster ≈ 0.121.
    assert alpha_cluster > alpha_iid, \
        f"Clustered returns should show larger ARCH α: cluster={alpha_cluster:.3f} vs iid={alpha_iid:.3f}"
    assert alpha_cluster > 0.02, f"Clustering α too small to be detected: {alpha_cluster:.3f}"
    # Both fits stationary and non-negative.
    assert alpha_iid >= 0 and beta_iid >= 0 and alpha_iid + beta_iid < 1.0
    assert alpha_cluster >= 0 and beta_cluster >= 0 and alpha_cluster + beta_cluster < 1.0

    print("PASS")
