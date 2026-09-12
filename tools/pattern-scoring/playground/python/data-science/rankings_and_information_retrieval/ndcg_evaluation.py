"""
NDCG (Normalized Discounted Cumulative Gain).

Evaluate ranking quality: DCG sums relevance scores discounted by position.
NDCG normalizes DCG by ideal DCG (perfect ranking).
Perfect ranking = NDCG 1.0, shuffled = lower score.
We verify on a hand-computed example and show degraded ranking scores lower.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List


def dcg(relevances: List[float]) -> float:
    """Discounted Cumulative Gain: DCG = Σ (rel[i] / log2(i+2))."""
    return sum(rel / math.log2(i + 2) for i, rel in enumerate(relevances))


def ndcg(predicted_relevances: List[float], ideal_relevances: List[float]) -> float:
    """NDCG: DCG(predicted) / DCG(ideal)."""
    dcg_pred = dcg(predicted_relevances)
    dcg_ideal = dcg(ideal_relevances)
    if dcg_ideal == 0:
        return 0.0
    return dcg_pred / dcg_ideal


if __name__ == "__main__":
    # Hand-computed example: 4 results with ideal relevances [3, 2, 1, 0]
    ideal = [3.0, 2.0, 1.0, 0.0]
    perfect = [3.0, 2.0, 1.0, 0.0]
    degraded = [0.0, 0.0, 0.0, 3.0]  # Worst: highest relevance last

    # Compute DCG for hand-verified example
    # ideal DCG = 3/log2(2) + 2/log2(3) + 1/log2(4) + 0/log2(5)
    #           = 3/1 + 2/1.585 + 1/2 + 0
    #           = 3 + 1.262 + 0.5 + 0 = 4.762
    dcg_ideal_computed = dcg(ideal)
    expected_ideal_dcg = 3.0 / math.log2(2) + 2.0 / math.log2(3) + 1.0 / math.log2(4)

    assert abs(dcg_ideal_computed - expected_ideal_dcg) < 0.01, (
        f"Ideal DCG mismatch: {dcg_ideal_computed:.2f} vs {expected_ideal_dcg:.2f}"
    )

    # Perfect ranking should have NDCG = 1.0
    ndcg_perfect = ndcg(perfect, ideal)
    assert abs(ndcg_perfect - 1.0) < 0.01, (
        f"Perfect ranking NDCG should be ~1.0, got {ndcg_perfect:.2f}"
    )

    # Degraded (reversed) ranking should have much lower NDCG
    ndcg_degraded = ndcg(degraded, ideal)
    assert ndcg_degraded < 0.5, (
        f"Degraded ranking NDCG should be < 0.5, got {ndcg_degraded:.2f}"
    )

    # Degraded must score much lower than perfect
    assert ndcg_perfect > 2 * ndcg_degraded, (
        f"Perfect NDCG {ndcg_perfect:.2f} should be >> degraded {ndcg_degraded:.2f}"
    )

    print(
        f"Ideal DCG: {dcg_ideal_computed:.2f} | Perfect NDCG: {ndcg_perfect:.2f} | "
        f"Degraded NDCG: {ndcg_degraded:.2f} | Ratio: {ndcg_perfect/ndcg_degraded:.1f}x | PASS"
    )
