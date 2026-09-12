// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Gamma-Poisson conjugate prior: Gamma prior on Poisson rate parameter.
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <utility>

double log_gamma_func(double x) {
    if (x < 1.0) return -1e18;
    // Stirling
    return 0.5 * std::log(2.0 * M_PI) + (x - 0.5) * std::log(x) - x;
}

std::pair<double, double> gamma_poisson_posterior(const std::vector<int>& counts,
                                                  double alpha_prior, double beta_prior) {
    int n = static_cast<int>(counts.size());
    int sum_counts = 0;
    for (int c : counts) sum_counts += c;
    return {alpha_prior + sum_counts, beta_prior + n};
}

double gamma_posterior_mean(double alpha, double beta) {
    return alpha / beta;
}

double gamma_posterior_var(double alpha, double beta) {
    return alpha / (beta * beta);
}

double gamma_poisson_ll(const std::vector<int>& counts, double alpha, double beta) {
    double ll = 0.0;
    for (int count : counts) {
        ll += log_gamma_func(alpha + count) - log_gamma_func(alpha);
        if (beta + 1.0 > 0.0) {
            ll -= count * std::log(beta + 1.0);
        }
        for (int j = 1; j <= count; ++j) {
            ll -= std::log(static_cast<double>(j));
        }
    }
    return ll;
}

int main() {
    // Exact Python Knuth Poisson samples for seed=42, λ=3.5, n=50
    const std::vector<int> counts = {
        1, 4, 2, 2, 3, 2, 3, 2, 4, 7, 2, 1, 1, 3, 4, 2, 7, 1, 4, 4,
        3, 5, 1, 3, 5, 5, 5, 4, 4, 1, 1, 4, 4, 4, 3, 3, 4, 3, 1, 4,
        3, 6, 6, 3, 3, 5, 7, 1, 5, 5
    };

    const double true_lambda = 3.5;
    (void)true_lambda;  // Documentary reference only in this twin

    // Weak prior: Gamma(1, 1)
    double alpha_weak = 1.0, beta_weak = 1.0;
    auto [alpha_weak_post, beta_weak_post] = gamma_poisson_posterior(counts, alpha_weak, beta_weak);
    double mean_weak_post = gamma_posterior_mean(alpha_weak_post, beta_weak_post);

    // Strong prior: Gamma(2, 1)
    double alpha_strong = 2.0, beta_strong = 1.0;
    auto [alpha_strong_post, beta_strong_post] = gamma_poisson_posterior(counts, alpha_strong, beta_strong);
    double mean_strong_post = gamma_posterior_mean(alpha_strong_post, beta_strong_post);

    // Assertions
    assert(alpha_weak_post == alpha_weak + 170);
    assert(beta_weak_post == beta_weak + 50);

    double empirical_mean = 170.0 / 50.0;
    double prior_mean_weak = gamma_posterior_mean(alpha_weak, beta_weak);
    assert((prior_mean_weak < mean_weak_post && mean_weak_post < empirical_mean) ||
           (prior_mean_weak > mean_weak_post && mean_weak_post > empirical_mean));

    double prior_mean_strong = gamma_posterior_mean(alpha_strong, beta_strong);
    assert(mean_strong_post >= std::min(prior_mean_strong, empirical_mean) - 1e-9 &&
           mean_strong_post <= std::max(prior_mean_strong, empirical_mean) + 1e-9);

    double var_weak_prior = gamma_posterior_var(alpha_weak, beta_weak);
    double var_weak_post = gamma_posterior_var(alpha_weak_post, beta_weak_post);
    assert(var_weak_post < var_weak_prior);

    double ll = gamma_poisson_ll(counts, alpha_weak, beta_weak);
    assert(!std::isnan(ll) && !std::isinf(ll));

    double seq_alpha = alpha_weak, seq_beta = beta_weak;
    for (int count : counts) {
        seq_alpha += count;
        seq_beta += 1;
    }
    assert(seq_alpha == alpha_weak_post && seq_beta == beta_weak_post);

    std::cout << "gamma_poisson_conjugate.cpp PASS" << std::endl;
    return 0;
}
