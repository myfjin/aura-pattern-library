# length prefixed framing

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(msg: &[u8]) → Vec<u8>`

## What it does

Length-prefixed framing: u32 big-endian length prefix + message bytes.
Core idea: each message preceded by 4-byte big-endian length; streams are parsed sequentially.
When to use: binary protocols, framed message transmission, delimited records.

## Guarantee

When it runs, length prefixed framing guarantees assert_eq!(&encoded1, &expected1); assert_eq!(decoded1.len(), 1); assert_eq!(decoded.len(), 3) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(&encoded1, &expected1)`
- `assert_eq!(decoded1.len(), 1)`
- `assert_eq!(&decoded1[0], msg1)`
- `assert_eq!(decoded.len(), 3)`
- `assert_eq!(&decoded[0], msg_a)`
- `assert_eq!(&decoded[1], msg_b)`
- `assert_eq!(&decoded[2], msg_c)`
- `assert_eq!(&encoded_empty, &[0, 0, 0, 0])`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
