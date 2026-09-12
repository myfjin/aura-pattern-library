# Pseudo-Relevance Feedback (PRF) for Query Expansion

**File:** `python/data-science/rankings_and_information_retrieval/query_expansion_prf.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Expand a query with terms from top-k initially retrieved docs.** PRF finds synonym/related-term docs that the raw query misses. A query for "dog" finds docs with "dog" but misses docs with "canine" — PRF expands the query with "canine" from the top retrieved docs and surfaces the missed documents.

**When to use:** Improving recall in search — finding relevant docs that use different vocabulary than the query.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `query_terms` | List[str], initial query | |
| `docs` | Dict[str, str], doc_id → text | |
| `k` | int, top docs for feedback | |
| `expansion_terms` | int, terms to add | |

---

## How inputs shape the output

- **Raw query finds docs with query terms** but misses synonym docs.
- **Expanded query includes synonym terms** from top retrieved docs.
- **Expanded query retrieves previously missed docs** — the defining claim.

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/query_expansion_prf.py
Raw query: ['dog'] → ['doc1', 'doc2'] | Expanded: ['dog', 'canine'] → ['doc1', 'doc2', 'doc4'] | doc4 found: True | PASS
```

**Reading the output:** raw query "dog" finds doc1 and doc2 but misses doc4 ("canine wolf species"). PRF expands with "canine" and doc4 is now retrieved.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| top-k docs have no new terms | expansion is a no-op | no new vocabulary to add |
| irrelevant top-k docs | expansion adds noise | PRF quality depends on initial retrieval |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20