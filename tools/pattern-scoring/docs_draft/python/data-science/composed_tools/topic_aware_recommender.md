# Topic-Aware Recommender

**File:** `python/data-science/composed_tools/topic_aware_recommender.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**A 4-pattern workflow that recommends documents by topic, not just word overlap.** Stages: (1) build a PMI-weighted term co-occurrence graph; (2) find topic communities by weighted label propagation; (3) PageRank terms within each community for signature terms; (4) recommend documents by their overlap with a query document's TOPIC signature. A flat term-overlap baseline mixes topics; the topic-aware pipeline stays within-topic.

**When to use:** You need recommendations that respect topic structure, especially when documents share a large common vocabulary across topics.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `docs` | List[List[str]], tokenized documents | should span multiple topics |

---

## How inputs shape the output

- **Each topic's core terms form one distinct community** — PPMI discounts shared vocabulary.
- **Topic-aware recommendations stay within-topic** (> 80% same-topic rate).
- **Topic-aware beats flat term-overlap by > 15%** — the end-to-end claim.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/topic_aware_recommender.py
real (multi-term) communities: 3 · each topic's cores cohesive: [True, True, True]
same-topic recommendation rate — topic-aware 87% vs flat 62%
topic_aware_recommender.py PASS
```

**Reading the output:** 3 topics with shared vocabulary. Topic-aware recommends same-topic documents 87% of the time vs. flat overlap's 62% — a 25% improvement.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| disjoint vocabularies | flat baseline also works | topic-aware still doesn't hurt |
| single topic only | one community | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20