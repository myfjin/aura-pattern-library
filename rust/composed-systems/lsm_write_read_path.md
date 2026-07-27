# lsm write read path

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

## What it does

composes: memtable-write + sorted-run-flush + multi-run-merge-read

## Guarantee

When it runs, lsm write read path guarantees assert_eq!(result.get("a"), Some(&"1".to_string()), "a still has original value"); assert_eq!(result.get("b"), Some(&"2-updated".to_string()), "b has updated value from run2"); assert_eq!(result.get("c"), Some(&"3".to_string()), "c still has original value") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(result.get("a"), Some(&"1".to_string()), "a still has original value")`
- `assert_eq!(result.get("b"), Some(&"2-updated".to_string()), "b has updated value from run2")`
- `assert_eq!(result.get("c"), Some(&"3".to_string()), "c still has original value")`
- `assert_eq!(result.get("d"), Some(&"4".to_string()), "d added in run2")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
