# mvcc snapshot query engine

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

## What it does

composes: versioned-writes-by-ts + snapshot-open-at-T + range-query-returns-versions-visible-at-T

## Guarantee

When it runs, mvcc snapshot query engine guarantees assert_eq!(snapshot_data.len(), 2, "Snapshot has exactly 2 keys") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(snapshot_data.get("a"), Some(&"a-v2".to_string()), "a visible at ts=3")`
- `assert_eq!(snapshot_data.get("b"), Some(&"b-v1".to_string()), "b visible at ts=3 (v2 hidden)")`
- `assert_eq!(snapshot_data.get("c"), None, "c not visible at ts=3")`
- `assert_eq!(snapshot_data.len(), 2, "Snapshot has exactly 2 keys")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
