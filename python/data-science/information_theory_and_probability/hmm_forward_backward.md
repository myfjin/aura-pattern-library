# hmm forward backward

**Language:** Python · **Sphere:** data-science · **Category:** Information Theory & Probability

**Signature:** `(observations: List[int], initial_state: List[float], transition_matrix: List[List[float]], emission_matrix: List[List[float]]) → Tuple[float, List[List[float]]]`

## What it does

HMM forward-backward algorithm: sequence likelihood and smoothed state posteriors.

Core idea: Forward pass computes P(observation_sequence, hidden_state_t) at each step.
Backward pass computes P(future_observations | hidden_state_t). Combined, they yield
smoothed posteriors P(hidden_state_t | entire_sequence) and sequence likelihood.
This differs from Viterbi (which finds the most likely state path) — forward-backward
computes marginal probabilities and total likelihood.

Use when: computing posterior state probabilities in a sequence, computing sequence likelihood,
smoothing noisy observations in a hidden Markov model.

## Guarantee

When it runs, hmm forward backward guarantees abs(total - 1.0) < 1e-09; abs(ll_fb - ll_bf) < 1e-09; 0 <= smoothed[t][s] <= 1 (proven by run).

**Checkable constraints:**

- `abs(ll_fb - ll_bf) < 1e-09`
- `abs(total - 1.0) < 1e-09`
- `0 <= smoothed[t][s] <= 1`
- `smoothed_strong[0][0] > 0.5`
- `smoothed_weak[0][1] > 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def forward_backward(observations: List[int], initial_state: List[float], transition_matrix: List[List[float]], emission_matrix: List[List[float]]) -> Tuple[float, List[List[float]]]:`, `def brute_force_likelihood(observations: List[int], initial_state: List[float], transition_matrix: List[List[float]], emission_matrix: List[List[float]]) -> float:`, `def enumerate_paths(state_seq: List[int], obs_idx: int) -> float:`
**Valid input:** `initial_state` is a probability vector; `transition_matrix` and `emission_matrix` are stochastic matrices with compatible dimensions; `observations` indices are valid emission columns.
**Core:** Forward-backward algorithm for hidden Markov models: computes log sequence likelihood and smoothed state posteriors `P(state_t | all observations)`. A brute-force likelihood enumerates all state sequences for small verification examples.
**Assert:** Forward-backward likelihood matches brute-force likelihood within 1e-9 on a 2-state toy HMM; smoothed posteriors sum to 1.0 at each step and lie in [0, 1]; strong evidence sequences concentrate posterior mass on the favored state.
**⚠️ Defect:** No validation of matrix/vector dimensions or probability-row sums; malformed matrices raise opaque index errors later. Forward probabilities are stored as raw products, so long sequences can underflow to zero before the final `math.log(sum(...))`, making the reported likelihood `-inf` even when the model is valid.

---
*△ AURA Pattern Library — © Reality Optimizer*
