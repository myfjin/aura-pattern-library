# dir tree diff

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(tree1_index: dict, tree2_index: dict) → ?`

## What it does

dir_tree_diff: compute a diff between two directory trees (file presence, size, content hash).
Failure simulated: create two similar trees; modify one file; diff trees and assert
the difference is detected (changed file flagged, unchanged files not).
Recovery asserted: diff correctly identifies added, removed, modified, and unchanged files.
Pattern's own diff function is called.

## Guarantee

When it runs, dir tree diff guarantees len(diff['unchanged']) == expected_unchanged_count; len(diff['added']) == 0; len(diff['removed']) == 0 (proven by run).

**Checkable constraints:**

- `len(diff['added']) == 0`
- `len(diff['removed']) == 0`
- `len(diff['modified']) == 0`
- `len(diff['unchanged']) == expected_unchanged_count`
- `'file_b.txt' in diff['modified']`
- `len(diff['modified']) == 1`
- `len(diff['added']) == 0`
- `len(diff['removed']) == 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
