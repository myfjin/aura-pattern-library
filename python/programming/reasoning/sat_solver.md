# sat solver

**Language:** Python · **Sphere:** programming · **Category:** Reasoning

**Signature:** `(formula: Formula, assignment: Dict[int, bool]) → Optional[Dict[int, bool]]`

## What it does

DPLL SAT solver for Boolean formulas in CNF.

Represents literals, clauses, and CNF formulas, then decides satisfiability by
the DPLL search: unit propagation, pure-literal elimination, and backtracking
branch on an unassigned variable. Returns a satisfying assignment or None if
none exists. Use it to solve small propositional constraint problems. Guarantees
(self-test oracle): known SAT/UNSAT verdicts are exact, unit propagation forces
the required assignments, and across 60 random 3-CNF formulas the verdict
matches an exhaustive truth-table oracle with every SAT model verified.

## Guarantee

When it runs, sat solver guarantees sat_seen + unsat_seen == 60; m1 is not None; f1.is_satisfied(m1) (proven by run).

**Checkable constraints:**

- `m1 is not None`
- `f1.is_satisfied(m1)`
- `solve_sat(f2) is None`
- `m3 is not None and f3.is_satisfied(m3)`
- `m3[1] is True and m3[2] is True and (m3[3] is True)`
- `solve_sat(_build(all_clauses)) is None`
- `model is not None`
- `_build(spec).is_satisfied(model)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
