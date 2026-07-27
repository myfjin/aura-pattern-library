# session token expiry

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(id: &str, now: u64, ttl: u64) → SessionToken`

## What it does

Session token expiry — virtual-clock based lifecycle.
Core idea: issue timestamp, validate expiry window, revocation.
When to use: OAuth tokens, session cookies, temporary credentials.

## Guarantee

When it runs, session token expiry guarantees assert_eq!(token.issued_at, 100); assert_eq!(token.expires_at, 150) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(token.issued_at, 100)`
- `assert_eq!(token.expires_at, 150)`
- `assert!(validate_token(&token, 125, &revoked), "token valid within window")`
- `assert!(!validate_token(&token, 150, &revoked), "token expired at boundary")`
- `assert!(!validate_token(&token, 99, &revoked), "token not yet valid")`
- `assert!(!validate_token(&token, 125, &revoked), "revoked token rejected")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
