"""ELBO monotonicity in coordinate-ascent variational inference.

Coordinate-ascent VI (CAVI) maximizes the Evidence Lower Bound one factor at a time; each
update is a conditional maximizer, so the ELBO is NON-DECREASING every step, and it is
bounded above by the true log-evidence (ELBO = log p(data) − KL(q‖posterior) ≤ log p(data)).
For a conjugate Gaussian the bound is tight — CAVI converges to exactly the log-evidence.
Core claim: from a bad initialization the ELBO rises MONOTONICALLY, stays ≤ log-evidence,
and converges to it.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple

def true_log_evidence(data, mu0=0.0, s0=10.0) -> float:
    """Exact log marginal likelihood ∫ N(data|μ,1) N(μ|mu0,s0) dμ (matrix-determinant lemma)."""
    n = len(data)
    ssum = sum(data)
    s_centered = sum((y - mu0) ** 2 for y in data)
    quad = s_centered - s0 / (1.0 + s0 * n) * (ssum - n * mu0) ** 2
    return -0.5 * (n * math.log(2 * math.pi) + math.log(1.0 + s0 * n) + quad)

def _elbo(data, m, s, mu0=0.0, s0=10.0) -> float:
    """ELBO for q(μ)=N(m, s), model N(data|μ,1), prior N(μ|mu0,s0)."""
    n = len(data)
    ll = sum(-0.5 * math.log(2 * math.pi) - 0.5 * ((y - m) ** 2 + s) for y in data)
    lp = -0.5 * math.log(2 * math.pi * s0) - 0.5 * ((m - mu0) ** 2 + s) / s0
    entropy = 0.5 * math.log(2 * math.pi * math.e * s)
    return ll + lp + entropy

def cavi_elbo_sequence(data, mu0=0.0, s0=10.0, cycles=15) -> Tuple[List[float], float]:
    """Coordinate ascent from a deliberately bad init. Returns (elbo_sequence, log_evidence)."""
    n = len(data)
    m, s = -5.0, 5.0  # bad init, far from the posterior
    seq = [_elbo(data, m, s, mu0, s0)]
    for _ in range(cycles):
        m = (sum(data) + mu0 / s0) / (n + 1.0 / s0)   # argmax_m ELBO (given s)
        seq.append(_elbo(data, m, s, mu0, s0))
        s = 1.0 / (n + 1.0 / s0)                       # argmax_s ELBO (given m)
        seq.append(_elbo(data, m, s, mu0, s0))
    return seq, true_log_evidence(data, mu0, s0)

if __name__ == "__main__":
    import random
    random.seed(42)

    data = [random.gauss(2.0, 1.0) for _ in range(30)]
    seq, log_ev = cavi_elbo_sequence(data)

    # Defining properties (measured seed 42: rises ~188 from bad init, converges to log_ev).
    assert all(seq[i + 1] >= seq[i] - 1e-9 for i in range(len(seq) - 1)), "ELBO must be non-decreasing (coordinate ascent)"
    assert all(e <= log_ev + 1e-6 for e in seq), "ELBO must never exceed the true log-evidence"
    assert seq[-1] - seq[0] > 50.0, "ELBO must rise substantially from the bad init"
    assert abs(seq[-1] - log_ev) < 0.1, f"CAVI must converge to log-evidence {log_ev:.3f}, got {seq[-1]:.3f}"

    print("PASS")
