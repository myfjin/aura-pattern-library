// Welford's online algorithm for running mean and variance.
// Converted from the Python oracle.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <cassert>

struct WelfordStats {
    int count = 0;
    double mean = 0.0;
    double m2 = 0.0;

    void update(double x) {
        count += 1;
        double delta = x - mean;
        mean += delta / count;
        double delta2 = x - mean;
        m2 += delta * delta2;
    }

    double variance() const {
        if (count < 2) return 0.0;
        return m2 / (count - 1);
    }

    double std_dev() const { return std::sqrt(variance()); }
};

double batch_variance(const std::vector<double>& values) {
    if (values.size() < 2) return 0.0;
    double mean = 0.0;
    for (double x : values) mean += x;
    mean /= values.size();
    double sum_sq_dev = 0.0;
    for (double x : values) sum_sq_dev += (x - mean) * (x - mean);
    return sum_sq_dev / (values.size() - 1);
}

double naive_variance(const std::vector<double>& values) {
    if (values.size() < 2) return 0.0;
    double mean = 0.0;
    for (double x : values) mean += x;
    mean /= values.size();
    double sum_sq = 0.0;
    for (double x : values) sum_sq += x * x;
    double n = values.size();
    double var = (sum_sq / n) - (mean * mean);
    return var > 0 ? var * n / (n - 1) : 0.0;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> dist(0.0, 1.0);

    // Test 1
    std::vector<double> normal_data;
    for (int i = 0; i < 1000; ++i) normal_data.push_back(dist(rng));
    WelfordStats welford;
    for (double x : normal_data) welford.update(x);
    double batch_var = batch_variance(normal_data);
    double welford_var = welford.variance();
    assert(std::abs(welford_var - batch_var) < 1e-10);
    std::cout << "Test 1: Welford variance=" << welford_var << " batch=" << batch_var << "\n";

    // Test 2
    double offset = 1e10;
    std::vector<double> offset_data;
    for (int i = 0; i < 1000; ++i) offset_data.push_back(offset + dist(rng));
    double naive_var = naive_variance(offset_data);
    double batch_var2 = batch_variance(offset_data);
    WelfordStats welford2;
    for (double x : offset_data) welford2.update(x);
    double welford_var2 = welford2.variance();
    assert(std::abs(welford_var2 - batch_var2) < 1e-6);
    assert(std::abs(naive_var - batch_var2) > 1.0);
    std::cout << "Test 2: naive=" << naive_var << " batch=" << batch_var2 << " welford=" << welford_var2 << "\n";
    std::cout << "welford_online_stats PASS\n";
    return 0;
}
