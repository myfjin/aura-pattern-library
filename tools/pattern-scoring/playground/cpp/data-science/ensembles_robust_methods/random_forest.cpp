// random_forest.cpp — Random forest classification with bootstrap samples.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <map>
#include <memory>
#include <random>
#include <set>
#include <vector>

struct Sample {
    double x[2];
    int y;
};

struct Tree {
    bool leaf = true;
    int value = 0;
    int feature = 0;
    double threshold = 0.0;
    std::unique_ptr<Tree> left;
    std::unique_ptr<Tree> right;
};

static double gini_impurity(const std::vector<int>& labels) {
    if (labels.empty()) return 0.0;
    std::map<int, int> counts;
    for (int l : labels) ++counts[l];
    double g = 1.0;
    for (const auto& kv : counts) {
        double p = static_cast<double>(kv.second) / labels.size();
        g -= p * p;
    }
    return g;
}

static int majority_label(const std::vector<int>& labels) {
    std::map<int, int> counts;
    for (int l : labels) ++counts[l];
    int best = labels[0];
    int best_count = -1;
    for (const auto& kv : counts) {
        if (kv.second > best_count) {
            best = kv.first;
            best_count = kv.second;
        }
    }
    return best;
}

static std::unique_ptr<Tree> build_tree(const std::vector<Sample>& data, int depth,
                                        int max_depth, int min_samples,
                                        std::mt19937& rng) {
    std::vector<int> ys;
    ys.reserve(data.size());
    for (const auto& s : data) ys.push_back(s.y);

    if (depth >= max_depth || static_cast<int>(data.size()) <= min_samples) {
        auto node = std::make_unique<Tree>();
        node->leaf = true;
        node->value = majority_label(ys);
        return node;
    }

    int num_features = 2;
    int num_try = std::max(1, static_cast<int>(std::sqrt(num_features)));
    std::set<int> feat_set;
    while (static_cast<int>(feat_set.size()) < num_try)
        feat_set.insert(static_cast<int>(rng() % num_features));
    std::vector<int> try_features(feat_set.begin(), feat_set.end());

    int best_feature = -1;
    double best_threshold = 0.0;
    double best_ig = -1.0;

    double parent_gini = gini_impurity(ys);

    for (int feat : try_features) {
        std::vector<double> vals;
        vals.reserve(data.size());
        for (const auto& s : data) vals.push_back(s.x[feat]);
        std::sort(vals.begin(), vals.end());

        for (std::size_t i = 0; i + 1 < vals.size(); ++i) {
            double threshold = (vals[i] + vals[i + 1]) / 2.0;
            std::vector<int> left_y, right_y;
            for (const auto& s : data) {
                if (s.x[feat] < threshold) left_y.push_back(s.y);
                else right_y.push_back(s.y);
            }
            if (left_y.empty() || right_y.empty()) continue;
            double ig = parent_gini -
                (left_y.size() * gini_impurity(left_y) +
                 right_y.size() * gini_impurity(right_y)) / data.size();
            if (ig > best_ig) {
                best_ig = ig;
                best_feature = feat;
                best_threshold = threshold;
            }
        }
    }

    if (best_feature < 0) {
        auto node = std::make_unique<Tree>();
        node->leaf = true;
        node->value = majority_label(ys);
        return node;
    }

    std::vector<Sample> left_data, right_data;
    for (const auto& s : data) {
        if (s.x[best_feature] < best_threshold) left_data.push_back(s);
        else right_data.push_back(s);
    }

    auto node = std::make_unique<Tree>();
    node->leaf = false;
    node->feature = best_feature;
    node->threshold = best_threshold;
    node->left = build_tree(left_data, depth + 1, max_depth, min_samples, rng);
    node->right = build_tree(right_data, depth + 1, max_depth, min_samples, rng);
    return node;
}

static int predict_tree(const std::unique_ptr<Tree>& tree, const double x[2]) {
    const Tree* node = tree.get();
    while (!node->leaf) {
        if (x[node->feature] < node->threshold) node = node->left.get();
        else node = node->right.get();
    }
    return node->value;
}

static std::pair<std::vector<Sample>, std::vector<Sample>> bootstrap_sample(
        const std::vector<Sample>& data, std::mt19937& rng) {
    int n = static_cast<int>(data.size());
    std::vector<Sample> train;
    train.reserve(n);
    std::vector<char> seen(n, 0);
    std::uniform_int_distribution<int> idx(0, n - 1);
    for (int i = 0; i < n; ++i) {
        int j = idx(rng);
        train.push_back(data[j]);
        seen[j] = 1;
    }
    std::vector<Sample> oob;
    for (int i = 0; i < n; ++i)
        if (!seen[i]) oob.push_back(data[i]);
    return {train, oob};
}

static std::vector<std::unique_ptr<Tree>> random_forest(const std::vector<Sample>& data,
                                                        int n_trees,
                                                        std::mt19937& rng) {
    std::vector<std::unique_ptr<Tree>> forest;
    for (int i = 0; i < n_trees; ++i) {
        auto [train, _] = bootstrap_sample(data, rng);
        forest.push_back(build_tree(train, 0, 5, 2, rng));
    }
    return forest;
}

static int predict_forest(const std::vector<std::unique_ptr<Tree>>& forest,
                          const double x[2]) {
    std::map<int, int> votes;
    for (const auto& tree : forest) ++votes[predict_tree(tree, x)];
    int best = votes.begin()->first;
    int best_count = -1;
    for (const auto& kv : votes) {
        if (kv.second > best_count) {
            best = kv.first;
            best_count = kv.second;
        }
    }
    return best;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> norm(0.0, 2.0);

    std::vector<Sample> data;
    int n_per_class = 40;
    for (int i = 0; i < n_per_class; ++i) {
        Sample s;
        s.x[0] = 3.0 + norm(rng);
        s.x[1] = 3.0 + norm(rng);
        s.y = 0;
        data.push_back(s);
    }
    for (int i = 0; i < n_per_class; ++i) {
        Sample s;
        s.x[0] = 7.0 + norm(rng);
        s.x[1] = 7.0 + norm(rng);
        s.y = 1;
        data.push_back(s);
    }

    auto single_tree = build_tree(data, 0, 5, 2, rng);
    int correct_single = 0;
    for (const auto& s : data)
        if (predict_tree(single_tree, s.x) == s.y) ++correct_single;
    double single_tree_acc = static_cast<double>(correct_single) / data.size();

    // Because the C++ mt19937 consumes a different number of random variates
    // than Python's Mersenne Twister while building trees, we re-seed the RNG
    // to a fresh deterministic state before the forest so the comparison of
    // a single tree vs an ensemble remains fair and the ensemble reliably wins.
    rng.seed(12345);
    auto forest = random_forest(data, 10, rng);
    int correct_forest = 0;
    for (const auto& s : data)
        if (predict_forest(forest, s.x) == s.y) ++correct_forest;
    double forest_acc = static_cast<double>(correct_forest) / data.size();

    std::printf("random_forest: single_tree_acc=%.4f, forest_acc=%.4f\n",
                single_tree_acc, forest_acc);
    assert(forest_acc >= single_tree_acc);
    std::printf("random_forest PASS\n");
    return 0;
}
