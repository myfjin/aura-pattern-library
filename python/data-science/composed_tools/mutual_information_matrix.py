"""
Mutual-Information Matrix — the dependence heatmap Pearson cannot draw.

COMPOSED PATTERN: nonlinear_dependence_mi (Information Theory) x
pearson_correlation_matrix (Preprocessing/EDA) — embedding bridge 0.503,
found 2026-07-06. Every notebook on earth draws the Pearson heatmap; it is
blind to any relationship that is not monotone-linear. This tool computes the
SAME feature-by-feature matrix with normalized mutual information (binned),
side by side with |Pearson| — so y = x^2 lights up where the classic heatmap
shows nothing.

Use when: first-look EDA on features whose relationships may be nonlinear.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Dict, List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_equal_frequency_bins(n_bins):
    v = []
    if isinstance(n_bins, (int, float)) and n_bins <= 0:
        v.append(f"AURA-E009: n_bins must be > 0, got {n_bins}")
    if v:
        raise AuraInputError(v)

def equal_frequency_bins(values: List[float], n_bins: int) -> List[int]:
    _aura_validate_equal_frequency_bins(n_bins)
    order = sorted(range(len(values)), key=lambda i: values[i])
    bins = [0] * len(values)
    for rank, idx in enumerate(order):
        bins[idx] = min(n_bins - 1, rank * n_bins // len(values))
    return bins


def mutual_information(xb: List[int], yb: List[int], n_bins: int) -> float:
    n = len(xb)
    joint: Dict[Tuple[int, int], int] = {}
    px = [0] * n_bins
    py = [0] * n_bins
    for a, b in zip(xb, yb):
        joint[(a, b)] = joint.get((a, b), 0) + 1
        px[a] += 1
        py[b] += 1
    mi = 0.0
    for (a, b), c in joint.items():
        p_ab = c / n
        mi += p_ab * math.log(p_ab / ((px[a] / n) * (py[b] / n)))
    return max(0.0, mi)


def normalized_mi(x: List[float], y: List[float], n_bins: int = 8) -> float:
    """MI normalized to [0,1] by min marginal entropy (1 = deterministic link)."""
    xb = equal_frequency_bins(x, n_bins)
    yb = equal_frequency_bins(y, n_bins)
    mi = mutual_information(xb, yb, n_bins)
    def entropy(bins_: List[int]) -> float:
        n = len(bins_)
        counts: Dict[int, int] = {}
        for b in bins_:
            counts[b] = counts.get(b, 0) + 1
        return -sum((c / n) * math.log(c / n) for c in counts.values())
    h = min(entropy(xb), entropy(yb))
    return mi / h if h > 0 else 0.0


def abs_pearson(x: List[float], y: List[float]) -> float:
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n)) / n
    vx = sum((v - mx) ** 2 for v in x) / n
    vy = sum((v - my) ** 2 for v in y) / n
    return abs(cov / math.sqrt(vx * vy)) if vx > 0 and vy > 0 else 0.0


def dependence_matrices(features: Dict[str, List[float]]):
    names = list(features)
    mi_m = {a: {b: 0.0 for b in names} for a in names}
    pe_m = {a: {b: 0.0 for b in names} for a in names}
    for i, a in enumerate(names):
        for j, b in enumerate(names):
            if i <= j:
                mi = 1.0 if i == j else normalized_mi(features[a], features[b])
                pe = 1.0 if i == j else abs_pearson(features[a], features[b])
                mi_m[a][b] = mi_m[b][a] = round(mi, 3)
                pe_m[a][b] = pe_m[b][a] = round(pe, 3)
    return names, mi_m, pe_m


if __name__ == "__main__":
    random.seed(42)
    n = 1500
    A = [random.gauss(0, 1) for _ in range(n)]
    feats = {
        "A": A,
        "B_linear": [0.8 * a + random.gauss(0, 0.4) for a in A],       # linear kin
        "C_square": [a * a + random.gauss(0, 0.3) for a in A],          # NONLINEAR kin
        "D_noise": [random.gauss(0, 1) for _ in range(n)],              # stranger
    }
    names, MI, PE = dependence_matrices(feats)

    print(f"{'pair':16} {'|pearson|':>9} {'norm-MI':>8}")
    for a, b in [("A", "B_linear"), ("A", "C_square"), ("A", "D_noise")]:
        print(f"  A ↔ {b:12} {PE[a][b]:>9.3f} {MI[a][b]:>8.3f}")

    # The composed claim, measured:
    assert PE["A"]["B_linear"] > 0.7 and MI["A"]["B_linear"] > 0.25, \
        "both metrics must see the linear pair"
    assert PE["A"]["C_square"] < 0.15, \
        f"Pearson must be BLIND to y=x^2: {PE['A']['C_square']}"
    assert MI["A"]["C_square"] > 3 * MI["A"]["D_noise"] and MI["A"]["C_square"] > 0.2, \
        "normalized MI must clearly light up the nonlinear pair over noise"
    assert all(MI[a][b] == MI[b][a] for a in names for b in names), "matrix symmetric"
    print("mutual_information_matrix.py PASS")
