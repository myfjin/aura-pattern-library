# matrix factorization sgd

**Language:** Python · **Sphere:** data-science · **Category:** Recommenders & Graph Sampling

**Signature:** `(ratings: Dict[Tuple[int, int], float], num_users: int, num_items: int, rank: int, learning_rate: float, lambda_reg: float, epochs: int) → Tuple[Dict[int, Dict[int, float]], Dict[int, Dict[int, float]], float]`

## What it does

Matrix factorization via stochastic gradient descent.

Core idea: decompose a sparse rating matrix into user (U) and item (V) factor
matrices of low rank, trained by SGD to minimize rating prediction error.
Convergence is verified by RMSE dropping below a threshold.

When to use: when you have sparse user-item rating data and want latent factors
for dimensionality reduction or to fill missing entries.

## Guarantee

When it runs, matrix factorization sgd guarantees final_rmse < 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `final_rmse < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def matrix_factorization_sgd(ratings: Dict[Tuple[int, int], float], num_users: int, num_items: int, rank: int = 2, learning_rate: float = 0.01, lambda_reg: float = 0.1, epochs: int = 500,) -> Tuple[Dict[int, Dict[int, float]], Dict[int, Dict[int, float]], float]:`
**Valid input:** `ratings` maps `(user, item)` → rating; `num_users`, `num_items`, `rank`, `epochs` > 0; `learning_rate`, `lambda_reg` > 0; all user/item IDs in `ratings` are within declared ranges.
**Core:** Stochastic gradient descent matrix factorization: learns user and item latent factor matrices to minimize squared reconstruction error on observed ratings plus L2 regularization. Returns final user factors, item factors, and training RMSE.
**Assert:** On a synthetic rank-2 rating matrix with small noise, final RMSE < 0.5 after 500 epochs.
**⚠️ Defect:** The SGD pass iterates over `ratings.items()` in insertion order with no shuffling, so the update trajectory is deterministic and can converge slowly or to a suboptimal ordering-sensitive minimum. There are no user/item bias terms, so global rating shifts must be absorbed into the latent factors. The returned RMSE is training RMSE, not a held-out metric.

---
*△ AURA Pattern Library — © Reality Optimizer*
