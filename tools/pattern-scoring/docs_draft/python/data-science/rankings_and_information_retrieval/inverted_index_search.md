# Inverted Index and Boolean Search

**File:** `python/data-science/rankings_and_information_retrieval/inverted_index_search.py`
**Sphere:** Data Science — Rankings and Information Retrieval

---

## What it solves

**Build an inverted index (term → docs) and answer AND/OR queries.** The inverted index maps each term to the set of documents containing it. AND queries return docs containing ALL terms; OR queries return docs containing ANY term.

**When to use:** The foundation of search — understanding how search engines map query terms to documents.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `docs` | Dict[str, str], doc_id → text | |
| `terms` | List[str], query terms | |

---

## How inputs shape the output

- **AND query returns only docs containing ALL terms** — verified against hand-computed results.
- **OR query returns docs containing ANY term** — verified against hand-computed results.
- **Irrelevant docs are excluded** from query results.

---

## Worked example (real run)

```
$ python3 python/data-science/rankings_and_information_retrieval/inverted_index_search.py
Index size: 8 terms | AND (python, machine): ['doc1'] | OR (python, machine): ['doc1', 'doc2', 'doc3', 'doc5'] | Term 'python': ['doc1', 'doc2', 'doc5'] | PASS
```

**Reading the output:** AND query for "python" AND "machine" returns only doc1 (has both). OR query returns all docs with either term. Doc4 (data science) is correctly excluded.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty query | AND returns empty set | correct |
| term not in index | treated as empty set | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20