// Woodbury matrix identity: update A^-1 efficiently after rank-1 A change.
// Converted from the Python oracle.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>

using Matrix = std::vector<std::vector<double>>;

Matrix vector_outer_product(const std::vector<double>& u, const std::vector<double>& v) {
    size_t n = u.size();
    Matrix result(n, std::vector<double>(n, 0.0));
    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < n; ++j)
            result[i][j] = u[i] * v[j];
    return result;
}

Matrix matrix_add(const Matrix& A, const Matrix& B) {
    size_t n = A.size();
    Matrix result(n, std::vector<double>(n, 0.0));
    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < n; ++j)
            result[i][j] = A[i][j] + B[i][j];
    return result;
}

Matrix woodbury_update(const Matrix& A_inv, const std::vector<double>& u,
                       const std::vector<double>& v) {
    size_t n = A_inv.size();
    std::vector<double> A_inv_u(n, 0.0);
    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < n; ++j)
            A_inv_u[i] += A_inv[i][j] * u[j];
    double v_T_A_inv_u = 0.0;
    for (size_t i = 0; i < n; ++i) v_T_A_inv_u += v[i] * A_inv_u[i];
    std::vector<double> v_T_A_inv(n, 0.0);
    for (size_t j = 0; j < n; ++j)
        for (size_t k = 0; k < n; ++k)
            v_T_A_inv[j] += v[k] * A_inv[k][j];
    double denom = 1.0 + v_T_A_inv_u;
    assert(std::abs(denom) > 1e-14);
    Matrix result(n, std::vector<double>(n, 0.0));
    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < n; ++j)
            result[i][j] = A_inv[i][j] - A_inv_u[i] * v_T_A_inv[j] / denom;
    return result;
}

int main() {
    Matrix A = {{4.0, 1.0}, {1.0, 3.0}};
    double det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0];
    Matrix A_inv = {{A[1][1]/det_A, -A[0][1]/det_A},
                    {-A[1][0]/det_A, A[0][0]/det_A}};
    std::vector<double> u = {1.0, 0.0};
    std::vector<double> v = {2.0, 1.0};

    Matrix A_new_direct = matrix_add(A, vector_outer_product(u, v));
    Matrix A_new_inv_woodbury = woodbury_update(A_inv, u, v);

    double det_A_new = A_new_direct[0][0]*A_new_direct[1][1] - A_new_direct[0][1]*A_new_direct[1][0];
    Matrix A_new_inv_direct = {{A_new_direct[1][1]/det_A_new, -A_new_direct[0][1]/det_A_new},
                               {-A_new_direct[1][0]/det_A_new, A_new_direct[0][0]/det_A_new}};

    for (size_t i = 0; i < 2; ++i)
        for (size_t j = 0; j < 2; ++j)
            assert(std::abs(A_new_inv_woodbury[i][j] - A_new_inv_direct[i][j]) < 1e-8);
    std::cout << "PASS\n";
    return 0;
}
