# bloom filter

**Language:** Python · **Oracle sphere:** rust (this file is the Python twin) · **Category:** data structures

## What it does

Probabilistic set-membership via a Bloom filter with md5-derived double hashing
and an analytically sized bit array and hash count.

Use when false positives are tolerable but false negatives are not, to test
'possibly present' cheaply. add() sets k bits; contains() reports absence with
certainty. resize() grows the structure but (documented) clears its contents.

Guarantees (self-test): zero false negatives across 1000 added items, measured
false-positive rate stays near the configured target, bit-count sizing is
monotone in capacity/strictness, and invalid construction is refused.

## Guarantee

When it runs, bloom filter guarantees assert!(filter[h1 / 8] & (1 << (h1 % 8)) != 0); assert!(filter[h2 / 8] & (1 << (h2 % 8)) != 0); assert!(filter[h3 / 8] & (1 << (h3 % 8)) != 0) (weak-grade: proven by rustc-run on the RUST original).

**Checkable constraints:**

- `assert!(filter[h1 / 8] & (1 << (h1 % 8)) != 0)`
- `assert!(filter[h2 / 8] & (1 << (h2 % 8)) != 0)`
- `assert!(filter[h3 / 8] & (1 << (h3 % 8)) != 0)`
- `assert!(false_positives <= bound, "FP {} exceeds computed bound {} (bits_set={}, expected≈{:.4})", false_positives, bound, bits_set, expected_fp)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: hard, positive, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
