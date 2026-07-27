# env diff

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(env1: dict, env2: dict) → ?`

## What it does

env_diff: compare two environment dictionaries (env vars) and report differences.
Failure simulated: missing a key variable, wrong value, or extra variable. The differ
must accurately report all three types of changes.

## Guarantee

When it runs, env diff guarantees 'NEW_VAR' in diff['added']; 'DEBUG' in diff['changed']; diff['changed']['DEBUG'] == ('0', '1') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `'NEW_VAR' in diff['added']`
- `'DEBUG' in diff['changed']`
- `diff['changed']['DEBUG'] == ('0', '1')`
- `len(diff['removed']) == 0`
- `'SECRET' in diff2['removed']`
- `'REMOVED_IN_ENV1' in diff2['removed']`
- `len(diff2['added']) == 0`
- `len(diff2['changed']) == 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
