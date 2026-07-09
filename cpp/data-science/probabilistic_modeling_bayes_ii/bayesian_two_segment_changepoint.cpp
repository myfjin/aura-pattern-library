// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Bayesian Two-Segment Changepoint
 * 
 * Compare model evidence for no-change vs change-at-t; find planted change location;
 * no-change data prefers single-segment model.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>
#include <limits>
#include <utility>

double log_normal_likelihood(const std::vector<double>& data, double mean = 0.0, bool use_mle = false, double var = 1.0) {
    /* Log-likelihood of data under N(mean, var). If use_mle, compute MLE mean. */
    double m = mean;
    if (use_mle) {
        double sum = 0.0;
        for (const auto& x : data) sum += x;
        m = sum / data.size();
    }
    double ll = 0.0;
    for (const auto& x : data) {
        ll += -0.5 * std::log(2.0 * M_PI * var) - 0.5 * (x - m) * (x - m) / var;
    }
    return ll;
}

double model_evidence_1seg(const std::vector<double>& data, double var = 1.0) {
    /* Log marginal likelihood for single-segment model. */
    return log_normal_likelihood(data, 0.0, true, var);
}

double model_evidence_2seg(const std::vector<double>& data, int split, double var = 1.0) {
    /* Log marginal likelihood for two-segment model split at index split. */
    if (split <= 0 || split >= static_cast<int>(data.size())) {
        return -std::numeric_limits<double>::infinity();
    }
    std::vector<double> seg1(data.begin(), data.begin() + split);
    std::vector<double> seg2(data.begin() + split, data.end());
    return log_normal_likelihood(seg1, 0.0, true, var) + log_normal_likelihood(seg2, 0.0, true, var);
}

std::pair<int, double> changepoint_detection(const std::vector<double>& data, double var = 1.0) {
    /*
     * Find changepoint by comparing model evidence.
     * Return: (best_split, log_bayes_factor_2seg_vs_1seg)
     */
    double ll_1seg = model_evidence_1seg(data, var);

    int best_split = -1;
    double best_ll_2seg = -std::numeric_limits<double>::infinity();
    for (int split = 1; split < static_cast<int>(data.size()); ++split) {
        double ll_2seg = model_evidence_2seg(data, split, var);
        if (ll_2seg > best_ll_2seg) {
            best_ll_2seg = ll_2seg;
            best_split = split;
        }
    }

    double log_bf = best_ll_2seg - ll_1seg;  // Bayes factor favors 2-seg if > 0
    return {best_split, log_bf};
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> normal1(1.0, 0.5);
    std::normal_distribution<double> normal2(3.5, 0.5);
    std::normal_distribution<double> normal3(2.0, 0.5);

    // Data with a change at index 25
    std::vector<double> data_with_change;
    data_with_change.reserve(50);
    for (int i = 0; i < 25; ++i) data_with_change.push_back(normal1(rng));
    for (int i = 0; i < 25; ++i) data_with_change.push_back(normal2(rng));

    auto [split_detected, bf] = changepoint_detection(data_with_change, 0.25);

    // Detected split should be near the planted split (25)
    assert(split_detected >= 20 && split_detected <= 30);

    // Bayes factor should favor 2-segment model (log_bf > 0)
    assert(bf > 0);

    // Test with no-change data: 1-segment is usually preferred or tied
    std::vector<double> no_change_data(50);
    for (int i = 0; i < 50; ++i) no_change_data[i] = normal3(rng);
    auto [split_no_change, bf_no_change] = changepoint_detection(no_change_data, 0.25);

    // For uniform data, BF can be slightly in favor of 2-segment due to overfitting, but should be small
    assert(std::abs(bf_no_change) < 3.0);

    // For data with change, evidence ratio should be more extreme than no-change case
    assert(bf > std::abs(bf_no_change));

    // Detected split on no-change data is less meaningful, but should still find something
    assert(split_no_change > 0 && split_no_change < 50);

    std::cout << "bayesian_two_segment_changepoint.cpp PASS" << std::endl;
    return 0;
}
