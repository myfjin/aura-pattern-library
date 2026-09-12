// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * LOESS-Lite: Locally Weighted Linear Regression.
 *
 * Oracle asserts:
 *   mse_loess < mse_linear
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <random>
#include <algorithm>

double tricube_weight(double u) {
    if (std::abs(u) > 1.0) return 0.0;
    return std::pow(1.0 - std::pow(std::abs(u), 3), 3);
}

double loess_point(const std::vector<double>& x_vals,
                   const std::vector<double>& y_vals,
                   double x_target,
                   double frac_nearest = 0.3) {
    int n = static_cast<int>(x_vals.size());
    int k = std::max(1, static_cast<int>(n * frac_nearest));

    std::vector<std::pair<double, int>> dists;
    for (int i = 0; i < n; ++i) dists.push_back({std::abs(x_vals[i] - x_target), i});
    std::sort(dists.begin(), dists.end());

    double max_dist = dists[k - 1].first;
    if (max_dist == 0.0) max_dist = 1.0;

    double sum_w = 0.0, sum_wx = 0.0, sum_wy = 0.0, sum_wxy = 0.0, sum_wx2 = 0.0;
    for (int i = 0; i < k; ++i) {
        int idx = dists[i].second;
        double w = tricube_weight(std::abs(x_vals[idx] - x_target) / max_dist);
        sum_w += w;
        sum_wx += w * x_vals[idx];
        sum_wy += w * y_vals[idx];
        sum_wxy += w * x_vals[idx] * y_vals[idx];
        sum_wx2 += w * x_vals[idx] * x_vals[idx];
    }
    if (sum_w == 0.0) return sum_wy / n;

    double mean_x = sum_wx / sum_w;
    double mean_y = sum_wy / sum_w;
    double denom = sum_wx2 - mean_x * sum_wx;
    if (std::abs(denom) < 1e-10) return mean_y;

    double slope = (sum_wxy - mean_x * sum_wy) / denom;
    double intercept = mean_y - slope * mean_x;
    return intercept + slope * x_target;
}

double mse(const std::vector<double>& y_true, const std::vector<double>& y_pred) {
    double s = 0.0;
    for (size_t i = 0; i < y_true.size(); ++i) s += (y_true[i] - y_pred[i]) * (y_true[i] - y_pred[i]);
    return s / y_true.size();
}

int main() {
    std::mt19937_64 rng(42);
    std::normal_distribution<double> nd(0.0, 0.3);
    int n = 60;
    std::vector<double> x_vals, y_vals, x_grid;
    for (int i = 0; i < n; ++i) {
        double x = i * M_PI / 15.0;
        x_vals.push_back(x);
        x_grid.push_back(x);
        y_vals.push_back(std::sin(x) + nd(rng));
    }

    std::vector<double> y_loess;
    for (double x : x_grid) y_loess.push_back(loess_point(x_vals, y_vals, x, 0.3));

    double sum_x = 0.0, sum_y = 0.0, sum_xy = 0.0, sum_x2 = 0.0;
    for (int i = 0; i < n; ++i) {
        sum_x += x_vals[i]; sum_y += y_vals[i];
        sum_xy += x_vals[i] * y_vals[i]; sum_x2 += x_vals[i] * x_vals[i];
    }
    double mean_x = sum_x / n, mean_y = sum_y / n;
    double slope = (sum_xy - mean_x * sum_y) / (sum_x2 - mean_x * sum_x);
    double intercept = mean_y - slope * mean_x;
    std::vector<double> y_linear;
    for (double x : x_vals) y_linear.push_back(intercept + slope * x);

    double mse_loess = mse(y_vals, y_loess);
    double mse_linear = mse(y_vals, y_linear);
    assert(mse_loess < mse_linear);

    std::cout << "loess_local_regression.cpp PASS" << std::endl;
    return 0;
}
