# tf idf bm25 comparison

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP II

**Signature:** `(docs: List[List[str]], query: List[str]) → List[float]`

## What it does

TF-IDF vs BM25: compare relevance ranking on length-biased documents.

BM25 dampens length bias (saturation on high-TF terms) whereas TF-IDF linear.
Core claim: on variable-length docs, BM25 ranks short docs higher; measured.

## Guarantee

When it runs, tf idf bm25 comparison guarantees scores_bm25[0] > scores_bm25[1] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `scores_bm25[0] > scores_bm25[1]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def tf_idf(docs: List[List[str]], query: List[str]) -> List[float]:`, `def bm25(docs: List[List[str]], query: List[str], k1: float = 1.5, b: float = 0.75) -> List[float]:`
**Valid input:** `docs` is a list of tokenized documents; `query` is a list of query tokens; `k1` > 0; `b` ∈ [0, 1].
**Core:** Compares TF-IDF (linear term-frequency scoring) with Okapi BM25 (dampened, length-normalized term-frequency scoring). BM25 penalizes long documents relative to TF-IDF, reducing length bias in retrieval.
**Assert:** For a short document with high query-term frequency versus a long document with a single query-term occurrence, BM25 ranks the short document higher; TF-IDF may or may not, depending on IDF, but the demo asserts the BM25 ordering.
**⚠️ Defect:** Both functions build IDF on every call instead of caching it across repeated queries over the same corpus. The TF-IDF IDF uses `log(num_docs / (1 + doc_count))`, which is a non-standard smoothing choice and can produce negative scores. BM25 uses the standard Robertson/Sparck-Jones IDF form, which can be negative when a term appears in more than half the documents.

---
*△ AURA Pattern Library — © Reality Optimizer*
