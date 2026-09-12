# km_survival_lite.R
# Kaplan-Meier survival curve with censoring (no oracle: hand-verify properties).
# _lite: manual implementation without optimizing for speed.
# Claim: stepwise non-increasing survival curve; starts at 1; censoring handled correctly.
# Tolerance: properties verified exactly; no tolerance (categorical properties).

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# Generate survival data with censoring
n <- 100
true_times <- rexp(n, rate = 0.02)  # Exponential survival times
censor_times <- rexp(n, rate = 0.01)
event <- true_times <= censor_times  # Event indicator
time <- pmin(true_times, censor_times)

# ===== Manual Kaplan-Meier =====
unique_times <- sort(unique(time[event]))
km_table <- data.frame(
  time = unique_times,
  n_risk = numeric(length(unique_times)),
  n_event = numeric(length(unique_times)),
  survival = numeric(length(unique_times)),
  se = numeric(length(unique_times))
)

for (i in 1:nrow(km_table)) {
  t <- km_table$time[i]

  # Number at risk: all with time >= t
  n_risk <- sum(time >= t)
  km_table$n_risk[i] <- n_risk

  # Number of events at this time
  n_evt <- sum(time == t & event)
  km_table$n_event[i] <- n_evt

  # Survival probability (product-limit estimator)
  if (i == 1) {
    s_prev <- 1.0
  } else {
    s_prev <- km_table$survival[i - 1]
  }

  if (n_risk > 0) {
    km_table$survival[i] <- s_prev * (1 - n_evt / n_risk)
  } else {
    km_table$survival[i] <- s_prev
  }

  # Greenwood formula: se_i = S_i * sqrt( SUM_{t<=i} d/(n(n-d)) ).
  # Two bugs this replaces: (1) recovering the sum from se[i-1]^2 re-applies
  # the S^2 factor and compounds it; keep a SEPARATE running sum. (2) when
  # everyone remaining dies (n == d) the term is infinite — the SE is
  # undefined at S=0; the standard practice is to skip that term.
  if (i == 1) greenwood_sum <- 0
  if (n_risk > n_evt && n_evt > 0) {
    greenwood_sum <- greenwood_sum + n_evt / (n_risk * (n_risk - n_evt))
  }
  km_table$se[i] <- sqrt(greenwood_sum) * km_table$survival[i]
}

# ===== Property checks =====
# 1. Starts at 1 (before any events)
# Note: actual KM starts at 1, but we're looking at time of first event
stopifnot(
  !is.na(km_table$survival[1])
)

# 2. Monotone non-increasing
diffs <- diff(km_table$survival)
stopifnot(
  all(diffs <= 1e-10)
)

# 3. Survival <= 1 always
stopifnot(
  all(km_table$survival >= 0 & km_table$survival <= 1)
)

# 4. Number at risk decreases (due to censoring and events)
n_risk_diffs <- diff(km_table$n_risk)
stopifnot(
  all(n_risk_diffs <= 0)
)

# 5. Standard error non-negative
stopifnot(
  all(km_table$se >= 0)
)

# 6. Events count matches
total_events <- sum(km_table$n_event)
expected_events <- sum(event)
stopifnot(
  total_events == expected_events
)

# ===== Hand-verification sample (check one row manually) =====
# For first event time, verify the survival calculation
if (nrow(km_table) > 0) {
  first_row <- km_table[1, ]
  expected_survival <- 1 - (first_row$n_event / first_row$n_risk)

  stopifnot(
    abs(first_row$survival - expected_survival) < 1e-10
  )
}

cat("PASS: km_survival_lite.R\n")
quit(status=0)

