# hotp

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(secret: &[u8], counter: u64, digits: u32) → u32`

## What it does

HOTP (HMAC-based One-Time Password, RFC 4226) — time-independent OTP.
Core idea: HMAC counter mode, dynamic truncation to 6-8 digit code.
When to use: multi-factor authentication, app-based OTP generation.

## Guarantee

When it runs, hotp guarantees assert_eq!(code, exp, "HOTP counter {} mismatch: got {}, expected {}", counter, code, exp) (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(code, exp, "HOTP counter {} mismatch: got {}, expected {}", counter, code, exp)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
