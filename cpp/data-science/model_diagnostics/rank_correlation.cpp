// rank_correlation.cpp — Spearman's rho and Kendall's tau.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <random>
#include <vector>

static std::vector<double> rank_data(const std::vector<double>& data) {
    int n = static_cast<int>(data.size());
    std::vector<int> indices(n);
    std::iota(indices.begin(), indices.end(), 0);
    std::sort(indices.begin(), indices.end(),
              [&](int a, int b) { return data[a] < data[b]; });

    std::vector<double> ranks(n, 0.0);
    int i = 0;
    while (i < n) {
        int j = i;
        while (j < n && data[indices[j]] == data[indices[i]]) ++j;
        double avg_rank = (i + j + 1) / 2.0;  // 1-indexed
        for (int k = i; k < j; ++k) ranks[indices[k]] = avg_rank;
        i = j;
    }
    return ranks;
}

static double spearman_correlation(const std::vector<double>& x,
                                   const std::vector<double>& y) {
    assert(x.size() == y.size());
    int n = static_cast<int>(x.size());
    auto rx = rank_data(x);
    auto ry = rank_data(y);

    double mx = std::accumulate(rx.begin(), rx.end(), 0.0) / n;
    double my = std::accumulate(ry.begin(), ry.end(), 0.0) / n;

    double num = 0.0, varx = 0.0, vary = 0.0;
    for (int i = 0; i < n; ++i) {
        double dx = rx[i] - mx;
        double dy = ry[i] - my;
        num += dx * dy;
        varx += dx * dx;
        vary += dy * dy;
    }
    if (varx == 0.0 || vary == 0.0) return 0.0;
    return num / std::sqrt(varx * vary);
}

static double kendall_tau(const std::vector<double>& x,
                          const std::vector<double>& y) {
    assert(x.size() == y.size());
    int n = static_cast<int>(x.size());
    int concordant = 0, discordant = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            double prod = (x[i] - x[j]) * (y[i] - y[j]);
            if (prod > 0) ++concordant;
            else if (prod < 0) ++discordant;
        }
    }
    int total = concordant + discordant;
    if (total == 0) return 0.0;
    return static_cast<double>(concordant - discordant) / total;
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform(0.0, 10.0);

    // Perfect monotone increasing
    std::vector<double> x_perfect = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::vector<double> y_perfect = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    double rho_perfect = spearman_correlation(x_perfect, y_perfect);
    double tau_perfect = kendall_tau(x_perfect, y_perfect);
    assert(std::abs(rho_perfect - 1.0) < 0.01);
    assert(std::abs(tau_perfect - 1.0) < 0.01);

    // Independent random data
    std::vector<double> x_random, y_random;
    for (int i = 0; i < 100; ++i) {
        x_random.push_back(uniform(rng));
        y_random.push_back(uniform(rng));
    }
    double rho_random = spearman_correlation(x_random, y_random);
    double tau_random = kendall_tau(x_random, y_random);
    assert(std::abs(rho_random) < 0.4);
    assert(std::abs(tau_random) < 0.4);

    // Perfect decreasing
    std::vector<double> x_dec = {1, 2, 3, 4, 5};
    std::vector<double> y_dec = {5, 4, 3, 2, 1};
    double rho_dec = spearman_correlation(x_dec, y_dec);
    double tau_dec = kendall_tau(x_dec, y_dec);
    assert(std::abs(rho_dec - (-1.0)) < 0.01);
    assert(std::abs(tau_dec - (-1.0)) < 0.01);

    std::printf("rank_correlation.cpp: PASS\n");
    return 0;
}
