// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Box-Muller Transform: Generate Gaussian-Distributed Samples
 * 
 * Given two independent Uniform(0, 1) variables U1 and U2, compute
 * Z1 = sqrt(-2 * log(U1)) * cos(2π * U2) and Z2 = sqrt(-2 * log(U1)) * sin(2π * U2).
 * Both Z1 and Z2 are independent standard Normal(0, 1).
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>
#include <utility>

std::pair<double, double> box_muller_pair(std::mt19937& rng) {
    /* Generate one pair of independent standard normal random variables. */
    std::uniform_real_distribution<double> uniform(0.0, 1.0);

    double u1 = uniform(rng);
    double u2 = uniform(rng);

    // Ensure u1 is not exactly 0 (log(0) is undefined)
    if (u1 < 1e-10) u1 = 1e-10;

    double r = std::sqrt(-2.0 * std::log(u1));
    double theta = 2.0 * M_PI * u2;

    double z1 = r * std::cos(theta);
    double z2 = r * std::sin(theta);

    return {z1, z2};
}

std::vector<double> generate_gaussians(int n, std::mt19937& rng) {
    /* Generate n Gaussian samples using Box-Muller. */
    std::vector<double> samples;
    samples.reserve(n);

    for (int i = 0; i < n / 2; ++i) {
        auto [z1, z2] = box_muller_pair(rng);
        samples.push_back(z1);
        samples.push_back(z2);
    }

    // If n is odd, generate one more pair and use one value
    if (n % 2 == 1) {
        auto [z1, z2] = box_muller_pair(rng);
        samples.push_back(z1);
    }

    if (static_cast<int>(samples.size()) > n) {
        samples.resize(n);
    }

    return samples;
}

double empirical_mean(const std::vector<double>& samples) {
    if (samples.empty()) return 0.0;
    double sum = 0.0;
    for (double x : samples) sum += x;
    return sum / samples.size();
}

double empirical_variance(const std::vector<double>& samples) {
    if (samples.size() < 2) return 0.0;
    double mean = empirical_mean(samples);
    double sum_sq = 0.0;
    for (double x : samples) {
        double diff = x - mean;
        sum_sq += diff * diff;
    }
    return sum_sq / (samples.size() - 1);
}

double empirical_skewness(const std::vector<double>& samples) {
    if (samples.size() < 3) return 0.0;
    double mean = empirical_mean(samples);
    double std = std::sqrt(empirical_variance(samples));
    if (std < 1e-10) return 0.0;
    double third_moment = 0.0;
    for (double x : samples) {
        double diff = x - mean;
        third_moment += diff * diff * diff;
    }
    third_moment /= samples.size();
    return third_moment / (std * std * std);
}

double coverage_percentile(const std::vector<double>& samples, double num_stds) {
    /* Fraction of samples within num_stds standard deviations of mean. */
    double mean = empirical_mean(samples);
    double std = std::sqrt(empirical_variance(samples));
    if (std < 1e-10) return 0.0;

    int within = 0;
    for (double x : samples) {
        if (std::abs(x - mean) <= num_stds * std) {
            within++;
        }
    }
    return static_cast<double>(within) / samples.size();
}

int main() {
    std::mt19937 rng(42);

    // Generate large sample
    const int n = 10000;
    auto samples = generate_gaussians(n, rng);

    // Test 1: Mean should be close to 0
    double emp_mean = empirical_mean(samples);
    assert(std::abs(emp_mean) < 0.05);

    // Test 2: Variance should be close to 1
    double emp_var = empirical_variance(samples);
    assert(emp_var > 0.95 && emp_var < 1.05);

    // Test 3: Skewness should be close to 0 (normal is symmetric)
    double emp_skew = empirical_skewness(samples);
    assert(std::abs(emp_skew) < 0.1);

    // Test 4: Empirical rule ~ 68% within 1σ
    double coverage_1sigma = coverage_percentile(samples, 1.0);
    assert(coverage_1sigma > 0.65 && coverage_1sigma < 0.72);

    // Test 5: Empirical rule ~ 95% within 2σ
    double coverage_2sigma = coverage_percentile(samples, 2.0);
    assert(coverage_2sigma > 0.93 && coverage_2sigma < 0.97);

    // Test 6: Empirical rule ~ 99.7% within 3σ
    double coverage_3sigma = coverage_percentile(samples, 3.0);
    assert(coverage_3sigma > 0.99 && coverage_3sigma < 1.0);

    // Test 7: Negative values should be present (symmetric around 0)
    int negatives = 0, positives = 0;
    for (double x : samples) {
        if (x < 0) negatives++;
        if (x > 0) positives++;
    }
    assert(negatives > 0 && positives > 0);
    double ratio = static_cast<double>(std::min(negatives, positives)) / std::max(negatives, positives);
    assert(ratio > 0.45);

    std::cout << "Box-Muller Gaussian generation: all assertions PASS" << std::endl;
    return 0;
}
