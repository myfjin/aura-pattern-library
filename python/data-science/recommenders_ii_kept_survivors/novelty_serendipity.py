"""Novelty and serendipity: how unexpected / long-tail are recommendations.

Novelty is measured as the average inverse popularity of recommended items.
Long-tail, rarely-popular items score high; mainstream, frequently-popular
items score low. This is one proxy for the serendipity of a recommendation slate.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Iterable, Mapping


def novelty_score(recommendations: Iterable[int], popularity: Mapping[int, float]) -> float:
    """Return the mean inverse popularity of a recommendation list.

    Args:
        recommendations: Item identifiers recommended to the user.
        popularity:      A mapping from item id to its popularity count/score.
                         Higher value means more popular.

    Returns:
        Mean inverse popularity across the list. Long-tail items dominate.

    Guarantees:
        - Items with high popularity contribute low novelty.
        - Items with low popularity contribute high novelty.
        - Missing popularity entries are treated as popularity 1.0 (max novelty).

    Failure scenario:
        A recommender that only returns blockbuster items yields a novelty score
        near zero, indicating no serendipity.
    """
    recs = list(recommendations)
    if not recs:
        return 0.0

    def inv_pop(item: int) -> float:
        pop = popularity.get(item, 1.0)
        if pop <= 0:
            raise ValueError(f"Popularity for item {item} must be positive, got {pop}")
        return 1.0 / pop

    return sum(inv_pop(r) for r in recs) / len(recs)


def main() -> None:
    """Self-test with hand-computable planted truths."""
    popularity = {1: 100.0, 2: 80.0, 3: 50.0, 4: 20.0, 5: 5.0}

    # Popular recommendations: items 1 and 2 only.
    # Sum of inverse popularity = 1/100 + 1/80 + 1/100 + 1/80 + 1/100
    #                           = 0.01 + 0.0125 + 0.01 + 0.0125 + 0.01 = 0.055
    # Mean = 0.055 / 5 = 0.011.
    recs_popular = [1, 2, 1, 2, 1]
    novelty_popular = novelty_score(recs_popular, popularity)
    assert abs(novelty_popular - 0.011) < 1e-9, f"Expected 0.011, got {novelty_popular}"

    # Long-tail recommendations: items 5, 4, and 3.
    # Sum of inverse popularity = 1/5 + 1/20 + 1/50 + 1/5 + 1/20
    #                           = 0.2 + 0.05 + 0.02 + 0.2 + 0.05 = 0.52
    # Mean = 0.52 / 5 = 0.104.
    recs_longtail = [5, 4, 3, 5, 4]
    novelty_longtail = novelty_score(recs_longtail, popularity)
    assert abs(novelty_longtail - 0.104) < 1e-9, f"Expected 0.104, got {novelty_longtail}"

    # The core claim: long-tail recs have higher novelty than popular recs.
    assert novelty_longtail > novelty_popular, "Long-tail recs should have higher novelty"

    # Failure path: only the most popular item gives the lowest possible score.
    only_popular = novelty_score([1, 1, 1], {1: 100.0})
    assert abs(only_popular - 0.01) < 1e-9, f"Expected 0.01, got {only_popular}"

    print("PASS")


if __name__ == "__main__":
    main()
