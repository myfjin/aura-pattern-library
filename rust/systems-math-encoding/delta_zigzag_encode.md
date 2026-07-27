# delta zigzag encode

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(n: i64) → u64`

## What it does

Delta-encoding + zigzag: compress sequences with small deltas.
Core idea: store first value, then encode (value[i] - value[i-1]) as zigzag varints.
When to use: time series, monotonic sequences, low-entropy deltas.

## Guarantee

When it runs, delta zigzag encode guarantees assert_eq!(encoded, expected, "delta_zigzag encode mismatch for {:?}", sequence); assert_eq!(enc_empty.len(), 0); assert_eq!(dec_empty.len(), 0) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(encoded, expected, "delta_zigzag encode mismatch for {:?}", sequence)`
- `assert_eq!(decoded, sequence, "delta_zigzag round-trip failed")`
- `assert_eq!(decoded2, sequence2, "delta_zigzag round-trip failed for {:?}", sequence2)`
- `assert_eq!(enc_empty.len(), 0)`
- `assert_eq!(dec_empty.len(), 0)`
- `assert_eq!(dec_single, single)`
- `assert!(delta_encoded.len() < direct_encoded.len(), "delta encoding {} should be < direct {}", delta_encoded.len(), direct_encoded.len())`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
