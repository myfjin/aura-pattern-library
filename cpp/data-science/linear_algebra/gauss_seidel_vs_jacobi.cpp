// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Gauss–Seidel vs Jacobi: convergence rate comparison.
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <utility>

std::pair<std::vector<double>, int> jacobi_iteration(
    const std::vector<std::vector<double>>& A,
    const std::vector<double>& b,
    const std::vector<double>& x0,
    int max_iter = 100,
    double tol = 1e-8
) {
    int n = static_cast<int>(A.size());
    std::vector<double> x = x0;

    for (int iteration = 0; iteration < max_iter; ++iteration) {
        std::vector<double> x_new(n, 0.0);
        for (int i = 0; i < n; ++i) {
            double sum_val = b[i];
            for (int j = 0; j < n; ++j) {
                if (j != i) sum_val -= A[i][j] * x[j];
            }
            x_new[i] = sum_val / A[i][i];
        }

        double residual = 0.0;
        for (int i = 0; i < n; ++i) {
            double diff = x_new[i] - x[i];
            residual += diff * diff;
        }
        residual = std::sqrt(residual);
        x = x_new;

        if (residual < tol) return {x, iteration + 1};
    }

    return {x, max_iter};
}

std::pair<std::vector<double>, int> gauss_seidel_iteration(
    const std::vector<std::vector<double>>& A,
    const std::vector<double>& b,
    const std::vector<double>& x0,
    int max_iter = 100,
    double tol = 1e-8
) {
    int n = static_cast<int>(A.size());
    std::vector<double> x = x0;

    for (int iteration = 0; iteration < max_iter; ++iteration) {
        std::vector<double> x_old = x;
        for (int i = 0; i < n; ++i) {
            double sum_val = b[i];
            for (int j = 0; j < i; ++j) sum_val -= A[i][j] * x[j];
            for (int j = i + 1; j < n; ++j) sum_val -= A[i][j] * x_old[j];
            x[i] = sum_val / A[i][i];
        }

        double residual = 0.0;
        for (int i = 0; i < n; ++i) {
            double diff = x[i] - x_old[i];
            residual += diff * diff;
        }
        residual = std::sqrt(residual);

        if (residual < tol) return {x, iteration + 1};
    }

    return {x, max_iter};
}

int main() {
    std::vector<std::vector<double>> A = {{10, 1, 2}, {1, 8, 1}, {2, 1, 10}};
    std::vector<double> b = {13, 10, 13};
    std::vector<double> x0 = {0, 0, 0};

    auto [x_jacobi, iter_jacobi] = jacobi_iteration(A, b, x0, 1000);
    auto [x_gs, iter_gs] = gauss_seidel_iteration(A, b, x0, 1000);

    assert(iter_gs < iter_jacobi);
    for (int i = 0; i < 3; ++i) {
        assert(std::abs(x_jacobi[i] - x_gs[i]) < 0.01);
    }

    std::cout << "gauss_seidel_vs_jacobi.cpp PASS" << std::endl;
    return 0;
}
