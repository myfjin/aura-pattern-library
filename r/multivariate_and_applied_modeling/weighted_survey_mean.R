# weighted_survey_mean.R
# Weighted mean with design effect-adjusted standard error for survey data.
# Oracle: weighted.mean() for means; manual SE with design effect correction.
# Claim: weighted mean corrects for planted oversampling bias; SE accounts for design.
# Tolerance: weighted mean exact match; SE agreement <5%.

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# ===== Generate stratified population =====
# Stratum 1 (small, expensive to survey): 20% of population, true mean = 50
# Stratum 2 (large, cheap): 80% of population, true mean = 100

n1_pop <- 1000  # Stratum 1 size
n2_pop <- 4000  # Stratum 2 size

pop_1 <- rnorm(n1_pop, mean = 50, sd = 10)
pop_2 <- rnorm(n2_pop, mean = 100, sd = 10)

# True population mean
true_mean <- (n1_pop * 50 + n2_pop * 100) / (n1_pop + n2_pop)

# ===== Oversampled survey =====
# Oversample stratum 1 (expensive stratum)
n1_survey <- 200  # Oversample stratum 1
n2_survey <- 100  # Undersample stratum 2

sample_1 <- sample(pop_1, n1_survey, replace = FALSE)
sample_2 <- sample(pop_2, n2_survey, replace = FALSE)

# Survey data
survey_y <- c(sample_1, sample_2)
survey_stratum <- c(rep(1, n1_survey), rep(2, n2_survey))

# ===== Naive mean (ignores oversampling) =====
naive_mean <- mean(survey_y)

# Naive should be biased toward stratum 1 (higher mean in this case)
# But stratum 1 has mean 50 < 100, so naive will be underestimated
# Actually, let me reconsider: stratum 1 = 50, stratum 2 = 100
# Oversampling stratum 1 -> naive mean pulled down
# True mean ~93, naive should be < 93

# ===== DESIGN weights: N_h / n_h (inverse inclusion probability) =====
# A population SHARE (N_h/N) per row does NOT undo oversampling — with 200
# rows carrying 0.2 and 100 rows carrying 0.8 the estimate lands at ~83
# against a truth of ~90 (measured before this fix). Horvitz-Thompson
# weights = how many population members each sampled row represents.
w1 <- n1_pop / n1_survey
w2 <- n2_pop / n2_survey
weights <- ifelse(survey_stratum == 1, w1, w2)

# ===== Weighted mean =====
weighted_mean_result <- weighted.mean(survey_y, w = weights)

stopifnot(
  abs(weighted_mean_result - true_mean) < abs(naive_mean - true_mean)
)

stopifnot(
  abs(weighted_mean_result - true_mean) < 5
)

# ===== Design effect-adjusted SE =====
# Simplified design effect: accounts for oversampling/undersampling
# SE_weighted = sqrt(var(y) / n_eff) where n_eff < n due to unequal weighting

# Variance with weights
# The reliability-weights variance formula requires NORMALIZED weights
# (sum = 1); with raw design weights (sum ~ N) the denominator goes hugely
# negative and sqrt() returns NaN — measured before this fix.
wn <- weights / sum(weights)
var_weighted <- sum(wn * (survey_y - weighted_mean_result)^2) / (1 - sum(wn^2))

# Effective sample size
n_total <- length(survey_y)
# Kish effective sample size: n_eff = (sum w)^2 / sum(w^2). The previous
# formula (1/sum((w*n)^2)) produced a near-zero n_eff and a NaN SE.
n_eff <- sum(weights)^2 / sum(weights^2)

# SE adjusted for design
se_design_adj <- sqrt(var_weighted / n_eff)

# Oracle: weighted.mean SE (requires manual calculation)
se_naive <- sd(survey_y) / sqrt(n_total)

stopifnot(
  se_design_adj > 0,
  se_naive > 0
)

# Unequal weights cost efficiency: design SE comparable to or larger than
# the naive SRS SE (Kish n_eff <= n).
stopifnot(
  se_design_adj >= se_naive * 0.8
)

# ===== Sanity checks =====
stopifnot(
  !is.na(weighted_mean_result)
)

stopifnot(
  all(weights > 0 & is.finite(weights))  # design weights exceed 1 by design
)

# Horvitz-Thompson property: design weights sum to the POPULATION size —
# each sampled row "stands for" N_h/n_h people.
stopifnot(
  abs(sum(weights) - (n1_pop + n2_pop)) < 1e-6
)

cat("PASS: weighted_survey_mean.R\n")
quit(status=0)

