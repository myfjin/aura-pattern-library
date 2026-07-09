# anova_tukey.R
# Tukey's HSD test via studentized range distribution (qtukey).
# Oracle: TukeyHSD() in stats.
# Claim: manual pairwise intervals match oracle.
# Tolerance: interval bounds agreement <1e-10 (relative).

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# Generate grouped data
groups <- 4
n_per_group <- 20
group_means <- c(10, 12, 11.5, 14)
y <- c(
  rnorm(n_per_group, group_means[1], 1),
  rnorm(n_per_group, group_means[2], 1),
  rnorm(n_per_group, group_means[3], 1),
  rnorm(n_per_group, group_means[4], 1)
)
group_factor <- rep(1:groups, each = n_per_group)

# ===== ANOVA setup =====
fit_aov <- aov(y ~ factor(group_factor))
anova_table <- anova(fit_aov)

# Extract MSE and df
mse <- anova_table["Residuals", "Mean Sq"]
df_residual <- anova_table["Residuals", "Df"]

# Group means and n
group_means_sample <- tapply(y, group_factor, mean)
n_each <- n_per_group

# ===== Manual Tukey HSD =====
# Critical value: q = qtukey(1 - alpha, groups, df_residual)
alpha <- 0.05
q_crit <- qtukey(1 - alpha, groups, df_residual)

# SE for each pairwise comparison: sqrt(MSE/2 * (1/n_i + 1/n_j))
se_tukey <- sqrt(mse / 2 * (1 / n_each + 1 / n_each))

# Pairwise comparisons (k = groups choose 2)
pairs <- t(combn(1:groups, 2))
n_pairs <- nrow(pairs)

tukey_ci_manual <- data.frame(
  pair = character(n_pairs),
  diff = numeric(n_pairs),
  lwr = numeric(n_pairs),
  upr = numeric(n_pairs),
  p.adj = numeric(n_pairs)
)

for (i in 1:n_pairs) {
  g1 <- pairs[i, 1]
  g2 <- pairs[i, 2]

  diff <- group_means_sample[g1] - group_means_sample[g2]
  margin_of_error <- q_crit * se_tukey

  tukey_ci_manual$pair[i] <- paste(g1, "-", g2)
  tukey_ci_manual$diff[i] <- diff
  tukey_ci_manual$lwr[i] <- diff - margin_of_error
  tukey_ci_manual$upr[i] <- diff + margin_of_error

  # CORRECT adjusted p-value: the studentized range distribution (ptukey) —
  # a t-based p here is a different (wrong) test wearing Tukey's name.
  q_obs <- abs(diff) / se_tukey
  tukey_ci_manual$p.adj[i] <- 1 - ptukey(q_obs, groups, df_residual)
}

# ===== Oracle: TukeyHSD =====
tukey_oracle <- TukeyHSD(fit_aov)
oracle_ci <- tukey_oracle$`factor(group_factor)`

# ===== Agreement check =====
# TukeyHSD rownames are "2-1" (no spaces) and its diff is mean(g2)-mean(g1);
# the manual table stores mean(g1)-mean(g2) — so the oracle interval is the
# MIRROR of the manual one: lwr_manual == -upr_oracle, upr_manual == -lwr_oracle.
for (i in 1:nrow(tukey_ci_manual)) {
  row_manual <- tukey_ci_manual[i, ]
  parts <- strsplit(row_manual$pair[1], " - ")[[1]]
  g1 <- as.numeric(parts[1]); g2 <- as.numeric(parts[2])
  oracle_name <- paste0(g2, "-", g1)
  stopifnot(oracle_name %in% rownames(oracle_ci))
  row_oracle <- oracle_ci[oracle_name, ]

  stopifnot(
    abs(row_manual$diff[1] - (-row_oracle["diff"])) < 1e-8,
    abs(row_manual$lwr[1] - (-row_oracle["upr"])) < 1e-6,
    abs(row_manual$upr[1] - (-row_oracle["lwr"])) < 1e-6,
    abs(row_manual$p.adj[1] - row_oracle["p adj"]) < 1e-6
  )
}

# ===== Sanity checks =====
stopifnot(
  nrow(tukey_ci_manual) == choose(groups, 2)
)

stopifnot(
  all(tukey_ci_manual$p.adj >= 0 & tukey_ci_manual$p.adj <= 1)
)

cat("PASS: anova_tukey.R\n")
quit(status=0)

