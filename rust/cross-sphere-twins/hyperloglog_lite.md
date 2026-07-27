# hyperloglog lite

**Language:** Rust · **Sphere:** rust · **Category:** cross-sphere-twins

**Signature:** `(item: &str) → u64`

## What it does

hyperloglog_lite — cardinality estimate; relative error within a COMPUTED bound.

Core idea: hash each item to 64 bits; the low P bits pick a register (m = 2^P), the remaining
bits' leading-zero run + 1 (rho) is recorded as the register's max. The harmonic-mean estimate
α·m²/Σ2^-reg approximates the distinct count with standard error 1.04/√m. The bucket bits and
the rho bits must NOT overlap, and the hash must spread bits well — get either wrong and the
estimate blows up. THE LAW: estimate a large distinct set and assert the relative error is
within 3× the standard error (a real ~3σ bound, not a vacuous 10×). When to use: approximate
distinct counts, cardinality estimation. (`_lite`: no small/large-range bias correction.)

## Guarantee

When it runs, hyperloglog lite guarantees assert!(actual_error <= std_error * 3.0, "actual error {:.4} exceeds 3×std {:.4} (est {:.0}, true {})", actual_error, std_error * 3.0, estimated, true_cardinality); assert!((empty - alpha * m as f64).abs() < 1.0, "empty raw estimate floors near α·m ≈ {:.0}", alpha * m as f64); assert!(estimated > empty * 10.0, "a large distinct set estimates far above the empty floor") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(m.is_power_of_two(), "m must be a power of two")`
- `assert!(actual_error <= std_error * 3.0, "actual error {:.4} exceeds 3×std {:.4} (est {:.0}, true {})", actual_error, std_error * 3.0, estimated, true_cardinality)`
- `assert!((empty - alpha * m as f64).abs() < 1.0, "empty raw estimate floors near α·m ≈ {:.0}", alpha * m as f64)`
- `assert!(estimated > empty * 10.0, "a large distinct set estimates far above the empty floor")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
