# cosine similarity search

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP

## What it does

Cosine Similarity Search: Rank Documents by Query

Core idea: convert documents and query to TF-IDF vectors, rank documents by
cosine similarity to query. Fast baseline for relevance ranking and information
retrieval.

Use when: building a search engine, ranking results by relevance, finding top-k
similar documents without heavy infrastructure.

## Guarantee

When it runs, cosine similarity search guarantees docs[0] in top_docs; docs[4] in top_docs; results[0][0] == docs[2] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `docs[0] in top_docs`
- `docs[4] in top_docs`
- `results[0][0] == docs[2]`
- `results[0][0] == docs[0]`
- `results[0][1] > 0.9`
- `max(scores_web) <= max(scores_ml)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class SimpleSearchEngine:`, `def __init__(self):`, `def _tokenize(self, text: str) -> List[str]:`, `def index(self, documents: List[str]) -> None:`, `def _get_tfidf_vector(self, text: str) -> Dict[int, float]:`, `def _cosine_similarity(self, vec1: Dict[int, float], vec2: Dict[int, float]) -> float:`, `def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:`
**Valid input:** `documents` is a list of strings; `query` is a string; `top_k` is a non-negative integer.
**Core:** Builds a TF-IDF index over a corpus and ranks documents by cosine similarity to a free-text query. Returns the top-k `(document, score)` tuples.
**Assert:** Query "machine learning" ranks the two ML-related documents highest; query "python" returns the Python doc first; exact-query search returns the same document with score > 0.9.
**⚠️ Defect:** The private `_cosine_similarity` is not normalized by document length in any length-biased way; it uses raw term-frequency times IDF, so longer documents can dominate unless the query is also long. No validation that `documents` is non-empty before `index` is called; an empty corpus leaves IDF dictionaries empty and search silently returns `[]`.

---
*△ AURA Pattern Library — © Reality Optimizer*
