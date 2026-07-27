# constant time eq

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(a: &[u8], b: &[u8]) → bool`

## What it does

Constant-time equality (timing-attack resistance) — compare all bytes, always.
Core idea: OR all byte differences; never early-return on first mismatch, so the WORK
done is independent of WHERE (or whether) a difference occurs. THE ONE LAW: a naive
`==` that returns on the first mismatch leaks position via timing; we prove our version
does the SAME amount of work regardless of the difference position (an early-return impl
would fail that). When to use: HMAC/signature verification, password/secret comparison.

## Guarantee

When it runs, constant time eq guarantees assert_eq!(ops_first, 256, "every byte must be examined") (proven by rustc-run).

**Checkable constraints:**

- `assert!(const_eq(&[1, 2, 3], &[1, 2, 3]), "equal should be true")`
- `assert!(const_eq(&[], &[]), "empty should be equal")`
- `assert!(!const_eq(&[1, 2], &[1, 2, 3]), "different lengths should be false")`
- `assert!(!const_eq(&[1, 2, 3], &[1, 2, 4]), "different bytes should be false")`
- `assert!(!const_eq(&base, &b), "difference at position {pos} not detected")`
- `assert_eq!(ops_first, ops_last, "constant-time: work must not depend on difference position")`
- `assert_eq!(ops_first, ops_equal, "constant-time: mismatch and match do the same work")`
- `assert_eq!(ops_first, 256, "every byte must be examined")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
