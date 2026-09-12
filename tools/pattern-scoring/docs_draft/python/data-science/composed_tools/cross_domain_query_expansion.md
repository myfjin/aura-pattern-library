# Cross-Domain Query Expansion

**File:** `python/data-science/composed_tools/cross_domain_query_expansion.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**Expand a query with broker terms to surface cross-domain documents instead of deeper monoculture.** Classic pseudo-relevance feedback (PRF) expands a query with top-document terms and finds MORE OF THE SAME domain. Expanding with BROKER terms — the words that sit between topic clusters — makes retrieval surface the documents that CONNECT domains.

**When to use:** You need cross-domain discovery — finding documents that bridge fields, not just more documents in the same field.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `query` | List[str], tokenized query | should be from one domain |
| `docs` | List[List[str]], tokenized corpus | should span multiple domains |

---

## How inputs shape the output

- **Broker expansion picks actual broker terms** (words on shortest paths between topic clusters).
- **Classic PRF stays in its monoculture** (≤1 bridge doc in top-5).
- **Broker expansion surfaces ≥2 bridge docs** in top-5 — the defining claim.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/cross_domain_query_expansion.py
PRF expansion:    ['margin', 'portfolio'] → bridge docs in top-5: 0/3
broker expansion: ['model', 'network'] → bridge docs in top-5: 3/3
cross_domain_query_expansion.py PASS
```

**Reading the output:** a finance query ("market yield hedge") expanded with PRF stays in finance. Expanded with broker terms ("model", "network"), it surfaces all 3 bridge documents.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| single-domain corpus | no broker terms to expand with | correct — no bridges exist |
| query already contains broker terms | expansion is a no-op | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20