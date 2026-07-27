# textrank lite

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP II

**Signature:** `(sent1: List[str], sent2: List[str]) → float`

## What it does

TextRank: extract key sentences via graph centrality (damped power iteration).

Builds a sentence similarity graph (Jaccard word overlap) and ranks sentences with the
PageRank/TextRank recurrence, including the damping factor that keeps the iteration from
collapsing to a uniform tie:
    score_i = (1−d)/n + d · Σ_{j≠i} (w_ji / Σ_k w_jk) · score_j.
Core claim: the "hub" sentence that shares words with the others wins the strict top rank.

## Guarantee

When it runs, textrank lite guarantees top == 1; ranks[1] > ranks[0] and ranks[1] > ranks[2] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `top == 1`
- `ranks[1] > ranks[0] and ranks[1] > ranks[2]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def jaccard_similarity(sent1: List[str], sent2: List[str]) -> float:`, `def textrank_sentences(sentences: List[List[str]], damping: float = 0.85, iterations: int = 50) -> List[float]:`
**Valid input:** `sentences` is a list of tokenized sentences (list of string lists); `damping` ∈ [0, 1]; `iterations` > 0.
**Core:** Builds a sentence-similarity graph using Jaccard word overlap and runs the damped PageRank/TextRank power iteration to rank sentences by centrality.
**Assert:** On a three-sentence corpus where the middle sentence shares words with both neighbors (the hub), the hub sentence has the strict highest rank.
**⚠️ Defect:** The graph is fully connected even for very dissimilar sentences, so low-overlap edges still contribute small amounts of weight to every node. The implementation does not provide a convergence threshold; it always runs the fixed number of iterations regardless of whether ranks have stabilized.

---
*△ AURA Pattern Library — © Reality Optimizer*
