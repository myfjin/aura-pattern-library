# bm25 ranking

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(query_terms: List[str], all_docs: List[List[str]], doc_idx: int, k1: float, b: float) → float`

## What it does

BM25 Ranking (Okapi BM25).

BM25 ranks documents by relevance to a query via TF-IDF with saturation and length normalization.
BM25 outperforms raw TF on length-biased corpora (long docs get unfair boost without normalization).
We plant a query, make one doc longer (same term frequency but inflated raw TF), verify BM25
ranks the relevant doc higher despite length bias while naive TF is confused by length.

## Guarantee

When it runs, bm25 ranking guarantees 1 not in bm25_ranking[:1]; bm25_ranking.index(0) < bm25_ranking.index(2) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `bm25_top in [0, 2]`
- `1 not in bm25_ranking[:1]`
- `bm25_ranking.index(0) < bm25_ranking.index(2)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
