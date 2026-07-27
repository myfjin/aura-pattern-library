# particle filter 1d

**Language:** Python · **Sphere:** data-science · **Category:** Probabilistic Modeling

**Signature:** `(particles: List[float], weights: List[float], observation: float, process_noise: float, obs_noise: float) → Tuple[List[float], List[float], float]`

## What it does

Particle filter (SMC): track a noisy 1D random walk target.

Core idea: maintain weighted particles; predict, weight by observation likelihood,
resample. Particle-mean RMSE beats raw observations; effective sample size monitors degeneracy.

When to use: nonlinear filtering, state tracking, online Bayesian inference.

## Guarantee

When it runs, particle filter 1d guarantees len(particle_means) == len(observations); particle_rmse < obs_rmse; 0 < ess <= n_particles + 1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(particle_means) == len(observations)`
- `particle_rmse < obs_rmse`
- `0 < ess <= n_particles + 1`
- `5 < avg_ess < n_particles`
- `mean_diff < 1.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
