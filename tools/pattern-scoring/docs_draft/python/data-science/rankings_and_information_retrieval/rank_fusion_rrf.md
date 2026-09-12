# Reciprocal Rank Fusion (RRF)

**File:** `python/data-science/rankings_and_information_retrieval/rank_fusion_rrf.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Combine multiple rankers via RRF: score = Σ 1/(k + rank_i).** Fusion often beats individual rankers on noisy signals. Two mediocre rankers that disagree on specifics can be fused into a better ranking than either alone.

**When to use:** Combining results from multiple search systems or ranking methods — ensemble ranking.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `rankings` | List[List[str]], multiple rankings of same items | |
| `k` | int, RRF constant (default 60) | |

---

## How inputs shape the output

- **Fused ranking beats both individual rankers** in NDCG.
- **Fused ranking beats the average individual score** — the defining claim.
- **RRF is robust to individual ranker weaknesses** — each ranker's errors are diluted.

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/rank_fusion_rrf.py
Ranker1 NDCG: 0.72 | Ranker2 NDCG: 0.68 | Avg individual: 0.70 | Fused: 0.85 | PASS
```

**Reading the output:** two mediocre rankers (NDCG 0.72 and 0.68) are fused into a ranking with NDCG 0.85 — beating both individually and the average.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| identical rankers | fused = individual | no gain from fusion |
| one perfect ranker | fusion can't improve | already optimal |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20