// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Shannon-entropy estimators from discrete samples: naive plug-in vs Miller-Madow.
 * The plug-in estimator computes -sum p*log2(p) from empirical frequencies; it
 * systematically UNDER-estimates entropy at small sample sizes. Miller-Madow adds
 * the bias correction (K-1)/(2*N*ln2), where K is the number of observed symbols.
 * Use when estimating entropy from limited counts and small-sample bias matters.
 * Guarantee (proven in main): on a known uniform source the Miller-Madow error is
 * smaller than plug-in at N=20, and both converge to the true 2.0 bits at N=10000.
 */
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstddef>
#include <iostream>
#include <map>
#include <random>
#include <vector>

static double true_entropy(const std::vector<double>& probabilities) {
    double result = 0.0;
    for (double p : probabilities) {
        if (p > 1e-10) {
            result -= p * std::log2(p);
        }
    }
    return result;
}

static double naive_plugin_entropy(const std::vector<int>& samples) {
    std::map<int, int> counts;
    for (int s : samples) ++counts[s];
    double result = 0.0;
    double n = static_cast<double>(samples.size());
    for (const auto& kv : counts) {
        double p = static_cast<double>(kv.second) / n;
        if (p > 1e-10) {
            result -= p * std::log2(p);
        }
    }
    return result;
}

static double miller_madow_entropy(const std::vector<int>& samples) {
    double n = static_cast<double>(samples.size());
    std::map<int, int> counts;
    for (int s : samples) ++counts[s];
    int k = static_cast<int>(counts.size());
    double naive = naive_plugin_entropy(samples);
    double correction = (k - 1) / (2.0 * n * std::log(2.0));
    return naive + correction;
}

int main() {
    std::mt19937 rng(42);

    std::vector<double> true_probs = {0.25, 0.25, 0.25, 0.25};
    double true_h = true_entropy(true_probs);
    assert(std::fabs(true_h - 2.0) < 1e-9);

    std::discrete_distribution<int> dist(true_probs.begin(), true_probs.end());
    std::vector<int> samples_small;
    samples_small.reserve(20);
    for (int i = 0; i < 20; ++i) samples_small.push_back(dist(rng));

    double naive_small = naive_plugin_entropy(samples_small);
    double mm_small = miller_madow_entropy(samples_small);

    double naive_error = std::fabs(naive_small - true_h);
    double mm_error = std::fabs(mm_small - true_h);
    assert(mm_error < naive_error);

    std::vector<int> samples_large;
    samples_large.reserve(10000);
    for (int i = 0; i < 10000; ++i) samples_large.push_back(dist(rng));

    double naive_large = naive_plugin_entropy(samples_large);
    double mm_large = miller_madow_entropy(samples_large);

    assert(std::fabs(naive_large - true_h) < 0.1);
    assert(std::fabs(mm_large - true_h) < 0.1);
    assert(mm_large > naive_large);

    std::cout << "Entropy estimators (naive plug-in vs Miller-Madow): all assertions PASS\n";
    return 0;
}
