# 5S Batch 1 — DS Pattern Detail Docs (20 patterns)

Categories: `linear_algebra` (10) + `optimization_and_distances` (10).

---

## Category: linear_algebra

### 1. conjugate_gradient.py
**Entry fn:** `conjugate_gradient(A: list, b: list, x0: list, tol: float = 1e-8, max_iter: int = None) -> list`
**Valid input:** `A` is an n×n symmetric positive-definite matrix; `b` length n; `x0` length n; `tol > 0`.
**Core:** Iterative Krylov solver for SPD systems. Maintains search direction `p` conjugate w.r.t. `A`, updates residual `r`, step size `α`, and direction multiplier `β`. Stops when residual norm falls below `tol` or after `max_iter` (default n).
**Assert:** On planted SPD 3×3 system `A = [[4,1,0],[1,3,1],[0,1,2]]`, `b = [1,2,3]`, verifies `||A·x - b||∞ < 1e-6`.
**⚠️ Defect:** No input validation that `A` is symmetric or positive-definite. If `A` is indefinite, `p_dot_Ap` can be zero/negative and the method silently breaks with a near-arbitrary result. SPD assumption is asserted only by the demo matrix choice, not by the code.

### 2. gauss_seidel_vs_jacobi.py
**Entry fn:**
- `jacobi_iteration(A: list, b: list, x0: list, max_iter: int = 100, tol: float = 1e-8) -> Tuple[list, int]`
- `gauss_seidel_iteration(A: list, b: list, x0: list, max_iter: int = 100, tol: float = 1e-8) -> Tuple[list, int]`
**Valid input:** `A` n×n diagonally dominant (to guarantee convergence); `b`, `x0` length n.
**Core:** Two stationary iterative solvers for `A·x = b`. Jacobi updates all coordinates from the previous iterate; Gauss–Seidel uses freshly updated values immediately. Both return the solution and the iteration count to convergence.
**Assert:** On planted diagonally dominant 3×3 system, asserts Gauss–Seidel iterations < Jacobi iterations and that both solutions agree within `0.01`.
**⚠️ Defect:** No diagonal-zero guard. If any diagonal element is zero, both methods divide by zero and crash. Convergence is also not guaranteed for non-diagonally-dominant matrices; the docstring claims GS is faster as a general rule, but this only holds for systems where both methods converge.

### 3. householder_reflection.py
**Entry fn:**
- `householder_reflection(x: list) -> Tuple[list, float]`
- `apply_householder(H_vector: list, beta: float, x: list) -> list`
**Valid input:** `x` is a non-zero length-n numeric vector. `H_vector` is a unit vector, `beta` is `2.0` as returned by `householder_reflection`.
**Core:** Computes a Householder vector `v` and scalar `β=2` such that `H = I - β·v·v^T` reflects `x` onto the first axis. `apply_householder` multiplies `H` by a vector.
**Assert:** On `x = [3,4,0]`, verifies `H·x = [±5, 0, 0]` within `1e-10`.
**⚠️ Defect:** `householder_reflection` always returns `beta = 2.0`, but the docstring says `H = I - 2·v·v^T / (v^T·v)` while the code normalizes `v` to unit length. The returned pair is internally consistent with `apply_householder`, but the API is misleading: `beta` is a fixed constant rather than `2/(v^T·v)` as the comment suggests.

### 4. jacobi_eigen_symmetric.py
**Entry fn:** `jacobi_eigen(A: list, max_iter: int = 100, tol: float = 1e-10) -> Tuple[list, list]`
**Valid input:** `A` is an n×n symmetric matrix.
**Core:** Jacobi eigenvalue algorithm. Repeatedly applies Givens rotations to zero the largest off-diagonal element, accumulating rotations in `V`. Returns eigenvalues (diagonal of the transformed matrix) and eigenvector matrix `V`.
**Assert:** On planted symmetric 3×3 matrix with known spectrum `{3-√3, 3, 3+√3}`, sorts eigenpairs and verifies each eigenvalue within `1e-8` and `A·v = λ·v` within `1e-8`.
**⚠️ Defect:** Eigenvector matrix layout is transposed relative to the docstring. The docstring says "eigenvectors[i] is the i-th eigenvector", but the code stores `V[i][j]` as component `i` of eigenvector `j`. The demo happens to access it correctly, but a caller using `eigenvectors[i]` directly will get the wrong vector.

### 5. least_squares_qr.py
**Entry fn:**
- `qr_gram_schmidt_tall(A: list) -> Tuple[list, list]`
- `least_squares_qr(A: list, b: list) -> list`
**Valid input:** `A` is m×n with `m > n` and full column rank; `b` length m.
**Core:** Gram–Schmidt QR for tall matrices, then solves `R·x = Q^T·b` by back-substitution. Avoids normal-equation squaring of the condition number.
**Assert:** On overdetermined 4×2 system `A = [[1,1],[1,2],[1,3],[1,4]]`, `b = [2,3,5,4]`, checks residual norm is between `0.1` and `2.0`.
**⚠️ Defect:** Uses classical (not modified) Gram–Schmidt, which is numerically unstable for nearly dependent columns. The test matrix is well-conditioned, so the defect is hidden; on ill-conditioned least-squares problems the computed `Q` can lose orthogonality and the solution accuracy degrades.

### 6. lu_decomposition_pivoting.py
**Entry fn:**
- `lu_decomposition_pivoting(A: list) -> Tuple[list, list, list]`
- `matrix_mult(A: list, B: list) -> list`
**Valid input:** `A` is an n×n invertible matrix.
**Core:** LU factorization with partial row pivoting. Returns permutation matrix `P`, lower triangular `L`, and upper triangular `U` such that `P·A = L·U`.
**Assert:** On planted 3×3 matrix, verifies `P·A = L·U` element-wise within `1e-10`.
**⚠️ Defect:** No forward/backward substitution helper is provided, so the factorization cannot actually be used to solve `A·x = b` without the caller writing the solve step. The module advertises "decomposition and forward/backward solves tested" in the top comment, but only the decomposition is exposed.

### 7. matrix_condition_number.py
**Entry fn:**
- `condition_number(A: list) -> float`
- `matrix_norm_frobenius(A: list) -> float`
- `matrix_inverse_lu(A: list) -> list`
**Valid input:** `A` is an n×n invertible matrix.
**Core:** Estimates `κ(A) = ||A||_F · ||A⁻¹||_F` by inverting `A` via LU with partial pivoting and computing Frobenius norms.
**Assert:** Compares a well-conditioned matrix (`κ ≈ 4.6`) against an ill-conditioned matrix (`κ ≈ 60001`) and asserts the ill-conditioned one is at least 100× larger.
**⚠️ Defect:** The internal inverse routine is fragile. The forward-substitution loop uses `b[j]` after it has already been overwritten (`b[i] = sum_val`), so the solve with multiple right-hand sides is wrong for all columns after the first. The demo only computes the condition number, and the bug may still produce a plausible-looking (but incorrect) inverse for matrices larger than 2×2.

### 8. power_iteration_shifted.py
**Entry fn:** `power_iteration_shifted(A: list, shift: float, max_iter: int = 100, tol: float = 1e-8) -> Tuple[float, list]`
**Valid input:** `A` n×n symmetric matrix; `shift` larger than the largest eigenvalue of `A`.
**Core:** Shifted power iteration to find the smallest eigenvalue of `A`. Iterates on `(A - shift·I)⁻¹` implicitly by multiplying by `(A - shift·I)`, then recovers the eigenvalue via the Rayleigh quotient.
**Assert:** On `A = [[4,1,0],[1,3,1],[0,1,2]]` with `shift = 5.0`, asserts smallest eigenvalue in `[0.5, 1.5]` and `A·v ≈ λ·v` within `0.1`.
**⚠️ Defect:** The method does not invert `(A - shift·I)`; it directly multiplies by `(A - shift·I)`, which is power iteration on the *most shifted* matrix rather than inverse iteration. Convergence is to the eigenvalue farthest from `shift` (largest magnitude of `λ - shift`), which equals the smallest `λ` only if `shift > λ_max`. The docstring claims this is verified, but the implementation silently gives the wrong eigenpair if `shift` is chosen differently.

### 9. qr_gram_schmidt.py
**Entry fn:**
- `qr_gram_schmidt(A: list) -> Tuple[list, list]`
- `matrix_mult(A: list, B: list) -> list`
- `matrix_transpose(A: list) -> list`
**Valid input:** `A` is an n×m matrix with `m` linearly independent columns.
**Core:** Classical Gram–Schmidt QR factorization. Returns Q (n×m orthonormal) and R (m×m upper triangular) such that `A = Q·R`.
**Assert:** On planted 3×3 matrix, verifies `Q^T·Q = I` and `A = Q·R` within `1e-10`.
**⚠️ Defect:** Same numerical stability issue as `least_squares_qr`: classical Gram–Schmidt loses orthogonality for nearly dependent or ill-conditioned columns. The test matrix is well-conditioned, so orthogonality appears perfect; a more realistic near-rank-deficient matrix would fail the `Q^T·Q = I` check.

### 10. woodbury_rank1_update.py
**Entry fn:**
- `matrix_inverse_lu(A: list) -> list`
- `vector_outer_product(u: list, v: list) -> list`
- `matrix_add(A: list, B: list) -> list`
- `woodbury_update(A_inv: list, u: list, v: list) -> list`
**Valid input:** `A_inv` is the inverse of an n×n invertible matrix `A`; `u`, `v` length-n vectors; `1 + v^T·A_inv·u ≠ 0`.
**Core:** Applies the Woodbury identity for a rank-1 update: `(A + u·v^T)⁻¹ = A⁻¹ - (A⁻¹·u·v^T·A⁻¹)/(1 + v^T·A⁻¹·u)`.
**Assert:** On 2×2 matrix `A = [[4,1],[1,3]]` with `u = [1,0]`, `v = [2,1]`, compares Woodbury result against direct 2×2 inversion within `1e-8`.
**⚠️ Defect:** The helper `matrix_inverse_lu` has the same forward-substitution bug as `matrix_condition_number` (overwrites `b` during the loop). For the demo’s 2×2 case the bug does not trigger visibly, but for larger matrices the supplied `A_inv` would be inaccurate, making `woodbury_update` silently wrong.

---

## Category: optimization_and_distances

### 11. distance_metrics_toolkit.py
**Entry fn:**
- `euclidean(p: List[float], q: List[float]) -> float`
- `manhattan(p: List[float], q: List[float]) -> float`
- `minkowski(p: List[float], q: List[float], p_order: float = 2.0) -> float`
- `chebyshev(p: List[float], q: List[float]) -> float`
- `cosine_similarity(p: List[float], q: List[float]) -> float`
- `cosine_distance(p: List[float], q: List[float]) -> float`
**Valid input:** `p`, `q` same-length numeric vectors. For `cosine_similarity`, non-zero vectors (returns `0.0` if either is zero).
**Core:** Computes L2, L1, Lp, L∞, and cosine similarity/distance between two vectors. Minkowski correctly switches to Chebyshev when `p_order == inf`.
**Assert:** On `p=[1,2,3]`, `q=[4,5,6]`, checks Euclidean=`√27`, Manhattan=`9`, Chebyshev=`3`, Minkowski(p=2)=Euclidean, Minkowski(p=1)=Manhattan, Minkowski(p=inf)=Chebyshev, cosine identical vectors = 1, and symmetry for Euclidean/Manhattan/Chebyshev/cosine.
**⚠️ Defect:** `minkowski` with non-integer or very large `p_order` on negative inputs can raise a `ValueError` from Python’s `**` operator (e.g. `p_order=0.5` with positive distances is fine, but a negative difference with non-integer power would fail). The function uses `abs(pi - qi) ** p_order`, which is safe for the demo but still restricts `p_order` to values valid for real exponentiation.

### 12. dtw_dynamic_time_warping.py
**Entry fn:** `dtw_distance(series1: List[float], series2: List[float]) -> Tuple[float, List[Tuple[int, int]]]`
**Valid input:** `series1`, `series2` non-empty lists of numbers.
**Core:** Dynamic Time Warping: fills an `(n+1)×(m+1)` cost matrix with `cost[i][j] = dist + min(cost[i-1][j], cost[i][j-1], cost[i-1][j-1])`, then backtracks to recover the optimal alignment path.
**Assert:** Identical series yield DTW distance `0`; warped series produce a positive distance with a non-empty alignment.
**⚠️ Defect:** The backtracking logic is incorrect. When `i>0` and `j>0` it chooses the minimum of three predecessors, but when either `i` or `j` hits zero it only decrements the non-zero index without checking whether the diagonal predecessor would have been cheaper. More importantly, the alignment path can skip the start `(0,0)` in some cases. The demo only checks non-negative distance, so the defect is not caught.

### 13. epsilon_greedy_bandit.py
**Entry fn:** `MultiArmedBandit` class with methods:
- `__init__(arm_means: List[float], arm_stds: List[float] = None)`
- `pull(arm: int) -> float`
- `run_pure_greedy(num_pulls: int = 1000) -> Tuple[float, List[int]]`
- `run_epsilon_greedy(epsilon: float = 0.1, num_pulls: int = 1000) -> Tuple[float, List[int]]`
**Valid input:** `arm_means` non-empty; `num_pulls >= len(arm_means)`; `epsilon` in `[0, 1]`.
**Core:** Simulates a multi-armed bandit. Pure greedy estimates each arm once then commits to the best first estimate. Epsilon-greedy explores with probability `ε` and exploits the empirical best arm otherwise, updating running mean estimates.
**Assert:** On 5 arms with means `[1.0, 1.5, 2.0, 0.5, 1.2]` and `num_pulls=1000`, asserts both total rewards are positive, epsilon-greedy pulls the true best arm at least once, and the best arm gets at least half the maximum pull count.
**⚠️ Defect:** `run_pure_greedy` never updates the estimated mean after the initial single pull, so it cannot recover if the first pull from the true best arm was unlucky. The comparison to epsilon-greedy is therefore comparing a deliberately broken baseline to a reasonable algorithm, overstating the benefit of epsilon-greedy.

### 14. feature_scaling_toolkit.py
**Entry fn:**
- `min_max_scale(data: List[float]) -> Tuple[List[float], float, float]`
- `z_score_scale(data: List[float]) -> Tuple[List[float], float, float]`
- `robust_scale(data: List[float]) -> Tuple[List[float], float, float]`
- `verify_properties(scaled: List[float], ...) -> bool`
**Valid input:** `data` is a list of numbers (empty list allowed, returns empty/zero stats).
**Core:** Three feature scalers: min-max to `[0,1]`, z-score to zero mean/unit std, and robust `(x - median)/IQR`.
**Assert:** On data `[10,12,11,13,14,100]`, checks min-max bounds, z-score mean≈0 and std≈1, robust finite values, outlier ranking, and invertibility of min-max and z-score.
**⚠️ Defect:** `robust_scale` computes quartiles with naive index slicing (`n//4` and `3*n//4`) rather than a proper percentile method. For small or even-length data this can be quite inaccurate; the demo does not verify that the scaled robust values actually have median 0 or that the interquartile range is 1.

### 15. genetic_algorithm.py
**Entry fn:** `GeneticAlgorithm` class with methods:
- `__init__(pop_size: int, bitstring_length: int, fitness_func: Callable, mutation_rate: float = 0.01, generations: int = 100)`
- `initialize_population()`, `evaluate_fitness(...)`, `selection_roulette_wheel()`, `crossover(...)`, `mutate(...)`, `evolve() -> Tuple[List[int], int]`
**Valid input:** `pop_size > 0`, `bitstring_length > 1`, `mutation_rate` in `[0,1]`, `generations >= 1`.
**Core:** Standard bit-string GA with roulette-wheel selection, single-point crossover, bit-flip mutation, and elitism-free generational replacement. Early-stops if an all-ones individual is found (only valid for OneMax).
**Assert:** Solves OneMax on length 20 with pop 100, mutation 0.02, 200 generations. Runs deceptive length-8 landscape and verifies its all-ones fitness is `18`.
**⚠️ Defect:** `evolve()` early-stops when `best_fitness == bitstring_length`, which is only correct for OneMax. If used with the deceptive fitness (max = `length + 10`), the loop may stop at a suboptimal all-zeros solution with fitness `length` (not `length+10`). The deceptive demo only checks fitness `>= 1`, so this subtle mis-convergence is not caught.

### 16. gradient_descent_momentum.py
**Entry fn:**
- `vanilla_gd(x: float, y: float, learning_rate: float = 0.005, tolerance: float = 1e-6, max_iters: int = 10000) -> Tuple[int, float]`
- `momentum_gd(x: float, y: float, learning_rate: float = 0.005, momentum: float = 0.9, tolerance: float = 1e-6, max_iters: int = 10000) -> Tuple[int, float]`
**Valid input:** Any real `x`, `y`; `learning_rate > 0`; `momentum` in `[0,1)`; `tolerance > 0`.
**Core:** Minimizes the 2D quadratic bowl `f(x,y)=100x²+y²`. Vanilla GD takes raw gradient steps; momentum GD accumulates velocity `v = β·v + lr·grad` and subtracts `v` from parameters.
**Assert:** From `(10,10)` with `lr=0.005`, both reach `f < 1e-6`, and momentum uses fewer iterations than vanilla.
**⚠️ Defect:** The momentum update adds the gradient to velocity (`vx = momentum*vx + learning_rate*gx`) and then subtracts the full velocity (`x -= vx`). This is the "heavy ball" form but with the learning rate applied inside the velocity accumulation, which changes the effective step size and can overshoot if momentum or learning rate is tuned differently. The demo’s tuned parameters hide the issue.

### 17. hill_climbing_restarts.py
**Entry fn:**
- `hill_climbing(x: float, y: float, step_size: float = 0.05, tolerance: float = 1e-4, max_iters: int = 1000) -> Tuple[float, float, float]`
- `hill_climbing_with_restarts(num_restarts: int = 10, step_size: float = 0.05, bounds: Tuple[float, float] = (-1.0, 1.0)) -> Tuple[float, float, float]`
**Valid input:** `x`, `y` within `bounds`; `step_size > 0`; `num_restarts >= 1`.
**Core:** Maximizes a rugged 2D landscape (`sin(5πx)·cos(5πy) + 0.1·(x²+y²)`) via greedy hill climbing with 4-neighbor search and random restarts. Bounds are clamped.
**Assert:** With `random.seed(42)`, restarts produce a value at least as good as a single run, and the final value is above `-0.5`.
**⚠️ Defect:** The single-step hill climbing breaks after the first improving neighbor (`break` inside the candidate loop), so it only checks one direction order per iteration rather than choosing the best neighbor. This makes convergence order-dependent and can stop at lower local optima than a true greedy ascent would.

### 18. mahalanobis_distance.py
**Entry fn:**
- `compute_covariance_2d(points: List[Tuple[float, float]]) -> List[List[float]]`
- `matrix_invert_2x2(M: List[List[float]]) -> List[List[float]]`
- `mahalanobis_distance(point: Tuple[float, float], mean: Tuple[float, float], cov_inv: List[List[float]]) -> float`
- `euclidean_distance(p: Tuple[float, float], q: Tuple[float, float]) -> float`
**Valid input:** `points` non-empty list of 2D points (need at least 2 non-identical points for invertible covariance); `cov_inv` inverse of a 2×2 covariance matrix.
**Core:** Computes 2×2 covariance, inverts it, and evaluates Mahalanobis distance `√((x-μ)^T Σ⁻¹ (x-μ))`. Also provides Euclidean distance for comparison.
**Assert:** On 5 correlated points along `x≈y`, verifies self-distance ≈ 0, perpendicular direction is penalized more than aligned direction, and Euclidean treats them equally.
**⚠️ Defect:** Hard-coded for 2D only. The module name and docstring do not warn that all helpers are 2×2. Passing a 3D point or a larger covariance matrix will silently fail or produce nonsense. Additionally, `matrix_invert_2x2` uses `assert` instead of raising a proper exception for singular matrices.

### 19. newton_method_optimization.py
**Entry fn:**
- `newton_method(x_init: float, tolerance: float = 1e-10, max_iters: int = 100) -> Tuple[int, float]`
- `gradient_descent(x_init: float, learning_rate: float = 0.1, tolerance: float = 1e-10, max_iters: int = 1000) -> Tuple[int, float]`
**Valid input:** Any real `x_init`; hard-wired to the quadratic `f(x)=3x²-12x+10`.
**Core:** Demonstrates 1D Newton’s method and gradient descent on a fixed quadratic. Newton uses exact gradient and constant Hessian (`6.0`); GD uses fixed learning rate.
**Assert:** From `x_init=0`, both methods converge to `x=2` and `f=-2`, and Newton uses fewer iterations than GD.
**⚠️ Defect:** The functions are not generic optimizers: `gradient(x)` and `hessian(x)` are module-level closures for one specific function. A user cannot pass their own objective. The docstring presents them as general 1D optimizers, but the API has no way to supply a different function.

### 20. simulated_annealing.py
**Entry fn:** `simulated_annealing(x_init: float, y_init: float, func, bounds: Tuple[float, float], initial_temp: float = 10.0, cooling_rate: float = 0.95, max_iters: int = 5000) -> Tuple[float, float, float]`
**Valid input:** `func(x,y) -> float`; `bounds[0] < bounds[1]`; `initial_temp > 0`; `cooling_rate` in `(0,1)`.
**Core:** 2D simulated annealing. Proposes Gaussian neighbors with scale proportional to temperature, accepts worse moves via the Metropolis criterion, and cools geometrically. Bounds are clamped.
**Assert:** On 2D Rastrigin centered at `(3,3)` with `random.seed(42)`, finds `best_value < 2.0` and final point within distance `2.0` of `(3,3)`.
**⚠️ Defect:** No lower bound on proposed move scale: as temperature drops, `scale = 0.5 * temperature` can become extremely small (`< 1e-8`), so the final iterations make no meaningful progress. Combined with the geometric cooling, the algorithm can freeze before truly converging, and the tolerance is loose enough to accept a wide neighborhood around the optimum.

---

*5S · Batch 1 detail docs · 2026-07-20*
