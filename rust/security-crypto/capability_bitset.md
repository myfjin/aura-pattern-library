# capability bitset

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

## What it does

Capability bitset — permission flags via bit operations.
Core idea: grant/revoke/has via AND/OR/XOR, union/intersect checks.
When to use: ACLs, role-based access, feature flags.

## Guarantee

When it runs, capability bitset guarantees assert!(perms & EXECUTE == 0, "should not have EXECUTE"); assert!(perms & WRITE == 0, "WRITE should be revoked") (proven by rustc-run).

**Checkable constraints:**

- `assert!(perms & READ != 0, "should have READ")`
- `assert!(perms & WRITE != 0, "should have WRITE")`
- `assert!(perms & EXECUTE == 0, "should not have EXECUTE")`
- `assert!((perms & ro_perms) == ro_perms, "should contain READ")`
- `assert!((perms & (READ | EXECUTE)) != (READ | EXECUTE), "should not contain both READ+EXECUTE")`
- `assert!(perms & WRITE == 0, "WRITE should be revoked")`
- `assert!(perms & READ != 0, "READ should remain")`
- `assert!(combined & READ != 0)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
