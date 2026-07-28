"""Ranking metrics suite: Mean Reciprocal Rank, Precision@K, Recall@K.

MRR = mean over queries of 1/(rank of the first relevant item). Precision@K = |relevant ∩
top-K| / K. Recall@K = |relevant ∩ top-K| / |relevant|. Core claim: each metric returns its
EXACT known value on a planted ranking, and MRR falls monotonically as the first relevant
item is demoted.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Set

def reciprocal_rank(ranking: List[int], relevant: Set[int]) -> float:
    for i, item in enumerate(ranking):
        if item in relevant:
            return 1.0 / (i + 1)
    return 0.0

def mean_reciprocal_rank(rankings: List[List[int]], relevant_sets: List[Set[int]]) -> float:
    return sum(reciprocal_rank(r, s) for r, s in zip(rankings, relevant_sets)) / len(rankings)

def precision_at_k(ranking: List[int], relevant: Set[int], k: int) -> float:
    top_k = ranking[:k]
    return sum(1 for x in top_k if x in relevant) / k



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_recall_at_k(relevant):
    v = []
    if isinstance(relevant, (int, float)) and relevant <= 0:
        v.append(f"AURA-E009: relevant must be > 0, got {relevant}")
    if v:
        raise AuraInputError(v)

def recall_at_k(ranking: List[int], relevant: Set[int], k: int) -> float:
    _aura_validate_recall_at_k(relevant)
    top_k = ranking[:k]
    return sum(1 for x in top_k if x in relevant) / len(relevant) if relevant else 0.0

if __name__ == "__main__":
    # Planted: ranking [1,2,3,4,5], relevant = {2, 4}.
    ranking = [1, 2, 3, 4, 5]
    relevant = {2, 4}

    # First relevant (item 2) sits at rank 2 → RR = 1/2 exactly.
    assert abs(reciprocal_rank(ranking, relevant) - 0.5) < 1e-9, "RR: first relevant at rank 2 → 0.5"
    # Precision@3: top-3 = [1,2,3] contains {2} → 1/3.
    assert abs(precision_at_k(ranking, relevant, 3) - 1.0 / 3.0) < 1e-9, "P@3 should be 1/3"
    # Recall@3: {2} of {2,4} recovered → 1/2.
    assert abs(recall_at_k(ranking, relevant, 3) - 0.5) < 1e-9, "R@3 should be 1/2"
    # Precision@4 = 2/4 = 0.5 ; Recall@4 = 2/2 = 1.0.
    assert abs(precision_at_k(ranking, relevant, 4) - 0.5) < 1e-9, "P@4 should be 0.5"
    assert abs(recall_at_k(ranking, relevant, 4) - 1.0) < 1e-9, "R@4 should be 1.0"

    # MRR is monotone: demoting the first relevant item lowers the reciprocal rank.
    rr_ideal = reciprocal_rank([2, 1, 3, 4, 5], {2})      # rank 1 → 1.0
    rr_demoted = reciprocal_rank([1, 3, 2, 4, 5], {2})    # rank 3 → 1/3
    assert rr_ideal > rr_demoted, "MRR must drop as the relevant item is demoted"

    # Aggregate MRR over two queries: RR = 1/1 and 1/3 → mean 2/3.
    mrr = mean_reciprocal_rank([[2, 1], [1, 3, 4]], [{2}, {4}])
    assert abs(mrr - (1.0 + 1.0 / 3.0) / 2.0) < 1e-9, "Aggregate MRR should be exactly 2/3"

    print("PASS")
