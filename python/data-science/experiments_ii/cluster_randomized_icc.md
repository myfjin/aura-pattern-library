# cluster randomized icc

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(t_obs: List[float], c_obs: List[float], true_effect: float) → bool`

## What it does

Cluster randomization: treatment assigned at the cluster level, not the individual.

Intracluster correlation (ICC) means observations within a cluster are not independent, so
the naive per-observation SE is too small — its 95% CIs UNDER-cover the true effect.
Aggregating to cluster means and testing on those (n = #clusters) restores nominal coverage.
Core claim: over many cluster-randomized datasets, the naive 95% CI under-covers while the
cluster-level 95% CI covers at ~95%.

## Guarantee

When it runs, cluster randomized icc guarantees naive_rate < 0.85; cluster_rate > 0.9; cluster_rate > naive_rate (weak-grade: directional, proven by run).

**Checkable constraints:**

- `naive_rate < 0.85`
- `cluster_rate > 0.9`
- `cluster_rate > naive_rate`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
