// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Least-squares via QR: solve A·x ≈ b using numerically stable QR factorization.
 *
 * Oracle asserts:
 *   0.1 < residual_norm < 2.0
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>

std::pair<std::vector<std::vector<double>>, std::vector<std::vector<double>>> qr_gram_schmidt_tall(
    const std::vector<std::vector<double>>& A) {
    int m = static_cast<int>(A.size());
    int n = static_cast<int>(A[0].size());
    std::vector<std::vector<double>> Q(m, std::vector<double>(n, 0.0));
    std::vector<std::vector<double>> R(n, std::vector<double>(n, 0.0));

    for (int j = 0; j < n; ++j) {
        std::vector<double> v(m);
        for (int i = 0; i < m; ++i) v[i] = A[i][j];
        for (int i = 0; i < j; ++i) {
            R[i][j] = 0.0;
            for (int k = 0; k < m; ++k) R[i][j] += Q[k][i] * v[k];
            for (int k = 0; k < m; ++k) v[k] -= R[i][j] * Q[k][i];
        }
        double norm_v = 0.0;
        for (double x : v) norm_v += x * x;
        norm_v = std::sqrt(norm_v);
        R[j][j] = norm_v;
        for (int i = 0; i < m; ++i) Q[i][j] = v[i] / norm_v;
    }
    return {Q, R};
}

std::vector<double> least_squares_qr(const std::vector<std::vector<double>>& A,
                                    const std::vector<double>& b) {
    auto [Q, R] = qr_gram_schmidt_tall(A);
    int m = static_cast<int>(A.size());
    int n = static_cast<int>(A[0].size());
    std::vector<double> Qt_b(n, 0.0);
    for (int j = 0; j < n; ++j) {
        for (int i = 0; i < m; ++i) Qt_b[j] += Q[i][j] * b[i];
    }
    std::vector<double> x(n, 0.0);
    for (int i = n - 1; i >= 0; --i) {
        double sum_val = Qt_b[i];
        for (int j = i + 1; j < n; ++j) sum_val -= R[i][j] * x[j];
        x[i] = sum_val / R[i][i];
    }
    return x;
}

int main() {
    std::vector<std::vector<double>> A = {{1, 1}, {1, 2}, {1, 3}, {1, 4}};
    std::vector<double> b = {2.0, 3.0, 5.0, 4.0};

    auto x = least_squares_qr(A, b);
    double residual_norm = 0.0;
    for (int i = 0; i < 4; ++i) {
        double r = A[i][0] * x[0] + A[i][1] * x[1] - b[i];
        residual_norm += r * r;
    }
    residual_norm = std::sqrt(residual_norm);

    assert(residual_norm < 2.0);
    assert(residual_norm > 0.1);

    std::cout << "least_squares_qr.cpp PASS: residual=" << residual_norm << std::endl;
    return 0;
}
