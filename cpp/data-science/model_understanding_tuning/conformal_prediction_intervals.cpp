// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Split-Conformal Prediction Intervals for Regression
 * 
 * Split data into train/calibration. Train a regression model, then on calibration
 * data compute residuals to set interval width such that coverage is guaranteed.
 */

#include <vector>
#include <random>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>

std::pair<double, double> simple_linear_model(const std::vector<double>& X, const std::vector<double>& y) {
    /* Fit y = a + b*x via least squares. */
    int n = static_cast<int>(X.size());
    double x_mean = 0.0, y_mean = 0.0;
    for (int i = 0; i < n; ++i) {
        x_mean += X[i];
        y_mean += y[i];
    }
    x_mean /= n;
    y_mean /= n;

    double num = 0.0, den = 1e-8;
    for (int i = 0; i < n; ++i) {
        num += (X[i] - x_mean) * (y[i] - y_mean);
        den += (X[i] - x_mean) * (X[i] - x_mean);
    }
    double b = num / den;
    double a = y_mean - b * x_mean;
    return {a, b};
}

double predict(double x, const std::pair<double, double>& params) {
    return params.first + params.second * x;
}

std::pair<std::pair<double, double>, double> split_conformal_intervals(
    const std::vector<double>& X_train, const std::vector<double>& y_train,
    const std::vector<double>& X_cal, const std::vector<double>& y_cal,
    double confidence = 0.9
) {
    /* Fit model on train, compute calibration residuals, set interval width. */
    auto params = simple_linear_model(X_train, y_train);

    // Compute calibration residuals
    std::vector<double> residuals;
    residuals.reserve(X_cal.size());
    for (size_t i = 0; i < X_cal.size(); ++i) {
        double pred = predict(X_cal[i], params);
        residuals.push_back(std::abs(y_cal[i] - pred));
    }

    // Sort residuals
    std::sort(residuals.begin(), residuals.end());
    int n_cal = static_cast<int>(residuals.size());

    // Ceiling of quantile index
    int quantile_idx = std::min(static_cast<int>(n_cal * confidence), n_cal - 1);

    return {params, residuals[quantile_idx]};
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform_x(-5.0, 5.0);
    std::normal_distribution<double> normal(0.0, 2.0);

    // Generate synthetic data: y = 5 + 2*x + noise
    std::vector<double> X_all, y_all;
    X_all.reserve(400);
    y_all.reserve(400);
    for (int i = 0; i < 400; ++i) {
        double x = uniform_x(rng);
        double y = 5.0 + 2.0 * x + normal(rng);
        X_all.push_back(x);
        y_all.push_back(y);
    }

    // Split: 150 train, 125 calibration, 125 test
    std::vector<double> X_train(X_all.begin(), X_all.begin() + 150);
    std::vector<double> y_train(y_all.begin(), y_all.begin() + 150);
    std::vector<double> X_cal(X_all.begin() + 150, X_all.begin() + 275);
    std::vector<double> y_cal(y_all.begin() + 150, y_all.begin() + 275);
    std::vector<double> X_test(X_all.begin() + 275, X_all.end());
    std::vector<double> y_test(y_all.begin() + 275, y_all.end());

    // Fit conformal predictor
    auto [params, half_width] = split_conformal_intervals(X_train, y_train, X_cal, y_cal, 0.9);

    // Generate intervals on test set
    int coverage_count = 0;
    double width_sum = 0.0;
    for (size_t i = 0; i < X_test.size(); ++i) {
        double pred = predict(X_test[i], params);
        double lower = pred - half_width, upper = pred + half_width;
        if (y_test[i] >= lower && y_test[i] <= upper) coverage_count++;
        width_sum += (upper - lower);
    }

    double coverage = static_cast<double>(coverage_count) / X_test.size();
    double avg_width = width_sum / X_test.size();

    // Assertion: coverage should be reasonable
    assert(coverage >= 0.70);
    assert(avg_width > 0.0 && avg_width < 100.0);

    std::cout << "Conformal Prediction Intervals: PASS" << std::endl;
    return 0;
}
