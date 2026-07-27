# index compaction pipeline

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

## What it does

composes: build-inverted-index + apply-tombstone-deletes + compact + query-exact-live-postings

## Guarantee

When it runs, index compaction pipeline guarantees assert_eq!(rust_docs.len(), 3, "rust has 3 posting docs"); assert_eq!(programming_docs.len(), 2, "programming has 2 posting docs"); assert_eq!(safety_docs.len(), 2, "safety has 2 posting docs") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(rust_docs.len(), 3, "rust has 3 posting docs")`
- `assert!(rust_docs.contains(&1), "doc 1 has rust")`
- `assert!(rust_docs.contains(&2), "doc 2 has rust")`
- `assert!(rust_docs.contains(&3), "doc 3 has rust")`
- `assert_eq!(compiler_docs, None, "compiler term deleted after compaction")`
- `assert_eq!(programming_docs.len(), 2, "programming has 2 posting docs")`
- `assert_eq!(safety_docs.len(), 2, "safety has 2 posting docs")`
- `assert_eq!(index.len(), 4, "Uncompacted index still has 4 terms (including tombstone)")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
