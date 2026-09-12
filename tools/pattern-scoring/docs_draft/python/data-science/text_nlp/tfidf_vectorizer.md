# TF-IDF Vectorizer

**File:** `python/data-science/text_nlp/tfidf_vectorizer.py`
**Sphere:** Data Science — Text NLP

---

## What it solves

**Turn text into numbers that capture what matters.** TF-IDF weights each word by how often it appears in a document (TF) divided by how many documents contain it (IDF). Common words like "the" get low weight; rare, distinctive words get high weight. This is the standard baseline for document ranking, similarity search, and text classification.

**When to use:** Ranking documents by relevance to a query, finding similar documents, or preparing text for ML classifiers where term importance matters. TF-IDF is the first thing to try before moving to neural embeddings.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `documents` | list of str | — |
| `smooth_idf` | bool | — |

---

## How inputs shape the output

- **IDF captures rarity:** "apple" appears in 3/5 docs → low IDF. "date" appears in 2/5 docs → higher IDF. Rare terms get more weight.
- **TF-IDF vectors enable similarity search:** documents with shared distinctive terms have higher cosine similarity.
- **Query ranking works:** a query for "apple" ranks documents containing "apple" above those that don't.

---

## Worked example (real run)

```
$ python3 python/data-science/text_nlp/tfidf_vectorizer.py
PASS: TF-IDF vectorizer learns IDF, ranks distinctive terms higher, queries match relevant documents
```

**Reading the output:** "apple" has lower IDF than "date" (more common). Documents with shared terms have higher cosine similarity. Query "apple" ranks apple-containing docs highest.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty corpus | empty vocabulary, all vectors zero | correct |
| single document | IDF = 0 for all terms (log(1/1) = 0) | correct with smooth_idf |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
