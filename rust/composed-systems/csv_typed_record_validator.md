# csv typed record validator

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(line: &str) → Vec<String>`

## What it does

composes: csv-parse-rfc4180 + type-coercion + row-validation

## Guarantee

When it runs, csv typed record validator guarantees assert_eq!(valid.len(), 2, "Should accept exactly 2 records"); assert_eq!(invalid.len(), 3, "Should reject exactly 3 records"); assert_eq!(valid[0].name, "Alice") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(valid.len(), 2, "Should accept exactly 2 records")`
- `assert_eq!(invalid.len(), 3, "Should reject exactly 3 records")`
- `assert_eq!(valid[0].name, "Alice")`
- `assert_eq!(valid[0].age, 25)`
- `assert_eq!(valid[1].name, "David")`
- `assert_eq!(valid[1].age, 35)`
- `assert!(!valid.is_empty(), "Validation happened")`
- `assert!(invalid.len() > 0, "Invalid records were rejected")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
