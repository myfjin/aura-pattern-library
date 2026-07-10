// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * k-Nearest Neighbors Classifier (from scratch).
 *
 * Oracle asserts:
 *   accuracy >= 0.8
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <random>
#include <algorithm>
#include <map>

double euclidean_distance(const std::vector<double>& p1,
                          const std::vector<double>& p2) {
    double s = 0.0;
    for (size_t i = 0; i < p1.size(); ++i) s += (p1[i] - p2[i]) * (p1[i] - p2[i]);
    return std::sqrt(s);
}

int knn_predict(const std::vector<double>& x_test,
                const std::vector<std::vector<double>>& X_train,
                const std::vector<int>& y_train,
                int k) {
    std::vector<std::pair<double, int>> distances;
    for (size_t i = 0; i < X_train.size(); ++i) {
        distances.push_back({euclidean_distance(x_test, X_train[i]), y_train[i]});
    }
    std::sort(distances.begin(), distances.end());
    std::map<int, int> votes;
    for (int i = 0; i < k; ++i) ++votes[distances[i].second];
    int best = 0, best_count = -1;
    for (const auto& kv : votes) {
        if (kv.second > best_count) { best_count = kv.second; best = kv.first; }
    }
    return best;
}

int main() {
    std::mt19937_64 rng(42);
    std::normal_distribution<double> c0(0.0, 1.0), c1(5.0, 1.0), t0(0.0, 0.8), t1(5.0, 0.8);

    std::vector<std::vector<double>> X_train;
    std::vector<int> y_train;
    for (int i = 0; i < 25; ++i) { X_train.push_back({c0(rng), c0(rng)}); y_train.push_back(0); }
    for (int i = 0; i < 25; ++i) { X_train.push_back({c1(rng), c1(rng)}); y_train.push_back(1); }

    std::vector<std::vector<double>> X_test;
    std::vector<int> y_test;
    for (int i = 0; i < 10; ++i) { X_test.push_back({t0(rng), t0(rng)}); y_test.push_back(0); }
    for (int i = 0; i < 10; ++i) { X_test.push_back({t1(rng), t1(rng)}); y_test.push_back(1); }

    std::vector<int> preds;
    for (const auto& x : X_test) preds.push_back(knn_predict(x, X_train, y_train, 5));

    int correct = 0;
    for (size_t i = 0; i < preds.size(); ++i) if (preds[i] == y_test[i]) ++correct;
    double accuracy = static_cast<double>(correct) / preds.size();
    assert(accuracy >= 0.8);

    std::cout << "knn_classifier.cpp PASS: accuracy=" << accuracy << std::endl;
    return 0;
}
