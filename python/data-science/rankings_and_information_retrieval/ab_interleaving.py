"""
Team-Draft Interleaving for A/B Testing Rankers.

Compare two rankers (A and B) by interleaving their results in a single ranking.
Users click on interleaved results. The ranker whose document the user clicked on wins
that "team". We count wins and determine which ranker is better.
We plant a stronger ranker and verify it wins the interleaving.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Dict


def interleave_team_draft(ranking_a: List[str], ranking_b: List[str]) -> List[tuple]:
    """
    Team-draft interleaving: alternately pick the next unchosen document from A or B.
    Returns list of (doc, source) where source is 'A' or 'B'.
    """
    interleaved = []
    a_idx, b_idx = 0, 0
    teams = ["A", "B"]
    team_idx = 0

    while a_idx < len(ranking_a) or b_idx < len(ranking_b):
        source = teams[team_idx % 2]

        if source == "A" and a_idx < len(ranking_a):
            interleaved.append((ranking_a[a_idx], "A"))
            a_idx += 1
        elif source == "B" and b_idx < len(ranking_b):
            interleaved.append((ranking_b[b_idx], "B"))
            b_idx += 1
        else:
            # Fall back to other source if current is exhausted
            other = "B" if source == "A" else "A"
            if other == "B" and b_idx < len(ranking_b):
                interleaved.append((ranking_b[b_idx], "B"))
                b_idx += 1
            elif other == "A" and a_idx < len(ranking_a):
                interleaved.append((ranking_a[a_idx], "A"))
                a_idx += 1

        team_idx += 1

    return interleaved


def simulate_clicks_on_interleaving(
    interleaved: List[tuple],
    relevant_docs: set,
    click_prob_relevant: float = 0.8,
) -> Dict[str, int]:
    """
    Simulate user clicks on interleaved ranking.
    User clicks on a relevant doc with some probability.
    Returns win count for each ranker.
    """
    wins = {"A": 0, "B": 0}

    for doc, source in interleaved:
        # Click if document is relevant
        if doc in relevant_docs and random.random() < click_prob_relevant:
            wins[source] += 1

    return wins


if __name__ == "__main__":
    random.seed(42)

    # True relevant documents
    relevant_docs = {"A1", "A2", "B1", "B2"}

    # Ranker A: strong (finds most relevant docs)
    ranking_a = ["A1", "A2", "B1", "B2", "C1"]

    # Ranker B: weak (misses some relevant docs)
    ranking_b = ["B1", "C1", "A1", "A2", "C2"]

    # Interleave
    interleaved = interleave_team_draft(ranking_a, ranking_b)

    # Simulate clicks over 50 trials
    total_wins = {"A": 0, "B": 0}
    for trial in range(50):
        wins = simulate_clicks_on_interleaving(interleaved, relevant_docs, click_prob_relevant=0.7)
        total_wins["A"] += wins["A"]
        total_wins["B"] += wins["B"]

    # Check: A should win more than B
    assert total_wins["A"] > total_wins["B"], (
        f"Stronger ranker A should win more ({total_wins['A']}) than B ({total_wins['B']})"
    )

    # A's win ratio should be significant
    total_clicks = total_wins["A"] + total_wins["B"]
    a_win_ratio = total_wins["A"] / total_clicks if total_clicks > 0 else 0

    assert a_win_ratio > 0.5, (
        f"Ranker A win ratio {a_win_ratio:.2f} should be > 0.5"
    )

    print(
        f"Interleaved results: {len(interleaved)} docs | "
        f"A wins: {total_wins['A']} | B wins: {total_wins['B']} | "
        f"A win ratio: {a_win_ratio:.1%} | PASS"
    )
