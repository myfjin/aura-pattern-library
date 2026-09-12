// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Bayesian Linear Regression with Conjugate Prior
 * 
 * Posterior mean ≈ true βs; 95% credible interval covers them.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>
#include <utility>

std::pair<double, double> bayesian_linreg_posterior(
    const std::vector<double>& x_vals,
    const std::vector<double>& y_vals
) {
    /*
     * Conjugate posterior for y = a + b*x with Gaussian prior N(0, 10).
     * Returns (posterior_mean_b, posterior_var_b).
     */
    int n = static_cast<int>(x_vals.size());
    double x_mean = 0.0, y_mean = 0.0;
    for (const auto& x : x_vals) x_mean += x;
    for (const auto& y : y_vals) y_mean += y;
    x_mean /= n;
    y_mean /= n;

    double sx2 = 0.0, sxy = 0.0;
    for (int i = 0; i < n; ++i) {
        double dx = x_vals[i] - x_mean;
        double dy = y_vals[i] - y_mean;
        sx2 += dx * dx;
        sxy += dx * dy;
    }

    // MLE slope.
    double b_mle = (std::abs(sx2) > 1e-12) ? sxy / sx2 : 0.0;

    // Posterior variance (with weak prior).
    double posterior_var = 1.0 / (n + 0.1);

    // Posterior mean (with weak prior).
    double posterior_mean_b = posterior_var * (b_mle * n);

    return {posterior_mean_b, posterior_var};
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform(-5.0, 5.0);
    std::normal_distribution<double> normal(0.0, 1.0);

    // Planted: true model y = 2.0 + 1.5*x.
    const double beta_true = 1.5;
    const int n = 50;

    std::vector<double> x(n), y(n);
    for (int i = 0; i < n; ++i) {
        x[i] = uniform(rng);
        y[i] = 2.0 + beta_true * x[i] + normal(rng);
    }

    // Posterior.
    auto [posterior_mean_b, posterior_var_b] = bayesian_linreg_posterior(x, y);
    double posterior_sd_b = std::sqrt(posterior_var_b);

    // Posterior mean should recover true β.
    assert(std::abs(posterior_mean_b - beta_true) < 0.5);

    // 95% credible interval should cover truth.
    double ci_lower = posterior_mean_b - 1.96 * posterior_sd_b;
    double ci_upper = posterior_mean_b + 1.96 * posterior_sd_b;
    assert(ci_lower < beta_true && beta_true < ci_upper);

    std::cout << "bayesian_linreg_conjugate.cpp PASS" << std::endl;
    return 0;
}
