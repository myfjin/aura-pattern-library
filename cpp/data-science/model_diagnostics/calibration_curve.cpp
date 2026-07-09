// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Calibration Curve & Brier Score
 * 
 * Evaluates classifier calibration by binning predicted probabilities and comparing
 * observed frequency vs predicted probability. Also computes Brier score (MSE of predictions).
 */

#include <vector>
#include <random>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <utility>

std::pair<std::vector<double>, std::vector<int>> generate_well_calibrated_data(int n, std::mt19937& rng) {
    /* Generate synthetic data where predicted probabilities match true frequencies. */
    std::uniform_real_distribution<double> uniform(0.0, 1.0);
    std::vector<double> scores;
    std::vector<int> labels;
    scores.reserve(n);
    labels.reserve(n);

    for (int i = 0; i < n; ++i) {
        double score = uniform(rng);
        int label = (uniform(rng) < score) ? 1 : 0;
        scores.push_back(score);
        labels.push_back(label);
    }
    return {scores, labels};
}

std::pair<std::vector<double>, std::vector<int>> generate_overconfident_data(int n, std::mt19937& rng) {
    /* Generate overconfident predictions (predicted prob >> observed freq). */
    std::uniform_real_distribution<double> uniform(0.0, 1.0);
    std::vector<double> scores;
    std::vector<int> labels;
    scores.reserve(n);
    labels.reserve(n);

    for (int i = 0; i < n; ++i) {
        double raw = uniform(rng);
        double score;
        if (raw < 0.3) {
            score = uniform(rng) * 0.2;
        } else if (raw < 0.7) {
            score = 0.4 + uniform(rng) * 0.2;
        } else {
            score = 0.8 + uniform(rng) * 0.2;
        }
        int label = (uniform(rng) < 0.5) ? 1 : 0;
        scores.push_back(score);
        labels.push_back(label);
    }
    return {scores, labels};
}

struct CalibrationResult {
    std::vector<double> bin_centers;
    std::vector<double> predicted_probs;
    std::vector<double> observed_freqs;
};

CalibrationResult calibration_curve(
    const std::vector<double>& scores,
    const std::vector<int>& labels,
    int n_bins = 5
) {
    /* Compute calibration curve: bin scores, compute observed and predicted frequencies. */
    CalibrationResult result;

    for (int i = 0; i < n_bins; ++i) {
        double lo = static_cast<double>(i) / n_bins;
        double hi = static_cast<double>(i + 1) / n_bins;

        std::vector<int> indices;
        for (size_t j = 0; j < scores.size(); ++j) {
            if ((lo <= scores[j] && scores[j] < hi) || (j == scores.size() - 1 && scores[j] == 1.0)) {
                indices.push_back(static_cast<int>(j));
            }
        }

        if (indices.empty()) continue;

        result.bin_centers.push_back((lo + hi) / 2.0);

        double sum_score = 0.0;
        double sum_label = 0.0;
        for (int idx : indices) {
            sum_score += scores[idx];
            sum_label += labels[idx];
        }
        result.predicted_probs.push_back(sum_score / indices.size());
        result.observed_freqs.push_back(sum_label / indices.size());
    }

    return result;
}

double brier_score(const std::vector<double>& scores, const std::vector<int>& labels) {
    /* Brier score: MSE between predicted probabilities and actual labels. */
    double sum = 0.0;
    for (size_t i = 0; i < scores.size(); ++i) {
        double diff = scores[i] - labels[i];
        sum += diff * diff;
    }
    return sum / scores.size();
}

double calibration_error(const std::vector<double>& predicted, const std::vector<double>& observed) {
    /* Expected Calibration Error (ECE): mean |predicted - observed| across bins. */
    if (predicted.empty()) return 0.0;
    double sum = 0.0;
    for (size_t i = 0; i < predicted.size(); ++i) {
        sum += std::abs(predicted[i] - observed[i]);
    }
    return sum / predicted.size();
}

int main() {
    std::mt19937 rng(42);

    // Well-calibrated model
    auto [scores_good, labels_good] = generate_well_calibrated_data(500, rng);
    auto cal_good = calibration_curve(scores_good, labels_good, 5);
    double ece_good = calibration_error(cal_good.predicted_probs, cal_good.observed_freqs);
    double brier_good = brier_score(scores_good, labels_good);

    // Overconfident model
    auto [scores_bad, labels_bad] = generate_overconfident_data(500, rng);
    auto cal_bad = calibration_curve(scores_bad, labels_bad, 5);
    double ece_bad = calibration_error(cal_bad.predicted_probs, cal_bad.observed_freqs);
    double brier_bad = brier_score(scores_bad, labels_bad);

    // Verify: well-calibrated should have lower ECE and lower Brier
    assert(ece_good < ece_bad);
    assert(brier_good < brier_bad);

    std::cout << "calibration_curve.cpp PASS" << std::endl;
    return 0;
}
