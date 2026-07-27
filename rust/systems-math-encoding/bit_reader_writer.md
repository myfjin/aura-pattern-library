# bit reader writer

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(value: u64, n_bits: usize) → ?`

## What it does

Bit-level reader/writer: pack arbitrary-width bit fields and read them back exactly.
Core idea: maintain bit position in a byte buffer; write/read N bits at cursor.
When to use: binary protocols, image compression, bitfield serialization.

## Guarantee

When it runs, bit reader writer guarantees assert_eq!(packed.len(), 3); assert_eq!(v1, 5, "3-bit field mismatch"); assert_eq!(v2, 26, "5-bit field mismatch") (proven by rustc-run).

**Checkable constraints:**

- `assert!(n_bits <= 64)`
- `assert!(n_bits <= 64)`
- `assert_eq!(packed.len(), 3)`
- `assert_eq!(v1, 5, "3-bit field mismatch")`
- `assert_eq!(v2, 26, "5-bit field mismatch")`
- `assert_eq!(v3, 0xabc, "12-bit field mismatch")`
- `assert_eq!(packed2, vec![0xff])`
- `assert_eq!(bit, 1, "bit {} mismatch", i)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
