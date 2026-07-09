// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Portfolio Value-at-Risk via Bootstrap
 * 
 * VaR at confidence c is the (1−c) quantile of the RETURN distribution.
 * Bootstrap here resamples returns, takes the (1−c) quantile of each resample, and averages.
 */

#include <vector>
#include <random>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <iostream>
#include <utility>

double quantile(std::vector<double> sorted_vals, double q) {
    /* Lower-index empirical quantile of an already-sorted list. */
    int idx = static_cast<int>(q * sorted_vals.size());
    idx = std::max(0, std::min(idx, static_cast<int>(sorted_vals.size()) - 1));
    return sorted_vals[idx];
}

std::pair<double, double> portfolio_var_bootstrap(
    const std::vector<double>& returns,
    double confidence_level = 0.95,
    int num_bootstrap = 1000
) {
    /* Estimate Value-at-Risk via bootstrap. Returns (var_estimate, var_se). */
    int n = static_cast<int>(returns.size());
    double tail = 1.0 - confidence_level;

    std::mt19937 rng(42);
    std::uniform_int_distribution<int> uniform(0, n - 1);

    std::vector<double> resample_vars;
    resample_vars.reserve(num_bootstrap);

    for (int b = 0; b < num_bootstrap; ++b) {
        // Resample with replacement
        std::vector<double> sample(n);
        for (int i = 0; i < n; ++i) {
            sample[i] = returns[uniform(rng)];
        }
        std::sort(sample.begin(), sample.end());
        resample_vars.push_back(quantile(sample, tail));
    }

    // Mean VaR
    double sum = 0.0;
    for (double v : resample_vars) sum += v;
    double mean_var = sum / resample_vars.size();

    // Standard error
    double var_sum = 0.0;
    for (double v : resample_vars) {
        double diff = v - mean_var;
        var_sum += diff * diff;
    }
    double var_se = std::sqrt(var_sum / resample_vars.size());

    return {mean_var, var_se};
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> normal(-0.001, 0.02);

    // Planted: daily portfolio returns, small negative drift, 2% volatility.
    std::vector<double> returns(250);
    for (int i = 0; i < 250; ++i) {
        returns[i] = normal(rng);
    }

    auto [var_95, var_se] = portfolio_var_bootstrap(returns, 0.95, 1000);

    // Empirical 5% return quantile
    std::vector<double> sorted_returns = returns;
    std::sort(sorted_returns.begin(), sorted_returns.end());
    double empirical_q05 = quantile(sorted_returns, 0.05);

    // Defining property: bootstrap VaR ≈ the empirical 5% RETURN quantile
    assert(std::abs(var_95 - empirical_q05) < 0.005);

    // VaR is a loss (negative) and of the right order of magnitude for ~2% vol.
    assert(var_95 < 0.0);
    assert(var_95 < -0.015);
    assert(var_95 > -0.10);

    std::cout << "bootstrap_portfolio_var.cpp PASS" << std::endl;
    return 0;
}
