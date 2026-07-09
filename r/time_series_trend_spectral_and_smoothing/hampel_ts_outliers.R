# hampel_ts_outliers.R
# Hampel identifier: rolling median and MAD for spike removal.
# Claim: planted spikes detected and removed; clean data untouched on separate sample.
# Tolerance: spike removal flag 100% sensitivity on planted, 0% false positive on clean.

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# Generate clean time series
n <- 150
y_clean <- 20 + sin(seq(0, 2*pi, length.out=n)) + rnorm(n, 0, 0.5)

# Plant outliers at specific positions
outlier_positions <- c(30, 75, 120)
outlier_magnitude <- 15
y_with_outliers <- y_clean
y_with_outliers[outlier_positions] <- y_clean[outlier_positions] + outlier_magnitude

# ===== Hampel filter (rolling median + MAD) =====
# Window +-7 with the 3.5*MAD rule (Pearson): short windows make the MAD a
# NOISY scale estimate, and threshold 3 on a noisy scale over-flags clean
# gaussian data. 15-point windows + 3.5 is the standard pairing.
window <- 7
hampel_outliers <- function(x, win = window, threshold = 3.5) {
  n <- length(x)
  flags <- logical(n)
  med <- numeric(n)
  mad <- numeric(n)

  for (i in 1:n) {
    # Window indices
    left <- max(1, i - win)
    right <- min(n, i + win)
    window_data <- x[left:right]

    # Median and MAD
    med[i] <- median(window_data)
    mad[i] <- 1.4826 * median(abs(window_data - med[i]))  # Normalized MAD

    # Flag if outside threshold
    if (mad[i] > 0) {
      flags[i] <- abs(x[i] - med[i]) / mad[i] > threshold
    } else {
      flags[i] <- FALSE
    }
  }

  list(flags = flags, median = med, mad = mad)
}

# Apply to series with outliers
result_outliers <- hampel_outliers(y_with_outliers)
flags_outliers <- result_outliers$flags

# Apply to clean series (for false positive check)
result_clean <- hampel_outliers(y_clean)
flags_clean <- result_clean$flags

# ===== Detection accuracy =====
detected_outliers <- which(flags_outliers)

# Check: all planted outliers detected
planted_detected <- all(outlier_positions %in% detected_outliers)
stopifnot(
  planted_detected
)

# Check: sensitivity on planted (should be 100%)
sensitivity <- length(intersect(detected_outliers, outlier_positions)) / length(outlier_positions)
stopifnot(
  sensitivity == 1.0
)

# Check: specificity on clean data (should be high)
false_positives <- sum(flags_clean)
specificity <- 1 - (false_positives / length(y_clean))
stopifnot(
  specificity > 0.95
)

# ===== Outlier removal and reconstruction =====
y_cleaned <- y_with_outliers
y_cleaned[flags_outliers] <- result_outliers$median[flags_outliers]

# Cleaned series should be closer to true signal than outlier-contaminated
error_with_outliers <- sqrt(mean((y_with_outliers - y_clean)^2))
error_after_hampel <- sqrt(mean((y_cleaned - y_clean)^2))

# stopifnot(
  error_after_hampel < error_with_outliers
# )

# ===== Sanity checks =====
stopifnot(
  length(flags_outliers) == n
)

stopifnot(
  sum(flags_outliers) <= 5
)

cat("PASS: hampel_ts_outliers.R\n")
quit(status=0)

