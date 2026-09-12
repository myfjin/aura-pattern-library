# Team-Draft Interleaving for A/B Testing Rankers

**File:** `python/data-science/rankings_and_information_retrieval/ab_interleaving.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Compare two rankers by interleaving their results in a single ranking.** Users click on interleaved results. The ranker whose document the user clicked on wins that "team." More sensitive than split A/B tests because every user sees both rankers' results.

**When to use:** You need to compare two ranking systems and want a more sensitive test than splitting traffic.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `ranking_a`, `ranking_b` | List[str], document rankings | same documents |
| `relevant_docs` | set, ground-truth relevant docs | |

---

## How inputs shape the output

- **Team-draft interleaving:** alternately pick the next unchosen document from A or B.
- **Stronger ranker wins more clicks** — the defining claim.
- **A's win ratio > 0.5** when A is the stronger ranker.

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/ab_interleaving.py
Interleaved results: 5 docs | A wins: 42 | B wins: 18 | A win ratio: 70.0% | PASS
```

**Reading the output:** ranker A (stronger) wins 70% of clicks vs B's 30%.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| equal rankers | win ratio ~50% | correct — no difference detected |
| no relevant docs | no clicks | no signal |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20