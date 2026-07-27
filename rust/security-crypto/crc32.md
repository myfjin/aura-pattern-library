# crc32

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → u32`

## What it does

CRC-32/IEEE (Ethernet) — error detection via polynomial division.
Core idea: bit-wise XOR division by Ethernet polynomial 0x04c11db7.
When to use: data checksums, packet validation, file integrity.

## Guarantee

When it runs, crc32 guarantees assert_eq!(got, expected, "CRC32 mismatch: got 0x{:08x}, expected 0x{:08x}", got, expected) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(got, expected, "CRC32 mismatch: got 0x{:08x}, expected 0x{:08x}", got, expected)`
- `assert!(empty != single_a, "empty and single byte should differ")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
