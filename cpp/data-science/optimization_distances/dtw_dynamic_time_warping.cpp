// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>
#include <limits>

double euclidean_distance(double a, double b) { return std::abs(a - b); }

std::pair<double, std::vector<std::pair<int, int>>> dtw_distance(const std::vector<double>& series1, const std::vector<double>& series2) {
    size_t n = series1.size();
    size_t m = series2.size();

    std::vector<std::vector<double>> cost(n + 1, std::vector<double>(m + 1, std::numeric_limits<double>::infinity()));
    cost[0][0] = 0.0;

    for (size_t i = 1; i <= n; ++i) {
        for (size_t j = 1; j <= m; ++j) {
            double dist = euclidean_distance(series1[i - 1], series2[j - 1]);
            cost[i][j] = dist + std::min({cost[i - 1][j], cost[i][j - 1], cost[i - 1][j - 1]});
        }
    }

    std::vector<std::pair<int, int>> alignment;
    int i = static_cast<int>(n);
    int j = static_cast<int>(m);
    while (i > 0 || j > 0) {
        if (i == 0) {
            --j;
        } else if (j == 0) {
            --i;
        } else {
            std::tuple<double, int, int> candidates[3] = {
                {cost[i - 1][j - 1], i - 1, j - 1},
                {cost[i - 1][j], i - 1, j},
                {cost[i][j - 1], i, j - 1}
            };
            auto best = candidates[0];
            for (int k = 1; k < 3; ++k) {
                if (std::get<0>(candidates[k]) < std::get<0>(best)) best = candidates[k];
            }
            i = std::get<1>(best);
            j = std::get<2>(best);
        }
        alignment.emplace_back(i, j);
    }
    std::reverse(alignment.begin(), alignment.end());
    return {cost[n][m], alignment};
}

int main() {
    std::vector<double> series_a = {1.0, 2.0, 3.0, 4.0, 5.0};
    std::vector<double> series_b = {1.0, 2.0, 3.0, 4.0, 5.0};

    auto identical_result = dtw_distance(series_a, series_b);
    double dtw_dist_identical = identical_result.first;
    (void)identical_result.second;
    assert(dtw_dist_identical == 0.0);

    std::vector<double> series_c = {1.0, 1.0, 2.0, 3.0, 3.0, 4.0, 5.0};
    std::vector<double> series_d = {1.0, 2.0, 3.0, 4.0, 5.0};

    auto warped_result = dtw_distance(series_c, series_d);
    double dtw_dist = warped_result.first;
    const auto& alignment = warped_result.second;
    assert(!alignment.empty());
    assert(dtw_dist >= 0.0);

    std::vector<double> series_x = {0.0, 1.0, 2.0};
    std::vector<double> series_y = {0.0, 1.0};

    double dtw_xy = dtw_distance(series_x, series_y).first;
    assert(dtw_xy >= 0.0);

    std::cout << "dtw_dynamic_time_warping.cpp: identical_dtw=" << dtw_dist_identical << " warped_dtw=" << dtw_dist << " PASS\n";
    return 0;
}
