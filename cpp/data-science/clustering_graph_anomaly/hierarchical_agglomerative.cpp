// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Hierarchical Agglomerative Clustering from scratch.
 */

#include <vector>
#include <set>
#include <cmath>
#include <random>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <utility>

double euclidean_distance(const std::pair<double, double>& p1,
                          const std::pair<double, double>& p2) {
    double dx = p1.first - p2.first;
    double dy = p1.second - p2.second;
    return std::sqrt(dx * dx + dy * dy);
}

double cluster_distance(const std::vector<int>& cluster_a,
                        const std::vector<int>& cluster_b,
                        const std::vector<std::pair<double, double>>& points,
                        const std::string& linkage) {
    double best = (linkage == "single") ? 1e18 : -1e18;
    for (int i : cluster_a) {
        for (int j : cluster_b) {
            double d = euclidean_distance(points[i], points[j]);
            if (linkage == "single") best = std::min(best, d);
            else best = std::max(best, d);
        }
    }
    return best;
}

std::vector<int> cut_dendrogram(const std::vector<std::pair<double, double>>& points,
                                int k, const std::string& linkage) {
    std::vector<std::vector<int>> clusters;
    for (int i = 0; i < static_cast<int>(points.size()); ++i) {
        clusters.push_back({i});
    }

    while (static_cast<int>(clusters.size()) > k) {
        double min_distance = 1e18;
        int merge_i = -1, merge_j = -1;

        for (size_t i = 0; i < clusters.size(); ++i) {
            for (size_t j = i + 1; j < clusters.size(); ++j) {
                double dist = cluster_distance(clusters[i], clusters[j], points, linkage);
                if (dist < min_distance) {
                    min_distance = dist;
                    merge_i = static_cast<int>(i);
                    merge_j = static_cast<int>(j);
                }
            }
        }

        clusters[merge_i].insert(clusters[merge_i].end(), clusters[merge_j].begin(), clusters[merge_j].end());
        clusters.erase(clusters.begin() + merge_j);
    }

    std::vector<int> labels(points.size(), -1);
    for (size_t cluster_id = 0; cluster_id < clusters.size(); ++cluster_id) {
        for (int point_idx : clusters[cluster_id]) {
            labels[point_idx] = static_cast<int>(cluster_id);
        }
    }
    return labels;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> normal0(0.0, 0.5);
    std::normal_distribution<double> normal5(5.0, 0.5);
    std::normal_distribution<double> normal10(10.0, 0.5);

    std::vector<std::pair<double, double>> points;
    for (int i = 0; i < 10; ++i) points.push_back({normal0(rng), normal0(rng)});
    for (int i = 0; i < 10; ++i) points.push_back({normal5(rng), normal5(rng)});
    for (int i = 0; i < 10; ++i) points.push_back({normal10(rng), normal0(rng)});

    auto labels = cut_dendrogram(points, 3, "complete");

    std::set<int> unique_labels(labels.begin(), labels.end());
    assert(unique_labels.size() == 3);

    std::vector<int> c1_labels(labels.begin(), labels.begin() + 10);
    std::vector<int> c2_labels(labels.begin() + 10, labels.begin() + 20);
    std::vector<int> c3_labels(labels.begin() + 20, labels.end());

    std::set<int> s1(c1_labels.begin(), c1_labels.end());
    std::set<int> s2(c2_labels.begin(), c2_labels.end());
    std::set<int> s3(c3_labels.begin(), c3_labels.end());

    assert(s1.size() <= 2);
    assert(s2.size() <= 2);
    assert(s3.size() <= 2);

    std::cout << "hierarchical_agglomerative.cpp PASS" << std::endl;
    return 0;
}
