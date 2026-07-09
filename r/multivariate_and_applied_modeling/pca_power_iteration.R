# PCA via Power Iteration (with deflation) — oracle-verified against prcomp()
#
# Power iteration finds the dominant eigenvector of the covariance matrix; DEFLATION
# (subtract lambda1 * v1 v1^T) removes it so the SAME iteration finds the second.
# Two lessons this file carries from its own first draft:
#   - iid gaussian data has near-EQUAL eigenvalues (no structure): power iteration
#     converges slowly and any tolerance must be loose. Plant real factor structure
#     and the method converges fast and tight. Test data must contain the thing
#     the method claims to find.
#   - eigenvectors match the oracle up to a GLOBAL sign: align by dot product,
#     never compare abs() per element (that would accept mixed sign-flips that
#     are not the eigenvector at all).
# Use when: understanding eigenvalue geometry; PCA without an SVD library.

# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
.aura_mark <- "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
set.seed(42)

# Planted structure: two latent factors with distinct strengths drive 5 features.
n <- 300
f1 <- rnorm(n); f2 <- rnorm(n)
X <- cbind(
  3.0 * f1 + 0.3 * rnorm(n),
  2.8 * f1 + 0.3 * rnorm(n),
  1.5 * f2 + 0.3 * rnorm(n),
  1.4 * f2 + 0.3 * rnorm(n),
  0.5 * rnorm(n)
)
X_scaled <- scale(X, center = TRUE, scale = FALSE)
cov_mat <- cov(X_scaled)

power_iterate <- function(C, iters = 1000, tol = 1e-12) {
  v <- rnorm(ncol(C))
  v <- v / sqrt(sum(v^2))
  for (i in 1:iters) {
    w <- as.vector(C %*% v)
    w <- w / sqrt(sum(w^2))
    if (max(abs(w - v)) < tol && i > 1) { v <- w; break }
    v <- w
  }
  lambda <- as.numeric(t(v) %*% C %*% v)
  list(vector = v, value = lambda)
}

# PC1, then DEFLATE, then PC2 with the same machinery.
p1 <- power_iterate(cov_mat)
cov_deflated <- cov_mat - p1$value * (p1$vector %*% t(p1$vector))
p2 <- power_iterate(cov_deflated)

# Oracle
pca <- prcomp(X_scaled, scale. = FALSE)
o1 <- pca$rotation[, 1]; o2 <- pca$rotation[, 2]
ev1 <- pca$sdev[1]^2;    ev2 <- pca$sdev[2]^2

align <- function(v, oracle) if (sum(v * oracle) < 0) -v else v
v1 <- align(p1$vector, o1)
v2 <- align(p2$vector, o2)

cat(sprintf("PC1: max dev %.2e · eigenvalue %.4f vs oracle %.4f\n",
            max(abs(v1 - o1)), p1$value, ev1))
cat(sprintf("PC2: max dev %.2e · eigenvalue %.4f vs oracle %.4f\n",
            max(abs(v2 - o2)), p2$value, ev2))

# Tight, sign-aligned agreement on BOTH components and BOTH eigenvalues.
stopifnot(max(abs(v1 - o1)) < 1e-3)
stopifnot(max(abs(v2 - o2)) < 1e-3)
stopifnot(abs(p1$value - ev1) / ev1 < 1e-3)
stopifnot(abs(p2$value - ev2) / ev2 < 1e-3)

cat("pca_power_iteration.R PASS\n")

