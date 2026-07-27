# blue green deploy

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 12 · Deployment & rollback

**Signature:** `(app_code: str) → ?`

## What it does

Blue-green deployment (two full stacks, atomic switch).

## Guarantee

When it runs, blue green deploy guarantees bg.get_active_color() == 'blue'; new_color == 'green'; os.path.exists(os.path.join(bg.green_dir, 'app.py')) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `bg.get_active_color() == 'blue'`
- `new_color == 'green'`
- `os.path.exists(os.path.join(bg.green_dir, 'app.py'))`
- `bg.get_active_color() == 'blue'`
- `bg.get_active_color() == 'green'`
- `bg.get_active_color() == 'blue'`
- `bg.get_active_color() == 'green'`
- `bg.get_active_dir() == bg.blue_dir`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class BlueGreenDeploy:`, `def __init__(self, workspace_path):`, `def get_active_color(self):`, `def deploy_to_inactive(self, app_code):`, `def switch_active(self, new_color):`, `def get_active_dir(self):`
**Valid input:** `workspace_path` is a writable directory; `app_code` is a string; `new_color` is `'blue'` or `'green'`.
**Core:** Maintains two directories (`blue/` and `green/`); deploys new code to whichever directory is currently inactive, then atomically flips the active color via a JSON state file.
**Assert:** Initial active color is `'blue'`; deploying writes to the inactive (`green`) directory without affecting active traffic; switching makes green active and subsequent deploys go to blue; zero-downtime sequence works.
**⚠️ Defect:** `switch_active` writes the state file directly (not via temp+rename), so a crash during the write can leave the active color corrupted. `deploy_to_inactive` clears files but does not remove stale subdirectories, and it never validates `app_code` syntax or health.

---
*△ AURA Pattern Library — © Reality Optimizer*
