# query expansion prf

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(query_terms: List[str], docs: Dict[str, str]) → List[str]`

## What it does

Pseudo-Relevance Feedback (PRF) for Query Expansion.

Expand a query with terms from top-k initially-retrieved docs.
PRF finds synonym/related-term docs that the raw query misses.
We plant docs with synonyms, show that raw query misses them but expanded query finds them.

## Guarantee

When it runs, query expansion prf guarantees 'doc1' in initial_results; 'doc2' in initial_results; 'canine' in expanded_query (weak-grade: directional, proven by run).

**Checkable constraints:**

- `'doc1' in initial_results`
- `'doc2' in initial_results`
- `'canine' in expanded_query`
- `'doc4' in expanded_results`
- `'doc3' not in expanded_results`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
