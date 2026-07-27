# base32 codec

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → String`

## What it does

Base32 codec (RFC 4648) — encode/decode binary to case-insensitive ASCII.
Core idea: 5-bit groups mapped to 32-char alphabet, padding on remainder.
When to use: case-insensitive transmission, DNS records, TOTP secrets.

## Guarantee

When it runs, base32 codec guarantees assert_eq!(encoded, expected, "base32_encode('{}') mismatch", input) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(encoded, expected, "base32_encode('{}') mismatch", input)`
- `assert_eq!(decoded, input.as_bytes(), "base32_decode('{}') round-trip mismatch", expected)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
