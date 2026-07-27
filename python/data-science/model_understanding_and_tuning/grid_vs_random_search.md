# grid vs random search

**Language:** Python · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(params: Dict[str, float]) → float`

## What it does

Grid Search vs Random Search: Demonstrating Random Search Efficiency

Core idea: When hyperparameter space is high-dimensional but only a few params matter,
random search explores more efficiently than grid search.

When to use: You have many hyperparams but limited evaluation budget, or want to understand
when random search is preferable to grid search.

## Guarantee

When it runs, grid vs random search guarantees random_score > grid_score - 0.05; random_evals < grid_evals; random_score > -0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `random_score > grid_score - 0.05`
- `random_evals < grid_evals`
- `random_score > -0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
