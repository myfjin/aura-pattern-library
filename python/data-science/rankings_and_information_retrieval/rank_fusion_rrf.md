# rank fusion rrf

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(item: str, rankings: List[List[str]], k: int) → float`

## What it does

Reciprocal Rank Fusion (RRF).

Combine multiple rankers via RRF: score = Σ (1 / (k + rank_i)).
Fusion often beats individual rankers on noisy signals.
We plant two mediocre rankers and show that fusing them recovers better ranking.

## Guarantee

When it runs, rank fusion rrf guarantees ndcg_fused > ndcg1; ndcg_fused > ndcg2; ndcg_fused > avg_individual (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ndcg_fused > ndcg1`
- `ndcg_fused > ndcg2`
- `ndcg_fused > avg_individual`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
