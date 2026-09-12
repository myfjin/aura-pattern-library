// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Jacobi eigenvalue algorithm: iterative diagonalization of symmetric matrix.
 *
 * Oracle asserts:
 *   eigenvalues match {3 - sqrt(3), 3, 3 + sqrt(3)} within 1e-8
 *   each eigenvector satisfies A·v = λ·v within 1e-8
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <numeric>

std::pair<std::vector<double>, std::vector<std::vector<double>>> jacobi_eigen(
    const std::vector<std::vector<double>>& A, int max_iter = 100, double tol = 1e-10) {

    int n = static_cast<int>(A.size());
    std::vector<std::vector<double>> A_work = A;
    std::vector<std::vector<double>> V(n, std::vector<double>(n, 0.0));
    for (int i = 0; i < n; ++i) V[i][i] = 1.0;

    for (int iter = 0; iter < max_iter; ++iter) {
        int p = 0, q = 1;
        double max_elem = std::abs(A_work[0][1]);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (std::abs(A_work[i][j]) > max_elem) {
                    max_elem = std::abs(A_work[i][j]);
                    p = i; q = j;
                }
            }
        }
        if (max_elem < tol) break;

        double theta = 0.5 * std::atan2(2.0 * A_work[p][q], A_work[q][q] - A_work[p][p]);
        double c = std::cos(theta), s = std::sin(theta);

        for (int i = 0; i < n; ++i) {
            if (i != p && i != q) {
                double aip = A_work[i][p];
                double aiq = A_work[i][q];
                A_work[i][p] = c * aip - s * aiq;
                A_work[p][i] = A_work[i][p];
                A_work[i][q] = s * aip + c * aiq;
                A_work[q][i] = A_work[i][q];
            }
        }

        double app = A_work[p][p];
        double aqq = A_work[q][q];
        A_work[p][p] = c * c * app - 2.0 * s * c * A_work[p][q] + s * s * aqq;
        A_work[q][q] = s * s * app + 2.0 * s * c * A_work[p][q] + c * c * aqq;
        A_work[p][q] = 0.0;
        A_work[q][p] = 0.0;

        for (int i = 0; i < n; ++i) {
            double vip = V[i][p];
            double viq = V[i][q];
            V[i][p] = c * vip - s * viq;
            V[i][q] = s * vip + c * viq;
        }
    }

    std::vector<double> eigenvalues;
    for (int i = 0; i < n; ++i) eigenvalues.push_back(A_work[i][i]);
    return {eigenvalues, V};
}

int main() {
    std::vector<std::vector<double>> A = {{4, 1, 0}, {1, 3, 1}, {0, 1, 2}};
    std::vector<double> true_eigs = {
        3.0 - std::sqrt(3.0), 3.0, 3.0 + std::sqrt(3.0)
    };
    std::sort(true_eigs.begin(), true_eigs.end());

    auto eigen_result = jacobi_eigen(A);
    const auto& eigenvalues = eigen_result.first;
    const auto& eigenvectors = eigen_result.second;

    assert(eigenvalues.size() == 3);
    std::vector<int> order(eigenvalues.size());
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(),
              [&](int a, int b) { return eigenvalues[a] < eigenvalues[b]; });

    for (size_t rank = 0; rank < order.size(); ++rank) {
        int j = order[rank];
        double lam = eigenvalues[j];
        assert(std::abs(lam - true_eigs[rank]) < 1e-8);

        std::vector<double> v(3);
        for (int i = 0; i < 3; ++i) v[i] = eigenvectors[i][j];

        for (int i = 0; i < 3; ++i) {
            double av = A[i][0] * v[0] + A[i][1] * v[1] + A[i][2] * v[2];
            assert(std::abs(av - lam * v[i]) < 1e-8);
        }
    }

    std::cout << "jacobi_eigen_symmetric.cpp PASS" << std::endl;
    return 0;
}
