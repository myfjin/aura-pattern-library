// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Covariance Matrix
 * 
 * Computes sample covariance between all numeric columns.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>

std::vector<std::vector<double>> covariance_matrix(const std::vector<std::vector<double>>& data) {
    /* Compute sample covariance matrix. */
    int n_cols = static_cast<int>(data.size());
    if (n_cols == 0) return {};

    int n_rows = static_cast<int>(data[0].size());
    if (n_rows < 2) throw std::invalid_argument("Need at least 2 rows");

    for (const auto& col : data) {
        if (static_cast<int>(col.size()) != n_rows) {
            throw std::invalid_argument("All columns must have same length");
        }
    }

    // Compute means
    std::vector<double> means(n_cols, 0.0);
    for (int i = 0; i < n_cols; ++i) {
        for (double v : data[i]) means[i] += v;
        means[i] /= n_rows;
    }

    // Compute covariance matrix
    std::vector<std::vector<double>> cov_matrix(n_cols, std::vector<double>(n_cols, 0.0));
    for (int i = 0; i < n_cols; ++i) {
        for (int j = 0; j < n_cols; ++j) {
            double cov_sum = 0.0;
            for (int k = 0; k < n_rows; ++k) {
                cov_sum += (data[i][k] - means[i]) * (data[j][k] - means[j]);
            }
            cov_matrix[i][j] = cov_sum / (n_rows - 1);  // sample covariance
        }
    }

    return cov_matrix;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> normal1(0.0, 1.0);

    // Synthetic data with planted structure
    std::vector<double> x(20), y(20), z(20);
    for (int i = 0; i < 20; ++i) {
        x[i] = 5.0 + i + normal1(rng);
    }
    for (int i = 0; i < 20; ++i) {
        y[i] = 2.0 * x[i] + normal1(rng);
    }
    std::normal_distribution<double> normal50(50.0, 5.0);
    for (int i = 0; i < 20; ++i) {
        z[i] = normal50(rng);
    }

    std::vector<std::vector<double>> data = {x, y, z};
    auto cov_mat = covariance_matrix(data);

    // Verify symmetric
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            assert(std::abs(cov_mat[i][j] - cov_mat[j][i]) < 1e-6);
        }
    }

    // Diagonal should be positive (variances)
    for (int i = 0; i < 3; ++i) {
        assert(cov_mat[i][i] > 0.0);
    }

    // x-y covariance should be positive
    assert(cov_mat[0][1] > 0.0);
    assert(cov_mat[1][0] > 0.0);

    // z should have lower covariance with x and y than x-y covariance
    assert(std::abs(cov_mat[0][2]) < std::abs(cov_mat[0][1]));

    // Verify diagonal via direct variance computation
    auto variance = [](const std::vector<double>& v) {
        double mean = 0.0;
        for (double val : v) mean += val;
        mean /= v.size();
        double sum_sq = 0.0;
        for (double val : v) {
            double diff = val - mean;
            sum_sq += diff * diff;
        }
        return sum_sq / (v.size() - 1);
    };

    double var_x = variance(x);
    double var_y = variance(y);
    double var_z = variance(z);

    assert(std::abs(cov_mat[0][0] - var_x) < 1e-6);
    assert(std::abs(cov_mat[1][1] - var_y) < 1e-6);
    assert(std::abs(cov_mat[2][2] - var_z) < 1e-6);

    std::cout << "covariance_matrix.cpp: PASS" << std::endl;
    return 0;
}
