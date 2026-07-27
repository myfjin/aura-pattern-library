# otp lockout

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(state: &mut OTPState, code: u32, correct: u32, now: u64, max_attempts: u32, lock_duration: u64) → bool`

## What it does

OTP lockout — N failed attempts triggers account lock (time-gated).
Core idea: counter resets on success, lock window enforced.
When to use: brute-force protection, TOTP/SMS validation.

## Guarantee

When it runs, otp lockout guarantees assert_eq!(state.failed_attempts, 0); assert_eq!(state.failed_attempts, 1); assert_eq!(state.failed_attempts, 2) (proven by rustc-run).

**Checkable constraints:**

- `assert!(attempt_otp(&mut state, correct_code, correct_code, 100, 3, 60))`
- `assert_eq!(state.failed_attempts, 0)`
- `assert!(!attempt_otp(&mut state, 999999, correct_code, 101, 3, 60))`
- `assert_eq!(state.failed_attempts, 1)`
- `assert!(!attempt_otp(&mut state, 111111, correct_code, 102, 3, 60))`
- `assert_eq!(state.failed_attempts, 2)`
- `assert!(!attempt_otp(&mut state, 222222, correct_code, 103, 3, 60))`
- `assert_eq!(state.failed_attempts, 3)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
