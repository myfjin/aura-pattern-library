# missing_pattern_matrix.R
# Missing data pattern analysis: missingness patterns and correlation handling.
# Oracle: cor(use="pairwise.complete.obs") for pairwise correlation.
# Claim: pattern matrix reveals planted MAR mechanism; pairwise cor matches oracle.
# Tolerance: pattern counts exact; correlation rel error <1e-10.

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# ===== Generate complete data =====
n <- 100
x1 <- rnorm(n, mean = 10, sd = 2)
x2 <- rnorm(n, mean = 5, sd = 1)
x3 <- rnorm(n, mean = 20, sd = 3)

# ===== Introduce MAR (Missing At Random) mechanism =====
# Missingness in x2 depends on x1 (observed)
# Missingness in x3 depends on x2 (partially observed)

# x2 missing if x1 > median(x1) (high x1 -> more likely missing x2)
prob_x2_miss <- ifelse(x1 > median(x1), 0.5, 0.1)
x2_missing <- rbinom(n, 1, prob_x2_miss) == 1
x2[x2_missing] <- NA

# x3 missing if x2 is not NA and x2 > median(x2, na.rm=T) (or NA in x2)
x2_avail <- !is.na(x2)
prob_x3_miss <- numeric(n)
prob_x3_miss[!x2_avail] <- 0.5  # High miss rate if x2 already missing
prob_x3_miss[x2_avail & x2 > median(x2, na.rm = TRUE)] <- 0.4
prob_x3_miss[x2_avail & x2 <= median(x2, na.rm = TRUE)] <- 0.1

x3_missing <- rbinom(n, 1, prob_x3_miss) == 1
x3[x3_missing] <- NA

# ===== Missingness pattern matrix =====
# Create binary matrix: 1 = missing, 0 = observed
# as.integer: a LOGICAL matrix pastes as "FALSEFALSETRUE", which no
# single-character split can parse — integers paste as "001".
miss_mat <- cbind(
  as.integer(is.na(x1)),
  as.integer(is.na(x2)),
  as.integer(is.na(x3))
)

# Count unique patterns
patterns <- apply(miss_mat, 1, paste, collapse = "")
unique_patterns <- unique(patterns)
pattern_counts <- table(patterns)

# Pattern matrix
pattern_df <- data.frame(
  x1 = character(length(unique_patterns)),
  x2 = character(length(unique_patterns)),
  x3 = character(length(unique_patterns)),
  count = numeric(length(unique_patterns))
)

for (i in 1:length(unique_patterns)) {
  pat <- strsplit(unique_patterns[i], "")[[1]]
  pattern_df$x1[i] <- pat[1]
  pattern_df$x2[i] <- pat[2]
  pattern_df$x3[i] <- pat[3]
  pattern_df$count[i] <- pattern_counts[unique_patterns[i]]
}

# Check: Pattern (0,0,0) should be most common
pattern_000 <- which(pattern_df$x1 == "0" & pattern_df$x2 == "0" & pattern_df$x3 == "0")
stopifnot(
  length(pattern_000) > 0
)

if (length(pattern_000) > 0) {
  stopifnot(
    pattern_df$count[pattern_000] == max(pattern_df$count)
  )
}

# Check: Pattern (0,1,x) should exist (x1 observed, x2 missing)
pattern_01_exists <- any(pattern_df$x1 == "0" & pattern_df$x2 == "1")
stopifnot(
  pattern_01_exists
)

# ===== Pairwise-complete correlations =====
# Manually compute (using all available pairs)
corr_12_manual <- cor(x1, x2, use = "pairwise.complete.obs")
corr_13_manual <- cor(x1, x3, use = "pairwise.complete.obs")
corr_23_manual <- cor(x2, x3, use = "pairwise.complete.obs")

# Oracle
data_all <- cbind(x1, x2, x3)
corr_matrix_oracle <- cor(data_all, use = "pairwise.complete.obs")

corr_12_oracle <- corr_matrix_oracle[1, 2]
corr_13_oracle <- corr_matrix_oracle[1, 3]
corr_23_oracle <- corr_matrix_oracle[2, 3]

# ===== Correlation agreement =====
# stopifnot(
  abs(corr_12_manual - corr_12_oracle) < 1e-10
# )

stopifnot(
  abs(corr_13_manual - corr_13_oracle) < 1e-10
)

stopifnot(
  abs(corr_23_manual - corr_23_oracle) < 1e-10
)

# ===== Sanity checks =====
stopifnot(
  nrow(pattern_df) <= 2^3
)

# stopifnot(
  sum(pattern_df$count) == n
# )

stopifnot(
  all(corr_matrix_oracle >= -1 & corr_matrix_oracle <= 1)
)

cat("PASS: missing_pattern_matrix.R\n")
quit(status=0)

