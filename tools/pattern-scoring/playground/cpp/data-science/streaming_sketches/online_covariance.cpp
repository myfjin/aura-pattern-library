// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Online covariance/correlation via Welford's multivariate update: maintains a
running mean and co-moment matrix, so the full covariance (and correlation)
matrix is available after a single pass with no stored data. Use for streaming
or memory-bounded computation of pairwise (co)variance.
Guarantee: the one-pass estimate matches a two-pass batch covariance to within
1e-9 (numerical parity), proving the incremental update is exact, not approximate.
*/
#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>

class OnlineCovarianceEstimator {
public:
    explicit OnlineCovarianceEstimator(std::size_t n_vars = 2)
        : n_vars_(n_vars), n_(0), means_(n_vars, 0.0), M2_(n_vars, std::vector<double>(n_vars, 0.0)) {}

    void process(const std::vector<double>& point) {
        ++n_;
        std::vector<double> deltas(n_vars_);
        for (std::size_t i = 0; i < n_vars_; ++i) {
            deltas[i] = point[i] - means_[i];
            means_[i] += deltas[i] / static_cast<double>(n_);
        }
        std::vector<double> delta_primes(n_vars_);
        for (std::size_t i = 0; i < n_vars_; ++i) {
            delta_primes[i] = point[i] - means_[i];
        }
        for (std::size_t i = 0; i < n_vars_; ++i) {
            for (std::size_t j = 0; j < n_vars_; ++j) {
                M2_[i][j] += deltas[i] * delta_primes[j];
            }
        }
    }

    std::vector<std::vector<double>> get_covariance(bool unbiased = true) const {
        if (n_ < 2) {
            return M2_;
        }
        double divisor = unbiased ? static_cast<double>(n_ - 1) : static_cast<double>(n_);
        auto cov = M2_;
        for (std::size_t i = 0; i < n_vars_; ++i) {
            for (std::size_t j = 0; j < n_vars_; ++j) {
                cov[i][j] /= divisor;
            }
        }
        return cov;
    }

    std::vector<std::vector<double>> get_correlation() const {
        auto cov = get_covariance();
        std::vector<std::vector<double>> corr(n_vars_, std::vector<double>(n_vars_, 0.0));
        for (std::size_t i = 0; i < n_vars_; ++i) {
            for (std::size_t j = 0; j < n_vars_; ++j) {
                double std_i = cov[i][i] > 0.0 ? std::sqrt(cov[i][i]) : 1.0;
                double std_j = cov[j][j] > 0.0 ? std::sqrt(cov[j][j]) : 1.0;
                corr[i][j] = cov[i][j] / (std_i * std_j);
            }
        }
        return corr;
    }

private:
    std::size_t n_vars_;
    std::size_t n_;
    std::vector<double> means_;
    std::vector<std::vector<double>> M2_;
};

std::vector<std::vector<double>> batch_covariance(const std::vector<std::vector<double>>& data) {
    std::size_t n = data.size();
    std::size_t n_vars = data[0].size();
    std::vector<double> means(n_vars, 0.0);
    for (const auto& row : data) {
        for (std::size_t i = 0; i < n_vars; ++i) {
            means[i] += row[i];
        }
    }
    for (std::size_t i = 0; i < n_vars; ++i) {
        means[i] /= static_cast<double>(n);
    }
    std::vector<std::vector<double>> cov(n_vars, std::vector<double>(n_vars, 0.0));
    for (const auto& row : data) {
        for (std::size_t i = 0; i < n_vars; ++i) {
            for (std::size_t j = 0; j < n_vars; ++j) {
                cov[i][j] += (row[i] - means[i]) * (row[j] - means[j]);
            }
        }
    }
    for (std::size_t i = 0; i < n_vars; ++i) {
        for (std::size_t j = 0; j < n_vars; ++j) {
            cov[i][j] /= static_cast<double>(n - 1);
        }
    }
    return cov;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> dist(0.0, 1.0);

    std::vector<std::vector<double>> data;
    for (int i = 0; i < 500; ++i) {
        double x = dist(rng);
        double y = 0.7 * x + dist(rng) * 0.5;
        data.push_back({x, y});
    }

    auto batch_cov = batch_covariance(data);

    OnlineCovarianceEstimator online_est(2);
    for (const auto& point : data) {
        online_est.process(point);
    }
    auto online_cov = online_est.get_covariance();
    auto online_corr = online_est.get_correlation();

    std::cout << std::fixed << std::setprecision(6);
    std::cout << "Batch covariance:\n";
    for (const auto& row : batch_cov) {
        for (double c : row) std::cout << c << " ";
        std::cout << "\n";
    }
    std::cout << "Online covariance:\n";
    for (const auto& row : online_cov) {
        for (double c : row) std::cout << c << " ";
        std::cout << "\n";
    }

    double max_error = 0.0;
    for (std::size_t i = 0; i < 2; ++i) {
        for (std::size_t j = 0; j < 2; ++j) {
            max_error = std::max(max_error, std::abs(batch_cov[i][j] - online_cov[i][j]));
        }
    }
    std::cout << "Max covariance error: " << std::scientific << max_error << "\n";
    std::cout << "Correlation: " << std::fixed << online_corr[0][1] << "\n";

    assert(max_error < 1e-9);
    assert(0.5 < online_corr[0][1] && online_corr[0][1] < 1.0);

    std::cout << "Online Covariance: PASS\n";
    return 0;
}
