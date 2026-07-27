# open fd count

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(fd_dir_listing: str) → ?`

## What it does

open_fd_count: Count open file descriptors from /proc/[pid]/fd.
THE ONE LAW: Parse directory listing, assert exact count matches directory size.
Portable fallback on non-Linux.

## Guarantee

When it runs, open fd count guarantees count == 8; dirty_count == 4; dup_count == 5 (proven by run).

**Checkable constraints:**

- `count == 8`
- `dirty_count == 4`
- `dirty_count != 8`
- `empty_count == 0`
- `dup_count == 5`
- `real_count > 0`
- `isinstance(real_count, int)`
- `real_count is None or real_count > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
