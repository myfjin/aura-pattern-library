# Ranking Metrics Suite: MRR, Precision@K, Recall@K

**File:** `python/data-science/rankings_and_information_retrieval/mean_reciprocal_rank.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Evaluate ranking quality with standard metrics.** MRR = mean over queries of 1/(rank of the first relevant item). Precision@K = |relevant ∩ top-K| / K. Recall@K = |relevant ∩ top-K| / |relevant|. Each metric returns its exact known value on a planted ranking.

**When to use:** Evaluating search and ranking systems — how good is the ranked list?

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `ranking` | List[int], ranked item IDs | |
| `relevant` | Set[int], ground-truth relevant items | |
| `k` | int, cutoff position | |

---

## How inputs shape the output

- **RR = 1/rank of first relevant** — verified on planted data.
- **Precision@K and Recall@K match hand-computed values** exactly.
- **MRR falls monotonically** as the first relevant item is demoted.

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/mean_reciprocal_rank.py
PASS
```

**Reading the output:** on ranking [1,2,3,4,5] with relevant {2,4}: RR=0.5, P@3=1/3, R@3=0.5, P@4=0.5, R@4=1.0. MRR over two queries = 2/3.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| no relevant items | RR = 0, P@K = 0, R@K = 0 | correct |
| empty ranking | division by zero | needs guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20