"""
HMM forward-backward algorithm: sequence likelihood and smoothed state posteriors.

Core idea: Forward pass computes P(observation_sequence, hidden_state_t) at each step.
Backward pass computes P(future_observations | hidden_state_t). Combined, they yield
smoothed posteriors P(hidden_state_t | entire_sequence) and sequence likelihood.
This differs from Viterbi (which finds the most likely state path) — forward-backward
computes marginal probabilities and total likelihood.

Use when: computing posterior state probabilities in a sequence, computing sequence likelihood,
smoothing noisy observations in a hidden Markov model.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple, Dict


def forward_backward(
    observations: List[int],
    initial_state: List[float],
    transition_matrix: List[List[float]],
    emission_matrix: List[List[float]]
) -> Tuple[float, List[List[float]]]:
    """
    Forward-backward algorithm for HMM.

    Args:
        observations: sequence of observation indices
        initial_state: P(state_0) vector
        transition_matrix: P(state_t | state_{t-1})
        emission_matrix: P(observation | state)

    Returns:
        (log_likelihood, smoothed_posteriors)
        where smoothed_posteriors[t][s] = P(state_t = s | all observations)
    """
    n_states = len(initial_state)
    n_obs = len(observations)

    # Forward pass
    forward = [[0.0] * n_states for _ in range(n_obs)]
    forward[0] = [initial_state[s] * emission_matrix[s][observations[0]] for s in range(n_states)]

    for t in range(1, n_obs):
        for s in range(n_states):
            forward[t][s] = emission_matrix[s][observations[t]] * sum(
                forward[t - 1][sp] * transition_matrix[sp][s] for sp in range(n_states)
            )

    # Likelihood
    log_likelihood = math.log(sum(forward[-1])) if sum(forward[-1]) > 0 else float('-inf')

    # Backward pass
    backward = [[0.0] * n_states for _ in range(n_obs)]
    backward[-1] = [1.0] * n_states

    for t in range(n_obs - 2, -1, -1):
        for s in range(n_states):
            backward[t][s] = sum(
                transition_matrix[s][sp] * emission_matrix[sp][observations[t + 1]] * backward[t + 1][sp]
                for sp in range(n_states)
            )

    # Smoothed posteriors: P(state_t | all observations)
    smoothed = [[0.0] * n_states for _ in range(n_obs)]
    for t in range(n_obs):
        norm = sum(forward[t][s] * backward[t][s] for s in range(n_states))
        if norm > 0:
            for s in range(n_states):
                smoothed[t][s] = (forward[t][s] * backward[t][s]) / norm

    return log_likelihood, smoothed


def brute_force_likelihood(
    observations: List[int],
    initial_state: List[float],
    transition_matrix: List[List[float]],
    emission_matrix: List[List[float]]
) -> float:
    """
    Brute-force likelihood: enumerate all possible state sequences.
    Used for verification on small examples only.
    """
    n_states = len(initial_state)
    n_obs = len(observations)

    def enumerate_paths(state_seq: List[int], obs_idx: int) -> float:
        if obs_idx == n_obs:
            # Compute probability of this path
            prob = initial_state[state_seq[0]]
            for s in state_seq:
                prob *= emission_matrix[s][observations[n_obs - n_obs + (state_seq.index(s) if state_seq.count(s) == 1 else 0)]]
            # Better: recompute properly
            prob = initial_state[state_seq[0]] * emission_matrix[state_seq[0]][observations[0]]
            for t in range(1, n_obs):
                prob *= transition_matrix[state_seq[t - 1]][state_seq[t]] * emission_matrix[state_seq[t]][observations[t]]
            return prob

        total = 0.0
        for next_state in range(n_states):
            total += enumerate_paths(state_seq + [next_state], obs_idx + 1)
        return total

    total_prob = enumerate_paths([], 0)
    return math.log(total_prob) if total_prob > 0 else float('-inf')


if __name__ == "__main__":
    import random
    random.seed(42)

    # Small 2-state HMM for verification
    initial_state = [0.6, 0.4]
    transition_matrix = [
        [0.7, 0.3],
        [0.4, 0.6]
    ]
    emission_matrix = [
        [0.9, 0.1],  # State 0: P(obs=0|s=0)=0.9, P(obs=1|s=0)=0.1
        [0.2, 0.8]   # State 1: P(obs=0|s=1)=0.2, P(obs=1|s=1)=0.8
    ]

    # Test sequence
    observations = [0, 1, 0]

    # Forward-backward
    log_ll_fb, smoothed = forward_backward(observations, initial_state, transition_matrix, emission_matrix)
    ll_fb = math.exp(log_ll_fb)

    # Brute-force verification
    ll_bf = math.exp(brute_force_likelihood(observations, initial_state, transition_matrix, emission_matrix))

    # Check likelihood match
    assert abs(ll_fb - ll_bf) < 1e-9, f"Likelihood mismatch: FB={ll_fb}, BF={ll_bf}"

    # Test 1: Smoothed posteriors sum to 1 at each time step
    for t in range(len(observations)):
        total = sum(smoothed[t])
        assert abs(total - 1.0) < 1e-9, f"Posteriors at t={t} should sum to 1, got {total}"

    # Test 2: All posteriors are in [0, 1]
    for t in range(len(observations)):
        for s in range(len(initial_state)):
            assert 0 <= smoothed[t][s] <= 1, f"Posterior at t={t}, s={s} out of range: {smoothed[t][s]}"

    # Test 3: Known scenario — strong evidence should concentrate posterior
    # Observation sequence [0, 0, 0] with emission favoring state 0 should give high P(state=0)
    obs_strong = [0, 0, 0]
    _, smoothed_strong = forward_backward(obs_strong, initial_state, transition_matrix, emission_matrix)
    # At t=0, P(state=0 | obs=[0,0,0]) should be substantial (strong evidence for state 0)
    assert smoothed_strong[0][0] > 0.5, f"Strong evidence for state 0 should give P(s=0)>0.5, got {smoothed_strong[0][0]}"

    # Test 4: Opposite sequence
    obs_weak = [1, 1, 1]
    _, smoothed_weak = forward_backward(obs_weak, initial_state, transition_matrix, emission_matrix)
    # At t=0, P(state=1 | obs=[1,1,1]) should be substantial (strong evidence for state 1)
    assert smoothed_weak[0][1] > 0.5, f"Strong evidence for state 1 should give P(s=1)>0.5, got {smoothed_weak[0][1]}"

    print("HMM forward-backward (likelihood + smoothed posteriors): all assertions PASS")
