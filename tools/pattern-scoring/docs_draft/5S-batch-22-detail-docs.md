# Batch 22 — DS Pattern Detail Docs (23 patterns)

Categories: `recommenders_ii_kept_survivors` (4) + `simulation_and_decision_science` (9) + `survival_and_reliability` (10).

---

## Category: recommenders_ii_kept_survivors

### 1. catalog_coverage_diversity.py
**Entry fn:** `def catalog_coverage(recommendations: Iterable[int], catalog_size: int) -> float:`, `def main() -> None:`
**Valid input:** `recommendations` is any iterable of item identifiers; `catalog_size` is a positive integer.
**Core:** Catalog coverage is the fraction of the full catalog that appears at least once in a recommendation list. It is a simple diversity metric: a higher value means the recommender explores more of the catalog instead of repeatedly returning the same popular items.
**Assert:** A list touching every item in a 5-item catalog gives coverage `1.0`; a narrow list touching only 2 items gives `0.4`; an empty list gives `0.0`; repeated items do not inflate coverage.
**⚠️ Defect:** The function silently clamps coverage to `1.0` if recommendations contain IDs larger than `catalog_size`, hiding a catalog-declaration mismatch rather than raising. It also validates `catalog_size` but not that recommendation IDs are non-negative or within any expected range.

### 2. content_tfidf_rec.py
**Entry fn:** `def tfidf_similarity(doc1: list, doc2: list) -> float:`
**Valid input:** `doc1` and `doc2` are equal-length numeric vectors (term counts or TF-IDF weights).
**Core:** Computes cosine similarity between two document vectors. Used for content-based recommendation: given a query item's bag-of-words vector, recommend the most similar unseen item by cosine similarity.
**Assert:** On four planted topic-A/topic-B items, a query for item 0 correctly returns item 1 as the top-1 similar candidate.
**⚠️ Defect:** The function does not validate that vectors are equal length or non-empty; mismatched lengths raise an opaque index error. It adds `1e-10` to the denominator to avoid division by zero, which is a hack that biases similarity downward for near-zero vectors. There is no actual TF or IDF computation here despite the filename — it is pure cosine on pre-computed vectors.

### 3. intra_list_diversity.py
**Entry fn:** `def intra_list_diversity(items: Sequence[Sequence[float]]) -> float:`, `def main() -> None:`
**Valid input:** `items` is a sequence of item vectors; all vectors must have the same dimension; at least two vectors are needed for a meaningful score.
**Core:** Intra-list diversity (ILD) is the average pairwise Euclidean distance between item vectors in a recommendation list. Higher ILD means the slate is more varied; ILD of zero means all items are identical.
**Assert:** Three orthonormal one-hot vectors in R³ have ILD `sqrt(2)`; three identical vectors have ILD `0.0`; a single-item list returns `0.0`.
**⚠️ Defect:** Returns `0.0` for fewer than 2 items, which is a sensible sentinel but cannot be distinguished from a genuinely homogeneous list without checking length. The O(n²) pairwise computation is fine for short slates but expensive for very long recommendation lists.

### 4. novelty_serendipity.py
**Entry fn:** `def novelty_score(recommendations: Iterable[int], popularity: Mapping[int, float]) -> float:`, `def inv_pop(item: int) -> float:`, `def main() -> None:`
**Valid input:** `recommendations` is an iterable of item IDs; `popularity` maps item IDs to positive popularity scores (higher = more popular).
**Core:** Novelty is the mean inverse popularity of the recommended items. Long-tail, rarely popular items score high; mainstream blockbusters score near zero. This is one proxy for serendipity.
**Assert:** A list of popular items yields mean inverse popularity `0.011`; a long-tail list yields `0.104`; the long-tail list scores higher; an item missing from the popularity map is treated as maximally novel.
**⚠️ Defect:** Treating missing items as popularity `1.0` is generous and can inflate novelty for unknown items. The helper `inv_pop` is nested inside `novelty_score`, so it is not independently testable. No validation that popularity values are positive until one is encountered.

---

## Category: simulation_and_decision_science

### 5. discrete_event_simulation.py
**Entry fn:** `def discrete_event_simulation() -> None:`
**Valid input:** None (function is self-contained with hardcoded parameters).
**Core:** Event-driven simulation of a single-server queue using a priority queue (heapq). Models Poisson arrivals and exponential service times, tracking arrivals, departures, queue length, server busy state, and total waiting time. Verifies conservation: total arrivals ≈ served + still in system.
**Assert:** Over `sim_time = 100` with arrival rate `0.9` and service rate `1.0`, more than 50 customers arrive and are served, and conservation holds within one customer.
**⚠️ Defect:** The simulation logic is hardcoded inside the function with no tunable parameters, so it cannot be reused for other arrival/service rates or queue disciplines. The `server_busy` flag can become inconsistent because service-end events set it to `False` before starting the next customer, which could briefly leave the flag wrong if multiple events share the same timestamp.

### 6. kelly_criterion.py
**Entry fn:** `def kelly_criterion() -> None:`, `def simulate_wealth(fraction: float, n_bets: int, seed_offset: int = 0) -> list[float]:`
**Valid input:** `fraction` ∈ [0, 1]; `n_bets` > 0; `seed_offset` any integer.
**Core:** Kelly criterion: optimal bet fraction `f* = (p·b − q) / b`. Demonstrates that full Kelly maximizes median terminal wealth and mean log-growth compared to overbetting (2× Kelly) across 300 paired seeded paths.
**Assert:** With `p_win = 0.6`, `odds = 1.0`, Kelly fraction is `0.2`; Kelly's median terminal wealth and mean log-growth exceed 2× Kelly's, and Kelly wins more than 60% of paired paths.
**⚠️ Defect:** `simulate_wealth` reseeds with `42 + seed_offset`, so different fractions on the same path are correlated by the same base seed, but the same `seed_offset` always produces the same sequence — the randomness is fully deterministic per path. The win/loss probability is hardcoded inside `kelly_criterion`; `simulate_wealth` cannot be used for arbitrary bet probabilities.

### 7. mm1_queue_littles_law.py
**Entry fn:** `def mm1_queue_littles_law() -> None:`
**Valid input:** None (self-contained with hardcoded rates).
**Core:** Simulates an M/M/1 queue for 1,000 arrivals, measuring average time in system `L` and average number in system `W`. Verifies Little's Law (`L = λ·W`) and compares empirical results to analytic M/M/1 formulas.
**Assert:** With `λ = 0.8`, `μ = 1.0`, empirical `W` and `L` are within 0.5×–2.0× of analytic values (`E[W] = 1/(μ−λ)`, `E[L] = ρ/(1−ρ)`), and Little's Law holds within 30%.
**⚠️ Defect:** The code labels `L` as "average time in system" and `W` as "average number in system", which is the opposite of the standard Little's Law convention (`L` = average number in system, `W` = average time in system). This is a documentation/naming bug that could confuse readers. Also, the simulation uses the time of the last arrival as the denominator, not total elapsed time, biasing utilization estimates.

### 8. monte_carlo_var_es.py
**Entry fn:** `def monte_carlo_var_es() -> None:`
**Valid input:** None (self-contained with hardcoded 10,000 simulations and 5% confidence level).
**Core:** Monte Carlo estimation of Value-at-Risk (VaR) and Expected Shortfall (ES) on a heavy-tailed synthetic return distribution. VaR is the α-quantile of losses; ES is the average of losses worse than VaR.
**Assert:** VaR is negative (a loss); ES is more negative than VaR; absolute ES ≥ absolute VaR; empirical exceedance rate of VaR is near the 5% confidence level.
**⚠️ Defect:** ES is computed as the mean of returns *below* VaR, which for a discrete sample of size 10,000 includes exactly 500 points. This is the standard empirical ES but uses the full left tail rather than the conditional tail mean, which can be noisy. No parameterization of α, sample size, or return distribution.

### 9. newsvendor_critical_fractile.py
**Entry fn:** `def newsvendor_critical_fractile() -> None:`, `def profit(order_qty: float, demand: float) -> float:`
**Valid input:** `order_qty` ≥ 0; `demand` ≥ 0.
**Core:** Newsvendor problem: optimal order quantity is the critical fractile `underage_cost / (underage_cost + overage_cost)` of demand. For Uniform(50,150) demand with cost=5, price=10, the critical fractile is 0.5 and optimal quantity is 100. The demo shows optimal stocking beats under-stocking by 20 units and over-stocking by 20 units.
**Assert:** Average optimal profit exceeds both under-stock and over-stock profits; average optimal profit > 250 over 100 seeded days.
**⚠️ Defect:** The `profit` function assumes zero salvage value for unsold units, which is a strong assumption not documented in the signature. Demand distribution and cost/price parameters are hardcoded inside `newsvendor_critical_fractile`, making the function non-reusable. Critical fractile is computed but never compared to the chosen quantity (the quantity is set manually).

### 10. q_learning_gridworld.py
**Entry fn:** `def q_learning_gridworld() -> None:`, `def get_neighbors(state: tuple[int, int]) -> list[tuple[int, int]]:`, `def get_reward(state: tuple[int, int]) -> float:`, `def state_to_action(state: tuple[int, int], action_idx: int) -> tuple[int, int]:`
**Valid input:** `state` is a grid coordinate within the 4×4 world; `action_idx` ∈ {0,1,2,3}.
**Core:** Tabular Q-learning on a 4×4 gridworld with a goal state (+1), a pit (−1), and step cost (−0.1). After 500 episodes the learned Q-values are used to extract a greedy policy, which is verified to avoid the pit.
**Assert:** No greedy action from any state moves the agent into the pit cell `(1, 1)`.
**⚠️ Defect:** The function has no convergence check on Q-values — it simply runs 500 episodes and asserts the policy avoids the pit, which is weak because many non-optimal policies also avoid the pit. There is no comparison to a known optimal policy. The learning rate, epsilon, and discount factor are hardcoded.

### 11. schelling_segregation.py
**Entry fn:** `def schelling_segregation() -> None:`, `def get_neighbors(r: int, c: int) -> list[int]:`, `def is_satisfied(r: int, c: int) -> bool:`, `def measure_segregation() -> float:`
**Valid input:** `r`, `c` are valid indices in the 10×10 grid.
**Core:** Schelling model of segregation on a 10×10 grid with two agent types. Agents are satisfied if at least 30% of their neighbors are the same type. Unsatisfied agents swap with random agents of the opposite type; global segregation is measured as the fraction of neighbor pairs that are same-type.
**Assert:** Initial segregation is recorded; final segregation > 0.5 and ≥ initial segregation after up to 100 iterations, showing mild individual preference produces high global segregation.
**⚠️ Defect:** The swap logic looks for "a random cell with a different type" and only attempts 20 random cells before giving up, so an unsatisfied agent may remain in place. The simulation moves only one random unsatisfied agent per iteration, which is slow and not the standard Schelling update. No guarantee that the final state has no unsatisfied agents.

### 12. sir_epidemic_model.py
**Entry fn:** `def sir_epidemic_model() -> None:`, `def simulate_sir(beta: float, gamma: float, n_steps: int = 100) -> tuple[list[int], list[int], list[int]:]`
**Valid input:** `beta` ≥ 0; `gamma` ≥ 0; `n_steps` > 0.
**Core:** Discrete-time SIR epidemic simulation with fixed population `N = 1000`. Tracks Susceptible, Infected, Recovered counts over time; enforces conservation `S + I + R = N`; compares final epidemic size under high vs low transmission rates.
**Assert:** Conservation holds at every step; final infected count is between 0 and N; peak infected > 0; a higher β produces a larger final epidemic than a lower β.
**⚠️ Defect:** Infections and recoveries are rounded to integers deterministically (`int(beta * contacts)` and `int(gamma * I)`), which is a coarse approximation of continuous rates and can produce zero infections for small `I` even when β > 0. The contact rate (5) is hardcoded. The model is not a standard SIR ODE; it is a discrete-event caricature.

### 13. tornado_sensitivity.py
**Entry fn:** `def tornado_sensitivity() -> None:`, `def profit(price: float, volume: float, cost: float, overhead: float) -> float:`
**Valid input:** Numeric inputs; `volume` ≥ 0 is implied for meaningful profit.
**Core:** Tornado (one-at-a-time) sensitivity analysis on a simple profit model. Each input is varied ±10% while others are held at base values, and the resulting profit impact is ranked to identify the dominant driver.
**Assert:** The top driver is either `price` or `volume`; both `cost` and `overhead` have nonzero impacts.
**⚠️ Defect:** The analysis is one-at-a-time, so it ignores interaction effects between variables. The ranking is based on absolute profit range, which conflates variable scale (e.g., `volume = 1000`) with true elasticity. No validation that base inputs are positive or that the model makes business sense.

---

## Category: survival_and_reliability

### 14. accelerated_failure_time_lite.py
**Entry fn:** `def aft_fit(log_times: List[float], x: List[float]) -> Tuple[float, float, float]:`
**Valid input:** `log_times` and `x` are equal-length numeric lists; `x` has nonzero variance.
**Core:** Fits a log-linear Accelerated Failure Time (AFT) model `log(T) = μ + β·x + ε` by ordinary least squares on the log survival times. Returns estimated intercept `μ`, coefficient `β`, and residual standard deviation `σ`.
**Assert:** On planted data (`μ=2.0`, `β=0.5`, `σ=0.3`), the estimated parameters are within ±0.3 of the true values.
**⚠️ Defect:** The function ignores censoring entirely; it assumes all log-times are observed, which is not true for censored survival data. No validation that inputs are equal length or that `var_x` is not zero; zero variance silently returns `(mean_log_t, 0.0, 1.0)`.

### 15. censoring_bias_demo.py
**Entry fn:** `def kaplan_meier_mean(times: List[float], events: List[int]) -> float:`
**Valid input:** `times` and `events` are equal-length lists; `events[i] = 1` if event observed, `0` if censored; `times` ≥ 0.
**Core:** Estimates mean survival time by integrating the Kaplan-Meier survival curve via trapezoidal rule. Demonstrates that ignoring censoring (naive mean of observed times) underestimates true mean survival, while KM corrects toward the true mean.
**Assert:** Naive mean is well below KM mean and below 75% of the true mean; KM mean is within 30 of the true mean for the planted exponential example.
**⚠️ Defect:** The KM integral is approximated crudely: it multiplies survival at each event time by the width to the previous time, rather than using midpoints or a more accurate numerical integration. No validation of input lengths or that events are in {0,1}.

### 16. competing_risks_naive_bias.py
**Entry fn:** `def naive_km_cif(times: List[float], events: List[int], event_type: int) -> Tuple[List[float], List[float]]:`, `def aalen_johansen_cif(times: List[float], events: List[int], event_type: int) -> Tuple[List[float], List[float]]:`
**Valid input:** `times` and `events` are equal-length lists; `events` ∈ {0,1,2} where 0 = censored, 1/2 = competing events; `event_type` is 1 or 2.
**Core:** Shows the bias in competing-risks analysis. The naive `1 − KM` cumulative incidence treats competing events as independent censoring and overstates incidence. The correct Aalen-Johansen estimator weights each cause-specific hazard increment by the overall survival probability just before the event time.
**Assert:** Final naive CIF exceeds final Aalen-Johansen CIF by at least 0.1; Aalen-Johansen CIF is a valid probability in (0, 1); naive CIF does not exceed 1.
**⚠️ Defect:** The estimator handles only two competing event types (1 and 2); additional event codes would be silently ignored or misclassified. No validation that `event_type` appears in `events`. Risk-set counting uses full list scans at each unique event time, giving O(n²) complexity.

### 17. cox_partial_likelihood_lite.py
**Entry fn:** `def cox_partial_likelihood_2cov(times: List[float], events: List[int], x1: List[float], x2: List[float], max_iter: int = 20, tol: float = 1e-6) -> Tuple[float, float]:`
**Valid input:** All input lists are equal-length; `events[i]` ∈ {0,1}; `max_iter` > 0; `tol` > 0.
**Core:** Fits a Cox proportional hazards model with two covariates by Newton-Raphson on the partial likelihood. Returns estimated log hazard ratios `β1` and `β2` where `h(t|x) = h₀(t)·exp(β1·x1 + β2·x2)`.
**Assert:** On planted data with true `β1 = 0.5`, `β2 = -0.3`, the estimates are within ±0.5 of the true values.
**⚠️ Defect:** The risk set at each event time is recomputed by scanning the entire dataset (O(n²)), which is impractical for large samples. The Hessian computation uses a simplified information matrix and may be unstable when covariates are highly correlated. No validation that inputs have equal length or that the Hessian is invertible.

### 18. exponential_reliability_mtbf.py
**Entry fn:** `def exponential_mtbf(failure_times: List[float]) -> float:`, `def exponential_survival(t: float, mtbf: float) -> float:`
**Valid input:** `failure_times` is a non-empty list of positive numbers; `t` ≥ 0; `mtbf` > 0.
**Core:** For a constant-hazard exponential model, MTBF = `1/λ` is estimated as the sample mean failure time, and survival probability is `S(t) = exp(−t/MTBF)`.
**Assert:** Estimated MTBF from 50 exponential samples is within 30 of the true MTBF=100; `S(MTBF)` ≈ `e^(−1)` ≈ 0.368 within 0.05.
**⚠️ Defect:** No validation that `failure_times` is non-empty (empty input raises `ZeroDivisionError`) or that times are positive. A single very large or negative value can badly bias the MTBF estimate. The function assumes exponentiality without any goodness-of-fit check.

### 19. hazard_vs_survival_conversion.py
**Entry fn:** `def hazard_from_survival(S: Callable[[float], float], t: float, eps: float = 1e-6) -> float:`, `def survival_from_cumhazard(H: Callable[[float], float], t: float) -> float:`, `def S_planted(t: float) -> float:`, `def H_planted(t: float) -> float:`
**Valid input:** `S` is a positive survival function near `t`; `H` is a non-negative cumulative hazard function at `t`; `eps` > 0 and small.
**Core:** Verifies the survival-hazard duality: `h(t) = −d/dt[log S(t)]` and `S(t) = exp(−H(t))`. Uses a central finite difference to estimate the hazard from a survival function and reconstructs survival from a cumulative hazard.
**Assert:** For planted exponential survival `S(t) = exp(−0.1·t)`, the estimated hazard at `t=5` is within 0.01 of `λ=0.1`; reconstructing survival from `H(t)=0.1·t` matches the true survival within 1e-10.
**⚠️ Defect:** `hazard_from_survival` returns `0.0` if either `S(t+eps)` or `S(t−eps)` is below `1e-14`, hiding the true hazard for very small survival probabilities. The finite-difference approximation can be inaccurate if `S` is not smooth or if `eps` is too large/small. The planted helper functions are hardcoded.

### 20. log_rank_test.py
**Entry fn:** `def log_rank_test(times_g1: List[float], events_g1: List[int], times_g2: List[float], events_g2: List[int]) -> Tuple[float, float]:`
**Valid input:** Each group's `times` and `events` are equal-length; `events[i]` ∈ {0,1}; at least some events occur in each group.
**Core:** Nonparametric log-rank test comparing two survival curves. At each unique event time it computes observed vs expected events in group 1 under the null of equal hazards, accumulating a z-statistic and approximate two-tailed p-value.
**Assert:** Two groups with clearly different exponential hazards produce a p-value < 0.10; two independent samples from the same exponential distribution produce a p-value > 0.10.
**⚠️ Defect:** The variance formula uses the standard hypergeometric variance but assumes `y1 + y2 − 1 > 0`; it skips time points with zero variance without clear reporting. No validation that the groups have any events or that time/event lists are equal length. The p-value is a normal approximation, which can be anticonservative for very small samples.

### 21. nelson_aalen_cumhazard.py
**Entry fn:** `def nelson_aalen_cumhazard(times: List[float], events: List[int]) -> Tuple[List[float], List[float]]:`
**Valid input:** `times` and `events` are equal-length lists; `events[i]` ∈ {0,1}; `times` ≥ 0.
**Core:** Nelson-Aalen estimator of the cumulative hazard function: `H(t) = Σ_{s ≤ t} d_s / y_s`, where `d_s` is the number of events at time `s` and `y_s` is the number at risk just before `s`.
**Assert:** The estimated cumulative hazard is monotone non-decreasing; the final value is positive for the planted exponential example with 50 uncensored observations.
**⚠️ Defect:** Censored observations are included in the risk set but do not contribute to the hazard increment, which is correct, but the function does not return the number at risk or event counts for diagnostics. Time points where no events occur are omitted from the output, so the step function is not directly plottable without interpolation. No input validation.

### 22. reliability_series_parallel.py
**Entry fn:** `def reliability_series(component_reliabilities: List[float]) -> float:`, `def reliability_parallel(component_reliabilities: List[float]) -> float:`, `def simulate_series(component_reliabilities: List[float], num_sim: int) -> float:`, `def simulate_parallel(component_reliabilities: List[float], num_sim: int) -> float:`
**Valid input:** `component_reliabilities` is a non-empty list of probabilities in [0, 1]; `num_sim` > 0.
**Core:** Analytic and simulation-based system reliability. Series: all components must work → product of reliabilities. Parallel: at least one must work → `1 − Π(1 − r_i)`. Monte Carlo simulations verify the analytic formulas.
**Assert:** For four components with `r = 0.9`, simulated series and parallel reliabilities are within 0.05 of analytic values; series reliability is below parallel reliability.
**⚠️ Defect:** No validation that component reliabilities are in [0, 1]; values outside this range silently produce nonsensical probabilities. `simulate_series` and `simulate_parallel` import `random` locally, so they are not seeded and not reproducible unless the caller seeds the global random state.

### 23. weibull_mle.py
**Entry fn:** `def weibull_mle(times: List[float], max_iter: int = 100, tol: float = 1e-10) -> Tuple[float, float]:`
**Valid input:** `times` is a non-empty list of positive numbers; `max_iter` > 0; `tol` > 0.
**Core:** Maximum likelihood estimation of Weibull shape `k` and scale `λ` for uncensored data. Profiles out `λ` and solves the single-variable shape equation by Newton-Raphson, then computes `λ = (Σ t_i^k / n)^(1/k)`.
**Assert:** On 80 samples from Weibull(`k=2.0`, `λ=5.0`), estimates are within ±0.3 for shape and ±0.5 for scale; the MLE stationarity score is near zero.
**⚠️ Defect:** The estimator does not handle censored observations, so it is only valid for complete failure data. If the Newton step would make `k ≤ 0`, it halves the current `k` instead of using a line search or trust region, which can slow convergence. No validation that `times` are positive or that the data actually look Weibull.
