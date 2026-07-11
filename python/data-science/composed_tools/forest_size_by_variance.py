"""
Forest Size by Variance — stop hiring trees when the crew is steady enough.

FUSED-BRIDGE COMPOSED PATTERN: bias_variance_decomposition (Model Diagnostics) x
random_forest (Ensembles & Robust) — proposed by BOTH signals 2026-07-10:
structural edge `matrix` (a data matrix flows into the diagnostic that wraps the
forest) + semantic 0.429. Practitioners guess n_trees (a default 100) or grid-
search it. The composition runs the bias-variance decomposition's bootstrap
estimator ACROSS forest sizes: bias stays flat (more trees don't change what the
forest is biased toward) while ensemble variance falls as ~1/n. HONEST PHYSICS:
independent trees give NO hard plateau — variance keeps decaying 1/n; a true
plateau needs correlated trees (variance -> rho*sigma^2). So the data-driven size
is the DIMINISHING-RETURNS knee: the smallest forest that captures most of the
achievable variance reduction, past which each doubling buys little.

Human logic of the name: you keep adding workers until the crew is steady
enough — the point where one more worker barely reduces the wobble.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import Dict, List, Tuple

Point = Tuple[float, float]


# ── parent mechanism: random forest (bootstrap trees + random feature splits) ──
def gini(labels: List[int]) -> float:
    if not labels:
        return 0.0
    p = sum(labels) / len(labels)
    return 1.0 - (p * p + (1 - p) * (1 - p))


def build_stump(X: List[Point], y: List[int], rng: random.Random) -> dict:
    """Depth-limited tree (a small tree keeps single-tree variance high, so the
    ensemble's variance-reduction is visible)."""
    best = None
    feats = [rng.randint(0, 1)]                       # random feature subset
    for f in feats:
        vals = sorted(set(p[f] for p in X))
        for k in range(1, len(vals)):
            thr = (vals[k - 1] + vals[k]) / 2
            ly = [y[i] for i in range(len(X)) if X[i][f] <= thr]
            ry = [y[i] for i in range(len(X)) if X[i][f] > thr]
            if not ly or not ry:
                continue
            imp = (len(ly) * gini(ly) + len(ry) * gini(ry)) / len(X)
            if best is None or imp < best[0]:
                lp = 1 if sum(ly) * 2 >= len(ly) else 0
                rp = 1 if sum(ry) * 2 >= len(ry) else 0
                best = (imp, f, thr, lp, rp)
    if best is None:
        return {"leaf": 1 if sum(y) * 2 >= len(y) else 0}
    _, f, thr, lp, rp = best
    return {"f": f, "thr": thr, "l": lp, "r": rp}


def predict_stump(x: Point, t: dict) -> int:
    if "leaf" in t:
        return t["leaf"]
    return t["l"] if x[t["f"]] <= t["thr"] else t["r"]


def random_forest(X: List[Point], y: List[int], n_trees: int, rng: random.Random) -> List[dict]:
    trees = []
    for _ in range(n_trees):
        idx = [rng.randint(0, len(X) - 1) for _ in range(len(X))]     # bootstrap
        trees.append(build_stump([X[i] for i in idx], [y[i] for i in idx], rng))
    return trees


def predict_forest(x: Point, forest: List[dict]) -> float:
    return sum(predict_stump(x, t) for t in forest) / len(forest)     # vote fraction


# ── parent mechanism: bootstrap bias/variance at fixed test points ──
def bias_variance_at_size(X, y, test_pts, truth, n_trees, n_boot, base_seed):
    """The bias-variance decomposition procedure applied to a forest of a given
    size: over many independently-seeded forests, per test point measure the
    mean prediction (for bias) and its spread (for variance)."""
    preds = [[] for _ in test_pts]
    for b in range(n_boot):
        rng = random.Random(base_seed * 1000 + b)
        forest = random_forest(X, y, n_trees, rng)
        for j, xt in enumerate(test_pts):
            preds[j].append(predict_forest(xt, forest))
    var = sum(_variance(p) for p in preds) / len(preds)
    bias2 = sum((sum(p) / len(p) - truth[j]) ** 2 for j, p in enumerate(preds)) / len(preds)
    return bias2, var


def _variance(v: List[float]) -> float:
    m = sum(v) / len(v)
    return sum((x - m) ** 2 for x in v) / len(v)


if __name__ == "__main__":
    random.seed(42)
    rng = random.Random(42)

    # Two gaussian classes; a diagonal boundary a stump can only crudely fit
    # (so single trees are high-variance and the ensemble has room to steady).
    X: List[Point] = []
    y: List[int] = []
    for _ in range(200):
        a = (rng.gauss(0, 1.2), rng.gauss(0, 1.2))
        X.append(a)
        y.append(1 if a[0] + a[1] > 0 else 0)
    test_pts = [(rng.gauss(0, 1.2), rng.gauss(0, 1.2)) for _ in range(40)]
    truth = [1.0 if p[0] + p[1] > 0 else 0.0 for p in test_pts]

    sizes = [1, 2, 4, 8, 16, 32]
    curve = [(n, *bias_variance_at_size(X, y, test_pts, truth, n, 12, 7)) for n in sizes]
    for n, b2, v in curve:
        print(f"  trees={n:2d}  bias²={b2:.3f}  variance={v:.4f}")

    variances = [v for _, _, v in curve]
    biases = [b for _, b, _ in curve]

    # DIMINISHING-RETURNS KNEE: the smallest forest that captures >= 80% of the
    # total achievable variance reduction. Below it you're leaving real steadiness
    # on the table; past it each doubling buys the remaining <20%.
    total_drop = variances[0] - variances[-1]
    captured_target = 0.80 * total_drop
    chosen = sizes[-1]
    for n, _, v in curve:
        if (variances[0] - v) >= captured_target:
            chosen = n
            break
    captured = (variances[0] - variances[sizes.index(chosen)]) / total_drop
    print(f"chosen forest size (80% variance-reduction knee): {chosen} "
          f"(captures {captured:.0%} of the achievable reduction)")

    # The composed claim, three parts measured:
    assert variances[0] > variances[-1] * 3, \
        f"variance must fall substantially with more trees: {variances[0]:.4f} -> {variances[-1]:.4f}"
    assert max(biases) - min(biases) < 0.3 * total_drop, \
        "bias should stay ~flat while variance falls (the whole premise)"
    below = variances[max(0, sizes.index(chosen) - 1)]
    assert below > variances[sizes.index(chosen)] * 1.3, \
        "a smaller forest than the knee must be measurably wobblier (knee isn't premature)"
    assert 4 <= chosen <= 16, f"the knee should be an interior size, not the extremes: {chosen}"
    print("forest_size_by_variance.py PASS")
