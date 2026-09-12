// Ridge Regression via Normal Equations (from scratch).
// w = (X^T X + λI)^(-1) X^T y.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <cassert>

using Matrix = std::vector<std::vector<double>>;
using Vec = std::vector<double>;

Matrix transpose(const Matrix& A) {
    if (A.empty()) return {};
    size_t m = A.size(), n = A[0].size();
    Matrix T(n, std::vector<double>(m));
    for (size_t i = 0; i < m; ++i)
        for (size_t j = 0; j < n; ++j)
            T[j][i] = A[i][j];
    return T;
}

Matrix multiply(const Matrix& A, const Matrix& B) {
    size_t m = A.size(), n = A[0].size(), p = B[0].size();
    Matrix R(m, std::vector<double>(p, 0.0));
    for (size_t i = 0; i < m; ++i)
        for (size_t j = 0; j < p; ++j)
            for (size_t k = 0; k < n; ++k)
                R[i][j] += A[i][k] * B[k][j];
    return R;
}

Vec matVecMul(const Matrix& A, const Vec& v) {
    Vec r(A.size(), 0.0);
    for (size_t i = 0; i < A.size(); ++i)
        for (size_t j = 0; j < v.size(); ++j)
            r[i] += A[i][j] * v[j];
    return r;
}

Matrix addIdentityScaled(const Matrix& A, double lambda_val) {
    Matrix R = A;
    for (size_t i = 0; i < A.size(); ++i)
        R[i][i] += lambda_val;
    return R;
}

Vec gaussianElimination(Matrix A, Vec b) {
    size_t n = A.size();
    for (size_t col = 0; col < n; ++col) {
        size_t maxRow = col;
        for (size_t row = col + 1; row < n; ++row)
            if (std::abs(A[row][col]) > std::abs(A[maxRow][col]))
                maxRow = row;
        std::swap(A[col], A[maxRow]);
        std::swap(b[col], b[maxRow]);
        for (size_t row = col + 1; row < n; ++row) {
            if (A[col][col] != 0.0) {
                double factor = A[row][col] / A[col][col];
                for (size_t j = col; j < n; ++j)
                    A[row][j] -= factor * A[col][j];
                b[row] -= factor * b[col];
            }
        }
    }
    Vec x(n, 0.0);
    for (int i = static_cast<int>(n) - 1; i >= 0; --i) {
        x[i] = b[i];
        for (size_t j = i + 1; j < n; ++j)
            x[i] -= A[i][j] * x[j];
        if (A[i][i] != 0.0)
            x[i] /= A[i][i];
    }
    return x;
}

Vec ridgeRegressionNormalEq(const Matrix& X, const Vec& y, double lambda_reg = 0.01) {
    Matrix XT = transpose(X);
    Matrix XTX = multiply(XT, X);
    Vec XTy = matVecMul(XT, y);
    Matrix XTX_reg = addIdentityScaled(XTX, lambda_reg);
    return gaussianElimination(XTX_reg, XTy);
}

int main() {
    std::mt19937 gen(42);
    std::uniform_real_distribution<double> xdist(-5.0, 5.0);
    std::normal_distribution<double> ndist(0.0, 0.5);

    const int n_samples = 30;
    const int n_features = 3;
    Matrix X(n_samples, std::vector<double>(n_features));
    for (int i = 0; i < n_samples; ++i)
        for (int j = 0; j < n_features; ++j)
            X[i][j] = xdist(gen);

    Vec true_w = {2.0, 3.0, -1.0};
    Vec y(n_samples);
    for (int i = 0; i < n_samples; ++i) {
        double sum = 0.0;
        for (int j = 0; j < n_features; ++j)
            sum += true_w[j] * X[i][j];
        y[i] = sum + ndist(gen);
    }

    Vec w = ridgeRegressionNormalEq(X, y, 0.01);
    Vec pred = matVecMul(X, w);

    double ss_res = 0.0, ymean = 0.0, ss_tot = 0.0;
    for (double v : y) ymean += v;
    ymean /= y.size();
    for (size_t i = 0; i < y.size(); ++i) {
        ss_res += (pred[i] - y[i]) * (pred[i] - y[i]);
        ss_tot += (y[i] - ymean) * (y[i] - ymean);
    }
    double r2 = ss_tot > 0.0 ? 1.0 - ss_res / ss_tot : 0.0;

    assert(r2 > 0.8);
    for (int i = 0; i < n_features; ++i)
        assert(std::abs(w[i] - true_w[i]) < 1.0);

    std::cout << "RIDGE_REGRESSION_NORMAL_EQ PASS: R2 = " << r2
              << ", weights = [" << w[0] << ", " << w[1] << ", " << w[2] << "]\n";
    return 0;
}
