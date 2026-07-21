"""Intra-list diversity (ILD) of a recommendation list.

ILD measures how different the recommended items are from one another by
averaging pairwise dissimilarity over the list. Higher ILD means the list is
more varied; lower ILD means the items are more similar.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import Sequence


def intra_list_diversity(items: Sequence[Sequence[float]]) -> float:
    """Return the average pairwise Euclidean distance across a list of items.

    Args:
        items: A sequence of item vectors. All vectors must have the same length.

    Returns:
        Mean pairwise Euclidean distance, or 0.0 if fewer than 2 items are given.

    Guarantees:
        - Identical items have ILD 0.0.
        - Orthonormal one-hot vectors in an n-dimensional space have ILD sqrt(2).

    Failure scenario:
        A recommender that returns the same item repeatedly yields ILD 0.0,
        signalling a lack of variety in the slate.
    """
    n = len(items)
    if n < 2:
        return 0.0
    dim = len(items[0])
    if any(len(v) != dim for v in items):
        raise ValueError("All item vectors must have the same dimension")

    total = 0.0
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            distance = math.sqrt(
                sum((items[i][k] - items[j][k]) ** 2 for k in range(dim))
            )
            total += distance
            count += 1
    return total / count if count > 0 else 0.0


def main() -> None:
    """Self-test with hand-computable planted truths."""
    # Three orthonormal one-hot vectors in R^3.
    # Pairwise distances: each pair differs by exactly two coordinates,
    # so every distance is sqrt((1-0)^2 + (0-1)^2) = sqrt(2).
    # There are C(3,2) = 3 pairs, so ILD = sqrt(2).
    list_diverse = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    ild_diverse = intra_list_diversity(list_diverse)
    expected_diverse = math.sqrt(2.0)
    assert abs(ild_diverse - expected_diverse) < 1e-9, f"Expected {expected_diverse}, got {ild_diverse}"

    # Three identical vectors: every pairwise distance is 0.0.
    list_narrow = [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
    ild_narrow = intra_list_diversity(list_narrow)
    assert ild_narrow == 0.0, f"Expected 0.0, got {ild_narrow}"

    # The core claim: diverse list has higher ILD than narrow list.
    assert ild_diverse > ild_narrow, "Diverse list should have higher intra-list diversity"

    # Failure path: fewer than 2 items yields zero diversity.
    assert intra_list_diversity([[1.0, 0.0, 0.0]]) == 0.0, "Single-item list must have ILD 0.0"

    print("PASS")


if __name__ == "__main__":
    main()
