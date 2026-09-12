# NDCG (Normalized Discounted Cumulative Gain)

**File:** `python/data-science/rankings_and_information_retrieval/ndcg_evaluation.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Evaluate ranking quality with graded relevance.** DCG sums relevance scores discounted by position: DCG = Σ rel[i] / log₂(i+2). NDCG normalizes DCG by ideal DCG (perfect ranking). Perfect ranking = NDCG 1.0; shuffled = lower score.

**When to use:** Evaluating ranked lists where items have graded relevance (not just relevant/not).

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `predicted_relevances` | List[float], relevance scores in ranking order | |
| `ideal_relevances` | List[float], relevance scores in ideal order | |

---

## How inputs shape the output

- **Perfect ranking has NDCG = 1.0** — verified against hand-computed DCG.
- **Degraded ranking has NDCG < 0.5** — the defining claim.
- **Perfect NDCG >> degraded NDCG** (> 2×).

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/ndcg_evaluation.py
Ideal DCG: 4.76 | Perfect NDCG: 1.00 | Degraded NDCG: 0.19 | Ratio: 5.3x | PASS
```

**Reading the output:** ideal relevances [3,2,1,0] give DCG 4.76. Perfect ranking scores NDCG 1.0. Degraded (highest relevance last) scores 0.19 — 5.3× worse.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all zero relevance | NDCG = 0 | correct |
| ideal DCG = 0 | NDCG = 0 | division guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20