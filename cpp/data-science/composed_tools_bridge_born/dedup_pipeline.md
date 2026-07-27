# dedup pipeline

**Language:** C++ · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(docs: List[str], cand_thresh: float, verify_ratio: float) → ?`

## What it does

Three-Stage Dedup Pipeline — C++17 port of the Python oracle.
Stages: MinHash candidate generation, edit-distance verification, LCS word diff.

## Guarantee

When it runs, dedup pipeline guarantees set(planted) <= set(verified); all((p in planted for p in verified)); len(candidates) < 0.2 * total_pairs (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `set(planted) <= set(verified)`
- `all((p in planted for p in verified))`
- `len(candidates) < 0.2 * total_pairs`
- `any((tok.startswith(('-', '+')) for tok in sample))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: hard, positive, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
