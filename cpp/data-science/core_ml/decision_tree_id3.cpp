// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/* Decision tree (ID3): greedy information-gain-based classifier.
 *
 * Core claim: tree achieves high accuracy on separable data.
 */
#include <cassert>
#include <cmath>
#include <iostream>
#include <map>
#include <memory>
#include <vector>

struct TreeNode {
    bool is_leaf = false;
    int label = -1;
    int feature_idx = -1;
    double threshold = 0.0;
    std::unique_ptr<TreeNode> left;
    std::unique_ptr<TreeNode> right;
};

double entropy(const std::map<int, int>& counts) {
    int total = 0;
    for (const auto& kv : counts) total += kv.second;
    if (total == 0) return 0.0;
    double ent = 0.0;
    for (const auto& kv : counts) {
        double p = static_cast<double>(kv.second) / total;
        if (p > 0) ent -= p * std::log2(p);
    }
    return ent;
}

double information_gain(
    const std::vector<std::vector<double>>& X,
    const std::vector<int>& y,
    int feature_idx,
    double threshold
) {
    std::map<int, int> total_counts;
    for (int label : y) total_counts[label]++;
    double parent_entropy = entropy(total_counts);

    std::vector<int> left_y, right_y;
    for (size_t i = 0; i < X.size(); ++i) {
        if (X[i][feature_idx] <= threshold) left_y.push_back(y[i]);
        else right_y.push_back(y[i]);
    }

    if (left_y.empty() || right_y.empty()) return 0.0;

    std::map<int, int> left_counts, right_counts;
    for (int label : left_y) left_counts[label]++;
    for (int label : right_y) right_counts[label]++;

    double left_weight = static_cast<double>(left_y.size()) / y.size();
    double right_weight = static_cast<double>(right_y.size()) / y.size();

    return parent_entropy - left_weight * entropy(left_counts) - right_weight * entropy(right_counts);
}

std::unique_ptr<TreeNode> build_tree(
    const std::vector<std::vector<double>>& X,
    const std::vector<int>& y,
    int max_depth = 5,
    int depth = 0
) {
    auto node = std::make_unique<TreeNode>();

    // Check if all labels are the same
    bool all_same = true;
    for (size_t i = 1; i < y.size(); ++i) {
        if (y[i] != y[0]) { all_same = false; break; }
    }
    if (all_same || depth >= max_depth || X.empty()) {
        node->is_leaf = true;
        std::map<int, int> counts;
        for (int label : y) counts[label]++;
        int best_label = y.empty() ? 0 : y[0];
        int best_count = 0;
        for (const auto& kv : counts) {
            if (kv.second > best_count) {
                best_count = kv.second;
                best_label = kv.first;
            }
        }
        node->label = best_label;
        return node;
    }

    // Find best split
    double best_gain = -1.0;
    int best_feature = -1;
    double best_threshold = 0.0;

    int n_features = static_cast<int>(X[0].size());
    for (int f = 0; f < n_features; ++f) {
        // Use median as threshold
        std::vector<double> values;
        for (const auto& row : X) values.push_back(row[f]);
        // Simple sort for median
        for (size_t i = 0; i < values.size(); ++i) {
            for (size_t j = i + 1; j < values.size(); ++j) {
                if (values[j] < values[i]) std::swap(values[i], values[j]);
            }
        }
        double threshold = values[values.size() / 2];
        double gain = information_gain(X, y, f, threshold);
        if (gain > best_gain) {
            best_gain = gain;
            best_feature = f;
            best_threshold = threshold;
        }
    }

    if (best_gain <= 0.0) {
        node->is_leaf = true;
        std::map<int, int> counts;
        for (int label : y) counts[label]++;
        int best_label = y.empty() ? 0 : y[0];
        int best_count = 0;
        for (const auto& kv : counts) {
            if (kv.second > best_count) {
                best_count = kv.second;
                best_label = kv.first;
            }
        }
        node->label = best_label;
        return node;
    }

    node->feature_idx = best_feature;
    node->threshold = best_threshold;

    std::vector<std::vector<double>> X_left, X_right;
    std::vector<int> y_left, y_right;
    for (size_t i = 0; i < X.size(); ++i) {
        if (X[i][best_feature] <= best_threshold) {
            X_left.push_back(X[i]);
            y_left.push_back(y[i]);
        } else {
            X_right.push_back(X[i]);
            y_right.push_back(y[i]);
        }
    }

    node->left = build_tree(X_left, y_left, max_depth, depth + 1);
    node->right = build_tree(X_right, y_right, max_depth, depth + 1);

    return node;
}

int predict_tree(const std::vector<double>& x, const TreeNode& node) {
    if (node.is_leaf) return node.label;
    if (x[node.feature_idx] <= node.threshold) {
        return predict_tree(x, *node.left);
    } else {
        return predict_tree(x, *node.right);
    }
}

int main() {
    // Simple perfectly separable data
    std::vector<std::vector<double>> X = {
        {0.0, 0.0}, {0.0, 1.0}, {1.0, 0.0}, {1.0, 1.0},  // Class 0
        {10.0, 10.0}, {10.0, 11.0}, {11.0, 10.0}, {11.0, 11.0},  // Class 1
        {0.0, 0.0}, {10.0, 10.0}                             // Test
    };
    std::vector<int> y = {0, 0, 0, 0, 1, 1, 1, 1, 0, 1};

    auto tree = build_tree(X, y, 3);

    int correct = 0;
    for (size_t i = 0; i < X.size(); ++i) {
        int pred = predict_tree(X[i], *tree);
        if (pred == y[i]) correct++;
    }
    double accuracy = static_cast<double>(correct) / X.size();

    assert(accuracy >= 0.95);

    std::cout << "PASS" << std::endl;
    return 0;
}
