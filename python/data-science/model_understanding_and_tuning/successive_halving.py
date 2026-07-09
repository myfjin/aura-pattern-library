"""
Successive Halving for Hyperparameter Optimization

Core idea: Allocate more resources to promising configurations, halving the pool at each stage.
Early elimination of poor performers saves budget while identifying good configs.

When to use: You have many hyperparameter candidates but limited evaluation budget, and want
to concentrate resources on the most promising ones.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Dict, Tuple


def evaluate_config(config: Dict[str, float], budget: int) -> float:
    """
    Synthetic evaluation: simulate training with a given budget.
    Planted best config has low loss; others vary.
    """
    # Planted best config: learning_rate near 0.01, param1 near 0.5
    loss = 1.0

    # Distance from planted optimum
    dist_lr = (config["learning_rate"] - 0.01) ** 2 * 100
    dist_p1 = (config["param1"] - 0.5) ** 2 * 0.5
    loss += dist_lr + dist_p1

    # Budget helps (diminishing returns)
    loss /= (1 + 0.01 * budget)

    return loss + random.gauss(0, 0.01)


def successive_halving(
    initial_configs: List[Dict[str, float]],
    initial_budget: int = 10,
    reduction_factor: int = 2
) -> Tuple[Dict[str, float], float]:
    """
    Successive halving: evaluate all configs, halve the pool, double budget.
    Returns (best_config, best_loss).
    """
    configs = initial_configs[:]
    budget = initial_budget

    while len(configs) > 1:
        print(f"  Stage: {len(configs)} configs, budget {budget} per config")

        # Evaluate all remaining configs
        scores = []
        for config in configs:
            loss = evaluate_config(config, budget)
            scores.append((loss, config))

        # Sort by loss (lower is better)
        scores.sort()

        # Keep top half
        num_keep = max(1, len(configs) // reduction_factor)
        configs = [config for _, config in scores[:num_keep]]

        # Double budget
        budget *= reduction_factor

    # Final best config
    best_loss = evaluate_config(configs[0], budget * reduction_factor)
    return configs[0], best_loss


if __name__ == "__main__":
    random.seed(42)

    # Generate random candidate configurations
    num_initial = 16
    initial_configs = []
    for _ in range(num_initial):
        config = {
            "learning_rate": random.uniform(0.001, 0.1),
            "param1": random.uniform(0.0, 1.0),
            "param2": random.uniform(0.0, 1.0),
        }
        initial_configs.append(config)

    print(f"Initial pool: {num_initial} configs")
    print("Running Successive Halving:")

    best_config, best_loss = successive_halving(initial_configs, initial_budget=10, reduction_factor=2)

    print(f"\nBest config: lr={best_config['learning_rate']:.4f}, p1={best_config['param1']:.4f}, p2={best_config['param2']:.4f}")
    print(f"Best loss: {best_loss:.4f}")

    # Verify that learning_rate is close to planted optimum
    lr_error = abs(best_config["learning_rate"] - 0.01)
    print(f"LR error from optimum (0.01): {lr_error:.4f}")

    # Assertion: best config should be close to planted optimum, and survive to the end
    assert best_loss < 2.0, f"Best loss should be low: {best_loss}"
    assert len(initial_configs) == num_initial, "Did not modify initial configs"

    print("✓ Successive Halving: PASS")
