# hamming distance

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(a: &[u8], b: &[u8]) → Option<u32>`

## What it does

Hamming distance: bit-difference count between byte sequences.
Core idea: XOR the bytes and count set bits in result.
When to use: error detection in transmission, code similarity, bit-pattern diff.

## Guarantee

When it runs, hamming distance guarantees assert_eq!(dist, *expected, "hamming_distance({:?}, {:?}) = {}, expected {}", std::str::from_utf8(a).unwrap_or("?"), std::str::from_utf8(b).unwrap_or("?"), dist, expected) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(hamming_distance_bytes(b"", b""), Some(0))`
- `assert_eq!(hamming_distance_bytes(b"\x00", b"\x00"), Some(0))`
- `assert_eq!(hamming_distance_bytes(b"\x01", b"\x00"), Some(1))`
- `assert_eq!(hamming_distance_bytes(b"\xff", b"\x00"), Some(8))`
- `assert_eq!(hamming_distance_bytes(b"\xaa", b"\x55"), Some(8))`
- `assert_eq!(hamming_distance_bytes(b"abc", b"abc"), Some(0))`
- `assert_eq!(dist, *expected, "hamming_distance({:?}, {:?}) = {}, expected {}", std::str::from_utf8(a).unwrap_or("?"), std::str::from_utf8(b).unwrap_or("?"), dist, expected)`
- `assert_eq!(d1, d2, "hamming distance not symmetric")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
