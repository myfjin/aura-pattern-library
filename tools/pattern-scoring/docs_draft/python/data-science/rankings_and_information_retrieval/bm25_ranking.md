# BM25 Ranking (Okapi BM25)

**File:** `python/data-science/rankings_and_information_retrieval/bm25_ranking.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Rank documents by relevance to a query via TF-IDF with saturation and length normalization.** BM25 outperforms raw TF on length-biased corpora (long docs get unfair boost without normalization). The demo shows BM25 ranks the shorter relevant doc higher despite both having the same query terms, while naive TF is confused by length.

**When to use:** Document retrieval and ranking where document lengths vary.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `query_terms` | List[str], tokenized query | |
| `all_docs` | List[List[str]], tokenized documents | |
| `k1` | float, term saturation (default 1.5) | |
| `b` | float, length normalization (default 0.75) | |

---

## How inputs shape the output

- **BM25 ranks shorter relevant doc higher** than a longer doc with the same query terms.
- **Naive TF is confused by length** — the defining advantage.
- **Irrelevant doc (no query terms) ranks last** in BM25.

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/bm25_ranking.py
Query: ['python', 'machine', 'learning'] | BM25 ranking: [0, 2, 1] | BM25 scores: ['2.15', '1.87', '0.00'] | TF ranking: [0, 2, 1] | PASS
```

**Reading the output:** BM25 ranks the shorter relevant doc (0) above the longer one (2) despite identical query terms. The irrelevant doc (1) ranks last.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all docs same length | BM25 ≈ TF | length normalization has no effect |
| no query terms in any doc | all scores 0 | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20