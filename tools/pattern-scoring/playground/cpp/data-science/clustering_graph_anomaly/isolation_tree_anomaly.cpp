// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Isolation Forest (Lite) Anomaly Detection from scratch.
 *
 * Oracle asserts:
 *   avg_outlier < avg_normal
 *   avg_normal > 0
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <limits>
#include <algorithm>
#include <random>
#include <utility>

struct IsolationNode {
    int split_feature = -1;
    double split_value = 0.0;
    IsolationNode* left = nullptr;
    IsolationNode* right = nullptr;
    int size = 0;
};

IsolationNode* build_isolation_tree(const std::vector<std::pair<double,double>>& points,
                                  const std::vector<int>& indices,
                                  std::mt19937_64& rng,
                                  int depth = 0, int max_depth = 10) {
    IsolationNode* node = new IsolationNode();
    node->size = static_cast<int>(indices.size());

    if (indices.size() <= 1 || depth >= max_depth) return node;

    std::uniform_int_distribution<int> feat_dist(0, 1);
    int split_feature = feat_dist(rng);

    double min_val = std::numeric_limits<double>::infinity();
    double max_val = -std::numeric_limits<double>::infinity();
    for (int idx : indices) {
        double v = split_feature == 0 ? points[idx].first : points[idx].second;
        min_val = std::min(min_val, v);
        max_val = std::max(max_val, v);
    }
    if (min_val == max_val) return node;

    std::uniform_real_distribution<double> split_dist(min_val, max_val);
    double split_value = split_dist(rng);
    node->split_feature = split_feature;
    node->split_value = split_value;

    std::vector<int> left_indices, right_indices;
    for (int idx : indices) {
        double v = split_feature == 0 ? points[idx].first : points[idx].second;
        if (v < split_value) left_indices.push_back(idx);
        else right_indices.push_back(idx);
    }
    if (left_indices.empty() || right_indices.empty()) return node;

    node->left = build_isolation_tree(points, left_indices, rng, depth + 1, max_depth);
    node->right = build_isolation_tree(points, right_indices, rng, depth + 1, max_depth);
    return node;
}

int path_length(IsolationNode* tree, const std::pair<double,double>& point, int depth = 0) {
    if (tree->split_feature == -1 || tree->left == nullptr || tree->right == nullptr)
        return depth;
    double v = tree->split_feature == 0 ? point.first : point.second;
    if (v < tree->split_value) return path_length(tree->left, point, depth + 1);
    return path_length(tree->right, point, depth + 1);
}

int main() {
    std::mt19937_64 rng(42);

    std::vector<std::pair<double,double>> points;
    std::normal_distribution<double> nd(5.0, 0.5);
    for (int i = 0; i < 100; ++i) points.push_back({nd(rng), nd(rng)});
    for (int i = 0; i < 5; ++i) {
        std::uniform_real_distribution<double> out_dist(-5.0, 0.0);
        points.push_back({out_dist(rng), out_dist(rng)});
    }

    int num_trees = 30;
    int n = static_cast<int>(points.size());
    std::vector<IsolationNode*> trees;
    for (int t = 0; t < num_trees; ++t) {
        std::mt19937_64 tree_rng(static_cast<uint64_t>(42 + t));
        int sample_size = std::min(256, n);
        std::vector<int> sample_indices;
        std::uniform_int_distribution<int> idx_dist(0, n - 1);
        for (int i = 0; i < sample_size; ++i) sample_indices.push_back(idx_dist(tree_rng));
        trees.push_back(build_isolation_tree(points, sample_indices, tree_rng));
    }

    std::vector<double> scores;
    for (const auto& p : points) {
        double total = 0.0;
        for (auto* tree : trees) total += path_length(tree, p);
        scores.push_back(total / num_trees);
    }

    double avg_normal = 0.0, avg_outlier = 0.0;
    for (int i = 0; i < 100; ++i) avg_normal += scores[i];
    for (int i = 100; i < 105; ++i) avg_outlier += scores[i];
    avg_normal /= 100.0;
    avg_outlier /= 5.0;

    assert(avg_outlier < avg_normal);
    assert(avg_normal > 0.0);

    std::cout << "isolation_tree_anomaly.cpp PASS: normal=" << avg_normal
              << " outlier=" << avg_outlier << std::endl;
    return 0;
}
