# process tree

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(proc_lines: str) → ?`

## What it does

process_tree: Build process tree from /proc-style data, re-parent orphans to ppid=1.
THE ONE LAW: Parse process list with dead-parent process, assert it's re-parented to 1.
Anti-fake rule 2: Failure case must assert orphan STAYS orphaned without the fix.

## Guarantee

When it runs, process tree guarantees broken_orphan[0][1] == 50; broken_tree[1][1] == 50; len(orphan) == 1 (proven by run).

**Checkable constraints:**

- `len(orphan) == 1`
- `orphan[0][1] == 1`
- `orphan[0][2] == 'orphan-child'`
- `normal[0][1] == 1`
- `broken_orphan[0][1] == 50`
- `tree[1][1] == 1`
- `broken_tree[1][1] == 50`
- `pids == [1, 100, 101]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
