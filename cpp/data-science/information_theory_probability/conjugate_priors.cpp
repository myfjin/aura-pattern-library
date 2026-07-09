// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Conjugate Priors: Beta-Binomial and Normal-Normal (known variance)
 * 
 * Conjugate priors have closed-form posterior updates.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>
#include <utility>

std::pair<double, double> beta_binomial_posterior(
    double alpha_prior, double beta_prior,
    int successes, int failures
) {
    /* Beta-Binomial conjugate update. */
    return {alpha_prior + successes, beta_prior + failures};
}

std::pair<double, double> beta_mean_variance(double alpha, double beta) {
    /* Mean and variance of Beta(alpha, beta) distribution. */
    double sum = alpha + beta;
    double mean = alpha / sum;
    double variance = (alpha * beta) / (sum * sum * (sum + 1.0));
    return {mean, variance};
}

std::pair<double, double> normal_normal_posterior_known_variance(
    double mu_prior, double sigma2_prior,
    double sigma2_obs,
    const std::vector<double>& observations
) {
    /* Normal-Normal conjugate update with known observation variance. */
    int n = static_cast<int>(observations.size());
    double obs_mean = (n > 0) ? 0.0 : 0.0;
    for (double x : observations) obs_mean += x;
    obs_mean /= (n > 0 ? n : 1);

    double precision_prior = 1.0 / sigma2_prior;
    double precision_obs = 1.0 / sigma2_obs;
    double precision_post = precision_prior + n * precision_obs;
    double sigma2_post = 1.0 / precision_post;
    double mu_post = (precision_prior * mu_prior + n * obs_mean * precision_obs) / precision_post;

    return {mu_post, sigma2_post};
}

int main() {
    // ======== Beta-Binomial ========
    // Test 1: Sequential update = Batch update
    double alpha_prior = 2.0, beta_prior = 2.0;
    auto [alpha_batch, beta_batch] = beta_binomial_posterior(alpha_prior, beta_prior, 5, 3);
    auto [alpha_seq, beta_seq] = beta_binomial_posterior(alpha_prior, beta_prior, 2, 1);
    auto [alpha_seq2, beta_seq2] = beta_binomial_posterior(alpha_seq, beta_seq, 3, 2);

    assert(std::abs(alpha_batch - alpha_seq2) < 1e-9);
    assert(std::abs(beta_batch - beta_seq2) < 1e-9);

    // Test 2: Posterior mean shifts toward observed proportion
    double alpha_uniform = 1.0, beta_uniform = 1.0;
    auto [mean_prior, var_prior] = beta_mean_variance(alpha_uniform, beta_uniform);
    assert(std::abs(mean_prior - 0.5) < 1e-9);

    auto [alpha_post, beta_post] = beta_binomial_posterior(alpha_uniform, beta_uniform, 80, 20);
    auto [mean_post, var_post] = beta_mean_variance(alpha_post, beta_post);
    assert(std::abs(mean_post - 81.0/102.0) < 1e-9);

    // Test 3: More data → smaller posterior variance
    auto [alpha_few2, beta_few2] = beta_binomial_posterior(1.0, 1.0, 5, 5);
    auto [mean_few, var_few] = beta_mean_variance(alpha_few2, beta_few2);
    auto [alpha_many2, beta_many2] = beta_binomial_posterior(1.0, 1.0, 50, 50);
    auto [mean_many, var_many] = beta_mean_variance(alpha_many2, beta_many2);
    assert(var_many < var_few);

    // ======== Normal-Normal (known variance) ========
    // Test 4: Sequential = Batch for Normal-Normal
    double mu_prior = 0.0, sigma2_prior = 1.0, sigma2_obs = 1.0;
    std::vector<double> obs_all = {1.0, 2.0, 3.0};
    auto [mu_batch, sigma2_batch] = normal_normal_posterior_known_variance(mu_prior, sigma2_prior, sigma2_obs, obs_all);

    double mu_seq = mu_prior, sigma2_seq = sigma2_prior;
    for (double obs : obs_all) {
        auto [mu_new, sigma2_new] = normal_normal_posterior_known_variance(mu_seq, sigma2_seq, sigma2_obs, {obs});
        mu_seq = mu_new;
        sigma2_seq = sigma2_new;
    }
    assert(std::abs(mu_batch - mu_seq) < 1e-9);
    assert(std::abs(sigma2_batch - sigma2_seq) < 1e-9);

    // Test 5: Posterior mean shifts toward observed data
    assert(std::abs(mu_batch - 1.5) < 1e-9);

    // Test 6: More observations → smaller posterior variance
    std::vector<double> obs_few = {1.0, 2.0};
    auto [mu_f, sigma2_f] = normal_normal_posterior_known_variance(mu_prior, sigma2_prior, sigma2_obs, obs_few);
    std::vector<double> obs_many(100, 1.0);
    auto [mu_m, sigma2_m] = normal_normal_posterior_known_variance(mu_prior, sigma2_prior, sigma2_obs, obs_many);
    assert(sigma2_m < sigma2_f);

    // Test 7: Posterior variance formula check
    int n = static_cast<int>(obs_all.size());
    double sigma2_post_expected = 1.0 / (1.0 / sigma2_prior + n / sigma2_obs);
    assert(std::abs(sigma2_batch - sigma2_post_expected) < 1e-9);

    // Test 8: Very strong prior keeps posterior close to prior
    double mu_strong_prior = 0.0, sigma2_strong_prior = 0.001;
    std::vector<double> obs_away = {10.0, 11.0, 12.0};
    auto [mu_strong_post, sigma2_strong_post] = normal_normal_posterior_known_variance(mu_strong_prior, sigma2_strong_prior, sigma2_obs, obs_away);
    assert(mu_strong_post < 2.0);

    std::cout << "Conjugate priors (Beta-Binomial + Normal-Normal): all assertions PASS" << std::endl;
    return 0;
}
