// Sequential Probability Ratio Test (SPRT).
// C++17 self-contained implementation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <string>
#include <utility>
#include <vector>

std::pair<std::string, int> sprt(const std::vector<int>& data,
                                   double p0, double p1,
                                   double alpha = 0.05, double beta = 0.05) {
    double A = (1.0 - beta) / alpha;
    double B = beta / (1.0 - alpha);

    double log_lr = 0.0;
    double logA = std::log(A);
    double logB = std::log(B);

    for (size_t i = 0; i < data.size(); ++i) {
        if (data[i] == 1) {
            log_lr += std::log(p1 / p0);
        } else {
            log_lr += std::log((1.0 - p1) / (1.0 - p0));
        }

        if (log_lr > logA) {
            return { "H1", static_cast<int>(i + 1) };
        }
        if (log_lr < logB) {
            return { "H0", static_cast<int>(i + 1) };
        }
    }

    return { "INCONCLUSIVE", static_cast<int>(data.size()) };
}

std::string fixedNTest(const std::vector<int>& data, double p0, double p1,
                       double /*alpha*/ = 0.05) {
    int successes = 0;
    for (int x : data) successes += x;
    double p_hat = static_cast<double>(successes) / data.size();
    double midpoint = (p0 + p1) / 2.0;
    return p_hat > midpoint ? "H1" : "H0";
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> udist(0.0, 1.0);

    constexpr double p0 = 0.4;
    constexpr double p1 = 0.6;
    constexpr double alpha = 0.05;
    constexpr double beta = 0.05;
    constexpr double trueP = 0.6;
    constexpr int maxSamples = 500;
    constexpr int numTrials = 100;
    constexpr int fixedNTypical = 200;

    std::vector<int> sprtSamples;

    for (int trial = 0; trial < numTrials; ++trial) {
        std::vector<int> data;
        data.reserve(maxSamples);
        for (int i = 0; i < maxSamples; ++i) {
            data.push_back(udist(rng) < trueP ? 1 : 0);
        }
        auto [decision, nUsed] = sprt(data, p0, p1, alpha, beta);
        if (decision == "H1") {
            sprtSamples.push_back(nUsed);
        }
    }

    std::vector<std::string> fixedNDecisions;
    fixedNDecisions.reserve(numTrials);
    for (int trial = 0; trial < numTrials; ++trial) {
        std::vector<int> data;
        data.reserve(fixedNTypical);
        for (int i = 0; i < fixedNTypical; ++i) {
            data.push_back(udist(rng) < trueP ? 1 : 0);
        }
        fixedNDecisions.push_back(fixedNTest(data, p0, p1, alpha));
    }

    assert(!sprtSamples.empty());
    double avgSprt = 0.0;
    for (int n : sprtSamples) avgSprt += n;
    avgSprt /= sprtSamples.size();

    int h1Count = 0;
    for (const auto& d : fixedNDecisions) {
        if (d == "H1") ++h1Count;
    }
    double h1RateFixed = static_cast<double>(h1Count) / fixedNDecisions.size();

    assert(avgSprt > 0.0);
    assert(avgSprt < fixedNTypical);
    assert(h1RateFixed > 0.7);

    std::cout << "sequential_probability_ratio PASS (avg SPRT samples: " << avgSprt
              << ", n=" << sprtSamples.size() << ", fixed H1 rate: "
              << h1RateFixed << ")\n";
    return 0;
}
