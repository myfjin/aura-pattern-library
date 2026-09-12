"""
Hoeffding tree (VFDT) lite -- a streaming decision stump with a Hoeffding-bound split test.
Core idea: accumulate class counts on each side of every candidate split as data streams
in. After n samples the true information gain of a split is within
eps = sqrt(R^2 ln(1/delta) / 2n) of its observed gain (Hoeffding bound). Split as soon as
the best candidate's observed gain beats the runner-up's by more than eps -- then that
choice is provably the true best with prob >= 1-delta. The leaf predicts its majority class.
When: grow a decision tree online with a statistical guarantee on each split decision.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
import random
from typing import Dict, List, Tuple


def _entropy(counts: Dict[int, int]) -> float:
    tot = sum(counts.values())
    if tot == 0:
        return 0.0
    h = 0.0
    for c in counts.values():
        if c:
            p = c / tot
            h -= p * math.log2(p)
    return h


def _gain(left: Dict[int, int], right: Dict[int, int]) -> float:
    nl, nr = sum(left.values()), sum(right.values())
    n = nl + nr
    if n == 0:
        return 0.0
    parent = {k: left.get(k, 0) + right.get(k, 0) for k in set(left) | set(right)}
    return _entropy(parent) - (nl / n) * _entropy(left) - (nr / n) * _entropy(right)


def hoeffding_tree_lite(X, y, thresholds, delta: float = 1e-6):
    """
    Stream (X,y); return (split_feature, split_threshold, left_pred, right_pred, n_seen).
    split_feature is None if the Hoeffding test never fired.
    """
    n_feat = len(X[0])
    # counts[(f, thr)] = (left_class_counts, right_class_counts)
    counts = {(f, thr): ({}, {}) for f in range(n_feat) for thr in thresholds}
    for i, (x, label) in enumerate(zip(X, y)):
        for (f, thr), (lc, rc) in counts.items():
            side = lc if x[f] <= thr else rc
            side[label] = side.get(label, 0) + 1
        n = i + 1
        if n < 50:
            continue
        gains = sorted(((_gain(lc, rc), f, thr) for (f, thr), (lc, rc) in counts.items()),
                       reverse=True)
        eps = math.sqrt(1.0 * math.log(1.0 / delta) / (2 * n))   # R=log2(2 classes)=1
        if gains[0][0] - gains[1][0] > eps and gains[0][0] > 0:
            _, bf, bthr = gains[0]
            lc, rc = counts[(bf, bthr)]
            lp = max(lc, key=lc.get) if lc else 0
            rp = max(rc, key=rc.get) if rc else 0
            return bf, bthr, lp, rp, n
    return None, None, 0, 0, len(X)


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation
    thresholds = [i / 10 for i in range(1, 10)]

    def make(n):
        X = [(random.random(), random.random()) for _ in range(n)]
        # true concept: class depends on a threshold in feature 0 (a split MATTERS)
        y = [1 if x[0] > 0.6 else 0 for x in X]
        return X, y

    Xtr, ytr = make(2000)
    Xte, yte = make(2000)

    bf, bthr, lp, rp, n_seen = hoeffding_tree_lite(Xtr, ytr, thresholds)
    print(f"streaming split: feature={bf} thr={bthr} after n={n_seen}")

    def stump_acc(f, thr, lp, rp, X, y):
        return sum((lp if x[f] <= thr else rp) == t for x, t in zip(X, y)) / len(y)

    # batch best split over all training data
    best = max(((_gain(*[{c: sum(1 for x, t in zip(Xtr, ytr) if t == c and (x[f] <= thr) == side)
                          for c in (0, 1)} for side in (True, False)]), f, thr)
                for f in range(2) for thr in thresholds), key=lambda g: g[0])
    bf2, bthr2 = best[1], best[2]
    lc = {c: sum(1 for x, t in zip(Xtr, ytr) if t == c and x[bf2] <= bthr2) for c in (0, 1)}
    rc = {c: sum(1 for x, t in zip(Xtr, ytr) if t == c and x[bf2] > bthr2) for c in (0, 1)}
    blp, brp = max(lc, key=lc.get), max(rc, key=rc.get)

    stream_acc = stump_acc(bf, bthr, lp, rp, Xte, yte)
    batch_acc = stump_acc(bf2, bthr2, blp, brp, Xte, yte)
    majority = max(sum(t == 0 for t in yte), sum(t == 1 for t in yte)) / len(yte)
    print(f"test acc: streaming={stream_acc:.3f} batch={batch_acc:.3f} majority={majority:.3f}")

    # RECOVERY ASSERT 1: the Hoeffding test actually fired and picked feature 0 (the true
    # split feature) -- not "always split on 0" like the old dead code.
    assert bf == 0, f"Hoeffding tree split on the wrong feature: {bf}"

    # RECOVERY ASSERT 2: the split MATTERS -- streaming stump crushes the majority baseline
    # (impossible for the old majority-vs-majority tautology) and matches the batch stump.
    assert stream_acc > majority + 0.25, f"split adds no signal: {stream_acc:.3f} vs maj {majority:.3f}"
    assert abs(stream_acc - batch_acc) < 0.03, f"streaming != batch: {stream_acc:.3f} vs {batch_acc:.3f}"
    print("Hoeffding tree PASS")
