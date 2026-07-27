# jwt hs256 verify

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → String`

## What it does

JWT (HMAC-SHA256) verification — header.payload.sig integrity check.
Core idea: base64url decode, verify HMAC, check expiry claim.
When to use: API tokens, session claims, stateless auth.

## Guarantee

When it runs, jwt hs256 verify guarantees assert!(verify_jwt(&token, secret, 500), "valid token should verify") (none-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(verify_jwt(&token, secret, 500), "valid token should verify")`
- `assert!(!verify_jwt(&token, secret, 1000), "expired token should fail")`
- `assert!(!verify_jwt(&token, b"wrong-secret", 500), "wrong secret should fail")`
- `assert!(!verify_jwt("a.b.c", secret, 500), "invalid base64 should fail")`
- `assert!(!verify_jwt("no-dots", secret, 500), "missing dots should fail")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** none (no checkable constraint)
- **Independent oracle:** ✓ **hard** — positive, roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
