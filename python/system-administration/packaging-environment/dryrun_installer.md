# dryrun installer

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(install_dir: str, packages: dict, dry_run: bool) → ?`

## What it does

dryrun_installer: perform a dry-run installation (no actual modifications), verify it
would succeed, then do a real installation and verify the system state changed correctly.
The dry-run must NOT modify the system; a broken dry-run would leave side effects.

## Guarantee

When it runs, dryrun installer guarantees sorted(dry_result) == ['app1', 'app2']; not os.path.exists(install_dir); sorted(real_result) == ['app1', 'app2'] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `sorted(dry_result) == ['app1', 'app2']`
- `not os.path.exists(install_dir)`
- `sorted(real_result) == ['app1', 'app2']`
- `os.path.exists(install_dir)`
- `os.path.exists(manifest_path)`
- `os.path.exists(os.path.join(install_dir, 'app1-1.0.0.pkg'))`
- `os.path.exists(os.path.join(install_dir, 'app2-2.0.0.pkg'))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
