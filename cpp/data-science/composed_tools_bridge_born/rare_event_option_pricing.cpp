// rare_event_option_pricing.cpp — Deep OTM option: naive MC vs importance sampling.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <random>
#include <utility>
#include <vector>

constexpr double S0 = 100.0;
constexpr double K = 200.0;
constexpr double R = 0.02;
constexpr double SIGMA = 0.2;
constexpr double T = 1.0;

static double norm_cdf(double x) {
    return 0.5 * (1.0 + std::erf(x / std::sqrt(2.0)));
}

static double black_scholes_call() {
    double d1 = (std::log(S0 / K) + (R + SIGMA * SIGMA / 2.0) * T) / (SIGMA * std::sqrt(T));
    double d2 = d1 - SIGMA * std::sqrt(T);
    return S0 * norm_cdf(d1) - K * std::exp(-R * T) * norm_cdf(d2);
}

static double terminal_price(double z) {
    return S0 * std::exp((R - SIGMA * SIGMA / 2.0) * T + SIGMA * std::sqrt(T) * z);
}

static double naive_mc(int n, std::mt19937& rng) {
    std::normal_distribution<double> norm(0.0, 1.0);
    double disc = std::exp(-R * T);
    double total = 0.0;
    for (int i = 0; i < n; ++i) {
        total += std::max(terminal_price(norm(rng)) - K, 0.0);
    }
    return disc * total / n;
}

static std::pair<double, double> importance_sampled_mc(int n, std::mt19937& rng) {
    double theta = (std::log(K / S0) - (R - SIGMA * SIGMA / 2.0) * T) / (SIGMA * std::sqrt(T));
    double disc = std::exp(-R * T);
    std::normal_distribution<double> shifted(theta, 1.0);

    std::vector<double> vals;
    vals.reserve(n);
    for (int i = 0; i < n; ++i) {
        double z = shifted(rng);
        double w = std::exp(-theta * z + theta * theta / 2.0);
        vals.push_back(disc * std::max(terminal_price(z) - K, 0.0) * w);
    }

    double mean = std::accumulate(vals.begin(), vals.end(), 0.0) / n;
    double var = 0.0;
    for (double v : vals) {
        double d = v - mean;
        var += d * d;
    }
    var /= (n - 1);
    double se = std::sqrt(var / n);
    return {mean, se};
}

int main() {
    std::mt19937 rng_naive(42);
    std::mt19937 rng_is(42);

    double truth = black_scholes_call();
    const int n = 2000;

    double naive = naive_mc(n, rng_naive);
    auto [is_price, se] = importance_sampled_mc(n, rng_is);

    double err_naive = std::abs(naive - truth) / truth;
    double err_is = std::abs(is_price - truth) / truth;

    std::printf("Black-Scholes truth: %.6f\n", truth);
    std::printf("naive MC  (n=%d): %.6f  rel err %.0f%%\n", n, naive, 100.0 * err_naive);
    std::printf("IS MC     (n=%d): %.6f  rel err %.1f%% · SE/truth %.1f%%\n",
                n, is_price, 100.0 * err_is, 100.0 * se / truth);

    assert(err_is < 0.10);
    assert(err_naive > 3.0 * err_is);
    assert(se / truth < 0.10);
    std::printf("rare_event_option_pricing.cpp PASS\n");
    return 0;
}
