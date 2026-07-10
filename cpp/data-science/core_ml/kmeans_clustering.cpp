// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * k-Means Clustering (from scratch).
 *
 * Oracle asserts:
 *   intra-cluster distance < 2.0
 *   min centroid pairwise distance > 2.0
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <random>

double euclidean_distance(const std::vector<double>& p1,
                          const std::vector<double>& p2) {
    double s = 0.0;
    for (size_t i = 0; i < p1.size(); ++i) s += (p1[i] - p2[i]) * (p1[i] - p2[i]);
    return std::sqrt(s);
}

std::pair<std::vector<std::vector<double>>, std::vector<int>> kmeans(
    const std::vector<std::vector<double>>& X, int k,
    int max_iterations = 100, double tolerance = 1e-4) {

    int n = static_cast<int>(X.size());
    int f = n > 0 ? static_cast<int>(X[0].size()) : 0;

    std::mt19937_64 rng(42);
    std::vector<int> indices(n);
    for (int i = 0; i < n; ++i) indices[i] = i;
    std::shuffle(indices.begin(), indices.end(), rng);

    std::vector<std::vector<double>> centroids;
    for (int i = 0; i < k; ++i) centroids.push_back(X[indices[i]]);

    std::vector<int> assignments;
    for (int iter = 0; iter < max_iterations; ++iter) {
        assignments.assign(n, 0);
        for (int i = 0; i < n; ++i) {
            double best = std::numeric_limits<double>::infinity();
            for (int c = 0; c < k; ++c) {
                double d = euclidean_distance(X[i], centroids[c]);
                if (d < best) { best = d; assignments[i] = c; }
            }
        }

        std::vector<std::vector<double>> new_centroids(k, std::vector<double>(f, 0.0));
        std::vector<int> counts(k, 0);
        for (int i = 0; i < n; ++i) {
            int c = assignments[i];
            ++counts[c];
            for (int j = 0; j < f; ++j) new_centroids[c][j] += X[i][j];
        }
        for (int c = 0; c < k; ++c) {
            if (counts[c] > 0) {
                for (int j = 0; j < f; ++j) new_centroids[c][j] /= counts[c];
            } else {
                new_centroids[c] = centroids[c];
            }
        }

        double movement = 0.0;
        for (int c = 0; c < k; ++c) movement += euclidean_distance(centroids[c], new_centroids[c]);
        centroids = new_centroids;
        if (movement < tolerance) break;
    }

    assignments.assign(n, 0);
    for (int i = 0; i < n; ++i) {
        double best = std::numeric_limits<double>::infinity();
        for (int c = 0; c < k; ++c) {
            double d = euclidean_distance(X[i], centroids[c]);
            if (d < best) { best = d; assignments[i] = c; }
        }
    }
    return {centroids, assignments};
}

int main() {
    std::mt19937_64 rng(42);
    std::normal_distribution<double> nd(0.0, 0.5);
    std::vector<std::vector<double>> X;
    for (int i = 0; i < 20; ++i) X.push_back({nd(rng), nd(rng)});
    std::normal_distribution<double> nd2(5.0, 0.5);
    for (int i = 0; i < 20; ++i) X.push_back({nd2(rng), nd(rng)});
    std::normal_distribution<double> nd3(2.5, 0.5), nd4(4.0, 0.5);
    for (int i = 0; i < 20; ++i) X.push_back({nd3(rng), nd4(rng)});

    auto [centroids, assignments] = kmeans(X, 3);

    double intra = 0.0;
    for (size_t i = 0; i < X.size(); ++i) intra += euclidean_distance(X[i], centroids[assignments[i]]);
    intra /= X.size();
    assert(intra < 2.0);

    double min_dist = std::numeric_limits<double>::infinity();
    for (int i = 0; i < 3; ++i) {
        for (int j = i + 1; j < 3; ++j) {
            min_dist = std::min(min_dist, euclidean_distance(centroids[i], centroids[j]));
        }
    }
    assert(min_dist > 2.0);

    std::cout << "kmeans_clustering.cpp PASS: intra=" << intra << std::endl;
    return 0;
}
