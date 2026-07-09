"""
UCB1 Multi-Armed Bandit

Implements the Upper Confidence Bound (UCB1) algorithm for the multi-armed bandit problem.
UCB1 balances exploration and exploitation by selecting the arm with the highest upper confidence bound.

Use this for online decision-making under uncertainty: e.g., which variant to show users,
which ad to run, which hypothesis to test next.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


class BernoulliArm:
    """A Bernoulli arm with a fixed success probability."""

    def __init__(self, success_prob: float):
        self.p = success_prob

    def draw(self) -> int:
        """Draw from Bernoulli: return 1 with prob p, 0 otherwise."""
        return 1 if random.random() < self.p else 0


def ucb1_select_arm(counts: List[int], rewards: List[float], c: float = 1.0) -> int:
    """
    Select arm with highest UCB.
    UCB = avg_reward + c * sqrt(ln(total_pulls) / arm_pulls)
    """
    total_pulls = sum(counts)
    if total_pulls == 0:
        return 0

    ucb_values = []
    for i in range(len(counts)):
        if counts[i] == 0:
            # Unplayed arm: infinite UCB (or high value)
            ucb_values.append(float('inf'))
        else:
            avg_reward = rewards[i] / counts[i]
            exploration_bonus = c * math.sqrt(math.log(total_pulls) / counts[i])
            ucb_values.append(avg_reward + exploration_bonus)

    return ucb_values.index(max(ucb_values))


def run_ucb1_experiment(
    arms: List[BernoulliArm], n_pulls: int, c: float = 1.0
) -> Tuple[List[int], List[float]]:
    """
    Run UCB1 algorithm for n_pulls.
    Returns (arm_counts, arm_rewards_sum).
    """
    counts = [0] * len(arms)
    rewards = [0.0] * len(arms)

    for _ in range(n_pulls):
        arm_idx = ucb1_select_arm(counts, rewards, c=c)
        reward = arms[arm_idx].draw()

        counts[arm_idx] += 1
        rewards[arm_idx] += reward

    return counts, rewards


def test_ucb1() -> None:
    """
    Test UCB1: best arm should receive most pulls, regret should be sublinear.
    """
    random.seed(42)

    # Three Bernoulli arms: p=[0.1, 0.5, 0.9]
    # Best arm is 2 (p=0.9)
    arms = [BernoulliArm(0.1), BernoulliArm(0.5), BernoulliArm(0.9)]
    n_pulls = 500

    counts, rewards = run_ucb1_experiment(arms, n_pulls, c=1.0)

    # Best arm (index 2) should be pulled the most
    best_arm_pulls = counts[2]
    assert best_arm_pulls > counts[0], f"Best arm should be pulled more than worst: {best_arm_pulls} vs {counts[0]}"
    assert best_arm_pulls > counts[1], f"Best arm should be pulled more than medium: {best_arm_pulls} vs {counts[1]}"

    # Best arm should be pulled significantly more than others
    assert best_arm_pulls > n_pulls * 0.5, f"Best arm should be pulled >50% of time: {best_arm_pulls / n_pulls}"

    # Compare with random policy: expected pulls for random = n_pulls / 3
    assert best_arm_pulls > (n_pulls / 3), f"UCB1 should pull best arm more than 1/3: {best_arm_pulls / n_pulls}"

    print("ucb_bandit.py: PASS")


if __name__ == "__main__":
    test_ucb1()
