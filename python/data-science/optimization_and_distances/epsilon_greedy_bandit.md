# epsilon greedy bandit

**Language:** Python · **Sphere:** data-science · **Category:** Optimization & Distances

## What it does

OPTIMIZATION: Epsilon-Greedy Multi-Armed Bandit

Core idea: In a multi-armed bandit, each arm yields stochastic reward.
Epsilon-greedy balances exploration (try random arms) vs exploitation (pull best known).
Pure greedy exploits only; epsilon-greedy explores with probability epsilon.

When to use: Online decision-making with unknown reward distributions (ad serving,
clinical trials, A/B testing). Epsilon controls exploration-exploitation tradeoff.

## Guarantee

When it runs, epsilon greedy bandit guarantees len(sequence_greedy) == num_pulls; len(sequence_epsilon) == num_pulls; pulls_arm2_epsilon > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(sequence_greedy) == num_pulls`
- `len(sequence_epsilon) == num_pulls`
- `pulls_arm2_epsilon > 0`
- `reward_greedy > 0`
- `reward_epsilon > 0`
- `pulls_per_arm_epsilon[2] >= 0.5 * max_pulls_epsilon`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `MultiArmedBandit` class with methods:
- `__init__(arm_means: List[float], arm_stds: List[float] = None)`
- `pull(arm: int) -> float`
- `run_pure_greedy(num_pulls: int = 1000) -> Tuple[float, List[int]]`
- `run_epsilon_greedy(epsilon: float = 0.1, num_pulls: int = 1000) -> Tuple[float, List[int]]`
**Valid input:** `arm_means` non-empty; `num_pulls >= len(arm_means)`; `epsilon` in `[0, 1]`.
**Core:** Simulates a multi-armed bandit. Pure greedy estimates each arm once then commits to the best first estimate. Epsilon-greedy explores with probability `ε` and exploits the empirical best arm otherwise, updating running mean estimates.
**Assert:** On 5 arms with means `[1.0, 1.5, 2.0, 0.5, 1.2]` and `num_pulls=1000`, asserts both total rewards are positive, epsilon-greedy pulls the true best arm at least once, and the best arm gets at least half the maximum pull count.
**⚠️ Defect:** `run_pure_greedy` never updates the estimated mean after the initial single pull, so it cannot recover if the first pull from the true best arm was unlucky. The comparison to epsilon-greedy is therefore comparing a deliberately broken baseline to a reasonable algorithm, overstating the benefit of epsilon-greedy.

---
*△ AURA Pattern Library — © Reality Optimizer*
