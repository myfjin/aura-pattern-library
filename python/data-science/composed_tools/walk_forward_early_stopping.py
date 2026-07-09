"""
Walk-Forward Early Stopping — training halted by the future, not by a random split.

COMPOSED PATTERN: early_stopping (Neural Networks) x walk_forward_validation
(Time Series) — embedding bridge 0.502, found 2026-07-06. Both parents encode
the same ethic — judge yourself only on data from AFTER your training window —
and their child is a tool neither field names: iterative training (here,
gradient-boosted stumps on lag features) monitored per-round on a FORWARD
time window, stopped with patience when forward error degrades. A random
validation split would leak future regime into training; the forward window
cannot.

Use when: tuning training duration/rounds for any iterative model on
time-ordered data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple

Stump = Tuple[int, float, float, float]  # (feature, threshold, left_val, right_val)


def fit_stump_to_residuals(X: List[List[float]], r: List[float]) -> Stump:
    best = (0, 0.0, 0.0, 0.0)
    best_sse = float("inf")
    for f in range(len(X[0])):
        vals = sorted(set(x[f] for x in X))
        for k in range(1, len(vals)):
            thr = (vals[k - 1] + vals[k]) / 2.0
            left = [r[i] for i in range(len(X)) if X[i][f] <= thr]
            right = [r[i] for i in range(len(X)) if X[i][f] > thr]
            lm = sum(left) / len(left) if left else 0.0
            rm = sum(right) / len(right) if right else 0.0
            sse = sum((v - lm) ** 2 for v in left) + sum((v - rm) ** 2 for v in right)
            if sse < best_sse:
                best_sse, best = sse, (f, thr, lm, rm)
    return best


def predict_stump(x: List[float], s: Stump) -> float:
    f, thr, lm, rm = s
    return lm if x[f] <= thr else rm


def predict_ensemble(x: List[float], stumps: List[Stump], lr: float) -> float:
    return sum(lr * predict_stump(x, s) for s in stumps)


def mae(y_true: List[float], y_pred: List[float]) -> float:
    return sum(abs(a - b) for a, b in zip(y_true, y_pred)) / len(y_true)


if __name__ == "__main__":
    random.seed(42)

    # Noisy trend+season series; lag features [y_{t-1}, y_{t-2}, y_{t-3}].
    n = 110
    y = [0.03 * t + 2.0 * math.sin(2 * math.pi * t / 25) + random.gauss(0, 0.8)
         for t in range(n)]
    rows = [([y[t - 1], y[t - 2], y[t - 3]], y[t]) for t in range(3, n)]

    # WALK-FORWARD split: train on the past, validate on the NEXT window.
    split = 80
    X_tr = [x for x, _ in rows[:split]]
    y_tr = [v for _, v in rows[:split]]
    X_fw = [x for x, _ in rows[split:]]
    y_fw = [v for _, v in rows[split:]]

    lr, max_rounds, patience = 0.4, 120, 15
    stumps: List[Stump] = []
    fit_tr = [0.0] * len(X_tr)
    forward_curve: List[float] = []
    best_fw, best_round, since_best = float("inf"), 0, 0
    stopped_at = max_rounds

    for rnd in range(1, max_rounds + 1):
        residuals = [y_tr[i] - fit_tr[i] for i in range(len(X_tr))]
        s = fit_stump_to_residuals(X_tr, residuals)
        stumps.append(s)
        for i in range(len(X_tr)):
            fit_tr[i] += lr * predict_stump(X_tr[i], s)
        fw_err = mae(y_fw, [predict_ensemble(x, stumps, lr) for x in X_fw])
        forward_curve.append(fw_err)
        if fw_err < best_fw - 1e-9:
            best_fw, best_round, since_best = fw_err, rnd, 0
        else:
            since_best += 1
            if since_best >= patience and stopped_at == max_rounds:
                stopped_at = rnd     # early stop fires; keep going only to
                                     # MEASURE what we were saved from

    final_fw = forward_curve[-1]
    train_final = mae(y_tr, fit_tr)

    print(f"train MAE at round {max_rounds}: {train_final:.3f} (memorizing noise)")
    print(f"forward MAE: best {best_fw:.3f} @ round {best_round} · "
          f"final {final_fw:.3f} @ round {max_rounds} · early-stopped @ {stopped_at}")

    # The composed claim, measured:
    # 1. training kept "improving" long after the forward window said stop
    assert train_final < best_fw, "training error should undercut forward error (overfit)"
    # 2. the forward curve is a U: continuing past the best round HURT
    assert final_fw > best_fw * 1.05, \
        f"no overfit detected: final {final_fw:.3f} vs best {best_fw:.3f}"
    # 3. early stopping fired before the end and near the true minimum
    assert stopped_at < max_rounds, "early stopping never fired"
    assert stopped_at - best_round == patience, \
        "stop should fire exactly `patience` rounds after the forward minimum"
    print("walk_forward_early_stopping.py PASS")
