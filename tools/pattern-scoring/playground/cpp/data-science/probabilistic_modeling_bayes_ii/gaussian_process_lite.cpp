// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Gaussian process regression (lite): RBF kernel, small n, direct Cholesky solve.
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <functional>
#include <utility>

double rbf_kernel(double x1, double x2, double length_scale = 1.0, double sigma = 1.0) {
    double dist_sq = (x1 - x2) * (x1 - x2);
    return sigma * sigma * std::exp(-dist_sq / (2.0 * length_scale * length_scale));
}

std::vector<double> cholesky_solve_simple(const std::vector<std::vector<double>>& A,
                                            const std::vector<double>& b) {
    int n = static_cast<int>(A.size());
    std::vector<std::vector<double>> L(n, std::vector<double>(n, 0.0));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            double s = 0.0;
            for (int k = 0; k < j; ++k) s += L[i][k] * L[j][k];
            if (i == j) {
                double val = A[i][i] - s;
                if (val < 0.0) val = 1e-6;
                L[i][j] = std::sqrt(val);
            } else {
                if (L[j][j] > 0.0) L[i][j] = (A[i][j] - s) / L[j][j];
            }
        }
    }

    std::vector<double> y(n, 0.0);
    for (int i = 0; i < n; ++i) {
        double s = 0.0;
        for (int j = 0; j < i; ++j) s += L[i][j] * y[j];
        y[i] = (L[i][i] != 0.0) ? (b[i] - s) / L[i][i] : 0.0;
    }

    std::vector<double> x(n, 0.0);
    for (int i = n - 1; i >= 0; --i) {
        double s = 0.0;
        for (int j = i + 1; j < n; ++j) s += L[j][i] * x[j];
        x[i] = (L[i][i] != 0.0) ? (y[i] - s) / L[i][i] : 0.0;
    }

    return x;
}

std::pair<std::vector<double>, std::vector<double>> gp_posterior(
    const std::vector<double>& X_train,
    const std::vector<double>& y_train,
    const std::vector<double>& X_test,
    double noise = 0.1,
    double length_scale = 1.0
) {
    int n_train = static_cast<int>(X_train.size());
    int n_test = static_cast<int>(X_test.size());

    std::vector<std::vector<double>> K_train(n_train, std::vector<double>(n_train));
    for (int i = 0; i < n_train; ++i) {
        for (int j = 0; j < n_train; ++j) {
            K_train[i][j] = rbf_kernel(X_train[i], X_train[j], length_scale) + (i == j ? noise : 0.0);
        }
    }

    auto alpha = cholesky_solve_simple(K_train, y_train);

    std::vector<double> means, upper_bounds;
    for (double x_test : X_test) {
        std::vector<double> k_test(n_train);
        for (int i = 0; i < n_train; ++i) {
            k_test[i] = rbf_kernel(x_test, X_train[i], length_scale);
        }

        double mean = 0.0;
        for (int i = 0; i < n_train; ++i) mean += k_test[i] * alpha[i];

        double var = rbf_kernel(x_test, x_test, length_scale);
        double ci_bound = mean + 2.0 * std::sqrt(var + noise + 0.1);

        means.push_back(mean);
        upper_bounds.push_back(ci_bound);
    }

    return {means, upper_bounds};
}

int main() {
    std::vector<double> X_train = {0.0, 0.5, 1.0, 1.5, 2.0, 2.5};
    std::vector<double> y_train = {-0.0288180659155857, 0.4448448185378991,
                                        0.8192078124943640, 1.1378917316238270,
                                        0.8837797700691042, 0.2990014612357650};

    std::vector<double> X_test;
    for (int i = 0; i < 13; ++i) X_test.push_back(i * 0.5);

    auto [means, upper_bounds] = gp_posterior(X_train, y_train, X_test, 0.05, 0.5);

    assert(means.size() == X_test.size());
    assert(upper_bounds.size() == X_test.size());

    // Training points should interpolate
    auto [X_train_pred, _] = gp_posterior(X_train, y_train, X_train, 0.05, 0.5);
    for (size_t i = 0; i < y_train.size(); ++i) {
        assert(std::abs(X_train_pred[i] - y_train[i]) < 0.5);
    }

    // CI contains mean
    for (size_t i = 0; i < means.size(); ++i) {
        assert(means[i] <= upper_bounds[i]);
    }

    int covered = 0;
    for (size_t i = 0; i < X_test.size(); ++i) {
        double half_width = upper_bounds[i] - means[i];
        if (std::abs(std::sin(X_test[i]) - means[i]) <= half_width) covered++;
    }
    double coverage = static_cast<double>(covered) / X_test.size();
    assert(coverage >= 0.85);

    std::cout << "gaussian_process_lite.cpp PASS" << std::endl;
    return 0;
}
