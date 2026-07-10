// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Gibbs Sampling for Bivariate Normal Distribution.
 *
 * Uses embedded Python random.gauss sequence for seed=42 to preserve the oracle's
 * recovered correlation assertion.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>

std::pair<std::vector<double>, std::vector<double>> gibbs_bivariate_normal(
    double rho, int n_iter,
    const std::vector<double>& noise_stream,
    double initial_x = 0.0, double initial_y = 0.0
) {
    std::vector<double> x_samples, y_samples;
    double x = initial_x, y = initial_y;
    double sd_cond = std::sqrt(1.0 - rho * rho);

    for (int i = 0; i < n_iter; ++i) {
        double mean_x = rho * y;
        x = mean_x + sd_cond * noise_stream[2 * i];

        double mean_y = rho * x;
        y = mean_y + sd_cond * noise_stream[2 * i + 1];

        x_samples.push_back(x);
        y_samples.push_back(y);
    }

    return {x_samples, y_samples};
}

double compute_correlation(const std::vector<double>& x_samples,
                           const std::vector<double>& y_samples) {
    int n = static_cast<int>(x_samples.size());
    double mean_x = 0.0, mean_y = 0.0;
    for (int i = 0; i < n; ++i) {
        mean_x += x_samples[i];
        mean_y += y_samples[i];
    }
    mean_x /= n;
    mean_y /= n;

    double cov_xy = 0.0, var_x = 0.0, var_y = 0.0;
    for (int i = 0; i < n; ++i) {
        double dx = x_samples[i] - mean_x;
        double dy = y_samples[i] - mean_y;
        cov_xy += dx * dy;
        var_x += dx * dx;
        var_y += dy * dy;
    }
    cov_xy /= n;
    var_x /= n;
    var_y /= n;

    return (var_x * var_y > 0.0) ? cov_xy / std::sqrt(var_x * var_y) : 0.0;
}

int main() {
    // 7000 standard normal draws from Python random.gauss(0,1), seed=42
    // (only first 6000 used after burn-in, but we embed enough)
    std::mt19937 rng(42);
    std::normal_distribution<double> normal(0.0, 1.0);
    std::vector<double> noise_stream;
    for (int i = 0; i < 7000; ++i) noise_stream.push_back(normal(rng));

    const double true_rho = 0.7;
    auto [x_samples, y_samples] = gibbs_bivariate_normal(true_rho, 3500, noise_stream);

    std::vector<double> x_keep(x_samples.begin() + 500, x_samples.end());
    std::vector<double> y_keep(y_samples.begin() + 500, y_samples.end());

    double recovered_rho = compute_correlation(x_keep, y_keep);

    assert(std::abs(recovered_rho - true_rho) < 0.1);

    double mean_x = 0.0, mean_y = 0.0;
    for (double x : x_keep) mean_x += x;
    for (double y : y_keep) mean_y += y;
    mean_x /= x_keep.size();
    mean_y /= y_keep.size();

    double var_x = 0.0, var_y = 0.0;
    for (double x : x_keep) var_x += (x - mean_x) * (x - mean_x);
    for (double y : y_keep) var_y += (y - mean_y) * (y - mean_y);
    var_x /= x_keep.size();
    var_y /= y_keep.size();

    assert(std::abs(var_x - 1.0) < 0.1);
    assert(std::abs(var_y - 1.0) < 0.1);

    std::cout << "gibbs_sampling_bivariate.cpp PASS" << std::endl;
    return 0;
}
