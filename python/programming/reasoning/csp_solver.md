# csp solver

**Language:** Python · **Sphere:** programming · **Category:** Reasoning

## What it does

Constraint Satisfaction Problem (CSP) Solver Module

This module implements a complete CSP solver with backtracking search and
arc consistency (AC-3) algorithm for constraint propagation.

## Guarantee

When it runs, csp solver guarantees sum(g.values()) == 6; solution is not None; len(by_name) == 7 (proven by run).

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
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
