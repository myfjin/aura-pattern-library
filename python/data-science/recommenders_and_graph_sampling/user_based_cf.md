# user based cf

**Language:** Python · **Sphere:** data-science · **Category:** Recommenders & Graph Sampling

**Signature:** `(vec_a: Dict[int, float], vec_b: Dict[int, float]) → float`

## What it does

User-based collaborative filtering.

Core idea: compute cosine similarity between user rating vectors, then predict
ratings for unseen items as a weighted average of similar users' ratings.

When to use: when you have user×item rating data and want to leverage user
similarities to make personalized recommendations.

## Guarantee

When it runs, user based cf guarantees error < 1.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `error < 1.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def cosine_similarity(vec_a: Dict[int, float], vec_b: Dict[int, float]) -> float:`, `def predict_rating(user_id: int, item_id: int, ratings: Dict[int, Dict[int, float]], k: int = 3,) -> float:`
**Valid input:** `ratings` is a non-empty user×item rating matrix; `user_id` and `item_id` are keys (or at least `user_id` is present); `k >= 1`; ratings are numeric.
**Core:** User-based collaborative filtering: predicts a rating for `(user_id, item_id)` as a similarity-weighted average of the ratings of the `k` most similar users who rated that item. Cosine similarity is computed on sparse user rating vectors.
**Assert:** For a held-out planted rating, the predicted value is within 1.5 of the true rating in the synthetic example.
**⚠️ Defect:** Cosine similarity treats missing ratings as 0 rather than as unknown, so a user with few ratings can appear artificially similar to another sparse user. No mean-centering of ratings, so users with different base rates are compared on raw scale. If no neighbor has rated the item, the function returns a hardcoded default 2.5 with no indication of confidence or cold-start.

---
*△ AURA Pattern Library — © Reality Optimizer*
