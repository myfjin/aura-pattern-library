// OLS robust standard errors (White): correct inference under heteroskedasticity.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <cstddef>

struct OLSResult {
    std::vector<double> beta;
    std::vector<double> se_naive;
    std::vector<double> se_white;
};

OLSResult ols_fit(const std::vector<double>& y, const std::vector<std::vector<double>>& X) {
    std::size_t n = y.size();
    std::size_t p = X[0].size();

    // X^T X
    std::vector<std::vector<double>> XtX(p, std::vector<double>(p, 0.0));
    for (std::size_t a = 0; a < p; ++a) {
        for (std::size_t b = 0; b < p; ++b) {
            double s = 0.0;
            for (std::size_t i = 0; i < n; ++i) s += X[i][a] * X[i][b];
            XtX[a][b] = s;
        }
    }

    // (X^T X)^{-1} for p=2
    double det = XtX[0][0] * XtX[1][1] - XtX[0][1] * XtX[0][1];
    std::vector<std::vector<double>> XtX_inv(2, std::vector<double>(2));
    XtX_inv[0][0] =  XtX[1][1] / det;
    XtX_inv[0][1] = -XtX[0][1] / det;
    XtX_inv[1][0] = -XtX[1][0] / det;
    XtX_inv[1][1] =  XtX[0][0] / det;

    // X^T y
    std::vector<double> Xty(p, 0.0);
    for (std::size_t a = 0; a < p; ++a) {
        double s = 0.0;
        for (std::size_t i = 0; i < n; ++i) s += X[i][a] * y[i];
        Xty[a] = s;
    }

    // beta = (X^T X)^{-1} X^T y
    std::vector<double> beta(p, 0.0);
    for (std::size_t a = 0; a < p; ++a) {
        double s = 0.0;
        for (std::size_t b = 0; b < p; ++b) s += XtX_inv[a][b] * Xty[b];
        beta[a] = s;
    }

    // Residuals
    std::vector<double> residuals(n);
    for (std::size_t i = 0; i < n; ++i) {
        double pred = 0.0;
        for (std::size_t a = 0; a < p; ++a) pred += beta[a] * X[i][a];
        residuals[i] = y[i] - pred;
    }

    // Naive SE
    double ssq = 0.0;
    for (double r : residuals) ssq += r * r;
    double s2 = ssq / static_cast<double>(n - p);
    std::vector<double> se_naive(p);
    for (std::size_t a = 0; a < p; ++a) {
        se_naive[a] = std::sqrt(std::max(s2 * XtX_inv[a][a], 0.0));
    }

    // White sandwich: (X^T X)^{-1} X^T diag(e^2) X (X^T X)^{-1}
    std::vector<std::vector<double>> meat(p, std::vector<double>(p, 0.0));
    for (std::size_t a = 0; a < p; ++a) {
        for (std::size_t b = 0; b < p; ++b) {
            double s = 0.0;
            for (std::size_t i = 0; i < n; ++i) s += X[i][a] * residuals[i] * residuals[i] * X[i][b];
            meat[a][b] = s;
        }
    }

    std::vector<std::vector<double>> var_white(p, std::vector<double>(p, 0.0));
    for (std::size_t a = 0; a < p; ++a) {
        for (std::size_t b = 0; b < p; ++b) {
            double s = 0.0;
            for (std::size_t k = 0; k < p; ++k) {
                for (std::size_t l = 0; l < p; ++l) {
                    s += XtX_inv[a][k] * meat[k][l] * XtX_inv[l][b];
                }
            }
            var_white[a][b] = s;
        }
    }

    std::vector<double> se_white(p);
    for (std::size_t a = 0; a < p; ++a) {
        se_white[a] = std::sqrt(std::max(var_white[a][a], 0.0));
    }

    return {beta, se_naive, se_white};
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> x_dist(0.0, 2.0);

    std::size_t n = 200;
    std::vector<std::vector<double>> X(n, std::vector<double>(2));
    std::vector<double> y(n);

    for (std::size_t i = 0; i < n; ++i) {
        X[i][0] = 1.0;
        X[i][1] = x_dist(rng);
        double sigma = 1.0 + X[i][1] * X[i][1];
        std::normal_distribution<double> err_dist(0.0, sigma);
        y[i] = 2.0 + 1.0 * X[i][1] + err_dist(rng);
    }

    OLSResult res = ols_fit(y, X);

    assert(res.se_white[1] > 1.3 * res.se_naive[1]);
    for (double s : res.se_naive) assert(s > 0.0);
    for (double s : res.se_white) assert(s > 0.0);
    assert(res.beta[1] > 0.0 && res.beta[1] < 2.5);

    std::cout << "PASS" << std::endl;
    return 0;
}
