# varint leb128

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(mut n: u64) → Vec<u8>`

## What it does

Unsigned LEB128 (Little-Endian Base-128) varint encoding.
Core idea: 7 bits per byte, MSB continuation flag; 0–127 fit in 1 byte, larger requires chaining.
When to use: protocol buffers, binary formats needing variable-length integers.

## Guarantee

When it runs, varint leb128 guarantees assert_eq!(&encoded, expected_bytes, "varint_encode({}) mismatch", value); assert_eq!(consumed, expected_bytes.len(), "consumed length mismatch for {}", value) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(&encoded, expected_bytes, "varint_encode({}) mismatch", value)`
- `assert_eq!(decoded, *value, "varint_decode round-trip mismatch for {}", value)`
- `assert_eq!(consumed, expected_bytes.len(), "consumed length mismatch for {}", value)`
- `assert_eq!(decoded, n, "round-trip mismatch for {}", n)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
