// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Hierarchical shrinkage (James-Stein): partial-pooling beats no-pooling on MSE.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>

std::vector<double> no_pooling_estimates(const std::vector<std::vector<double>>& groups) {
    std::vector<double> means;
    for (const auto& g : groups) {
        double sum = 0.0;
        for (double x : g) sum += x;
        means.push_back(sum / g.size());
    }
    return means;
}

std::vector<double> james_stein_estimates(const std::vector<std::vector<double>>& groups) {
    int K = static_cast<int>(groups.size());
    int n = static_cast<int>(groups[0].size());

    auto ybar = no_pooling_estimates(groups);

    double grand = 0.0;
    for (double y : ybar) grand += y;
    grand /= K;

    double within_sum = 0.0;
    int total_n = 0;
    for (int i = 0; i < K; ++i) {
        for (double x : groups[i]) {
            within_sum += (x - ybar[i]) * (x - ybar[i]);
        }
        total_n += groups[i].size();
    }
    double within = within_sum / total_n;
    double se2 = within / n;

    double ss = 0.0;
    for (double y : ybar) ss += (y - grand) * (y - grand);

    double shrink = (ss > 0.0) ? std::max(0.0, 1.0 - (K - 3) * se2 / ss) : 0.0;

    std::vector<double> result;
    for (int i = 0; i < K; ++i) {
        result.push_back(grand + shrink * (ybar[i] - grand));
    }
    return result;
}

int main() {
    std::mt19937 rng(1);
    std::normal_distribution<double> true_dist(50.0, 1.0);

    const int K = 12;
    const int n_per_group = 8;
    std::vector<double> true_means;
    for (int i = 0; i < K; ++i) true_means.push_back(true_dist(rng));

    std::vector<std::vector<double>> groups;
    for (int i = 0; i < K; ++i) {
        std::vector<double> g;
        std::normal_distribution<double> sample_dist(true_means[i], 8.0);
        for (int j = 0; j < n_per_group; ++j) g.push_back(sample_dist(rng));
        groups.push_back(g);
    }

    auto no_pool = no_pooling_estimates(groups);
    auto js = james_stein_estimates(groups);

    double mse_no_pool = 0.0, mse_js = 0.0;
    for (int i = 0; i < K; ++i) {
        double d1 = no_pool[i] - true_means[i];
        double d2 = js[i] - true_means[i];
        mse_no_pool += d1 * d1;
        mse_js += d2 * d2;
    }
    mse_no_pool /= K;
    mse_js /= K;

    assert(mse_js < mse_no_pool);
    assert(mse_js < 0.6 * mse_no_pool);

    std::cout << "hierarchical_shrinkage_2level.cpp PASS" << std::endl;
    return 0;
}
