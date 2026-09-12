"""Matrix factorization via stochastic gradient descent.

Core idea: decompose a sparse rating matrix into user (U) and item (V) factor
matrices of low rank, trained by SGD to minimize rating prediction error.
Convergence is verified by RMSE dropping below a threshold.

When to use: when you have sparse user-item rating data and want latent factors
for dimensionality reduction or to fill missing entries.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Dict, Tuple


def matrix_factorization_sgd(
    ratings: Dict[Tuple[int, int], float],
    num_users: int,
    num_items: int,
    rank: int = 2,
    learning_rate: float = 0.01,
    lambda_reg: float = 0.1,
    epochs: int = 500,
) -> Tuple[Dict[int, Dict[int, float]], Dict[int, Dict[int, float]], float]:
    """
    Train matrix factorization via SGD.
    Returns (user_factors, item_factors, final_rmse).
    """
    # Initialize factors randomly
    U: Dict[int, Dict[int, float]] = {
        u: {f: random.gauss(0, 0.1) for f in range(rank)} for u in range(num_users)
    }
    V: Dict[int, Dict[int, float]] = {
        i: {f: random.gauss(0, 0.1) for f in range(rank)} for i in range(num_items)
    }

    rmse_history = []

    for epoch in range(epochs):
        total_error = 0.0
        count = 0

        # SGD pass over all observed ratings
        for (u, i), rating in ratings.items():
            # Predict: sum_f U[u][f] * V[i][f]
            pred = sum(U[u][f] * V[i][f] for f in range(rank))
            error = rating - pred
            total_error += error**2
            count += 1

            # Update factors
            for f in range(rank):
                dU = -error * V[i][f] + lambda_reg * U[u][f]
                dV = -error * U[u][f] + lambda_reg * V[i][f]
                U[u][f] -= learning_rate * dU
                V[i][f] -= learning_rate * dV

        rmse = math.sqrt(total_error / count) if count > 0 else 0.0
        rmse_history.append(rmse)

    return U, V, rmse_history[-1]


if __name__ == "__main__":
    random.seed(42)

    # Synthetic low-rank rating matrix: 5×4 with rank-2 structure
    # Generate as outer product of two low-rank factors, then add noise
    true_rank = 2
    num_users = 5
    num_items = 4

    # True latent factors
    true_U = {u: [random.uniform(1, 2) for _ in range(true_rank)] for u in range(num_users)}
    true_V = {i: [random.uniform(1, 2) for _ in range(true_rank)] for i in range(num_items)}

    # Generate noisy observations
    ratings: Dict[Tuple[int, int], float] = {}
    for u in range(num_users):
        for i in range(num_items):
            true_rating = sum(true_U[u][f] * true_V[i][f] for f in range(true_rank))
            noisy_rating = true_rating + random.gauss(0, 0.1)
            ratings[(u, i)] = max(1.0, min(5.0, noisy_rating))  # Clip to 1-5

    # Train matrix factorization
    U, V, final_rmse = matrix_factorization_sgd(
        ratings,
        num_users,
        num_items,
        rank=2,
        learning_rate=0.05,
        lambda_reg=0.01,
        epochs=500,
    )

    # RMSE should drop well below initial reconstruction error
    assert final_rmse < 0.5, f"Final RMSE {final_rmse} exceeds threshold 0.5"

    print(f"matrix_factorization_sgd.py: final_rmse={final_rmse:.4f} PASS")
