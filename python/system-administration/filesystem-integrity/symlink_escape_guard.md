# symlink escape guard

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 2 · Filesystem Integrity & Atomic Ops

**Signature:** `(link_path: str, target_path: str, root_dir: str) → ?`

## What it does

symlink_escape_guard: refuse to create symlinks that escape the root directory.
Failure simulated: attempt to create symlinks that point outside root (escape attack);
assert the guard refuses it. Allow symlinks within root.
Recovery asserted: escape attempts are blocked; safe symlinks are created; path resolution
proves the target is within root or denied. Pattern's own guard function is called.

## Guarantee

When it runs, symlink escape guard guarantees os.readlink(link_safe) == relative_target; False; 'escape detected' in str(e) (proven by run).

**Checkable constraints:**

- `'escape detected' in str(e)`
- `not Path(link_path).exists()`
- `not os.path.islink(link_path)`
- `'escape detected' in str(e)`
- `not Path(link_path2).exists()`
- `os.path.islink(link_safe)`
- `os.readlink(link_safe) == relative_target`
- `content_via_link == b'safe_target_content'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
