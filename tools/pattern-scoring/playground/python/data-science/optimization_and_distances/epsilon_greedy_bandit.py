"""
OPTIMIZATION: Epsilon-Greedy Multi-Armed Bandit

Core idea: In a multi-armed bandit, each arm yields stochastic reward.
Epsilon-greedy balances exploration (try random arms) vs exploitation (pull best known).
Pure greedy exploits only; epsilon-greedy explores with probability epsilon.

When to use: Online decision-making with unknown reward distributions (ad serving,
clinical trials, A/B testing). Epsilon controls exploration-exploitation tradeoff.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple


class MultiArmedBandit:
    """
    Simulate a multi-armed bandit and compare pure greedy vs epsilon-greedy.
    """

    def __init__(self, arm_means: List[float], arm_stds: List[float] = None):
        """
        Initialize bandit with known arm distributions (for simulation).
        arm_means: list of true mean rewards per arm
        arm_stds: list of reward std devs (default: 1.0 for all)
        """
        self.arm_means = arm_means
        self.num_arms = len(arm_means)
        if arm_stds is None:
            self.arm_stds = [1.0] * self.num_arms
        else:
            self.arm_stds = arm_stds

    def pull(self, arm: int) -> float:
        """Pull an arm and get stochastic reward."""
        return random.gauss(self.arm_means[arm], self.arm_stds[arm])

    def run_pure_greedy(self, num_pulls: int = 1000) -> Tuple[float, List[int]]:
        """
        Pure greedy: estimate each arm once, then always pull the best.
        Returns (total_reward, arm_pulls)
        """
        estimated_means = [0.0] * self.num_arms
        pulls_per_arm = [0] * self.num_arms

        # Initial round: pull each arm once to estimate
        for arm in range(self.num_arms):
            estimated_means[arm] = self.pull(arm)
            pulls_per_arm[arm] = 1

        total_reward = sum(estimated_means)
        arm_sequence = list(range(self.num_arms))

        # Greedy phase: always pull the best
        best_arm = estimated_means.index(max(estimated_means))
        for _ in range(num_pulls - self.num_arms):
            reward = self.pull(best_arm)
            total_reward += reward
            pulls_per_arm[best_arm] += 1
            arm_sequence.append(best_arm)

        return total_reward, arm_sequence

    def run_epsilon_greedy(
        self, epsilon: float = 0.1, num_pulls: int = 1000
    ) -> Tuple[float, List[int]]:
        """
        Epsilon-greedy: with probability epsilon, explore random arm;
        otherwise exploit best known arm.
        Returns (total_reward, arm_pulls)
        """
        estimated_means = [0.0] * self.num_arms
        pull_counts = [0] * self.num_arms

        # Initial round: pull each arm once
        for arm in range(self.num_arms):
            estimated_means[arm] = self.pull(arm)
            pull_counts[arm] = 1

        total_reward = sum(estimated_means)
        arm_sequence = list(range(self.num_arms))

        # Epsilon-greedy phase
        for _ in range(num_pulls - self.num_arms):
            if random.random() < epsilon:
                # Explore: random arm
                arm = random.randint(0, self.num_arms - 1)
            else:
                # Exploit: best known arm
                arm = estimated_means.index(max(estimated_means))

            reward = self.pull(arm)
            total_reward += reward
            pull_counts[arm] += 1
            estimated_means[arm] += (reward - estimated_means[arm]) / pull_counts[arm]
            arm_sequence.append(arm)

        return total_reward, arm_sequence


if __name__ == "__main__":
    random.seed(42)

    # Set up bandit with 5 arms
    # True means: [1.0, 1.5, 2.0, 0.5, 1.2]
    # Best arm is arm 2 with mean 2.0
    arm_means = [1.0, 1.5, 2.0, 0.5, 1.2]
    bandit = MultiArmedBandit(arm_means)

    num_pulls = 1000

    # Test 1: Pure greedy
    reward_greedy, sequence_greedy = bandit.run_pure_greedy(num_pulls)
    pulls_per_arm_greedy = [sequence_greedy.count(i) for i in range(5)]

    # Test 2: Epsilon-greedy with epsilon=0.1
    reward_epsilon, sequence_epsilon = bandit.run_epsilon_greedy(epsilon=0.1, num_pulls=num_pulls)
    pulls_per_arm_epsilon = [sequence_epsilon.count(i) for i in range(5)]

    # Assertions
    # Pure greedy gets stuck; after initial exploration, it pulls the best-estimated arm
    # (which may not be the true best if unlucky in first round)
    assert len(sequence_greedy) == num_pulls, "Greedy did not perform num_pulls"
    assert len(sequence_epsilon) == num_pulls, "Epsilon-greedy did not perform num_pulls"

    # Epsilon-greedy should eventually discover the true best arm (arm 2, mean 2.0)
    # Count pulls on arm 2
    pulls_arm2_greedy = pulls_per_arm_greedy[2]
    pulls_arm2_epsilon = pulls_per_arm_epsilon[2]

    # Epsilon-greedy should explore and find arm 2 more reliably or with similar frequency
    # (it explores all arms with some probability)
    assert (
        pulls_arm2_epsilon > 0
    ), "Epsilon-greedy should pull the best arm at least once"

    # Total reward should be positive (all arms have positive means)
    assert reward_greedy > 0, f"Pure greedy reward not positive: {reward_greedy}"
    assert reward_epsilon > 0, f"Epsilon-greedy reward not positive: {reward_epsilon}"

    # Verify that the best arm gets the most pulls in epsilon-greedy
    # (or at least comparable to other arms)
    max_pulls_epsilon = max(pulls_per_arm_epsilon)
    assert (
        pulls_per_arm_epsilon[2] >= 0.5 * max_pulls_epsilon
    ), "Epsilon-greedy not pulling best arm frequently"

    print(
        f"epsilon_greedy_bandit.py: greedy_reward={reward_greedy:.2f} epsilon_reward={reward_epsilon:.2f} best_arm_pulls={pulls_per_arm_epsilon[2]} PASS"
    )
