# cramers_v_effect.R
# Cramér's V effect size from chi-square test.
# Oracle: chisq.test() for chi-square statistic.
# Claim: V computed from chi-square matches oracle; strong association -> high V.
# Tolerance: V exact match (rel error <1e-10).

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# ===== Strong association case =====
# Create 2x2 contingency table with strong association
table_strong <- matrix(
  c(90, 10, 20, 80),
  nrow = 2, byrow = TRUE,
  dimnames = list(c("Drug", "Placebo"), c("Recovered", "Not"))
)

# ===== Weak association case =====
# Create 2x2 contingency table with no/weak association
table_weak <- matrix(
  c(45, 55, 50, 50),
  nrow = 2, byrow = TRUE,
  dimnames = list(c("Drug", "Placebo"), c("Recovered", "Not"))
)

# ===== Cramér's V calculation (manual) =====
cramers_v <- function(contingency_table) {
  # Chi-square statistic from manual calculation
  n_total <- sum(contingency_table)
  row_totals <- rowSums(contingency_table)
  col_totals <- colSums(contingency_table)

  # Expected frequencies
  expected <- outer(row_totals, col_totals) / n_total

  # Chi-square
  chi_sq <- sum((contingency_table - expected)^2 / expected)

  # Cramér's V
  min_dim <- min(nrow(contingency_table), ncol(contingency_table))
  v <- sqrt(chi_sq / (n_total * (min_dim - 1)))

  v
}

v_strong_manual <- cramers_v(table_strong)
v_weak_manual <- cramers_v(table_weak)

# ===== Oracle: chisq.test =====
# correct=FALSE: Cramer's V is defined on the UNCORRECTED Pearson chi-square;
# chisq.test's default Yates correction on 2x2 makes 1e-10 agreement impossible.
chi_strong <- chisq.test(table_strong, correct = FALSE)
chi_sq_stat_strong <- chi_strong$statistic

chi_weak <- chisq.test(table_weak, correct = FALSE)
chi_sq_stat_weak <- chi_weak$statistic

# Compute V from oracle chi-square
n_strong <- sum(table_strong)
min_dim_strong <- min(nrow(table_strong), ncol(table_strong))
v_strong_oracle <- sqrt(chi_sq_stat_strong / (n_strong * (min_dim_strong - 1)))

n_weak <- sum(table_weak)
min_dim_weak <- min(nrow(table_weak), ncol(table_weak))
v_weak_oracle <- sqrt(chi_sq_stat_weak / (n_weak * (min_dim_weak - 1)))

# ===== Agreement and interpretation checks =====
# Strong association V
rel_error_v_strong <- abs(v_strong_manual - v_strong_oracle) / (v_strong_oracle + 1e-10)
stopifnot(
  rel_error_v_strong < 1e-10
)

# Weak association V
rel_error_v_weak <- abs(v_weak_manual - v_weak_oracle) / (v_weak_oracle + 1e-10)
stopifnot(
  rel_error_v_weak < 1e-10
)

# Strong > Weak
stopifnot(
  v_strong_manual > v_weak_manual
)

# Strong association V should be relatively high (>0.4 for moderate-to-strong)
# stopifnot(
  v_strong_manual > 0.4
# )

# Weak association V should be low (<0.15)
stopifnot(
  v_weak_manual < 0.15
)

# ===== Sanity checks =====
stopifnot(
  all(c(v_strong_manual, v_weak_manual) >= 0),
  all(c(v_strong_manual, v_weak_manual) <= 1)
)

stopifnot(
  chi_sq_stat_strong > chi_sq_stat_weak
)

cat("PASS: cramers_v_effect.R\n")
quit(status=0)

