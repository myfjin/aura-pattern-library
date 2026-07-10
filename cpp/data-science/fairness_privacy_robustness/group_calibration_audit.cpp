// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Group Calibration Audit: verify per-group reliability of predicted probabilities.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>

double expected_calibration_error(const std::vector<double>& probs,
                                  const std::vector<int>& labels, int bins = 5) {
    double ece = 0.0;
    int total = 0;

    for (int b = 0; b < bins; ++b) {
        double lower = static_cast<double>(b) / bins;
        double upper = static_cast<double>(b + 1) / bins;

        std::vector<double> in_bin_probs;
        std::vector<int> in_bin_labels;
        for (size_t i = 0; i < probs.size(); ++i) {
            if ((probs[i] >= lower && probs[i] < upper) ||
                (b == bins - 1 && probs[i] == upper)) {
                in_bin_probs.push_back(probs[i]);
                in_bin_labels.push_back(labels[i]);
            }
        }

        if (!in_bin_probs.empty()) {
            double avg_pred = 0.0;
            for (double p : in_bin_probs) avg_pred += p;
            avg_pred /= in_bin_probs.size();

            double avg_true = 0.0;
            for (int y : in_bin_labels) avg_true += y;
            avg_true /= in_bin_labels.size();

            ece += std::abs(avg_pred - avg_true) * in_bin_probs.size();
            total += in_bin_probs.size();
        }
    }

    return (total > 0) ? ece / total : 0.0;
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform_good(0.1, 0.9);
    std::uniform_real_distribution<double> uniform_bad(0.1, 0.5);

    const int n_per_group = 100;
    std::vector<double> probs_good, probs_bad;
    std::vector<int> labels_good, labels_bad;

    for (int i = 0; i < n_per_group; ++i) {
        double p = uniform_good(rng);
        probs_good.push_back(p);
        labels_good.push_back((std::uniform_real_distribution<double>(0.0, 1.0)(rng) < p) ? 1 : 0);
    }

    for (int i = 0; i < n_per_group; ++i) {
        double p = uniform_bad(rng);
        probs_bad.push_back(p);
        labels_bad.push_back((std::uniform_real_distribution<double>(0.0, 1.0)(rng) < 0.8) ? 1 : 0);
    }

    double ece_good = expected_calibration_error(probs_good, labels_good);
    double ece_bad = expected_calibration_error(probs_bad, labels_bad);

    assert(ece_good < 0.2);
    assert(ece_bad > ece_good);

    std::cout << "group_calibration_audit.cpp PASS" << std::endl;
    return 0;
}
