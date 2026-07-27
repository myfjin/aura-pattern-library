# dir size aggregate

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `() → u64`

## What it does

dir_size_aggregate — recursive size sum over a synthetic tree; equals brute force.

Core idea: walk a directory tree and sum file sizes. THE ONE LAW: create a synthetic
tree with known structure and sizes, compute total size via recursion, then assert
it matches a brute-force sum of all files. A missed file or double-count would fail.
When to use: disk usage analysis, quota checking, storage reporting.

## Guarantee

When it runs, dir size aggregate guarantees assert_eq!(recursive_total, 100 + 200 + 50 + 75, "total should be 425 bytes"); assert_eq!(root.file_count(), 4, "should count all 4 files"); assert_eq!(sparse_recursive, 999, "only one file with 999 bytes") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(recursive_total, brute_force_total, "recursive total must match brute force")`
- `assert_eq!(recursive_total, 100 + 200 + 50 + 75, "total should be 425 bytes")`
- `assert_eq!(root.file_count(), 4, "should count all 4 files")`
- `assert_eq!(sparse_recursive, sparse_brute, "empty dirs should not affect total")`
- `assert_eq!(sparse_recursive, 999, "only one file with 999 bytes")`
- `assert_eq!(single.total_size(), 12345)`
- `assert_eq!(single.file_count(), 1)`
- `assert_eq!(many_recursive, many_expected, "sum of 1..100 should be 5050")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
