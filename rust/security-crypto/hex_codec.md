# hex codec

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → String`

## What it does

Hex codec (RFC 4648 lowercase) — encode/decode binary to hex text.
Core idea: each byte is two hex digits (0-9a-f).
When to use: digest display, data dumps, debug output.

## Guarantee

When it runs, hex codec guarantees assert_eq!(encoded, expected, "hex_encode mismatch") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(encoded, expected, "hex_encode mismatch")`
- `assert_eq!(decoded, data, "hex_decode round-trip mismatch")`
- `assert_eq!(hex_decode("12x"), None, "non-hex should reject")`
- `assert_eq!(hex_decode("123"), None, "odd-length should reject")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
