# ndcg evaluation

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(relevances: List[float]) → float`

## What it does

NDCG (Normalized Discounted Cumulative Gain).

Evaluate ranking quality: DCG sums relevance scores discounted by position.
NDCG normalizes DCG by ideal DCG (perfect ranking).
Perfect ranking = NDCG 1.0, shuffled = lower score.
We verify on a hand-computed example and show degraded ranking scores lower.

## Guarantee

When it runs, ndcg evaluation guarantees abs(dcg_ideal_computed - expected_ideal_dcg) < 0.01; abs(ndcg_perfect - 1.0) < 0.01; ndcg_degraded < 0.5 (proven by run).

**Checkable constraints:**

- `abs(dcg_ideal_computed - expected_ideal_dcg) < 0.01`
- `abs(ndcg_perfect - 1.0) < 0.01`
- `ndcg_degraded < 0.5`
- `ndcg_perfect > 2 * ndcg_degraded`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
