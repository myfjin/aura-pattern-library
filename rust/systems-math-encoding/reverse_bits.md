# reverse bits

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(n: u8) → u8`

## What it does

Reverse bit order in an integer.
Core idea: swap bits from outside-in; double reverse is identity.
When to use: bitstream reversal, certain signal processing, DSP algorithms.

## Guarantee

When it runs, reverse bits guarantees assert_eq!(reverse_bits_8(0x01), 0x80); assert_eq!(reverse_bits_8(0x80), 0x01); assert_eq!(reverse_bits_8(0xaa), 0x55) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(reverse_bits_8(0x01), 0x80)`
- `assert_eq!(reverse_bits_8(0x80), 0x01)`
- `assert_eq!(reverse_bits_8(0xaa), 0x55)`
- `assert_eq!(reverse_bits_8(0x55), 0xaa)`
- `assert_eq!(reverse_bits_8(0xff), 0xff)`
- `assert_eq!(reverse_bits_8(0x00), 0x00)`
- `assert_eq!(reverse_bits_8(0b00001010), 0b01010000)`
- `assert_eq!(reverse_bits_16(0x0001), 0x8000)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
