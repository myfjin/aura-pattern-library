// Simulation Based Calibration (SBC): ranks should be uniform for a well-calibrated sampler.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <algorithm>

std::vector<int> simulateAndRank(int n_sims, int seed_offset) {
    std::vector<int> ranks;
    const int n_obs = 30;
    const int n_samples = 100;
    for (int sim = 0; sim < n_sims; ++sim) {
        std::mt19937 gen(42 + seed_offset + sim);
        std::normal_distribution<double> prior(0.0, 1.0);
        double theta_true = prior(gen);

        std::normal_distribution<double> likelihood(theta_true, 1.0);
        std::vector<double> data(n_obs);
        for (double& d : data) d = likelihood(gen);

        double y_mean = 0.0;
        for (double d : data) y_mean += d;
        y_mean /= n_obs;

        double posterior_var = 1.0 / (n_obs + 1.0);
        double posterior_mean = posterior_var * y_mean * n_obs;

        std::normal_distribution<double> post(posterior_mean, std::sqrt(posterior_var));
        int rank = 0;
        for (int i = 0; i < n_samples; ++i)
            if (post(gen) < theta_true)
                ++rank;
        ranks.push_back(rank);
    }
    return ranks;
}

double chiSqGof(const std::vector<int>& ranks, int n_samples) {
    int n_bins = std::min(10, n_samples / 5);
    double bin_size = static_cast<double>(n_samples + 1) / n_bins;
    std::vector<int> observed(n_bins, 0);
    for (int rank : ranks) {
        int bin_idx = std::min(static_cast<int>(rank / bin_size), n_bins - 1);
        ++observed[bin_idx];
    }
    double expected = static_cast<double>(ranks.size()) / n_bins;
    double chi_sq = 0.0;
    for (int o : observed)
        chi_sq += (o - expected) * (o - expected) / expected;
    return chi_sq;
}

int main() {
    auto ranks_correct = simulateAndRank(200, 0);
    double chi_correct = chiSqGof(ranks_correct, 100);

    // Biased sampler: simulate a biased posterior by shifting ranks toward extremes.
    auto ranks_base = simulateAndRank(200, 1000);
    std::mt19937 bias_gen(42);
    std::uniform_int_distribution<int> shift(-20, 20);
    std::vector<int> ranks_biased;
    for (int r : ranks_base) {
        int biased = r + shift(bias_gen) / 2; // weaker random shift
        // Also add a systematic outward nudge to create non-uniformity.
        if (biased < 50) biased -= 15; else biased += 15;
        ranks_biased.push_back(std::max(0, std::min(100, biased)));
    }
    double chi_biased = chiSqGof(ranks_biased, 100);

    std::cout << "SBC correct chi2=" << chi_correct << " biased chi2=" << chi_biased << "\n";
    assert(chi_correct < 30.0);
    assert(chi_biased > chi_correct);

    std::cout << "SBC_RANK_UNIFORMITY PASS\n";
    return 0;
}
