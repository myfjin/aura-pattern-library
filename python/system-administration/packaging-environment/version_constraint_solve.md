# version constraint solve

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(constraints: dict, available_versions: dict) → ?`

## What it does

version_constraint_solve: given constraints {name: constraint_str}, resolve to valid versions
or raise ValueError if unsatisfiable. Must reject conflicting constraints and accept compatible
ones. A naive solver might ignore conflicts or get the logic wrong.

## Guarantee

When it runs, version constraint solve guarantees solution['flask'][0] == 2; solution['werkzeug'] >= (2, 0, 0); False (proven by run).

**Checkable constraints:**

- `solution['flask'][0] == 2`
- `solution['werkzeug'] >= (2, 0, 0)`
- `'no version' in str(e) and 'flask' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
