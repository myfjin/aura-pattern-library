import math
"""
Target encoding with smoothing + out-of-fold fitting.

Target (mean) encoding replaces a category with the mean target of that
category — powerful, and the classic way to leak: if the encoding is fit on
data that includes the rows being encoded (or the test set), the feature
memorizes target noise and shows FAKE predictive skill. Two defenses, both
implemented here: SMOOTHING (shrink rare-category means toward the global
prior: (sum + a*prior)/(count + a)) and OUT-OF-FOLD fitting (each training
row is encoded using an encoding fit WITHOUT its own fold; test rows use an
encoding fit on all of train).

The demo plants PURE-NOISE targets, so any measured "skill" is fabricated:
leaky encoding shows high test correlation on noise; OOF shows ≈ zero — the
truth. Use when: encoding high-cardinality categoricals for models.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from collections import defaultdict
from typing import Dict, List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_fit_encoding(alpha):
    v = []
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    if isinstance(alpha, (int, float)) and math.isfinite(alpha) and alpha < 0:
        v.append(f"AURA-E-B5: alpha must be >= 0, got {alpha}")  # domain: smoothing strength
    if v:
        raise AuraInputError(v)

def _aura_validate_oof_encode_train(alpha):
    v = []
    if isinstance(alpha, (int, float)) and not math.isfinite(alpha):
        v.append(f"AURA-E008: alpha must be finite, got {alpha}")
    if isinstance(alpha, (int, float)) and math.isfinite(alpha) and alpha < 0:
        v.append(f"AURA-E-B5: alpha must be >= 0, got {alpha}")  # domain: smoothing strength
    if v:
        raise AuraInputError(v)

def fit_encoding(cats: List[str], targets: List[int],
                 alpha: float = 0.0) -> Dict[str, float]:
    """Category → smoothed mean target: (sum + alpha*prior) / (count + alpha).
    alpha=0 gives the raw (unsmoothed) mean."""
    _aura_validate_fit_encoding(alpha)
    sums: Dict[str, float] = defaultdict(float)
    counts: Dict[str, int] = defaultdict(int)
    for c, t in zip(cats, targets):
        sums[c] += t
        counts[c] += 1
    prior = sum(targets) / len(targets) if targets else 0.5
    return {c: (sums[c] + alpha * prior) / (counts[c] + alpha) for c in sums}


def apply_encoding(cats: List[str], enc: Dict[str, float],
                   default: float) -> List[float]:
    return [enc.get(c, default) for c in cats]


def oof_encode_train(cats: List[str], targets: List[int], n_folds: int = 5,
                     alpha: float = 5.0) -> List[float]:
    """TRUE out-of-fold: row i's encoding is fit on every fold EXCEPT row i's,
    so no training row's own target ever enters its own feature value."""
    _aura_validate_oof_encode_train(alpha)
    prior = sum(targets) / len(targets)
    folds = [i % n_folds for i in range(len(cats))]
    out = [0.0] * len(cats)
    for k in range(n_folds):
        fit_c = [c for c, f in zip(cats, folds) if f != k]
        fit_t = [t for t, f in zip(targets, folds) if f != k]
        enc = fit_encoding(fit_c, fit_t, alpha=alpha)
        for i, (c, f) in enumerate(zip(cats, folds)):
            if f == k:
                out[i] = enc.get(c, prior)
    return out


def abs_correlation(X: List[float], y: List[int]) -> float:
    n = len(X)
    mx, my = sum(X) / n, sum(y) / n
    cov = sum((X[i] - mx) * (y[i] - my) for i in range(n)) / n
    vx = sum((x - mx) ** 2 for x in X) / n
    vy = sum((v - my) ** 2 for v in y) / n
    if vx <= 1e-12 or vy <= 1e-12:
        return 0.0
    return abs(cov / (vx * vy) ** 0.5)


if __name__ == "__main__":
    random.seed(42)

    # 80 categories × 5 rows — HIGH-cardinality, RARE categories (the exact
    # regime the docstring names, and where leakage bites hardest: rarer
    # categories have noisier means, so a leaky fit memorizes more noise).
    # INTERLEAVED so every category appears in both splits (no unseen-category
    # artifact). Targets are PURE NOISE: honest predictive power is ZERO.
    n_cats, per_cat = 80, 5
    rows: List[Tuple[str, int]] = [(f"cat_{i % n_cats:02d}", random.randint(0, 1))
                                   for i in range(n_cats * per_cat)]
    split = int(0.7 * len(rows))
    train, test = rows[:split], rows[split:]
    c_tr, y_tr = [c for c, _ in train], [t for _, t in train]
    c_te, y_te = [c for c, _ in test], [t for _, t in test]
    prior = sum(y_tr) / len(y_tr)

    # LEAKY: encoding fit on train+test together (test targets leak into the
    # feature) → fake test-set "skill" on pure noise.
    enc_leaky = fit_encoding(c_tr + c_te, y_tr + y_te, alpha=0.0)
    corr_test_leaky = abs_correlation(apply_encoding(c_te, enc_leaky, prior), y_te)

    # PROPER: OOF for train rows, train-only fit (smoothed) for test rows.
    X_tr_oof = oof_encode_train(c_tr, y_tr, n_folds=5, alpha=5.0)
    enc_train_only = fit_encoding(c_tr, y_tr, alpha=5.0)
    corr_test_proper = abs_correlation(apply_encoding(c_te, enc_train_only, prior), y_te)
    corr_train_oof = abs_correlation(X_tr_oof, y_tr)

    # SMOOTHING: a rare category (2 rows, both target=1) must be pulled toward
    # the prior by smoothing, not trusted at its raw mean of 1.0.
    rare_c = ["rare", "rare"] + c_tr
    rare_y = [1, 1] + y_tr
    raw = fit_encoding(rare_c, rare_y, alpha=0.0)["rare"]
    smooth = fit_encoding(rare_c, rare_y, alpha=5.0)["rare"]
    rare_prior = sum(rare_y) / len(rare_y)

    print(f"pure-noise targets — honest skill is ZERO everywhere")
    print(f"  leaky  test |corr|: {corr_test_leaky:.3f}   (fabricated by leakage)")
    print(f"  proper test |corr|: {corr_test_proper:.3f}   (the truth)")
    print(f"  OOF   train |corr|: {corr_train_oof:.3f}   (no self-memorization)")
    print(f"  smoothing: rare cat raw {raw:.2f} → smoothed {smooth:.2f} "
          f"(prior {rare_prior:.2f})")

    # The claim, measured directly:
    assert corr_test_leaky > 0.30, \
        f"leaky encoding should fabricate test skill on noise: {corr_test_leaky:.3f}"
    assert corr_test_proper < 0.15, \
        f"proper encoding must show ~zero test skill on noise: {corr_test_proper:.3f}"
    assert corr_train_oof < 0.15, \
        f"OOF must not memorize its own training targets: {corr_train_oof:.3f}"
    assert abs(smooth - rare_prior) < abs(raw - rare_prior), \
        "smoothing must pull a rare category toward the prior"

    print("\ntarget_encoding_smoothing.py PASS")
