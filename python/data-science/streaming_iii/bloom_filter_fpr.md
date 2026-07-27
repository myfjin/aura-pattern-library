# bloom filter fpr

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: list, size: int, k: int) → float`

## What it does

Bloom filter with measured false-positive rate.
Core idea: hash items to k positions in a bit array; false positive = query position all set but item not inserted.
When: test membership with bounded false-positive rate and zero false negatives.

## Guarantee

When it runs, bloom filter fpr guarantees false_negatives == 0; measured_fpr <= theoretical_fpr + 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `false_negatives == 0`
- `measured_fpr <= theoretical_fpr + 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
