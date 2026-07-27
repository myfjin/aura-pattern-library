# csp solver

**Language:** Go · **Sphere:** programming · **Category:** Reasoning

## What it does

csp_solver: constraint satisfaction problem solver with backtracking and AC-3.

## Guarantee

When it runs, csp solver guarantees sum(g.values()) == 6; solution is not None; len(by_name) == 7 (proven by run on the PY-PROG original).

**Checkable constraints:**

- `solution is not None`
- `len(by_name) == 7`
- `violated == []`
- `all((v in ('red', 'green', 'blue') for v in by_name.values()))`
- `sol is not None`
- `g['X00'] != g['X01'] and g['X10'] != g['X11']`
- `g['X00'] != g['X10'] and g['X01'] != g['X11']`
- `g['X00'] == g['X11'] and g['X01'] == g['X10']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY-PROG original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
