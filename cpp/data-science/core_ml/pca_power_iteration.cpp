// pca_power_iteration.cpp
// Principal Component Analysis via power iteration (from scratch).

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <cassert>

using std::vector;

static vector<vector<double>> mean_center(const vector<vector<double>>& X,
                                          vector<double>& means) {
    size_t n = X.size();
    size_t d = n ? X[0].size() : 0;
    means.assign(d, 0.0);
    for (size_t j = 0; j < d; ++j) {
        for (size_t i = 0; i < n; ++i) means[j] += X[i][j];
        means[j] /= static_cast<double>(n);
    }
    vector<vector<double>> C(n, vector<double>(d));
    for (size_t i = 0; i < n; ++i)
        for (size_t j = 0; j < d; ++j)
            C[i][j] = X[i][j] - means[j];
    return C;
}

static vector<vector<double>> transpose(const vector<vector<double>>& A) {
    if (A.empty()) return {};
    size_t m = A.size(), n = A[0].size();
    vector<vector<double>> T(n, vector<double>(m));
    for (size_t i = 0; i < m; ++i)
        for (size_t j = 0; j < n; ++j)
            T[j][i] = A[i][j];
    return T;
}

static vector<vector<double>> matmul(const vector<vector<double>>& A,
                                     const vector<vector<double>>& B) {
    size_t m = A.size(), n = A[0].size(), p = B[0].size();
    vector<vector<double>> R(m, vector<double>(p, 0.0));
    for (size_t i = 0; i < m; ++i)
        for (size_t k = 0; k < n; ++k)
            for (size_t j = 0; j < p; ++j)
                R[i][j] += A[i][k] * B[k][j];
    return R;
}

static vector<vector<double>> covariance(const vector<vector<double>>& X) {
    size_t n = X.size();
    auto XT = transpose(X);
    auto M = matmul(XT, X);
    for (auto& row : M)
        for (auto& v : row) v /= static_cast<double>(n);
    return M;
}

static double norm(const vector<double>& v) {
    double s = 0.0;
    for (double x : v) s += x * x;
    return std::sqrt(s);
}

static vector<double> matvec(const vector<vector<double>>& A,
                             const vector<double>& v) {
    vector<double> r(A.size(), 0.0);
    for (size_t i = 0; i < A.size(); ++i)
        for (size_t j = 0; j < v.size(); ++j)
            r[i] += A[i][j] * v[j];
    return r;
}

static void power_iteration(const vector<vector<double>>& cov0,
                            size_t num_components,
                            vector<vector<double>>& components,
                            vector<double>& eigenvalues) {
    size_t d = cov0.size();
    vector<vector<double>> cov = cov0;
    std::mt19937 rng(42);
    std::normal_distribution<double> dist(0.0, 1.0);

    for (size_t c = 0; c < num_components; ++c) {
        vector<double> v(d);
        for (auto& x : v) x = dist(rng);
        double nv = norm(v);
        for (auto& x : v) x /= nv;

        for (int iter = 0; iter < 100; ++iter) {
            auto v_new = matvec(cov, v);
            nv = norm(v_new);
            if (nv > 1e-10)
                for (auto& x : v_new) x /= nv;
            else
                break;
            double change = 0.0;
            for (size_t i = 0; i < d; ++i)
                change += (v_new[i] - v[i]) * (v_new[i] - v[i]);
            v = v_new;
            if (change < 1e-6) break;
        }

        auto Av = matvec(cov, v);
        double lambda = 0.0;
        for (size_t i = 0; i < d; ++i) lambda += v[i] * Av[i];

        components.push_back(v);
        eigenvalues.push_back(lambda);

        for (size_t i = 0; i < d; ++i)
            for (size_t j = 0; j < d; ++j)
                cov[i][j] -= lambda * v[i] * v[j];
    }
}

static vector<vector<double>> pca_transform(const vector<vector<double>>& X,
                                            const vector<vector<double>>& comp) {
    size_t n = X.size(), k = comp.size();
    vector<vector<double>> R(n, vector<double>(k));
    for (size_t i = 0; i < n; ++i)
        for (size_t c = 0; c < k; ++c) {
            double s = 0.0;
            for (size_t j = 0; j < X[i].size(); ++j)
                s += X[i][j] * comp[c][j];
            R[i][c] = s;
        }
    return R;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> noise(0.0, 1.0);

    size_t n_samples = 50;
    vector<vector<double>> X;
    for (size_t i = 0; i < n_samples; ++i) {
        double x1 = noise(rng) * 3.0;
        double x2 = noise(rng) * 0.5;
        X.push_back({x1, x2});
    }

    vector<double> means;
    auto Xc = mean_center(X, means);
    auto cov = covariance(Xc);

    vector<vector<double>> components;
    vector<double> eigenvalues;
    power_iteration(cov, 2, components, eigenvalues);

    assert(eigenvalues[0] > eigenvalues[1]);
    assert(eigenvalues[0] > 2.0);

    std::cout << "PCA_POWER_ITERATION PASS: ev1 = " << eigenvalues[0]
              << ", ev2 = " << eigenvalues[1] << "\n";
    return 0;
}
