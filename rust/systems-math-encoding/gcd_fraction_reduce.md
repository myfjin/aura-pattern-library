# gcd fraction reduce

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(mut a: u64, mut b: u64) → u64`

## What it does

GCD-based fraction reduction: simplify fractions to lowest terms.
Core idea: GCD divides both numerator and denominator evenly; quotients are coprime.
When to use: rational arithmetic, simplifying ratios, lowest common multiple.

## Guarantee

When it runs, gcd fraction reduce guarantees assert_eq!(g, 1, "Reduced fraction {}/{} should be coprime (gcd=1)", r_num, r_den); assert_eq!(num % g, 0, "GCD should divide numerator"); assert_eq!(den % g, 0, "GCD should divide denominator") (proven by rustc-run).

**Checkable constraints:**

- `assert!(den != 0, "denominator cannot be zero")`
- `assert_eq!((r_num, r_den), (*exp_num, *exp_den), "reduce_fraction({}/{}) = {}/{}, expected {}/{}", num, den, r_num, r_den, exp_num, exp_den)`
- `assert_eq!(g, 1, "Reduced fraction {}/{} should be coprime (gcd=1)", r_num, r_den)`
- `assert_eq!(num % g, 0, "GCD should divide numerator")`
- `assert_eq!(den % g, 0, "GCD should divide denominator")`
- `assert_eq!(r_num * g, num, "Quotient * GCD should equal original numerator")`
- `assert_eq!(r_den * g, den, "Quotient * GCD should equal original denominator")`
- `assert_eq!(gcd(48, 18), 6)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
