// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Hoeffding tree (VFDT) lite -- a streaming decision stump with a Hoeffding-bound split test.
 */

#include <vector>
#include <map>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>
#include <utility>
#include <algorithm>

double entropy(const std::map<int, int>& counts) {
    int tot = 0;
    for (const auto& kv : counts) tot += kv.second;
    if (tot == 0) return 0.0;
    double h = 0.0;
    for (const auto& kv : counts) {
        if (kv.second > 0) {
            double p = static_cast<double>(kv.second) / tot;
            h -= p * std::log2(p);
        }
    }
    return h;
}

double gain(const std::map<int, int>& left, const std::map<int, int>& right) {
    int nl = 0, nr = 0;
    for (const auto& kv : left) nl += kv.second;
    for (const auto& kv : right) nr += kv.second;
    int n = nl + nr;
    if (n == 0) return 0.0;

    std::map<int, int> parent;
    for (const auto& kv : left) parent[kv.first] += kv.second;
    for (const auto& kv : right) parent[kv.first] += kv.second;

    return entropy(parent) - (nl / static_cast<double>(n)) * entropy(left) -
                             (nr / static_cast<double>(n)) * entropy(right);
}

std::tuple<int, double, int, int, int> hoeffding_tree_lite(
    const std::vector<std::pair<double, double>>& X,
    const std::vector<int>& y,
    const std::vector<double>& thresholds,
    double delta = 1e-6
) {
    int n_feat = 2;

    std::map<std::pair<int, double>, std::pair<std::map<int, int>, std::map<int, int>>> counts;
    for (int f = 0; f < n_feat; ++f) {
        for (double thr : thresholds) {
            counts[{f, thr}] = {{}, {}};
        }
    }

    for (size_t i = 0; i < X.size(); ++i) {
        for (auto& kv : counts) {
            int f = kv.first.first;
            double thr = kv.first.second;
            auto& lc = kv.second.first;
            auto& rc = kv.second.second;
            double val = (f == 0) ? X[i].first : X[i].second;
            if (val <= thr) lc[y[i]]++;
            else rc[y[i]]++;
        }
    }

    int n = static_cast<int>(X.size());
    if (n < 50) return {-1, 0.0, 0, 0, n};

    std::vector<std::tuple<double, int, double>> gains;
    for (const auto& kv : counts) {
        gains.push_back({gain(kv.second.first, kv.second.second), kv.first.first, kv.first.second});
    }
    std::sort(gains.begin(), gains.end(), [](const auto& a, const auto& b) {
        return std::get<0>(a) > std::get<0>(b);
    });

    double eps = std::sqrt(1.0 * std::log(1.0 / delta) / (2.0 * n));
    if (std::get<0>(gains[0]) - std::get<0>(gains[1]) > eps && std::get<0>(gains[0]) > 0.0) {
        int bf = std::get<1>(gains[0]);
        double bthr = std::get<2>(gains[0]);
        const auto& best_counts = counts.at({bf, bthr});
        int lp = 0, rp = 0;
        if (!best_counts.first.empty()) {
            lp = std::max_element(best_counts.first.begin(), best_counts.first.end(),
                [](const auto& a, const auto& b) { return a.second < b.second; })->first;
        }
        if (!best_counts.second.empty()) {
            rp = std::max_element(best_counts.second.begin(), best_counts.second.end(),
                [](const auto& a, const auto& b) { return a.second < b.second; })->first;
        }
        return {bf, bthr, lp, rp, n};
    }

    return {-1, 0.0, 0, 0, n};
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform(0.0, 1.0);

    std::vector<double> thresholds;
    for (int i = 1; i < 10; ++i) thresholds.push_back(i / 10.0);

    auto make = [&](int n) {
        std::vector<std::pair<double, double>> X;
        std::vector<int> y;
        for (int i = 0; i < n; ++i) {
            X.push_back({uniform(rng), uniform(rng)});
            y.push_back((X.back().first > 0.6) ? 1 : 0);
        }
        return std::make_pair(X, y);
    };

    auto train_pair = make(2000);
    const auto& Xtr = train_pair.first;
    const auto& ytr = train_pair.second;
    auto test_pair = make(2000);
    const auto& Xte = test_pair.first;
    const auto& yte = test_pair.second;

    auto tree_result = hoeffding_tree_lite(Xtr, ytr, thresholds);
    int bf = std::get<0>(tree_result);
    double bthr = std::get<1>(tree_result);
    int lp = std::get<2>(tree_result);
    int rp = std::get<3>(tree_result);
    int n_seen = std::get<4>(tree_result);
    assert(n_seen == 2000);

    auto stump_acc = [lp, rp, bf, bthr](const std::vector<std::pair<double, double>>& X,
                                       const std::vector<int>& y) {
        int correct = 0;
        for (size_t i = 0; i < X.size(); ++i) {
            double val = (bf == 0) ? X[i].first : X[i].second;
            int pred = (val <= bthr) ? lp : rp;
            if (pred == y[i]) correct++;
        }
        return static_cast<double>(correct) / y.size();
    };

    double stream_acc = stump_acc(Xte, yte);

    int majority_count = std::max(
        static_cast<int>(std::count(yte.begin(), yte.end(), 0)),
        static_cast<int>(std::count(yte.begin(), yte.end(), 1)));
    double majority = static_cast<double>(majority_count) / yte.size();


    // Batch (offline) decision stump for parity: exhaustive threshold search over same grid
    double batch_acc = 0.0;
    {
        double batch_best_acc = -1.0;
        for (int f = 0; f < 2; ++f) {
            for (double thr : thresholds) {
                int lp_f = 0, rp_f = 0;
                std::map<int, int> lc, rc;
                for (size_t i = 0; i < Xtr.size(); ++i) {
                    double val = (f == 0) ? Xtr[i].first : Xtr[i].second;
                    if (val <= thr) lc[ytr[i]]++;
                    else rc[ytr[i]]++;
                }
                if (!lc.empty()) lp_f = std::max_element(lc.begin(), lc.end(),
                    [](const auto& a, const auto& b) { return a.second < b.second; })->first;
                if (!rc.empty()) rp_f = std::max_element(rc.begin(), rc.end(),
                    [](const auto& a, const auto& b) { return a.second < b.second; })->first;
                int correct = 0;
                for (size_t i = 0; i < Xte.size(); ++i) {
                    double val = (f == 0) ? Xte[i].first : Xte[i].second;
                    int pred = (val <= thr) ? lp_f : rp_f;
                    if (pred == yte[i]) correct++;
                }
                double acc = static_cast<double>(correct) / yte.size();
                if (acc > batch_best_acc) {
                    batch_best_acc = acc;
                }
            }
        }
        batch_acc = batch_best_acc;
    }

    assert(std::abs(stream_acc - batch_acc) < 0.03);
    assert(bf == 0);
    assert(stream_acc > majority + 0.25);

    std::cout << "hoeffding_tree_lite.cpp PASS" << std::endl;
    return 0;
}
