# hmac signed url

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → [u8`

## What it does

HMAC-signed URLs — tamper-proof query parameters.
Core idea: canonicalize params, HMAC sign, verify all params + sig.
When to use: signed download links, form submissions, stateless auth.

## Guarantee

When it runs, hmac signed url guarantees assert!(verify_url(&url, secret), "signed URL should verify") (none-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(verify_url(&url, secret), "signed URL should verify")`
- `assert!(!verify_url(&url, b"wrong-secret"), "wrong secret should fail")`
- `assert!(!verify_url(&tampered, secret), "tampered param should fail")`
- `assert!(!verify_url(no_sig, secret), "missing sig should fail")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** none (no checkable constraint)
- **Independent oracle:** ✓ **hard** — chaos (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
