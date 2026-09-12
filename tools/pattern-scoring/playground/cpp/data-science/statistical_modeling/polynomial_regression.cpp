// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Polynomial least-squares regression: builds a Vandermonde matrix and solves the
normal equations (V^T V) c = V^T y via Gaussian elimination with partial
pivoting. Use to fit a degree-d polynomial to 1-D data with only the stdlib.
Guarantees: recovers known quadratic coefficients within 0.2 from noisy data, a
degree-2 fit beats degree-1 on MSE, and the pivot assert catches a singular /
near-zero pivot column (degenerate design matrix).
*/
#include <cassert>
#include <cmath>
#include <cstddef>
#include <iostream>
#include <random>
#include <vector>

std::vector<double> gaussian_elimination(std::vector<std::vector<double>> A, std::vector<double> b) {
    std::size_t n = A.size();
    for (std::size_t col = 0; col < n; ++col) {
        std::size_t max_row = col;
        for (std::size_t row = col + 1; row < n; ++row) {
            if (std::abs(A[row][col]) > std::abs(A[max_row][col])) {
                max_row = row;
            }
        }
        std::swap(A[col], A[max_row]);
        std::swap(b[col], b[max_row]);

        assert(std::abs(A[col][col]) > 1e-12);

        for (std::size_t row = col + 1; row < n; ++row) {
            double factor = A[row][col] / A[col][col];
            for (std::size_t j = col; j < n; ++j) {
                A[row][j] -= factor * A[col][j];
            }
            b[row] -= factor * b[col];
        }
    }

    std::vector<double> x(n, 0.0);
    for (int i = static_cast<int>(n) - 1; i >= 0; --i) {
        x[i] = b[i];
        for (std::size_t j = i + 1; j < n; ++j) {
            x[i] -= A[i][j] * x[j];
        }
        x[i] /= A[i][i];
    }
    return x;
}

std::vector<std::vector<double>> vandermonde_matrix(const std::vector<double>& x_vals, int degree) {
    std::size_t n = x_vals.size();
    std::vector<std::vector<double>> V(n, std::vector<double>(degree + 1));
    for (std::size_t i = 0; i < n; ++i) {
        double power = 1.0;
        for (int j = 0; j <= degree; ++j) {
            V[i][j] = power;
            power *= x_vals[i];
        }
    }
    return V;
}

std::vector<double> fit_polynomial(const std::vector<double>& x_vals, const std::vector<double>& y_vals, int degree) {
    auto V = vandermonde_matrix(x_vals, degree);
    int n_cols = degree + 1;
    std::vector<std::vector<double>> VtV(n_cols, std::vector<double>(n_cols, 0.0));
    std::vector<double> Vty(n_cols, 0.0);
    for (int j = 0; j < n_cols; ++j) {
        for (int k = 0; k < n_cols; ++k) {
            double sum = 0.0;
            for (std::size_t i = 0; i < x_vals.size(); ++i) {
                sum += V[i][j] * V[i][k];
            }
            VtV[j][k] = sum;
        }
        double sum = 0.0;
        for (std::size_t i = 0; i < x_vals.size(); ++i) {
            sum += V[i][j] * y_vals[i];
        }
        Vty[j] = sum;
    }
    return gaussian_elimination(VtV, Vty);
}

double eval_poly(const std::vector<double>& coeffs, double x) {
    double result = 0.0;
    double power = 1.0;
    for (double c : coeffs) {
        result += c * power;
        power *= x;
    }
    return result;
}

double mse(const std::vector<double>& y_true, const std::vector<double>& y_pred) {
    double sum = 0.0;
    for (std::size_t i = 0; i < y_true.size(); ++i) {
        double diff = y_true[i] - y_pred[i];
        sum += diff * diff;
    }
    return sum / y_true.size();
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> noise(0.0, 0.1);

    std::vector<double> true_coeffs = {2.0, 3.0, 0.5};
    std::vector<double> x_vals;
    std::vector<double> y_vals;
    for (int i = 0; i < 20; ++i) {
        double x = i * 0.5;
        x_vals.push_back(x);
        y_vals.push_back(eval_poly(true_coeffs, x) + noise(gen));
    }

    auto fitted_coeffs_2 = fit_polynomial(x_vals, y_vals, 2);
    auto fitted_coeffs_1 = fit_polynomial(x_vals, y_vals, 1);

    std::vector<double> y_pred_2, y_pred_1;
    for (double x : x_vals) {
        y_pred_2.push_back(eval_poly(fitted_coeffs_2, x));
        y_pred_1.push_back(eval_poly(fitted_coeffs_1, x));
    }

    double mse_2 = mse(y_vals, y_pred_2);
    double mse_1 = mse(y_vals, y_pred_1);

    for (std::size_t i = 0; i < true_coeffs.size(); ++i) {
        assert(std::abs(true_coeffs[i] - fitted_coeffs_2[i]) < 0.2);
    }
    assert(mse_2 < mse_1);

    std::cout << "polynomial_regression.cpp: fitted_coeffs=[";
    for (std::size_t i = 0; i < fitted_coeffs_2.size(); ++i) {
        if (i) std::cout << ", ";
        std::cout << fitted_coeffs_2[i];
    }
    std::cout << "], mse_2=" << mse_2 << ", mse_1=" << mse_1 << " PASS" << std::endl;
    return 0;
}
