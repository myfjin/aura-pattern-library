"""Item-based collaborative filtering.

Core idea: compute adjusted-cosine similarity between item rating vectors
(normalize by subtracting per-user mean), then recommend top-k unseen items
using weighted similarity to items the user has already rated.

When to use: when items have similar rating patterns across users and you want
item-stability (item similarities change less frequently than user similarities).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Dict, List, Tuple


def adjusted_cosine_similarity(
    item_a: Dict[int, float],
    item_b: Dict[int, float],
    user_means: Dict[int, float],
) -> float:
    """
    Compute adjusted-cosine similarity: normalize each user's rating
    by subtracting the user's mean before computing cosine.
    """
    common_users = set(item_a.keys()) & set(item_b.keys())
    if not common_users:
        return 0.0

    adj_a = {u: item_a[u] - user_means[u] for u in common_users}
    adj_b = {u: item_b[u] - user_means[u] for u in common_users}

    dot_product = sum(adj_a[u] * adj_b[u] for u in common_users)
    norm_a = math.sqrt(sum(v**2 for v in adj_a.values()))
    norm_b = math.sqrt(sum(v**2 for v in adj_b.values()))

    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)


def recommend_items(
    user_id: int,
    ratings_by_user: Dict[int, Dict[int, float]],
    ratings_by_item: Dict[int, Dict[int, float]],
    k: int = 3,
) -> List[Tuple[int, float]]:
    """
    Recommend top-k unseen items for a user based on item similarity
    to items they have already rated.
    """
    if user_id not in ratings_by_user:
        return []

    user_rated_items = set(ratings_by_user[user_id].keys())

    # Compute per-user means
    user_means: Dict[int, float] = {}
    for uid, item_ratings in ratings_by_user.items():
        if item_ratings:
            user_means[uid] = sum(item_ratings.values()) / len(item_ratings)
        else:
            user_means[uid] = 0.0

    # Score unseen items
    item_scores: Dict[int, float] = {}
    for item_id, item_raters in ratings_by_item.items():
        if item_id in user_rated_items:
            continue  # Skip already-rated items

        # Weighted average of similarities to user's rated items
        sim_sum = 0.0
        weight_sum = 0.0
        for rated_item_id in user_rated_items:
            sim = adjusted_cosine_similarity(
                ratings_by_item[item_id],
                ratings_by_item[rated_item_id],
                user_means,
            )
            user_rating = ratings_by_user[user_id][rated_item_id]
            sim_sum += sim * user_rating
            weight_sum += abs(sim)

        if weight_sum > 0:
            item_scores[item_id] = sim_sum / weight_sum

    # Return top-k
    top_items = sorted(item_scores.items(), key=lambda x: x[1], reverse=True)[:k]
    return top_items


if __name__ == "__main__":
    random.seed(42)

    # Synthetic data: 4 users, 5 items
    ratings_by_user: Dict[int, Dict[int, float]] = {
        0: {0: 5.0, 1: 4.0},
        1: {1: 4.0, 2: 5.0},
        2: {2: 5.0, 3: 4.0},
        3: {0: 3.0, 3: 4.0, 4: 5.0},
    }

    # Invert to item view
    ratings_by_item: Dict[int, Dict[int, float]] = {}
    for user_id, items in ratings_by_user.items():
        for item_id, rating in items.items():
            if item_id not in ratings_by_item:
                ratings_by_item[item_id] = {}
            ratings_by_item[item_id][user_id] = rating

    # Recommend for user 0 (who rated items 0,1)
    # Items 2,3 are similar to items already rated
    recommendations = recommend_items(0, ratings_by_user, ratings_by_item, k=2)

    assert len(recommendations) > 0, "No recommendations generated"
    assert all(item_id not in ratings_by_user[0] for item_id, _ in recommendations), \
        "Recommended an already-rated item"

    # Check that at least one unseen item is scored
    unseen_items = set(range(5)) - set(ratings_by_user[0].keys())
    recommended_items = set(item_id for item_id, _ in recommendations)
    assert len(recommended_items & unseen_items) > 0, "No unseen items in recommendations"

    print(f"item_based_cf.py: recommendations={recommendations} PASS")
