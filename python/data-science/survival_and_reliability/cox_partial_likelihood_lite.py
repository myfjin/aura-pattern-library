"""Cox partial likelihood: semiparametric survival model for 2-covariate hazard.

Estimates hazard ratios via Newton-Raphson on partial likelihood. Core claim:
planted hazard ratios recovered from censored data; Newton steps converge.
Planted survival times with true HR, censoring, and covariate structure.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_cox_partial_likelihood_2cov(tol):
    v = []
    if isinstance(tol, (int, float)) and not math.isfinite(tol):
        v.append(f"AURA-E008: tol must be finite, got {tol}")
    if v:
        raise AuraInputError(v)

def cox_partial_likelihood_2cov(
    times: List[float],
    events: List[int],
    x1: List[float],
    x2: List[float],
    max_iter: int = 20,
    tol: float = 1e-6
) -> Tuple[float, float]:
    """Fit Cox model for 2 covariates via partial likelihood.

    Returns: (beta1, beta2) where h(t|x) = h0(t) · exp(beta1·x1 + beta2·x2).
    """
    _aura_validate_cox_partial_likelihood_2cov(tol)
    n = len(times)
    beta = [0.0, 0.0]

    for iteration in range(max_iter):
        # Sort by time (ascending).
        order = sorted(range(n), key=lambda i: times[i])

        score = [0.0, 0.0]
        hess = [[0.0, 0.0], [0.0, 0.0]]

        for i in order:
            if events[i] == 0:
                continue

            # Risk set: all j with time_j >= time_i.
            at_risk = [j for j in range(n) if times[j] >= times[i]]

            # Weighted sum over risk set.
            sum_exp = sum(math.exp(beta[0] * x1[j] + beta[1] * x2[j]) for j in at_risk)
            sum_w_x1 = sum(math.exp(beta[0] * x1[j] + beta[1] * x2[j]) * x1[j] for j in at_risk)
            sum_w_x2 = sum(math.exp(beta[0] * x1[j] + beta[1] * x2[j]) * x2[j] for j in at_risk)

            if sum_exp < 1e-14:
                continue

            # Score contribution.
            score[0] += x1[i] - sum_w_x1 / sum_exp
            score[1] += x2[i] - sum_w_x2 / sum_exp

            # Hessian contribution (information matrix).
            sum_w_x1x1 = sum(math.exp(beta[0] * x1[j] + beta[1] * x2[j]) * x1[j]**2 for j in at_risk)
            sum_w_x2x2 = sum(math.exp(beta[0] * x1[j] + beta[1] * x2[j]) * x2[j]**2 for j in at_risk)
            sum_w_x1x2 = sum(math.exp(beta[0] * x1[j] + beta[1] * x2[j]) * x1[j] * x2[j] for j in at_risk)

            var_x1 = sum_w_x1x1 / sum_exp - (sum_w_x1 / sum_exp)**2
            var_x2 = sum_w_x2x2 / sum_exp - (sum_w_x2 / sum_exp)**2
            cov_x1x2 = sum_w_x1x2 / sum_exp - (sum_w_x1 / sum_exp) * (sum_w_x2 / sum_exp)

            hess[0][0] += var_x1
            hess[1][1] += var_x2
            hess[0][1] += cov_x1x2
            hess[1][0] += cov_x1x2

        # Newton step.
        det = hess[0][0] * hess[1][1] - hess[0][1]**2
        if abs(det) < 1e-14:
            break

        inv_hess = [[hess[1][1] / det, -hess[0][1] / det],
                    [-hess[1][0] / det, hess[0][0] / det]]

        delta = [sum(inv_hess[i][j] * score[j] for j in range(2)) for i in range(2)]

        beta_new = [beta[i] + delta[i] for i in range(2)]
        if max(abs(delta[i]) for i in range(2)) < tol:
            beta = beta_new
            break

        beta = beta_new

    return beta[0], beta[1]

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: true hazard ratios β1=0.5, β2=-0.3.
    # Generate 30 samples with covariates and exponential times.
    n = 30
    x1 = [random.gauss(0, 1) for _ in range(n)]
    x2 = [random.gauss(0, 1) for _ in range(n)]

    # Survival times: exp(lambda * exp(eta)).
    times = []
    events = []
    for i in range(n):
        eta = 0.5 * x1[i] - 0.3 * x2[i]
        lambda_i = 0.5 * math.exp(eta)
        t = -math.log(random.random()) / lambda_i
        c_time = random.expovariate(0.3)  # Censoring time.
        times.append(min(t, c_time))
        events.append(1 if t <= c_time else 0)

    beta1, beta2 = cox_partial_likelihood_2cov(times, events, x1, x2)

    # Check: estimated betas close to true values (within ±0.5).
    assert abs(beta1 - 0.5) < 0.5, f"β1={beta1}, expected ≈0.5"
    assert abs(beta2 - (-0.3)) < 0.5, f"β2={beta2}, expected ≈-0.3"

    print("PASS")
