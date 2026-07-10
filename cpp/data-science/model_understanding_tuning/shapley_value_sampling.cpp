// Shapley Value Sampling (Monte Carlo Approximation)
// C++17 self-contained implementation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <numeric>
#include <random>
#include <unordered_set>
#include <vector>

double additiveModel(const std::vector<double>& features) {
    double result = 0.0;
    for (size_t i = 0; i < features.size(); ++i) {
        result += features[i] * static_cast<double>(i + 1);
    }
    return result;
}

double coalitionValue(const std::vector<double>& features,
                      const std::vector<int>& coalitionIdx) {
    std::vector<double> current = features;
    std::unordered_set<int> inCoalition(coalitionIdx.begin(), coalitionIdx.end());
    for (size_t i = 0; i < features.size(); ++i) {
        if (inCoalition.find(static_cast<int>(i)) == inCoalition.end()) {
            current[i] = 0.0;
        }
    }
    return additiveModel(current);
}

double shapleyValueSample(int featureIdx, int numFeatures, int numSamples,
                          const std::vector<double>& featureValues,
                          std::mt19937& rng) {
    std::vector<double> marginalContributions;
    marginalContributions.reserve(numSamples);

    std::vector<int> perm(numFeatures);
    for (int i = 0; i < numFeatures; ++i) perm[i] = i;

    for (int sample = 0; sample < numSamples; ++sample) {
        std::shuffle(perm.begin(), perm.end(), rng);

        int pos = 0;
        while (pos < numFeatures && perm[pos] != featureIdx) ++pos;

        std::vector<int> coalitionWithout(perm.begin(), perm.begin() + pos);
        std::vector<int> coalitionWith(perm.begin(), perm.begin() + pos + 1);

        double valWithout = coalitionValue(featureValues, coalitionWithout);
        double valWith = coalitionValue(featureValues, coalitionWith);

        marginalContributions.push_back(valWith - valWithout);
    }

    double sum = std::accumulate(marginalContributions.begin(),
                                marginalContributions.end(), 0.0);
    return sum / marginalContributions.size();
}

double analyticShapley(int featureIdx, const std::vector<double>& featureValues) {
    double weight = static_cast<double>(featureIdx + 1);
    return weight * featureValues[featureIdx];
}

int main() {
    std::mt19937 rng(42);

    constexpr int numFeatures = 4;
    std::vector<double> featureValues = { 2.0, 3.0, 1.5, 2.5 };

    double maxError = 0.0;
    for (int featIdx = 0; featIdx < numFeatures; ++featIdx) {
        double sampled = shapleyValueSample(featIdx, numFeatures, 500,
                                            featureValues, rng);
        double analytic = analyticShapley(featIdx, featureValues);
        double error = std::abs(sampled - analytic);
        maxError = std::max(maxError, error);

        std::cout << "Feature " << featIdx << ": Sampled " << sampled
                  << ", Analytic " << analytic << ", Error " << error << "\n";
    }

    assert(maxError < 0.5);
    assert(maxError < analyticShapley(0, featureValues) * 0.3);

    std::cout << "shapley_value_sampling PASS (maxError=" << maxError << ")\n";
    return 0;
}
