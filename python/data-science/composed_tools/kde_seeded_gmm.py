"""
KDE-Seeded Gaussian Mixture — the nonparametric scout guides the parametric army.

COMPOSED PATTERN: kernel_density_estimation (Statistical Modeling) x
gaussian_mixture_em (Core ML) — embedding bridge 0.494, found 2026-07-06.
KDE and GMM are the two classic answers to "what distribution is this?" —
composed, KDE runs first as a scout: its density modes reveal HOW MANY
components exist and WHERE, seeding EM's initial means. Random-initialized EM
on unbalanced mixtures routinely collapses two components into one; the
KDE-seeded start doesn't have to guess.

Use when: fitting mixtures without knowing k, or when random-init EM is
unstable on unbalanced components.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple


def kde(values: List[float], grid: List[float]) -> List[float]:
    n = len(values)
    sd = math.sqrt(sum((v - sum(values) / n) ** 2 for v in values) / n)
    h = 1.06 * sd * n ** (-0.2)  # Silverman
    out = []
    for g in grid:
        s = sum(math.exp(-0.5 * ((g - v) / h) ** 2) for v in values)
        out.append(s / (n * h * math.sqrt(2 * math.pi)))
    return out


def kde_modes(values: List[float], n_grid: int = 200) -> List[float]:
    lo, hi = min(values), max(values)
    grid = [lo + (hi - lo) * i / (n_grid - 1) for i in range(n_grid)]
    dens = kde(values, grid)
    return [grid[i] for i in range(1, n_grid - 1)
            if dens[i] > dens[i - 1] and dens[i] > dens[i + 1]]




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_em_gmm(tol):
    v = []
    if isinstance(tol, (int, float)) and not math.isfinite(tol):
        v.append(f"AURA-E008: tol must be finite, got {tol}")
    if v:
        raise AuraInputError(v)

def em_gmm(values: List[float], means: List[float], iters: int = 200,
           tol: float = 1e-7) -> Tuple[List[float], List[float], List[float], float, int]:
    _aura_validate_em_gmm(tol)
    k = len(means)
    mu = list(means)
    var = [1.0] * k
    w = [1.0 / k] * k
    prev_ll = -float("inf")
    used = iters
    for it in range(iters):
        resp = []
        ll = 0.0
        for x in values:
            ps = [w[j] * math.exp(-0.5 * (x - mu[j]) ** 2 / var[j]) /
                  math.sqrt(2 * math.pi * var[j]) for j in range(k)]
            s = sum(ps) or 1e-300
            ll += math.log(s)
            resp.append([p / s for p in ps])
        for j in range(k):
            nj = sum(r[j] for r in resp) or 1e-12
            mu[j] = sum(resp[i][j] * values[i] for i in range(len(values))) / nj
            var[j] = max(1e-4, sum(resp[i][j] * (values[i] - mu[j]) ** 2
                                   for i in range(len(values))) / nj)
            w[j] = nj / len(values)
        if abs(ll - prev_ll) < tol:
            used = it + 1
            break
        prev_ll = ll
    return mu, var, w, prev_ll, used


def recovered(mu: List[float], truth: List[float], tol: float = 0.5) -> bool:
    """Every true mean matched by a distinct fitted mean within tol."""
    remaining = list(mu)
    for t in truth:
        best = min(remaining, key=lambda m: abs(m - t), default=None)
        if best is None or abs(best - t) > tol:
            return False
        remaining.remove(best)
    return True


if __name__ == "__main__":
    random.seed(42)

    # Unbalanced 3-component mixture — the regime where random init collapses.
    true_means = [0.0, 4.0, 9.0]
    weights = [0.6, 0.3, 0.1]
    data = []
    for _ in range(900):
        r = random.random()
        c = 0 if r < 0.6 else (1 if r < 0.9 else 2)
        data.append(random.gauss(true_means[c], 0.7))

    # SCOUT: KDE finds the modes → seeds EM.
    modes = kde_modes(data)
    mu_s, _, _, ll_seeded, it_seeded = em_gmm(data, modes[:3])

    # BASELINE: 6 random initializations.
    random_results = []
    for trial in range(6):
        init = [random.uniform(min(data), max(data)) for _ in range(3)]
        mu_r, _, _, ll_r, _ = em_gmm(data, init)
        random_results.append((recovered(mu_r, true_means), ll_r))
    n_random_ok = sum(1 for ok, _ in random_results if ok)
    best_random_ll = max(ll for _, ll in random_results)

    print(f"KDE modes found: {[round(m,2) for m in modes]} (true {true_means})")
    print(f"KDE-seeded EM:   means {[round(m,2) for m in mu_s]} · "
          f"LL {ll_seeded:.1f} · {it_seeded} iters")
    print(f"random inits:    {n_random_ok}/6 recovered all 3 components · "
          f"best LL {best_random_ll:.1f}")

    # The composed claim, measured:
    assert len(modes) == 3, f"KDE scout should find exactly 3 modes: {len(modes)}"
    assert recovered(mu_s, true_means), f"seeded EM must recover all true means: {mu_s}"
    assert n_random_ok < 6, \
        "random init should FAIL at least once here — else the seeding solves nothing"
    assert ll_seeded >= best_random_ll - 1.0, \
        "seeded solution must match or beat the best random restart"
    print("kde_seeded_gmm.py PASS")
