# roman numeral

**Language:** Rust · **Sphere:** rust · **Category:** systems-math-encoding

**Signature:** `(mut n: u16) → Option<String>`

## What it does

Roman numeral codec: integer ↔ Roman numeral (range 1..=3999).
Core idea: subtractive notation (IV=4, IX=9, XL=40, XC=90, CD=400, CM=900).
When to use: numeral display, parsing historical text, constraint-based encoding.

## Guarantee

When it runs, roman numeral guarantees assert_eq!(&roman, expected_roman, "int_to_roman({}) mismatch", num) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(&roman, expected_roman, "int_to_roman({}) mismatch", num)`
- `assert_eq!(decoded, *num, "roman round-trip mismatch")`
- `assert_eq!(decoded, i, "round-trip failed for {}", i)`
- `assert_eq!(int_to_roman(0), None, "0 should be invalid")`
- `assert_eq!(int_to_roman(4000), None, "4000 should be invalid")`
- `assert_eq!(roman_to_int("I" ), Some(1))`
- `assert_eq!(roman_to_int("MMMCMXCIX"), Some(3999))`
- `assert_eq!(roman_to_int("IV"), Some(4))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — roundtrip (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
