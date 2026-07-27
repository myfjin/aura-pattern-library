# luhn checksum

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(number: &str) → bool`

## What it does

Luhn checksum (mod-10 algorithm): validates credit card and similar numbers.
Core idea: double every second digit from right, sum digits, valid if sum % 10 == 0.
When to use: credit card validation, IMEI checking, single-digit error detection.

## Guarantee

When it runs, luhn checksum guarantees assert!(luhn_checksum("0"), "Single 0 should be valid") (none-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(luhn_checksum("0"), "Single 0 should be valid")`
- `assert!(luhn_checksum("18"), "Simple 18 should be valid")`
- `assert!(luhn_checksum("4111111111111111"), "Test card number")`
- `assert!(!luhn_checksum("4111111111111112"), "Modified should be invalid")`
- `assert!(luhn_checksum(number), "Expected {} to be valid", number)`
- `assert!(!luhn_checksum(&modified), "Single-digit error not detected at position {}", pos)`
- `assert!(luhn_checksum(test1), "{} should be valid", test1)`
- `assert!(!luhn_checksum(test2), "{} should be invalid", test2)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** none (no checkable constraint)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
