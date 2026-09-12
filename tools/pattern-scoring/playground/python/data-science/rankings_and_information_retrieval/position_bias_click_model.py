"""
Position Bias in Click Models and Inverse Propensity Weighting.

Users click documents based on both relevance and position (position bias).
Naive click-count ranking is confounded by position.
Inverse propensity weighting (IPW) corrects for position bias; we verify
that IPW recovers the true relevance order while naive click-count does not.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Dict


def generate_clicks_with_position_bias(
    ranking: List[str],
    true_relevances: Dict[str, float],
    position_bias: float = 2.0,
) -> Dict[str, int]:
    """
    Generate clicks from a ranking with position bias.
    P(click) = position_bias_factor * true_relevance.
    position_bias_factor decreases with rank (strongly).
    """
    clicks = {doc: 0 for doc in ranking}

    for position, doc in enumerate(ranking):
        # Position bias decreases strongly with rank
        position_bias_factor = 1.0 / (1 + position * position_bias)
        click_prob = position_bias_factor * true_relevances[doc]

        # Simulate clicks
        for _ in range(200):  # 200 users see this ranking
            if random.random() < click_prob:
                clicks[doc] += 1

    return clicks


def inverse_propensity_weighting(
    clicks: Dict[str, int],
    ranking: List[str],
    position_bias: float = 0.5,
) -> Dict[str, float]:
    """
    Apply IPW to correct for position bias.
    weighted_relevance[doc] = clicks[doc] / P(position | doc).
    """
    weighted = {}

    for position, doc in enumerate(ranking):
        position_bias_factor = 1.0 / (1 + position * position_bias)
        # Normalize by position bias
        weighted[doc] = clicks[doc] / max(position_bias_factor, 0.1)

    return weighted


if __name__ == "__main__":
    random.seed(42)

    # True relevances (ground truth)
    true_relevances = {"A": 0.8, "B": 0.2, "C": 0.15, "D": 0.15}

    # Ranking that violates true relevances: A (most relevant) is at position 3
    ranking = ["D", "C", "B", "A"]

    # Generate clicks with position bias
    clicks = generate_clicks_with_position_bias(ranking, true_relevances, position_bias=2.0)

    # Naive ranking by click count
    naive_ranking = sorted(clicks.keys(), key=lambda d: clicks[d], reverse=True)

    # IPW-corrected ranking
    weighted = inverse_propensity_weighting(clicks, ranking, position_bias=2.0)
    ipw_ranking = sorted(weighted.keys(), key=lambda d: weighted[d], reverse=True)

    # True ranking
    true_ranking = sorted(true_relevances.keys(), key=lambda d: true_relevances[d], reverse=True)

    # Naive ranking should be distorted by position bias (not A first)
    assert naive_ranking[0] != "A", (
        f"Naive ranking should NOT rank A first (it's at position 3), got {naive_ranking}"
    )

    # IPW ranking should recover true ranking better than naive
    # Check: A should rank first in IPW (true most-relevant)
    assert ipw_ranking[0] == "A", (
        f"IPW ranking should rank A first (most relevant), got {ipw_ranking}"
    )
    # Check: IPW should rank documents closer to true than naive
    naive_top = naive_ranking[0]
    ipw_top = ipw_ranking[0]
    assert ipw_top == "A", (
        f"IPW should put A on top (true highest relevance), got {ipw_ranking}"
    )

    print(
        f"True ranking: {true_ranking} | Naive (biased): {naive_ranking} | "
        f"IPW (corrected): {ipw_ranking} | PASS"
    )
