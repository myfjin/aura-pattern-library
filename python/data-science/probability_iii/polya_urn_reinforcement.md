# polya urn reinforcement

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(a: int, b: int, num_draws: int) → float`

## What it does

Pólya urn: reinforcement model whose limiting proportion is RANDOM ~ Beta(a, b).

Start with a balls of color A, b of color B. Each draw: pick a ball, return it plus one
more of the same color. The rich-get-richer feedback means a single urn's proportion does
NOT converge to the mean a/(a+b) — it converges to a RANDOM limit distributed as Beta(a,b).
Core claim (the actual theorem): across many urns the limiting proportions have mean
a/(a+b) AND variance matching Beta(a,b) — i.e. they SPREAD, they do not concentrate.

## Guarantee

When it runs, polya urn reinforcement guarantees abs(emp_mean - theo_mean) < 0.03; abs(emp_var - theo_var) < 0.005; emp_var > 0.01 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(emp_mean - theo_mean) < 0.03`
- `abs(emp_var - theo_var) < 0.005`
- `emp_var > 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
