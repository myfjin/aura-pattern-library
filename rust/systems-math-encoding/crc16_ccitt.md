# crc16 ccitt

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(data: &[u8]) → u16`

## What it does

CRC-16/CCITT-FALSE checksum (polynomial 0x1021, initial value 0xFFFF).
Core idea: process each bit, XOR with polynomial when MSB is 1.
When to use: serial communication, HDLC protocol, data integrity checks.

## Guarantee

When it runs, crc16 ccitt guarantees assert_eq!(result, 0x29b1, "CRC-16/CCITT-FALSE('123456789') = {:#06x}, expected 0x29b1", result); assert_eq!(empty, 0xffffu16, "CRC of empty is initial value") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(result, 0x29b1, "CRC-16/CCITT-FALSE('123456789') = {:#06x}, expected 0x29b1", result)`
- `assert_eq!(empty, 0xffffu16, "CRC of empty is initial value")`
- `assert_ne!(single, from_test)`
- `assert_eq!(data_a, data_a2, "CRC not deterministic")`
- `assert_ne!(data_a, data_b, "Different data should have different CRC")`
- `assert_ne!(crc1, crc2, "CRCs of different data should differ")`
- `assert_ne!(crc_short, crc_long)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
