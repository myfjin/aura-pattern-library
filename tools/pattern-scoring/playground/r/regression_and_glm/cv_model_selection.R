# cv_model_selection.R
# k-fold cross-validation for polynomial degree selection.
# Claim: CV MSE selects true-degree model over under/over-fit.
# Tolerance: true degree has lowest CV MSE with >95% probability.

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# ===== Generate data from polynomial of degree 3 =====
true_degree <- 3
n <- 100
x <- seq(-5, 5, length.out = n)
y <- 2 + 3*x - 1.5*x^2 + 0.5*x^3 + rnorm(n, 0, 1)

# ===== k-fold cross-validation =====
k_folds <- 5
fold_size <- n %/% k_folds
folds <- rep(1:k_folds, each = fold_size)
if (length(folds) < n) {
  folds <- c(folds, rep(k_folds, n - length(folds)))
}
folds <- folds[1:n]

# Test degrees: 1, 2, 3, 4, 5 (true is 3)
degrees_test <- 1:5
cv_mse <- numeric(length(degrees_test))

for (deg_idx in 1:length(degrees_test)) {
  deg <- degrees_test[deg_idx]
  mse_by_fold <- numeric(k_folds)

  for (fold_id in 1:k_folds) {
    # Train and test indices
    test_idx <- which(folds == fold_id)
    train_idx <- which(folds != fold_id)

    # Fit polynomial on training data
    poly_mat_train <- cbind(
      rep(1, length(train_idx)),
      x[train_idx],
      x[train_idx]^2,
      x[train_idx]^3,
      x[train_idx]^4,
      x[train_idx]^5
    )[, 1:(deg + 1)]

    # Normal equations
    coef_fit <- solve(t(poly_mat_train) %*% poly_mat_train) %*% t(poly_mat_train) %*% y[train_idx]

    # Predict on test data
    poly_mat_test <- cbind(
      rep(1, length(test_idx)),
      x[test_idx],
      x[test_idx]^2,
      x[test_idx]^3,
      x[test_idx]^4,
      x[test_idx]^5
    )[, 1:(deg + 1)]

    pred_test <- poly_mat_test %*% coef_fit

    # MSE
    mse_by_fold[fold_id] <- mean((y[test_idx] - pred_test)^2)
  }

  cv_mse[deg_idx] <- mean(mse_by_fold)
}

# ===== Model selection =====
selected_degree <- degrees_test[which.min(cv_mse)]

stopifnot(
  selected_degree == true_degree
)

# Under-fit (deg 1) and over-fit (deg 5) should have higher CV MSE
stopifnot(
  cv_mse[3] < cv_mse[1]  # deg 3 < deg 1
)

stopifnot(
  cv_mse[3] < cv_mse[5]  # deg 3 < deg 5
)

# ===== Sanity checks =====
stopifnot(
  all(cv_mse > 0)
)

stopifnot(
  length(cv_mse) == length(degrees_test)
)

stopifnot(
  which.min(cv_mse) > 0 && which.min(cv_mse) <= length(degrees_test)
)

cat("PASS: cv_model_selection.R\n")
quit(status=0)

