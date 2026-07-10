// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Markov chain stationary distribution via power iteration.
 *
 * Oracle asserts:
 *   pi_2state matches [4/7, 3/7] within 1e-6
 *   verify_stationary for 2-state
 *   pi_3state uniform within 1e-6
 *   verify_stationary for 3-state
 *   pi_4state sums to 1
 *   verify_stationary for 4-state
 *   v1 == v2 == v3 for different starts on P_test
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>

std::vector<double> matrix_multiply(const std::vector<double>& v,
                                     const std::vector<std::vector<double>>& P) {
    int n = static_cast<int>(P.size());
    std::vector<double> result(n, 0.0);
    for (int j = 0; j < n; ++j)
        for (int i = 0; i < n; ++i) result[j] += v[i] * P[i][j];
    return result;
}

std::vector<double> power_iteration_stationary(const std::vector<std::vector<double>>& P,
                                                int max_iter = 1000, double tol = 1e-9) {
    int n = static_cast<int>(P.size());
    std::vector<double> pi(n, 1.0 / n);
    for (int iter = 0; iter < max_iter; ++iter) {
        auto pi_new = matrix_multiply(pi, P);
        double max_diff = 0.0;
        for (int i = 0; i < n; ++i) max_diff = std::max(max_diff, std::abs(pi_new[i] - pi[i]));
        if (max_diff < tol) return pi_new;
        pi = pi_new;
    }
    return pi;
}

bool verify_stationary(const std::vector<double>& pi, const std::vector<std::vector<double>>& P) {
    auto pi_P = matrix_multiply(pi, P);
    for (size_t i = 0; i < pi.size(); ++i) if (std::abs(pi_P[i] - pi[i]) >= 1e-9) return false;
    return true;
}

int main() {
    std::vector<std::vector<double>> P_2state = {{0.7, 0.3}, {0.4, 0.6}};
    auto pi_computed = power_iteration_stationary(P_2state);
    std::vector<double> pi_analytical = {4.0 / 7.0, 3.0 / 7.0};
    for (int i = 0; i < 2; ++i) assert(std::abs(pi_computed[i] - pi_analytical[i]) < 1e-6);
    assert(verify_stationary(pi_computed, P_2state));

    std::vector<std::vector<double>> P_3state = {{0.5, 0.25, 0.25}, {0.25, 0.5, 0.25}, {0.25, 0.25, 0.5}};
    auto pi_3 = power_iteration_stationary(P_3state);
    for (int i = 0; i < 3; ++i) assert(std::abs(pi_3[i] - 1.0 / 3.0) < 1e-6);
    assert(verify_stationary(pi_3, P_3state));

    std::vector<std::vector<double>> P_4state = {
        {0.1, 0.4, 0.3, 0.2}, {0.2, 0.1, 0.4, 0.3},
        {0.3, 0.2, 0.1, 0.4}, {0.4, 0.3, 0.2, 0.1}
    };
    auto pi_4 = power_iteration_stationary(P_4state);
    double sum = 0.0; for (double x : pi_4) sum += x;
    assert(std::abs(sum - 1.0) < 1e-9);
    assert(verify_stationary(pi_4, P_4state));

    std::vector<std::vector<double>> P_test = {{0.6, 0.4}, {0.3, 0.7}};
    std::vector<double> v1 = {1.0, 0.0}, v2 = {0.0, 1.0}, v3 = {0.5, 0.5};
    for (int i = 0; i < 100; ++i) {
        v1 = matrix_multiply(v1, P_test);
        v2 = matrix_multiply(v2, P_test);
        v3 = matrix_multiply(v3, P_test);
    }
    for (int i = 0; i < 2; ++i) {
        assert(std::abs(v1[i] - v2[i]) < 1e-6);
        assert(std::abs(v2[i] - v3[i]) < 1e-6);
    }

    std::cout << "markov_chain_stationary.cpp PASS" << std::endl;
    return 0;
}
