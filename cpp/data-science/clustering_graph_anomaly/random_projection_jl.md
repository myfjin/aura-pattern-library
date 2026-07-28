# random projection jl

**Language:** C++ · **Sphere:** data-science · **Category:** Clustering, Graph & Anomaly

**Signature:** `(original_dim: int, target_dim: int, seed: int) → List[List[float]]`

## What it does

random_projection_jl.cpp — Johnson-Lindenstrauss random projection.

## Guarantee

When it runs, random projection jl guarantees correlation > 0.9; correlation < 1.1 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `correlation > 0.9`
- `correlation < 1.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `random_projection_matrix(original_dim, target_dim, seed=42) → List[List[float]]`, `project_point(point, projection_matrix) → Tuple[float, ...]`
**Valid input:** `original_dim > target_dim ≥ 1`. `point` dimension matches `original_dim`.
**Core:** Johnson-Lindenstrauss random projection. Generate Gaussian random matrix, normalize rows to unit norm. Project 50D points to 20D. JL lemma guarantees pairwise distances are approximately preserved. Tested on 42 points from 3 planted clusters in 50D.
**Assert:** On 42 points (3 clusters, 50D → 20D): Pearson correlation between original and projected pairwise distances > 0.9.
**⚠ Retrofit NOT in this twin:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E input-contract retrofit on the PY original (7497d40, 2026-07-21). That pass deliberately excluded the compiled lanes, so this C++ twin does NOT carry the contract its source now enforces. Declared in MANIFEST.json `twin_contract_divergence`; unblocking it needs the cpp attack lane. Corrected 2026-07-28 — the card previously claimed the fix was in this file.

---
*△ AURA Pattern Library — © Reality Optimizer*
