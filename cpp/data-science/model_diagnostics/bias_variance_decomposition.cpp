// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Bias-Variance Decomposition
 * 
 * Estimates bias and variance of a model using bootstrap resampling on synthetic data.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>
#include <tuple>

std::vector<double> generate_synthetic_data(int n, std::mt19937& rng) {
    /* Generate y = 0.5 + 0.1*x^2 + noise. Returns interleaved [x0,y0,x1,y1,...] */
    std::uniform_real_distribution<double> uniform_x(-3.0, 3.0);
    std::normal_distribution<double> normal(0.0, 0.2);
    
    std::vector<double> data;
    data.reserve(n * 2);
    for (int i = 0; i < n; ++i) {
        double x = uniform_x(rng);
        double y = 0.5 + 0.1 * x * x + normal(rng);
        data.push_back(x);
        data.push_back(y);
    }
    return data;
}

std::vector<double> polyfit(const std::vector<double>& x_list, const std::vector<double>& y_list, int degree) {
    /* Fit polynomial of given degree using least squares (normal equations). */
    int n = static_cast<int>(x_list.size());
    if (n <= degree) {
        return std::vector<double>(degree + 1, 0.0);
    }

    if (degree == 0) {
        double mean_y = 0.0;
        for (double y : y_list) mean_y += y;
        return {mean_y / n};
    } else if (degree == 1) {
        double x_mean = 0.0, y_mean = 0.0;
        for (double x : x_list) x_mean += x;
        for (double y : y_list) y_mean += y;
        x_mean /= n;
        y_mean /= n;

        double num = 0.0, den = 0.0;
        for (int i = 0; i < n; ++i) {
            num += (x_list[i] - x_mean) * (y_list[i] - y_mean);
            den += (x_list[i] - x_mean) * (x_list[i] - x_mean);
        }
        double a1 = (den != 0.0) ? num / den : 0.0;
        double a0 = y_mean - a1 * x_mean;
        return {a0, a1};
    } else if (degree == 2) {
        double sx0 = n, sx1 = 0.0, sx2 = 0.0, sx3 = 0.0, sx4 = 0.0;
        double sy = 0.0, sxy = 0.0, sx2y = 0.0;
        for (int i = 0; i < n; ++i) {
            double x = x_list[i], y = y_list[i];
            double x2 = x * x, x3 = x2 * x, x4 = x3 * x;
            sx1 += x; sx2 += x2; sx3 += x3; sx4 += x4;
            sy += y; sxy += x * y; sx2y += x2 * y;
        }

        double det = sx0 * (sx2 * sx4 - sx3 * sx3) 
                   - sx1 * (sx1 * sx4 - sx3 * sx2) 
                   + sx2 * (sx1 * sx3 - sx2 * sx2);

        if (std::abs(det) < 1e-10) {
            return {0.0, 0.0, 0.0};
        }

        double a0 = (sy * (sx2 * sx4 - sx3 * sx3) 
                   - sxy * (sx1 * sx4 - sx3 * sx2) 
                   + sx2y * (sx1 * sx3 - sx2 * sx2)) / det;
        double a1 = (sx0 * (sxy * sx4 - sx3 * sx2y) 
                   - sy * (sx1 * sx4 - sx3 * sx2) 
                   + sx2 * (sx1 * sx3 - sx2 * sx2)) / det;  // Fixed: was sx2y, should be sx2
        double a2 = (sx0 * (sx2 * sx2y - sx3 * sxy) 
                   - sx1 * (sx1 * sx2y - sx3 * sy) 
                   + sy * (sx1 * sx3 - sx2 * sx2)) / det;
        return {a0, a1, a2};
    } else {
        return std::vector<double>(degree + 1, 0.0);
    }
}

double evaluate_poly(double x, const std::vector<double>& coeffs) {
    /* Evaluate polynomial at x. */
    double result = 0.0;
    double x_pow = 1.0;
    for (double coeff : coeffs) {
        result += coeff * x_pow;
        x_pow *= x;
    }
    return result;
}

std::tuple<double, double, double> bootstrap_bias_variance(
    const std::vector<double>& train_data,
    const std::vector<double>& test_x,
    int degree,
    int n_bootstraps,
    std::mt19937& rng
) {
    /* Bootstrap bias-variance decomposition. Returns (bias, variance, mse). */
    int n_train = static_cast<int>(train_data.size()) / 2;
    std::vector<std::vector<double>> predictions_list;
    predictions_list.reserve(n_bootstraps);

    std::uniform_int_distribution<int> uniform(0, n_train - 1);

    for (int b = 0; b < n_bootstraps; ++b) {
        // Resample train data with replacement
        std::vector<double> boot_x, boot_y;
        boot_x.reserve(n_train);
        boot_y.reserve(n_train);
        for (int i = 0; i < n_train; ++i) {
            int idx = uniform(rng);
            boot_x.push_back(train_data[idx * 2]);
            boot_y.push_back(train_data[idx * 2 + 1]);
        }

        // Fit model
        auto coeffs = polyfit(boot_x, boot_y, degree);

        // Predict on test set
        std::vector<double> pred;
        pred.reserve(test_x.size());
        for (double x : test_x) {
            pred.push_back(evaluate_poly(x, coeffs));
        }
        predictions_list.push_back(pred);
    }

    // Compute bias and variance
    int n_test = static_cast<int>(test_x.size());
    double bias_sq_sum = 0.0, var_sum = 0.0;

    for (int i = 0; i < n_test; ++i) {
        std::vector<double> pred_at_i;
        pred_at_i.reserve(n_bootstraps);
        for (const auto& preds : predictions_list) {
            pred_at_i.push_back(preds[i]);
        }

        double mean_pred = 0.0;
        for (double p : pred_at_i) mean_pred += p;
        mean_pred /= n_bootstraps;

        // True value at test_x[i] is 0.5 + 0.1*x^2
        double true_y = 0.5 + 0.1 * test_x[i] * test_x[i];
        bias_sq_sum += (mean_pred - true_y) * (mean_pred - true_y);

        // Variance: E[(pred - mean_pred)^2]
        double var_at_i = 0.0;
        for (double p : pred_at_i) {
            var_at_i += (p - mean_pred) * (p - mean_pred);
        }
        var_sum += var_at_i / n_bootstraps;
    }

    double bias = std::sqrt(bias_sq_sum / n_test);
    double variance = var_sum / n_test;
    return {bias, variance, bias * bias + variance};
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform_x(-3.0, 3.0);

    auto train_data = generate_synthetic_data(100, rng);
    std::vector<double> test_x(50);
    for (int i = 0; i < 50; ++i) {
        test_x[i] = uniform_x(rng);
    }

    // Constant model (high bias)
    auto [bias_c, var_c, mse_c] = bootstrap_bias_variance(train_data, test_x, 0, 50, rng);

    // Linear model (medium bias)
    // Need to reset rng for fair comparison
    std::mt19937 rng2(42);
    auto [bias_l, var_l, mse_l] = bootstrap_bias_variance(train_data, test_x, 1, 50, rng2);

    // Verify patterns: constant should have much higher bias than linear
    assert(bias_c > bias_l);
    assert(bias_c > 0.25);

    std::cout << "bias_variance_decomposition.cpp: PASS" << std::endl;
    return 0;
}
