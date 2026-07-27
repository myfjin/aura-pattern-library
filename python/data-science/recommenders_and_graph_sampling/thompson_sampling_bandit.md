# thompson sampling bandit

**Language:** Python · **Sphere:** data-science · **Category:** Recommenders & Graph Sampling

**Signature:** `(num_arms: int, num_rounds: int, true_probabilities: List[float]) → Dict[str, float]`

## What it does

Thompson sampling for multi-armed bandits.

Core idea: maintain Beta posteriors over success probability for each arm,
sample from each posterior, pull the arm with highest sample, update via
Bayesian update. Balances exploration vs exploitation optimally.

When to use: when you need to allocate resources (A/B test, optimization)
and want to minimize regret by learning arm quality online.

## Guarantee

When it runs, thompson sampling bandit guarantees pulls_ts[0] > pulls_ts[2]; result_ts['cumulative_reward'] > cumulative_reward_random (weak-grade: directional, proven by run).

**Checkable constraints:**

- `pulls_ts[0] > pulls_ts[2]`
- `result_ts['cumulative_reward'] > cumulative_reward_random`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def sample_beta(alpha: float, beta: float) -> float:`, `def thompson_sampling_bandit(num_arms: int, num_rounds: int, true_probabilities: List[float],) -> Dict[str, float]:`
**Valid input:** `num_arms` > 0; `len(true_probabilities) == num_arms`; each true probability in [0, 1]; `num_rounds` > 0.
**Core:** Thompson sampling for multi-armed bandits: maintains Beta posteriors over each arm's success probability, samples each posterior, pulls the arm with the highest sample, and performs a Bayesian update. Balances exploration and exploitation online.
**Assert:** On a three-arm bandit with true probabilities [0.8, 0.6, 0.4] over 1,000 rounds, the best arm is pulled more often than the worst arm, and cumulative reward exceeds a random policy.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
