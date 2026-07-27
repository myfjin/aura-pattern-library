# crc32c castagnoli

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(data: &[u8]) → u32`

## What it does

CRC-32/Castagnoli (CRC-32C): polynomial 0x1EDC6F41, used in iSCSI and others.
Core idea: 32-bit shift register with Castagnoli polynomial; process 8 bits per byte.
When to use: data integrity, iSCSI protocol, storage checksums.

## Guarantee

When it runs, crc32c castagnoli guarantees assert_eq!(result, 0xe3069283, "CRC-32/Castagnoli('123456789') = {:#010x}, expected 0xe3069283", result) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(result, 0xe3069283, "CRC-32/Castagnoli('123456789') = {:#010x}, expected 0xe3069283", result)`
- `assert_ne!(empty, 0xffffffffu32, "CRC of empty should not be initial value")`
- `assert_eq!(data_a, data_a2, "CRC not deterministic")`
- `assert_ne!(data_a, data_b, "Different data should have different CRC")`
- `assert_ne!(single, from_test)`
- `assert_ne!(crc1, crc2)`
- `assert_ne!(crc_a, crc_b)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
