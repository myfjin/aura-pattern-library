// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Autoregressive (AR) Model
 * 
 * Fit an AR(p) model by regressing y_t on its p lagged values using least squares.
 * Solves the normal equations directly (no external libraries). Produces one-step-ahead
 * forecasts. Use for univariate time series prediction when past values predict the future.
 */

#include <vector>
#include <cmath>
#include <stdexcept>
#include <random>
#include <cassert>
#include <iostream>

std::pair<double, double> solve_2x2(double a, double b, double c, double d, double e, double f) {
    /* Solve 2x2 linear system: a*x + b*y = e, c*x + d*y = f. */
    double det = a * d - b * c;
    if (std::abs(det) < 1e-10) {
        throw std::invalid_argument("Singular matrix");
    }
    double x = (e * d - b * f) / det;
    double y = (a * f - e * c) / det;
    return {x, y};
}

std::vector<double> ar_fit(const std::vector<double>& series, int p) {
    /*
     * Fit AR(p) model: y_t = c + phi_1*y_{t-1} + ... + phi_p*y_{t-p} + noise
     * Returns coefficients [c, phi_1, ..., phi_p]
     * Uses least squares by solving normal equations.
     * For simplicity, we implement p=1 and p=2 explicitly.
     */
    if (p < 1 || p >= static_cast<int>(series.size())) {
        throw std::invalid_argument("p must be 1 <= p < len(series)");
    }

    // Center the series
    double sum = 0.0;
    for (const auto& s : series) {
        sum += s;
    }
    double mean = sum / series.size();

    std::vector<double> centered;
    centered.reserve(series.size());
    for (const auto& s : series) {
        centered.push_back(s - mean);
    }

    if (p == 1) {
        // y_t = phi_1 * y_{t-1} + noise (centered)
        // Minimize sum((y_t - phi_1 * y_{t-1})^2)
        // Normal eq: phi_1 * sum(y_{t-1}^2) = sum(y_{t-1} * y_t)
        double sum_y2_prev = 0.0;
        double sum_prod = 0.0;
        for (size_t i = 0; i < centered.size() - 1; ++i) {
            sum_y2_prev += centered[i] * centered[i];
            sum_prod += centered[i] * centered[i + 1];
        }
        double phi_1 = (std::abs(sum_y2_prev) < 1e-10) ? 0.0 : sum_prod / sum_y2_prev;
        return {mean, phi_1};
    } else if (p == 2) {
        // y_t = phi_1 * y_{t-1} + phi_2 * y_{t-2} + noise
        // Normal equations (2x2 system)
        int n = static_cast<int>(centered.size());
        double sum_y1_sq = 0.0, sum_y2_sq = 0.0, sum_y1_y2 = 0.0;
        double sum_y1_y = 0.0, sum_y2_y = 0.0;
        for (int i = 0; i < n - 2; ++i) {
            sum_y1_sq += centered[i] * centered[i];
            sum_y2_sq += centered[i + 1] * centered[i + 1];
            sum_y1_y2 += centered[i] * centered[i + 1];
            sum_y1_y += centered[i] * centered[i + 2];
            sum_y2_y += centered[i + 1] * centered[i + 2];
        }

        // [sum_y1_sq   sum_y1_y2] [phi_1]   [sum_y1_y]
        // [sum_y1_y2   sum_y2_sq] [phi_2] = [sum_y2_y]
        auto [phi_1, phi_2] = solve_2x2(
            sum_y1_sq, sum_y1_y2, sum_y1_y2, sum_y2_sq, sum_y1_y, sum_y2_y
        );
        return {mean, phi_1, phi_2};
    } else {
        throw std::invalid_argument("Only p=1 and p=2 implemented");
    }
}

std::vector<double> ar_forecast_one_step(const std::vector<double>& series, const std::vector<double>& coeffs) {
    /* One-step-ahead forecasts: y_hat_t = c + phi_1*y_{t-1} + ... */
    int p = static_cast<int>(coeffs.size()) - 1;
    double mean = coeffs[0];
    std::vector<double> phis(coeffs.begin() + 1, coeffs.end());
    
    std::vector<double> forecasts;
    forecasts.reserve(series.size() - p);
    for (int t = p; t < static_cast<int>(series.size()); ++t) {
        double yhat = mean;
        for (int i = 0; i < p; ++i) {
            yhat += phis[i] * series[t - i - 1];
        }
        forecasts.push_back(yhat);
    }
    return forecasts;
}

double compute_mae(const std::vector<double>& actual, const std::vector<double>& predicted) {
    /* Mean absolute error. */
    if (actual.size() != predicted.size()) {
        throw std::invalid_argument("Length mismatch");
    }
    double sum = 0.0;
    for (size_t i = 0; i < actual.size(); ++i) {
        sum += std::abs(actual[i] - predicted[i]);
    }
    return sum / actual.size();
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> normal(0.0, 1.0);

    // Generate AR(1) series: y_t = 0.7 * y_{t-1} + noise
    std::vector<double> series;
    series.push_back(10.0);
    for (int i = 0; i < 100; ++i) {
        series.push_back(0.7 * series.back() + normal(rng));
    }

    // Fit AR(1)
    auto coeffs_1 = ar_fit(series, 1);
    assert(coeffs_1.size() == 2);  // AR(1) should have 2 coefficients
    // Estimated phi should be close to 0.7
    assert(coeffs_1[1] > 0.5 && coeffs_1[1] < 0.9);

    // One-step forecasts
    auto fcst_1 = ar_forecast_one_step(series, coeffs_1);
    assert(fcst_1.size() == series.size() - 1);

    // Naive baseline: predict mean
    double sum = 0.0;
    for (const auto& s : series) {
        sum += s;
    }
    double mean_series = sum / series.size();
    std::vector<double> naive_fcst(series.size() - 1, mean_series);
    std::vector<double> actual_values(series.begin() + 1, series.end());

    double mae_ar = compute_mae(actual_values, fcst_1);
    double mae_naive = compute_mae(actual_values, naive_fcst);
    assert(mae_ar < mae_naive);  // AR should beat naive mean

    // Fit AR(2)
    auto coeffs_2 = ar_fit(series, 2);
    assert(coeffs_2.size() == 3);  // AR(2) should have 3 coefficients
    auto fcst_2 = ar_forecast_one_step(series, coeffs_2);
    assert(fcst_2.size() == series.size() - 2);

    std::cout << "autoregressive_model.cpp PASS" << std::endl;
    return 0;
}
