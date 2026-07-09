"""
Grid Search vs Random Search: Demonstrating Random Search Efficiency

Core idea: When hyperparameter space is high-dimensional but only a few params matter,
random search explores more efficiently than grid search.

When to use: You have many hyperparams but limited evaluation budget, or want to understand
when random search is preferable to grid search.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import List, Tuple, Dict


def evaluate_model(params: Dict[str, float]) -> float:
    """
    Synthetic objective: maximize model quality.
    Only param 'important' matters; others don't affect outcome.
    Quality = -|important - 0.7|^2 + small noise
    """
    important = params["important"]
    quality = -(important - 0.7) ** 2 + random.gauss(0, 0.01)
    return quality


def grid_search(
    param_ranges: Dict[str, Tuple[float, float]],
    num_values: int = 3
) -> Tuple[Dict[str, float], float, int]:
    """
    Grid search over hyperparameters.
    Returns (best_params, best_score, num_evals).
    """
    param_names = list(param_ranges.keys())
    best_score = -float("inf")
    best_params = {}
    num_evals = 0

    # Generate grid
    grids = {}
    for param, (low, high) in param_ranges.items():
        grids[param] = [low + (high - low) * i / (num_values - 1) for i in range(num_values)]

    # Enumerate grid
    def grid_enumerate(idx, current_params):
        nonlocal best_score, best_params, num_evals
        if idx == len(param_names):
            score = evaluate_model(current_params)
            num_evals += 1
            if score > best_score:
                best_score = score
                best_params = current_params.copy()
        else:
            param = param_names[idx]
            for val in grids[param]:
                current_params[param] = val
                grid_enumerate(idx + 1, current_params)

    grid_enumerate(0, {})
    return best_params, best_score, num_evals


def random_search(
    param_ranges: Dict[str, Tuple[float, float]],
    num_samples: int = 20
) -> Tuple[Dict[str, float], float, int]:
    """
    Random search over hyperparameters.
    Returns (best_params, best_score, num_evals).
    """
    best_score = -float("inf")
    best_params = {}

    for _ in range(num_samples):
        params = {}
        for param, (low, high) in param_ranges.items():
            params[param] = random.uniform(low, high)

        score = evaluate_model(params)
        if score > best_score:
            best_score = score
            best_params = params.copy()

    return best_params, best_score, num_samples


if __name__ == "__main__":
    random.seed(42)

    # Hyperparameter ranges: only 'important' matters for the true objective
    param_ranges = {
        "important": (0.0, 1.0),
        "useless1": (0.0, 1.0),
        "useless2": (0.0, 1.0),
    }

    # Grid search: 3 values per param = 3^3 = 27 evaluations
    print("Grid Search (3 values per param, 27 total):")
    grid_params, grid_score, grid_evals = grid_search(param_ranges, num_values=3)
    print(f"  Best score: {grid_score:.4f}, Evals: {grid_evals}")

    # Random search: 20 samples
    print("Random Search (20 samples):")
    random_params, random_score, random_evals = random_search(param_ranges, num_samples=20)
    print(f"  Best score: {random_score:.4f}, Evals: {random_evals}")

    # Assertion: random search should find comparable quality with fewer evaluations
    assert random_score > grid_score - 0.05, f"Random should find near-optimal: {random_score} vs {grid_score}"
    assert random_evals < grid_evals, f"Random should use fewer evals: {random_evals} vs {grid_evals}"
    assert random_score > -0.1, "Best score should be near optimum 0.0"

    print("✓ Grid vs Random Search: PASS")
