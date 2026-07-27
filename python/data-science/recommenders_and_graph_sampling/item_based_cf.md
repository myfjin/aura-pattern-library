# item based cf

**Language:** Python · **Sphere:** data-science · **Category:** Recommenders & Graph Sampling

**Signature:** `(item_a: Dict[int, float], item_b: Dict[int, float], user_means: Dict[int, float]) → float`

## What it does

Item-based collaborative filtering.

Core idea: compute adjusted-cosine similarity between item rating vectors
(normalize by subtracting per-user mean), then recommend top-k unseen items
using weighted similarity to items the user has already rated.

When to use: when items have similar rating patterns across users and you want
item-stability (item similarities change less frequently than user similarities).

## Guarantee

When it runs, item based cf guarantees all((item_id not in ratings_by_user[0] for item_id, _ in recommendations)) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(recommendations) > 0`
- `all((item_id not in ratings_by_user[0] for item_id, _ in recommendations))`
- `len(recommended_items & unseen_items) > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def adjusted_cosine_similarity(item_a: Dict[int, float], item_b: Dict[int, float], user_means: Dict[int],) -> float:`, `def recommend_items(user_id: int, ratings_by_user: Dict[int, Dict[int, float]], ratings_by_item: Dict[int, Dict[int, float]], k: int = 3,) -> List[Tuple[int, float]]:`
**Valid input:** `ratings_by_user` and `ratings_by_item` are consistent views of the same rating matrix; `user_id` present in `ratings_by_user`; `k >= 1`.
**Core:** Item-based collaborative filtering with adjusted cosine similarity. Normalizes ratings by subtracting per-user means, computes similarity between item rating vectors, and recommends top-k unseen items weighted by similarity to the user's rated items.
**Assert:** For a small synthetic rating matrix, recommendations are generated, no already-rated item is recommended, and at least one unseen item appears in the top-k list.
**⚠️ Defect:** `adjusted_cosine_similarity` returns 0.0 when items have no common raters, giving them no chance to be recommended even if global popularity would be a sensible fallback. `recommend_items` can return an empty list for users with no similarity to any unseen item, and there is no cold-start default.

---
*△ AURA Pattern Library — © Reality Optimizer*
