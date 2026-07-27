# hmac sha256

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → [u8`

## What it does

HMAC-SHA256 (RFC 2104/4231) — message authentication code from scratch.
Core idea: two hash calls with key, inner/outer padding constants.
When to use: API authentication, integrity+authenticity checks, JWT signing.

## Guarantee

When it runs, hmac sha256 guarantees assert_eq!(got, expected, "HMAC-SHA256 RFC 4231 TC2 mismatch"); assert_eq!(got1, expected1, "HMAC-SHA256 RFC 4231 TC1 mismatch") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(got, expected, "HMAC-SHA256 RFC 4231 TC2 mismatch")`
- `assert_eq!(got1, expected1, "HMAC-SHA256 RFC 4231 TC1 mismatch")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
