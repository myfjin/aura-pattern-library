# modexp

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(mut base: u64, mut exp: u64, m: u64) → u64`

## What it does

Fast modular exponentiation: compute (base^exp) mod m efficiently.
Core idea: binary exponentiation, squaring and multiplying modulo m.
When to use: cryptography, number theory, Fermat/Euler tests, RSA-like math.

## Guarantee

When it runs, modexp guarantees assert_eq!(result, *expected, "modexp({}, {}, {}) = {}, expected {}", base, exp, m, result, expected); assert_eq!(modexp(5, 0, m), 1, "base^0 should be 1"); assert_eq!(result, 1, "Fermat's little theorem failed for a={}, p={}", a, p) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(result, *expected, "modexp({}, {}, {}) = {}, expected {}", base, exp, m, result, expected)`
- `assert_eq!(fast, brute, "modexp mismatch: {}^{} mod {}", base, exp, m)`
- `assert_eq!(modexp(5, 0, m), 1, "base^0 should be 1")`
- `assert_eq!(modexp(base, 1, m), base % m, "base^1 should be base % m")`
- `assert_eq!(result, 1, "Fermat's little theorem failed for a={}, p={}", a, p)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
