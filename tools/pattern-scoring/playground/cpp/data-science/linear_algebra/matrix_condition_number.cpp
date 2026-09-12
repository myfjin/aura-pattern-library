// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Matrix condition number: measure sensitivity to perturbations in A and b.
 *
 * Oracle asserts:
 *   kappa_bad > 100 * kappa_good
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>

double matrix_norm_frobenius(const std::vector<std::vector<double>>& A) {
    double s = 0.0;
    for (const auto& row : A) for (double x : row) s += x * x;
    return std::sqrt(s);
}

std::vector<std::vector<double>> matrix_inverse_lu(const std::vector<std::vector<double>>& A) {
    int n = static_cast<int>(A.size());
    auto A_work = A;
    for (int k = 0; k < n; ++k) {
        int max_idx = k;
        for (int i = k + 1; i < n; ++i)
            if (std::abs(A_work[i][k]) > std::abs(A_work[max_idx][k])) max_idx = i;
        std::swap(A_work[k], A_work[max_idx]);
        for (int i = k + 1; i < n; ++i) {
            double factor = A_work[i][k] / A_work[k][k];
            for (int j = k; j < n; ++j) A_work[i][j] -= factor * A_work[k][j];
        }
    }

    std::vector<std::vector<double>> A_inv(n, std::vector<double>(n, 0.0));
    for (int col = 0; col < n; ++col) {
        std::vector<double> b(n, 0.0);
        b[col] = 1.0;
        for (int i = 0; i < n; ++i) {
            double sum_val = b[i];
            for (int j = 0; j < i; ++j) sum_val -= A_work[i][j] * b[j];
            b[i] = sum_val;
        }
        for (int i = n - 1; i >= 0; --i) {
            double sum_val = b[i];
            for (int j = i + 1; j < n; ++j) sum_val -= A_work[i][j] * b[j];
            b[i] = sum_val / A_work[i][i];
        }
        for (int i = 0; i < n; ++i) A_inv[i][col] = b[i];
    }
    return A_inv;
}

double condition_number(const std::vector<std::vector<double>>& A) {
    auto A_inv = matrix_inverse_lu(A);
    return matrix_norm_frobenius(A) * matrix_norm_frobenius(A_inv);
}

int main() {
    std::vector<std::vector<double>> A_good = {{4, 1, 0}, {1, 3, 1}, {0, 1, 2}};
    std::vector<std::vector<double>> A_bad = {{1, 1, 1}, {1, 1.0001, 1}, {1, 1, 1.0001}};

    double kappa_good = condition_number(A_good);
    double kappa_bad = condition_number(A_bad);
    assert(kappa_bad > 100.0 * kappa_good);

    std::cout << "matrix_condition_number.cpp PASS: good=" << kappa_good
              << " bad=" << kappa_bad << std::endl;
    return 0;
}
