"""
Particle filter (SMC): track a noisy 1D random walk target.

Core idea: maintain weighted particles; predict, weight by observation likelihood,
resample. Particle-mean RMSE beats raw observations; effective sample size monitors degeneracy.

When to use: nonlinear filtering, state tracking, online Bayesian inference.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List, Tuple



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_particle_filter_step(process_noise, obs_noise):
    v = []
    if isinstance(process_noise, (int, float)) and process_noise <= 0:
        v.append(f"AURA-E009: process_noise must be > 0, got {process_noise}")
    if isinstance(obs_noise, (int, float)) and not math.isfinite(obs_noise):
        v.append(f"AURA-E008: obs_noise must be finite, got {obs_noise}")
    if v:
        raise AuraInputError(v)



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_particle_filter_step(observation):
    v = []
    if isinstance(observation, (int, float)) and not math.isfinite(observation):
        v.append(f"AURA-E008: observation must be finite, got {observation}")
    if v:
        raise AuraInputError(v)

def particle_filter_step(particles: List[float], weights: List[float],
                         observation: float, process_noise: float = 0.2,
                         obs_noise: float = 0.5) -> Tuple[List[float], List[float], float]:
    """
    One step: predict, weight, resample.
    Return: (new_particles, new_weights, effective_sample_size)
    """
    _aura_validate_particle_filter_step(observation)
    _aura_validate_particle_filter_step(process_noise, obs_noise)
    n = len(particles)

    # Predict: add process noise
    predicted = [p + random.gauss(0, process_noise) for p in particles]

    # Weight by observation likelihood: w_i ∝ N(obs | x_i, obs_noise²)
    log_likelihoods = [-0.5 * ((observation - x) / obs_noise) ** 2 for x in predicted]
    max_ll = max(log_likelihoods)
    likelihoods = [math.exp(ll - max_ll) for ll in log_likelihoods]

    # Normalize weights
    new_weights = [w * ll / max(sum(w * ll for w, ll in zip(weights, likelihoods)), 1e-10)
                   for w, ll in zip(weights, likelihoods)]
    total_weight = sum(new_weights)
    if total_weight > 0:
        new_weights = [w / total_weight for w in new_weights]
    else:
        new_weights = [1.0 / n] * n

    # Effective sample size
    ess = 1.0 / max(sum(w ** 2 for w in new_weights), 1e-10)

    # Resample if ESS is low
    if ess < n / 2:
        # Multinomial resampling
        indices = random.choices(range(n), weights=new_weights, k=n)
        predicted = [predicted[i] for i in indices]
        new_weights = [1.0 / n] * n

    return predicted, new_weights, ess

if __name__ == '__main__':
    random.seed(42)

    # Generate true trajectory (random walk)
    true_traj = [0.0]
    for _ in range(50):
        true_traj.append(true_traj[-1] + random.gauss(0, 0.2))

    # Generate noisy observations
    observations = [x + random.gauss(0, 0.5) for x in true_traj]

    # Initialize particles
    n_particles = 100
    particles = [random.gauss(0, 1.0) for _ in range(n_particles)]
    weights = [1.0 / n_particles] * n_particles

    # Particle filter
    particle_means = [sum(p * w for p, w in zip(particles, weights)) / max(sum(weights), 1e-10)]
    raw_ess_values = []

    for obs in observations[1:]:
        particles, weights, ess = particle_filter_step(particles, weights, obs)
        mean = sum(p * w for p, w in zip(particles, weights)) / max(sum(weights), 1e-10)
        particle_means.append(mean)
        raw_ess_values.append(ess)

    # Assertions
    assert len(particle_means) == len(observations), "Should have a mean for each time step"

    # Particle-mean RMSE should beat raw observations
    particle_rmse = math.sqrt(sum((pm - tt) ** 2 for pm, tt in zip(particle_means[1:], true_traj[1:])) / len(true_traj[1:]))
    obs_rmse = math.sqrt(sum((ob - tt) ** 2 for ob, tt in zip(observations[1:], true_traj[1:])) / len(true_traj[1:]))
    assert particle_rmse < obs_rmse, f"Particle filter RMSE {particle_rmse} should beat obs RMSE {obs_rmse}"

    # ESS should be positive and <= n_particles
    for ess in raw_ess_values:
        assert 0 < ess <= n_particles + 1, f"ESS should be in (0, {n_particles}], got {ess}"

    # Average ESS should be reasonable (not always 1, not always n_particles)
    avg_ess = sum(raw_ess_values) / len(raw_ess_values)
    assert 5 < avg_ess < n_particles, f"Avg ESS should be reasonable, got {avg_ess}"

    # Particle means should be close to observations on average
    mean_diff = sum(abs(pm - ob) for pm, ob in zip(particle_means[1:], observations[1:])) / len(observations[1:])
    assert mean_diff < 1.5, f"Particle means should track observations, avg diff {mean_diff}"

    print("PASS")
