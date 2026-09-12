# Cross-Domain Search Engine

**File:** `python/data-science/composed_tools/cross_domain_search_engine.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**A 4-pattern workflow that retrieves cross-domain bridge documents a plain BM25 search leaves buried.** Stages: (1) stem the vocabulary so surface variants unify; (2) extract the corpus's broker terms (words on shortest paths between topic clusters); (3) expand the query with those broker terms; (4) BM25-rank. A domain-A query then surfaces the cross-domain bridge documents.

**When to use:** You need a search engine that finds documents connecting fields, not just documents matching your query's words.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `query` | List[str], tokenized query | should be from one domain |
| `docs` | List[List[str]], tokenized corpus | should span multiple domains |

---

## How inputs shape the output

- **Stage 2 recovers actual broker terms** from the corpus co-occurrence graph.
- **Plain BM25 stays in-domain** (≤1 bridge doc in top-6).
- **The pipeline surfaces ≥3 bridge docs** in top-6 — the end-to-end claim.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/cross_domain_search_engine.py
broker terms extracted: ['model', 'network'] (planted ['model', 'network'])
bridge docs in top-6 — plain BM25: 0/4 · broker-expanded: 4/4
cross_domain_search_engine.py PASS
```

**Reading the output:** a finance query returns 0 bridge docs with plain BM25. After broker-term expansion, all 4 bridge docs appear in the top 6.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| single-domain corpus | no broker terms found | correct |
| query terms are also broker terms | expansion is minimal | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20