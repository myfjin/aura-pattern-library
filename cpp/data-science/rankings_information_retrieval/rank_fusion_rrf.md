# rank fusion rrf

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Rankings & Information Retrieval

## What it does

rank_fusion_rrf.cpp — Reciprocal Rank Fusion.

## Guarantee

When it runs, rank fusion rrf guarantees ndcg_fused > ndcg1; ndcg_fused > ndcg2; ndcg_fused > avg_individual (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `ndcg_fused > ndcg1`
- `ndcg_fused > ndcg2`
- `ndcg_fused > avg_individual`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
