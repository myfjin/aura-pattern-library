# base64 codec

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → String`

## What it does

Base64 codec (RFC 4648) — encode/decode binary to ASCII-safe text.
Core idea: 6-bit groups mapped to 64-char alphabet, padding on remainder.
When to use: data transmission, API payloads, email attachment encoding.

## Guarantee

When it runs, base64 codec guarantees assert_eq!(encoded, expected, "base64_encode('{}') mismatch", input) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(encoded, expected, "base64_encode('{}') mismatch", input)`
- `assert_eq!(decoded, input.as_bytes(), "base64_decode('{}') round-trip mismatch", expected)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
