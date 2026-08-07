# diff engine

**Language:** Go · **Oracle sphere:** programming (this file is the Go twin) · **Category:** Io

## What it does

diff_engine: a simple line-based diff engine.

## Guarantee

When it runs, diff engine guarantees kinds.count(EditType.EQUAL) == 3; kinds.count(EditType.DELETE) == 3; kinds.count(EditType.INSERT) == 3 (proven by run on the PY-PROG original).

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
- **Independent oracle:** — established on the PY-PROG original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
