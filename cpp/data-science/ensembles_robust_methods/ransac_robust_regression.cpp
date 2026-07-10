// ransac_robust_regression.cpp — RANSAC robust line fitting vs OLS.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <random>
#include <utility>
#include <vector>

static std::pair<double, double> fit_line_2point(double x1, double y1,
                                                 double x2, double y2) {
    if (std::abs(x2 - x1) < 1e-10) return {1e6, y1};
    double m = (y2 - y1) / (x2 - x1);
    double b = y1 - m * x1;
    return {m, b};
}

static inline double predict_line(double x, double m, double b) {
    return m * x + b;
}

static inline double residual_distance(double y_true, double y_pred) {
    return std::abs(y_true - y_pred);
}

static std::pair<double, double> ransac_regression(const std::vector<double>& X,
                                                   const std::vector<double>& y,
                                                   int n_iterations,
                                                   double threshold,
                                                   std::mt19937& rng) {
    int n = static_cast<int>(X.size());
    double best_m = 0.0, best_b = 0.0;
    int best_inliers = 0;
    if (n < 2) return {0.0, 0.0};

    std::uniform_int_distribution<int> pick(0, n - 1);
    for (int it = 0; it < n_iterations; ++it) {
        int i1 = pick(rng);
        int i2 = pick(rng);
        while (i2 == i1) i2 = pick(rng);
        auto [m, b] = fit_line_2point(X[i1], y[i1], X[i2], y[i2]);
        int inliers = 0;
        for (int i = 0; i < n; ++i) {
            double pred = predict_line(X[i], m, b);
            if (residual_distance(y[i], pred) <= threshold) ++inliers;
        }
        if (inliers > best_inliers) {
            best_inliers = inliers;
            best_m = m;
            best_b = b;
        }
    }
    return {best_m, best_b};
}

static std::pair<double, double> ordinary_least_squares(const std::vector<double>& X,
                                                      const std::vector<double>& y) {
    int n = static_cast<int>(X.size());
    double mean_x = std::accumulate(X.begin(), X.end(), 0.0) / n;
    double mean_y = std::accumulate(y.begin(), y.end(), 0.0) / n;
    double num = 0.0, den = 0.0;
    for (int i = 0; i < n; ++i) {
        num += (X[i] - mean_x) * (y[i] - mean_y);
        den += (X[i] - mean_x) * (X[i] - mean_x);
    }
    if (den < 1e-10) return {0.0, mean_y};
    double m = num / den;
    return {m, mean_y - m * mean_x};
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> xdist(0.0, 10.0);
    std::normal_distribution<double> noise(0.0, 0.5);
    std::uniform_real_distribution<double> outlier_y(-10.0, 30.0);

    std::vector<double> X, y;
    int n_inliers = 50;
    for (int i = 0; i < n_inliers; ++i) {
        double x = xdist(rng);
        X.push_back(x);
        y.push_back(2.0 * x + 1.0 + noise(rng));
    }
    int n_outliers = static_cast<int>(0.3 * n_inliers);
    for (int i = 0; i < n_outliers; ++i) {
        double x = xdist(rng);
        X.push_back(x);
        y.push_back(outlier_y(rng));
    }

    auto [m_ols, b_ols] = ordinary_least_squares(X, y);
    auto [m_ransac, b_ransac] = ransac_regression(X, y, 200, 1.0, rng);

    double true_m = 2.0;
    double ols_error = std::abs(m_ols - true_m);
    double ransac_error = std::abs(m_ransac - true_m);

    std::printf("ransac_robust_regression: ols_slope_error=%.4f, ransac_slope_error=%.4f\n",
                ols_error, ransac_error);
    assert(ransac_error < ols_error);
    std::printf("PASS\n");
    return 0;
}
