"""
Reciprocal Rank Fusion (RRF).

Combine multiple rankers via RRF: score = Σ (1 / (k + rank_i)).
Fusion often beats individual rankers on noisy signals.
We plant two mediocre rankers and show that fusing them recovers better ranking.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict


def rrf_score(item: str, rankings: List[List[str]], k: int = 60) -> float:
    """
    RRF score for an item across multiple rankings.
    score = Σ (1 / (k + rank + 1)) for each ranking.
    """
    score = 0.0
    for ranking in rankings:
        if item in ranking:
            rank = ranking.index(item)
            score += 1.0 / (k + rank + 1)
    return score


def rrf_fusion(rankings: List[List[str]], k: int = 60) -> List[str]:
    """Fuse multiple rankings via RRF, return sorted by RRF score."""
    all_items = set()
    for ranking in rankings:
        all_items.update(ranking)

    scores = {item: rrf_score(item, rankings, k) for item in all_items}
    return sorted(all_items, key=lambda x: scores[x], reverse=True)


def ndcg_simple(ranking: List[str], ideal_order: List[str]) -> float:
    """Compute NDCG for a ranking against ideal order."""
    import math

    relevances = [1.0 if item in ideal_order[:i+1] else 0.0 for i, item in enumerate(ranking)]
    dcg = sum(rel / math.log2(i + 2) for i, rel in enumerate(relevances))

    ideal_relevances = [1.0] * len(ideal_order)
    ideal_dcg = sum(rel / math.log2(i + 2) for i, rel in enumerate(ideal_relevances))

    return dcg / ideal_dcg if ideal_dcg > 0 else 0.0


if __name__ == "__main__":
    # Ideal ranking (ground truth)
    ideal = ["A", "B", "C", "D", "E"]

    # Two mediocre rankers: each gets about 60% right, but disagree on specifics
    ranker1 = ["A", "C", "B", "E", "D"]  # Good: A first, but B and C swapped
    ranker2 = ["B", "A", "D", "C", "E"]  # Good: A and B in top 2, but D misplaced

    # Individual NDCG scores (should be moderate)
    ndcg1 = ndcg_simple(ranker1, ideal)
    ndcg2 = ndcg_simple(ranker2, ideal)

    # Fuse
    fused = rrf_fusion([ranker1, ranker2], k=60)
    ndcg_fused = ndcg_simple(fused, ideal)

    # Assertion: fused should beat both individual rankers
    assert ndcg_fused > ndcg1, (
        f"Fused NDCG {ndcg_fused:.2f} should beat ranker1 {ndcg1:.2f}"
    )
    assert ndcg_fused > ndcg2, (
        f"Fused NDCG {ndcg_fused:.2f} should beat ranker2 {ndcg2:.2f}"
    )

    # Average individual score
    avg_individual = (ndcg1 + ndcg2) / 2
    assert ndcg_fused > avg_individual, (
        f"Fused {ndcg_fused:.2f} should beat average individual {avg_individual:.2f}"
    )

    print(
        f"Ranker1 NDCG: {ndcg1:.2f} | Ranker2 NDCG: {ndcg2:.2f} | "
        f"Avg individual: {avg_individual:.2f} | Fused: {ndcg_fused:.2f} | PASS"
    )
