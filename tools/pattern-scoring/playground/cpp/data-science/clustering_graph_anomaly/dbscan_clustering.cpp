// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/* DBSCAN clustering: density-based spatial clustering.
 *
 * Core claim: finds clusters of arbitrary shape, marks noise points.
 */
#include <cassert>
#include <cmath>
#include <iostream>
#include <set>
#include <vector>

double euclidean_distance(const std::vector<double>& p1, const std::vector<double>& p2) {
    double sum = 0.0;
    for (size_t i = 0; i < p1.size(); ++i) {
        sum += (p1[i] - p2[i]) * (p1[i] - p2[i]);
    }
    return std::sqrt(sum);
}

std::set<int> region_query(
    const std::vector<std::vector<double>>& points,
    int p_idx,
    double eps
) {
    std::set<int> neighbors;
    for (size_t i = 0; i < points.size(); ++i) {
        if (euclidean_distance(points[p_idx], points[i]) <= eps) {
            neighbors.insert(static_cast<int>(i));
        }
    }
    return neighbors;
}

std::vector<int> dbscan(
    const std::vector<std::vector<double>>& points,
    double eps,
    int min_pts
) {
    int n = static_cast<int>(points.size());
    std::vector<int> labels(n, -2);  // -2 = unvisited
    int cluster_id = 0;

    for (int i = 0; i < n; ++i) {
        if (labels[i] != -2) continue;

        auto neighbors = region_query(points, i, eps);
        if (static_cast<int>(neighbors.size()) < min_pts) {
            labels[i] = -1;  // Noise
            continue;
        }

        // Start new cluster
        labels[i] = cluster_id;
        std::vector<int> seeds(neighbors.begin(), neighbors.end());
        seeds.erase(std::remove(seeds.begin(), seeds.end(), i), seeds.end());

        for (size_t s = 0; s < seeds.size(); ++s) {
            int j = seeds[s];
            if (labels[j] == -1) labels[j] = cluster_id;
            if (labels[j] != -2) continue;
            labels[j] = cluster_id;

            auto j_neighbors = region_query(points, j, eps);
            if (static_cast<int>(j_neighbors.size()) >= min_pts) {
                for (int idx : j_neighbors) {
                    if (labels[idx] == -2 || labels[idx] == -1) {
                        seeds.push_back(idx);
                    }
                }
            }
        }
        cluster_id++;
    }
    return labels;
}

int main() {
    // Two dense clusters + noise
    std::vector<std::vector<double>> points = {
        {0.0, 0.0}, {0.1, 0.1}, {0.2, 0.0}, {0.0, 0.2},  // Cluster 0
        {5.0, 5.0}, {5.1, 5.1}, {5.2, 5.0}, {5.0, 5.2},  // Cluster 1
        {2.5, 2.5}, {10.0, 10.0}, {0.0, 10.0}            // Noise
    };

    auto labels = dbscan(points, 0.5, 3);

    // Count clusters and noise
    std::set<int> clusters;
    int noise_count = 0;
    for (int l : labels) {
        if (l >= 0) clusters.insert(l);
        else if (l == -1) noise_count++;
    }

    assert(static_cast<int>(clusters.size()) == 2);
    assert(noise_count >= 3);
    assert(all_of(labels.begin(), labels.end(), [](int l) { return l >= -1; }));

    std::cout << "PASS" << std::endl;
    return 0;
}
