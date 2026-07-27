# pbkdf2 sha256

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → [u8`

## What it does

PBKDF2-SHA256 (RFC 2898/7914) — key derivation from password.
Core idea: iterative HMAC to slow down brute force attacks.
When to use: password hashing, key stretching, file encryption.

## Guarantee

When it runs, pbkdf2 sha256 guarantees assert_eq!(got1, expected1, "PBKDF2 c=1 mismatch"); assert_eq!(got2, expected2, "PBKDF2 c=2 mismatch") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(got1, expected1, "PBKDF2 c=1 mismatch")`
- `assert_eq!(got2, expected2, "PBKDF2 c=2 mismatch")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
