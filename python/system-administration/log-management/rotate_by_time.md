# rotate by time

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 5 · Log management

**Signature:** `(log_path: str, rotation_interval_sec: int, keep_duration_sec: int) → ?`

## What it does

Rotate logs by time: age past the retention window, assert old files are pruned.
Failure simulated: a fake logical clock ages rotated files well past the window.
Defended outcome: every file older than keep_duration is deleted; a no-op keeps them → fails.
NOTE: rotated files are stamped with the FAKE time via os.utime, so the prune comparison and
the age assert live on ONE clock (mixing fake time with real ~1.7e9 mtimes made this vacuous).

## Guarantee

When it runs, rotate by time guarantees age <= keep_window; os.path.exists(log_path); not glob.glob(f'{log_path}.[0-9]*') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(rotated_before) >= 2`
- `age <= keep_window`
- `os.path.exists(log_path)`
- `not glob.glob(f'{log_path}.[0-9]*')`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
