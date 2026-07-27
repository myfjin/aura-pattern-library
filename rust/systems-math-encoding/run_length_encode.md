# run length encode

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(data: &[u8]) → Vec<u8>`

## What it does

Run-length encoding: compress sequences of identical bytes.
Core idea: emit (run_byte, count) pairs; single byte encoded as (byte, 1).
When to use: simple compression, image data, sparse patterns.

## Guarantee

When it runs, run length encode guarantees assert_eq!(&encoded, expected_encoded, "rle_encode mismatch for {:?}", std::str::from_utf8(input).ok()); assert_eq!(empty_encoded.len(), 0) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(&encoded, expected_encoded, "rle_encode mismatch for {:?}", std::str::from_utf8(input).ok())`
- `assert_eq!(&decoded, input, "rle round-trip mismatch")`
- `assert_eq!(empty_encoded.len(), 0)`
- `assert_eq!(encoded, vec![42, 255])`
- `assert_eq!(decoded, long_run)`
- `assert_eq!(encoded, vec![99, 255, 99, 45])`
- `assert_eq!(decoded, very_long_run)`
- `assert_eq!(decoded, mixed, "mixed pattern round-trip failed")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
