# mean reciprocal rank

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(rankings: List[List[int]], relevant_sets: List[Set[int]]) → float`

## What it does

Ranking metrics suite: Mean Reciprocal Rank, Precision@K, Recall@K.

MRR = mean over queries of 1/(rank of the first relevant item). Precision@K = |relevant ∩
top-K| / K. Recall@K = |relevant ∩ top-K| / |relevant|. Core claim: each metric returns its
EXACT known value on a planted ranking, and MRR falls monotonically as the first relevant
item is demoted.

## Guarantee

When it runs, mean reciprocal rank guarantees abs(reciprocal_rank(ranking, relevant) - 0.5) < 1e-09; abs(recall_at_k(ranking, relevant, 3) - 0.5) < 1e-09; abs(precision_at_k(ranking, relevant, 4) - 0.5) < 1e-09 (proven by run).

**Checkable constraints:**

- `abs(reciprocal_rank(ranking, relevant) - 0.5) < 1e-09`
- `abs(precision_at_k(ranking, relevant, 3) - 1.0 / 3.0) < 1e-09`
- `abs(recall_at_k(ranking, relevant, 3) - 0.5) < 1e-09`
- `abs(precision_at_k(ranking, relevant, 4) - 0.5) < 1e-09`
- `abs(recall_at_k(ranking, relevant, 4) - 1.0) < 1e-09`
- `rr_ideal > rr_demoted`
- `abs(mrr - (1.0 + 1.0 / 3.0) / 2.0) < 1e-09`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
