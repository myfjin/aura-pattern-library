# password hash verify

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(data: &[u8]) → [u8`

## What it does

Password hash verification (PBKDF2-salted) — constant-time comparison.
Core idea: unique salt per password, verify via timing-safe compare.
When to use: login systems, credential storage, password resets.

## Guarantee

When it runs, password hash verify guarantees assert_ne!(hash, hash2, "same password with different salt should differ"); assert_eq!(hash, hash3, "deterministic hashing") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(verify_password(password, salt, &hash), "correct password should verify")`
- `assert!(!verify_password("wrongpassword", salt, &hash), "wrong password should fail")`
- `assert_ne!(hash, hash2, "same password with different salt should differ")`
- `assert_eq!(hash, hash3, "deterministic hashing")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
