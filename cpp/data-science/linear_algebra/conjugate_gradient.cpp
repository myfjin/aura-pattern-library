// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Conjugate Gradient: Iterative Solver for SPD Systems
 * 
 * Solves A*x = b using search directions conjugate w.r.t. A.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>

std::vector<double> conjugate_gradient(
    const std::vector<std::vector<double>>& A,
    const std::vector<double>& b,
    const std::vector<double>& x0,
    double tol = 1e-8,
    int max_iter = -1
) {
    /* Solve A*x = b for SPD matrix A via conjugate gradient. */
    int n = static_cast<int>(A.size());
    if (max_iter < 0) max_iter = n;

    std::vector<double> x = x0;
    std::vector<double> r(n);
    for (int i = 0; i < n; ++i) {
        r[i] = b[i];
        for (int j = 0; j < n; ++j) {
            r[i] -= A[i][j] * x[j];
        }
    }
    std::vector<double> p = r;

    double r_dot_r = 0.0;
    for (double v : r) r_dot_r += v * v;

    for (int iteration = 0; iteration < max_iter; ++iteration) {
        if (r_dot_r < tol * tol) break;

        // Compute Ap
        std::vector<double> Ap(n, 0.0);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                Ap[i] += A[i][j] * p[j];
            }
        }

        // Step size
        double p_dot_Ap = 0.0;
        for (int i = 0; i < n; ++i) {
            p_dot_Ap += p[i] * Ap[i];
        }
        if (std::abs(p_dot_Ap) < 1e-14) break;

        double alpha = r_dot_r / p_dot_Ap;

        // Update x and r
        for (int i = 0; i < n; ++i) {
            x[i] += alpha * p[i];
            r[i] -= alpha * Ap[i];
        }

        double r_dot_r_new = 0.0;
        for (double v : r) r_dot_r_new += v * v;
        double beta = r_dot_r_new / r_dot_r;

        // Update p
        for (int i = 0; i < n; ++i) {
            p[i] = r[i] + beta * p[i];
        }
        r_dot_r = r_dot_r_new;
    }

    return x;
}

int main() {
    // Planted: SPD 3x3 system.
    // A = [[4, 1, 0], [1, 3, 1], [0, 1, 2]] is SPD.
    // Solve A*x = b for b = [1, 2, 3].
    std::vector<std::vector<double>> A = {
        {4.0, 1.0, 0.0},
        {1.0, 3.0, 1.0},
        {0.0, 1.0, 2.0}
    };
    std::vector<double> b = {1.0, 2.0, 3.0};
    std::vector<double> x0 = {0.0, 0.0, 0.0};

    auto x_solution = conjugate_gradient(A, b, x0);

    // Verify: A*x ≈ b
    for (int i = 0; i < 3; ++i) {
        double Ax = 0.0;
        for (int j = 0; j < 3; ++j) {
            Ax += A[i][j] * x_solution[j];
        }
        assert(std::abs(Ax - b[i]) < 1e-6);
    }

    std::cout << "conjugate_gradient.cpp PASS" << std::endl;
    return 0;
}
