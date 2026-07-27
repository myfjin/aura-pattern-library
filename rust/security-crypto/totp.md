# totp

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(secret: &[u8], time_s: u64, step: u64, digits: u32) → u32`

## What it does

TOTP (Time-based OTP, RFC 6238) — time-synchronized one-time passwords.
Core idea: HOTP with time window (30s intervals), SHA1 truncation.
When to use: authenticator apps, 2FA, backup codes.

## Guarantee

When it runs, totp guarantees assert_eq!(totp(rfc, 59, 30, 8), 94287082, "RFC 6238 T=59 must be 94287082"); assert_eq!(totp(rfc, 1111111109, 30, 8), 7081804, "RFC 6238 T=1111111109 must be 07081804"); assert_eq!(totp(rfc, 1234567890, 30, 8), 89005924, "RFC 6238 T=1234567890 must be 89005924") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(code_t59, code_t45, "same window (30-59) codes must match")`
- `assert_ne!(code_t59, code_t60, "adjacent windows must differ")`
- `assert_eq!(code_t0, code_t15, "same window (0-29) must match")`
- `assert_eq!(totp(rfc, 59, 30, 8), 94287082, "RFC 6238 T=59 must be 94287082")`
- `assert_eq!(totp(rfc, 1111111109, 30, 8), 7081804, "RFC 6238 T=1111111109 must be 07081804")`
- `assert_eq!(totp(rfc, 1234567890, 30, 8), 89005924, "RFC 6238 T=1234567890 must be 89005924")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
