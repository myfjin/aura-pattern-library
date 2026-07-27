# diff engine

**Language:** Python · **Sphere:** programming · **Category:** Io

**Signature:** `() → None`

## What it does

A simple diff engine for text comparison.

## Guarantee

When it runs, diff engine guarantees kinds.count(EditType.EQUAL) == 3; kinds.count(EditType.DELETE) == 3; kinds.count(EditType.INSERT) == 3 (proven by run).

**Checkable constraints:**

- `old_r == old_text.splitlines(keepends=True)`
- `new_r == new_text.splitlines(keepends=True)`
- `kinds.count(EditType.EQUAL) == 3`
- `kinds.count(EditType.DELETE) == 3`
- `kinds.count(EditType.INSERT) == 3`
- `all((e.edit_type == EditType.EQUAL for e in same.compute_diff()))`
- `same.format_unified_diff() == ''`
- `unified.startswith('@@ -')`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
