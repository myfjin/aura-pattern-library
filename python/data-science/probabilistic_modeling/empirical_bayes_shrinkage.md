# empirical bayes shrinkage

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(groups: List[List[float]]) → Tuple[List[float], List[float], float]`

## What it does

Empirical Bayes shrinkage (James-Stein style): shrink group means toward grand mean.

Core idea: estimate hyperparameter from data; shrink group means via Bayesian posterior.
Total squared error BEATS raw group means (Stein's paradox measured).

When to use: meta-analysis, small-group inference, estimation of many parameters.

## Guarantee

When it runs, empirical bayes shrinkage guarantees len(shrunken_means) == K; 0 <= shrinkage <= 1; dist_shrunken <= dist_raw (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(shrunken_means) == K`
- `0 <= shrinkage <= 1`
- `dist_shrunken <= dist_raw`
- `tot_shr < tot_raw`
- `wins / reps > 0.55`
- `shrinkage >= 0`
- `shrink_unif < shrinkage - 0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
