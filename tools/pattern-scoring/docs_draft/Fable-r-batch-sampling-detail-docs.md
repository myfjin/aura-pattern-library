# Fable R Batch — sampling_and_simulation Detail Docs (8 patterns)

Categories: `sampling_and_simulation` (8). Documented directly by Fable (mesh writers offline — cloud outage); signatures + defects verified against source.

## Category: sampling_and_simulation

### 1. box_muller.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No parameters — `set.seed(42)`, `n_pairs=100` fixed. Depends only on base R `runif`.
**Core:** Box-Muller transform: from two uniforms U1,U2 produces two independent N(0,1) via `r=sqrt(-2*log(U1))`, `z1=r*cos(2πU2)`, `z2=r*sin(2πU2)`. Combines into 200 normals.
**Assert:** `ks.test` vs pnorm not rejected (p>0.05); `|mean|<0.1`; `|sd-1|<0.15`.
**⚠️ Defect:** No guard against `U1=0` → `log(0)=-Inf` → NaN normal (rare but unhandled). Fixed n=100 pairs is a small sample and the sd tolerance (0.15) is loose, so a mildly non-normal generator could still pass. Not reusable — a script, not a `rnorm2()`-style function.

### 2. inverse_cdf_sampling.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; `n=100`, exponential λ=1.5, logistic μ=2 s=0.8 hard-coded.
**Core:** Inverse-transform sampling: exponential `F⁻¹(u)=-log(1-u)/λ`, logistic `F⁻¹(u)=μ+s·log(u/(1-u))`. Verifies each via `ks.test` vs pexp / plogis.
**Assert:** Both KS p>0.05 (not rejected).
**⚠️ Defect:** No domain guard on `u`: `u→1` makes `-log(1-u)→+Inf` (exp) and `log(u/(1-u))→+Inf` (logistic); `u=0` breaks the logistic. n=100 is small for KS power. Params fixed, not caller-supplied.

### 3. mvn_cholesky.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; 2×2 Σ=[1,0.6;0.6,1], μ=0, n=500 fixed.
**Core:** Multivariate normal via Cholesky: hand-computes lower-triangular L (`L11=sqrt(Σ11)`, `L21=Σ21/L11`, `L22=sqrt(Σ22-L21²)`), checks against `t(chol(Σ))`, samples `X=Z·Lᵀ+μ`, compares sample covariance to Σ.
**Assert:** `all.equal(L, chol-oracle, tol=1e-6)`; sample cov `all.equal(Σ, tol=0.15)`.
**⚠️ Defect:** Hard-coded to the **2×2 case** — the Cholesky formula is not generalized to n×n, so it only works for this one covariance. No positive-definiteness check: if `Σ22-L21²<0`, `sqrt` yields NaN silently. Cov tolerance 0.15 is loose for n=500.

### 4. order_statistics.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; n=10 uniforms, 200 replications fixed.
**Core:** Order statistics of n uniforms: min ~ Beta(1,n), max ~ Beta(n,1). Loops 200× computing min/max, verifies distribution via `ks.test` vs pbeta.
**Assert:** min KS p>0.05, max KS p>0.05; `mean(min)<0.1`, `mean(max)>0.9`.
**⚠️ Defect:** Only min and max are distribution-tested — the **median** order statistic is discussed in comments (`Beta(5,6)/Beta(6,1)`) but never actually verified. Grows result vectors in an explicit R loop (slow, though preallocated here). 200 reps is a modest sample for KS.

### 5. poisson_process_thinning.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; T=4, λ_max=3.1, intensity `λ(t)=2+sin(πt/T)` fixed.
**Core:** Simulates an inhomogeneous Poisson process by thinning: generate a homogeneous process at rate λ_max (exponential gaps), keep each arrival with prob `λ(t)/λ_max`.
**Assert:** Homogeneous inter-arrivals `ks.test` vs pexp(λ_max) not rejected; reports #original vs #thinned.
**⚠️ Defect:** Only the **homogeneous** inter-arrivals are statistically verified — the **thinned** (inhomogeneous) result is *not* tested for the correct intensity (bin intensities are computed but never asserted against the empirical counts), so a wrong thinning probability would pass. Builds `arrivals`/`keep` via `c()` in a `while` loop → O(n²) reallocation.

### 6. probability_integral_transform.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; n=150 draws from N(0,1) fixed.
**Core:** Probability Integral Transform: applying the *correct* CDF F(X) to X yields Uniform(0,1); applying a *wrong* CDF does not. Tests both the true pnorm and a deliberately-wrong pexp.
**Assert:** correct-CDF KS p>0.05 (not rejected); wrong-CDF KS p<0.05 (rejected); `mean(u_wrong)<0.3`.
**⚠️ Defect:** Thin coverage — a single correct vs single wrong CDF; the `mean(u_wrong)<0.3` bound is a planted-specific expectation, not a general property. No input validation; not reusable as a function.

### 7. rejection_sampling_beta.R
**Entry fn:** Top-level script (no function wrapper). (Local helper `beta_density(x)` defined but the pattern runs as a script.)
**Valid input:** No params; target Beta(α=2, β=5), uniform proposal, n_target=200 fixed.
**Core:** Rejection sampling from Beta(2,5) with a Uniform(0,1) proposal: envelope constant `M=max` of a 1000-point density grid; accept X if `U < f(X)/M`. Vectorized in blocks of 1000.
**Assert:** `ks.test` vs pbeta not rejected; reports acceptance rate.
**⚠️ Defect:** The envelope `M` is estimated from a **discrete 1000-point grid**, so it can *under*-estimate the true density maximum → acceptance ratio >1 for some x → the accepted sample is no longer exactly Beta (silent bias). For Beta(2,5) the mode is interior so it's fine here, but the method is unsafe for peakier targets. `c()`-growth in the while loop.

### 8. truncated_normal.R
**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; N(0,1) truncated to [a=0, b=2], n_target=500 fixed.
**Core:** Truncated-normal sampling by rejection (draw N(μ,σ), keep those in [a,b]); compares sample mean/var to the closed-form truncated moments (via φ, Φ at standardized α,β).
**Assert:** `|mean_sample − mean_analytic|<0.15`; `|var_sample − var_analytic|<0.2`.
**⚠️ Defect:** Pure **rejection** truncation is inefficient when the truncation interval carries little probability mass (here [0,2] under N(0,1) keeps ~48%, so acceptable, but the method degrades badly for tail truncations — no fallback to inverse-CDF truncation). Draws in fixed blocks of 5000; variance tolerance (0.2) is loose.
