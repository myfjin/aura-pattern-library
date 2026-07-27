# ucb bandit

**Language:** Python · **Sphere:** data-science · **Category:** Model Diagnostics

**Signature:** `(counts: List[int], rewards: List[float], c: float) → int`

## What it does

UCB1 Multi-Armed Bandit

Implements the Upper Confidence Bound (UCB1) algorithm for the multi-armed bandit problem.
UCB1 balances exploration and exploitation by selecting the arm with the highest upper confidence bound.

Use this for online decision-making under uncertainty: e.g., which variant to show users,
which ad to run, which hypothesis to test next.

## Guarantee

When it runs, ucb bandit guarantees best_arm_pulls > counts[0]; best_arm_pulls > counts[1]; best_arm_pulls > n_pulls * 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `best_arm_pulls > counts[0]`
- `best_arm_pulls > counts[1]`
- `best_arm_pulls > n_pulls * 0.5`
- `best_arm_pulls > n_pulls / 3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `run_ucb1_experiment(arms, n_pulls, c=1.0) → (counts, rewards_sum)`
**Valid input:** `arms: List[BernoulliArm]` — each with `p` in [0, 1]. `n_pulls ≥ 1`. `c ≥ 0`.
**Core:** UCB1 multi-armed bandit. Select arm with highest UCB = avg_reward + c·√(ln(total_pulls) / arm_pulls). Unplayed arms get infinite UCB (always selected first). Three Bernoulli arms: p=[0.1, 0.5, 0.9]. Best arm (p=0.9) should receive most pulls.
**Assert:** On 500 pulls with c=1.0: best arm pulled more than worst and medium, best arm pulled > 50% of time, best arm pulled more than random baseline (1/3).
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
