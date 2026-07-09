"""
Concept-drift ensemble vs a frozen single learner.
Core idea: on a stream whose concept flips, a drift-aware ensemble that spawns a fresh
learner per window and weights learners by their RECENT accuracy adapts to the new
concept, while a single learner frozen on pre-drift data keeps predicting the old one.
When: streaming classification under concept drift -- the demo MEASURES the ensemble
beating the frozen model on the post-drift segment (the defining claim, not "acc>0.4").
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
from typing import List


def _majority(labels: List[int]) -> int:
    if not labels:
        return 0
    return max(set(labels), key=labels.count)


def concept_drift_ensemble(y: List[int], window: int = 50):
    """
    Run a drift-aware windowed ensemble AND a frozen single learner over the same
    prior-shift stream; return (ensemble_postdrift_acc, single_postdrift_acc).
    Args:
        y: label stream with a concept flip at the midpoint
        window: window length for spawning/weighting learners
    """
    n = len(y)
    drift = n // 2

    # Frozen single learner: majority of the FIRST window, never updated.
    single = _majority(y[:window])

    # Drift-aware ensemble: one learner per completed window (its window-majority),
    # each weighted by accuracy over the most recent `window` labels; predict the
    # weighted-best learner. Evaluate one-step-ahead over the post-drift segment.
    learners: List[int] = []
    ens_correct = 0
    single_correct = 0
    post = 0
    for i, label in enumerate(y):
        if i % window == 0 and i >= window:
            learners.append(_majority(y[i - window:i]))
        if i >= drift:  # score only the post-drift segment
            post += 1
            recent = y[max(0, i - window):i]
            if learners and recent:
                # weight each learner by its accuracy on the recent window
                best, best_w = learners[0], -1.0
                for lp in learners:
                    w = sum(1 for t in recent if t == lp) / len(recent)
                    if w > best_w:
                        best_w, best = w, lp
                pred = best
            else:
                pred = single
            ens_correct += (pred == label)
            single_correct += (single == label)

    return ens_correct / post, single_correct / post


if __name__ == "__main__":
    random.seed(42)  # deterministic: seed BEFORE any data generation
    # Prior-shift drift: concept A = P(y=1)=0.15, concept B = P(y=1)=0.85 after flip.
    n = 4000
    y = [1 if random.random() < 0.15 else 0 for _ in range(n // 2)]
    y += [1 if random.random() < 0.85 else 0 for _ in range(n // 2)]

    ens_acc, single_acc = concept_drift_ensemble(y, window=50)
    print(f"post-drift: ensemble={ens_acc:.3f}  frozen-single={single_acc:.3f}")

    # RECOVERY ASSERT: the adaptive ensemble recovers to the new concept (~0.85) while
    # the frozen learner, stuck on the old majority (0), collapses (~0.15). The claim is
    # the GAP, measured on post-drift data -- not either number in isolation.
    assert ens_acc > 0.75, f"ensemble did not adapt to new concept: {ens_acc:.3f}"
    assert single_acc < 0.30, f"frozen learner should collapse post-drift: {single_acc:.3f}"
    assert ens_acc - single_acc > 0.40, "ensemble must beat frozen single by a real margin"
    print("Concept-drift ensemble PASS")
