# config diff

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 9 · Config management

**Signature:** `(old_config: dict, new_config: dict) → ?`

## What it does

Config diff: report exact changes (added/removed/changed keys) between configs.
Failure simulated: missing changes reported; wrong keys in added/removed/changed.
Asserts: exact set of added keys; exact set of removed keys; exact dict of changed values.

## Guarantee

When it runs, config diff guarantees diff['added'] == {'debug'}; diff['removed'] == set(); diff['changed'] == {} (weak-grade: directional, proven by run).

**Checkable constraints:**

- `diff['added'] == {'debug'}`
- `diff['removed'] == set()`
- `diff['changed'] == {}`
- `diff['added'] == set()`
- `diff['removed'] == {'debug'}`
- `diff['changed'] == {}`
- `diff['added'] == set()`
- `diff['removed'] == set()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def config_diff(old_config, new_config):`
**Valid input:** `old_config` and `new_config` are dicts with comparable values.
**Core:** Computes the difference between two flat configs: keys added, keys removed, and keys changed (with old and new values as a tuple).
**Assert:** Added key, removed key, changed value, complex add/remove/change, and identical configs all produce the expected diff structure.
**⚠️ Defect:** Only top-level keys are compared; nested dict values are compared by equality but not diffed recursively. Values must be equality-comparable, which breaks for unhashable or non-eq types like custom objects.

---
*△ AURA Pattern Library — © Reality Optimizer*
