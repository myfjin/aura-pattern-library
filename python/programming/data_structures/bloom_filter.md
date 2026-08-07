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

When it runs, bloom filter guarantees `bf.false_positive_rate() == 0.0`; `sum((1 for i in range(50) if f'probe_{i}' in bf)) == 0`; `len(bf) == 1000` — read from this file's own self-test. The oracle behind this pattern was established on the rust original and is not claimed to have been run against this file.

**Checkable constraints:**

- `bf.false_positive_rate() == 0.0`
- `sum((1 for i in range(50) if f'probe_{i}' in bf)) == 0`
- `len(bf) == 1000`
- `found == 1000`
- `fp < 60`
- `0.0 < est < 0.05`
- `BloomFilter(2000, 0.01).bit_count > bf.bit_count`
- `BloomFilter(1000, 0.001).bit_count > bf.bit_count`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: hard, positive, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
