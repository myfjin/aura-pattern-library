# merkle verified sync

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(data: &[u8]) → u64`

## What it does

composes: chunk-two-versions + build-REAL-merkle-trees + root+subtree-diff + sync-only-changed

A real merkle tree: leaves are chunk hashes, each internal node = hash(left, right), up to a
single root. The diff descends from the root and SKIPS any subtree whose node hash matches —
that is the whole point of a merkle tree (verify/diff without touching every leaf). We prove
the skip: the unchanged sibling subtree's node hash is compared once and its leaves never are.

## Guarantee

When it runs, merkle verified sync guarantees assert_ne!(root(&tree1), root(&tree2), "a changed chunk must change the merkle root"); assert_eq!(changed, vec![1], "exactly leaf 1 changed"); assert!(visited_leaves < v1.len(), "unchanged subtree skipped (visited {visited_leaves} of {} leaves)", v1.len()) (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_ne!(root(&tree1), root(&tree2), "a changed chunk must change the merkle root")`
- `assert_eq!(changed, vec![1], "exactly leaf 1 changed")`
- `assert!(visited_leaves < v1.len(), "unchanged subtree skipped (visited {visited_leaves} of {} leaves)", v1.len())`
- `assert_eq!(synced, v2, "after syncing changed chunks, versions match exactly")`
- `assert_eq!(synced[0], v1[0])`
- `assert_eq!(synced[2], v1[2])`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
