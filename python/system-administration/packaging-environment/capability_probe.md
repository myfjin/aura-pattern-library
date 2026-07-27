# capability probe

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(test_dir: str) → ?`

## What it does

capability_probe: probe system capabilities (hardlinks, symlinks, sparse files, etc.)
and record which are available. Mutate the system state (remove capability) and re-probe;
verify the capability is no longer reported.

## Guarantee

When it runs, capability probe guarantees caps1.get('symlinks') or caps1.get('hardlinks'); 'execute_bit' in caps1; caps_before.get('symlinks') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `caps1.get('symlinks') or caps1.get('hardlinks')`
- `'execute_bit' in caps1`
- `caps_before.get('symlinks')`
- `not caps_after.get('symlinks')`
- `caps_before.get('symlinks')`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
