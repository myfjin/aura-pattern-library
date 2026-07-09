"""User-based collaborative filtering.

Core idea: compute cosine similarity between user rating vectors, then predict
ratings for unseen items as a weighted average of similar users' ratings.

When to use: when you have user×item rating data and want to leverage user
similarities to make personalized recommendations.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Dict, Tuple, List


def cosine_similarity(vec_a: Dict[int, float], vec_b: Dict[int, float]) -> float:
    """Compute cosine similarity between two sparse vectors."""
    dot_product = sum(vec_a.get(k, 0) * vec_b.get(k, 0) for k in set(vec_a) | set(vec_b))
    norm_a = math.sqrt(sum(v**2 for v in vec_a.values()))
    norm_b = math.sqrt(sum(v**2 for v in vec_b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)


def predict_rating(
    user_id: int,
    item_id: int,
    ratings: Dict[int, Dict[int, float]],
    k: int = 3,
) -> float:
    """Predict rating for user_id, item_id using k nearest neighbor users."""
    if user_id not in ratings:
        return 2.5

    user_vec = ratings[user_id]

    # Find k most similar users who have rated item_id
    similarities: List[Tuple[float, int]] = []
    for other_user_id, other_ratings in ratings.items():
        if other_user_id != user_id and item_id in other_ratings:
            sim = cosine_similarity(user_vec, other_ratings)
            similarities.append((sim, other_user_id))

    similarities.sort(reverse=True)
    neighbors = similarities[:k]

    if not neighbors:
        return 2.5

    total_sim = sum(sim for sim, _ in neighbors)
    if total_sim == 0:
        return 2.5

    weighted_sum = sum(sim * ratings[nid][item_id] for sim, nid in neighbors)
    return weighted_sum / total_sim


if __name__ == "__main__":
    random.seed(42)

    # Synthetic rating matrix: 5 users, 5 items (1-5 scale)
    # User 0: likes items 0,1,2 (high ratings)
    # User 1: likes items 1,2,3
    # User 2: likes items 2,3,4
    # User 3: likes items 0,1 (similar to user 0)
    # User 4: sparse (only 1 rating)

    ratings: Dict[int, Dict[int, float]] = {
        0: {0: 5.0, 1: 5.0, 2: 4.0},
        1: {1: 4.0, 2: 5.0, 3: 4.0},
        2: {2: 4.0, 3: 5.0, 4: 5.0},
        3: {0: 5.0, 1: 4.0},
        4: {0: 3.0},
    }

    # Hold out one rating for testing: user 0, item 3
    held_out_rating = ratings[0].pop(3, None)
    test_rating = 4.5  # planted true rating

    # Predict the held-out rating
    predicted = predict_rating(0, 3, ratings, k=2)

    # User 0 should be similar to user 1 (both like 1,2 highly)
    # User 1 rated item 3 as 4.0, so prediction should be close
    error = abs(predicted - test_rating)

    # Restore for final check
    ratings[0][3] = test_rating

    assert error < 1.5, f"Prediction error {error} exceeds tolerance; predicted {predicted}, true {test_rating}"
    print(f"user_based_cf.py: predicted={predicted:.2f}, true={test_rating}, error={error:.2f} PASS")
