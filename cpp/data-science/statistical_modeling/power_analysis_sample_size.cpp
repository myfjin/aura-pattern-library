// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <iostream>

// Uses built-in erf for accurate normal_cdf. The oracle uses tanh approximation;
// using erf keeps the C++ code simple, standard, and accurate enough for assertions.
double normal_cdf(double z) {
    return 0.5 * (1.0 + std::erf(z / std::sqrt(2.0)));
}

double normal_quantile(double p) {
    if (p < 0.5) return -normal_quantile(1.0 - p);
    double t = std::sqrt(-2.0 * std::log(1.0 - p));
    double num = 2.515517 + 0.802853 * t + 0.010328 * t * t;
    double denom = 1.0 + 1.432788 * t + 0.189269 * t * t + 0.001308 * t * t * t;
    return t - num / denom;
}

double two_proportion_power(int n, double p1, double p2, double alpha) {
    double z_crit = normal_quantile(1.0 - alpha / 2.0);
    double p_pool = (p1 + p2) / 2.0;
    (void)p_pool;
    double se_h1 = std::sqrt((p1 * (1.0 - p1) + p2 * (1.0 - p2)) / n);
    double effect = std::abs(p1 - p2);
    if (se_h1 == 0.0) return 1.0;
    double ncp = effect / se_h1;
    // Oracle uses 1 - Phi(z_crit - ncp), matching one-sided upper tail power approximation.
    return 1.0 - normal_cdf(z_crit - ncp);
}

int sample_size_two_proportion(double p1, double p2, double alpha, double target_power) {
    double z_alpha = normal_quantile(1.0 - alpha / 2.0);
    double z_beta = normal_quantile(target_power);
    double p_pool = (p1 + p2) / 2.0;
    double se_sq = 2.0 * p_pool * (1.0 - p_pool) + (p1 * (1.0 - p1) + p2 * (1.0 - p2));
    double effect = std::abs(p1 - p2);
    double n = (z_alpha + z_beta) * (z_alpha + z_beta) * se_sq / (effect * effect);
    return std::max(1, static_cast<int>(std::ceil(n)));
}

int main() {
    double p1 = 0.3, p2 = 0.5;
    double alpha = 0.05;
    double target_power = 0.80;

    int n_computed = sample_size_two_proportion(p1, p2, alpha, target_power);
    double achieved_power = two_proportion_power(n_computed, p1, p2, alpha);
    double power_lower = two_proportion_power(n_computed - 1, p1, p2, alpha);

    assert(achieved_power >= target_power - 0.05);
    assert(power_lower < achieved_power);

    std::cout << "power_analysis_sample_size.cpp: n_computed=" << n_computed
              << ", achieved_power=" << achieved_power
              << ", target=" << target_power << " PASS" << std::endl;
    return 0;
}
