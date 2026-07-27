# bloom filter

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → u32`

## What it does

Bloom filter — probabilistic set membership (zero false negatives).
Core idea: k hash functions, bitset, tunable FP rate.
When to use: IP reputation, URL blacklists, membership cache.

## Guarantee

When it runs, bloom filter guarantees assert!(filter[h1 / 8] & (1 << (h1 % 8)) != 0); assert!(filter[h2 / 8] & (1 << (h2 % 8)) != 0); assert!(filter[h3 / 8] & (1 << (h3 % 8)) != 0) (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(filter[h1 / 8] & (1 << (h1 % 8)) != 0)`
- `assert!(filter[h2 / 8] & (1 << (h2 % 8)) != 0)`
- `assert!(filter[h3 / 8] & (1 << (h3 % 8)) != 0)`
- `assert!(false_positives <= bound, "FP {} exceeds computed bound {} (bits_set={}, expected≈{:.4})", false_positives, bound, bits_set, expected_fp)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
