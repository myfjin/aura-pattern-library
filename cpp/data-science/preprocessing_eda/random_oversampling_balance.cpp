// random_oversampling_balance.cpp — Random oversampling and SMOTE-lite for class balance.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <random>
#include <vector>

using Sample = std::vector<double>;

static std::pair<std::vector<Sample>, std::vector<int>> random_oversample(
        const std::vector<Sample>& X, const std::vector<int>& y,
        std::mt19937& rng) {
    int count0 = static_cast<int>(std::count(y.begin(), y.end(), 0));
    int count1 = static_cast<int>(std::count(y.begin(), y.end(), 1));
    if (count0 == count1) return {X, y};

    int minority_label = (count0 > count1) ? 1 : 0;
    int majority_count = std::max(count0, count1);

    std::vector<Sample> X_res = X;
    std::vector<int> y_res = y;

    std::vector<int> minority_indices;
    for (std::size_t i = 0; i < y.size(); ++i)
        if (y[i] == minority_label) minority_indices.push_back(static_cast<int>(i));

    std::uniform_int_distribution<int> pick(0, static_cast<int>(minority_indices.size()) - 1);
    while (static_cast<int>(std::count(y_res.begin(), y_res.end(), minority_label)) < majority_count) {
        int idx = minority_indices[pick(rng)];
        X_res.push_back(X[idx]);
        y_res.push_back(minority_label);
    }
    return {X_res, y_res};
}

static std::pair<std::vector<Sample>, std::vector<int>> smote_lite(
        const std::vector<Sample>& X, const std::vector<int>& y, int k,
        std::mt19937& rng) {
    (void)k;  // kept to match the oracle signature
    int count0 = static_cast<int>(std::count(y.begin(), y.end(), 0));
    int count1 = static_cast<int>(std::count(y.begin(), y.end(), 1));
    if (count0 == count1) return {X, y};

    int minority_label = (count0 > count1) ? 1 : 0;
    int majority_count = std::max(count0, count1);

    std::vector<int> minority_indices;
    for (std::size_t i = 0; i < y.size(); ++i)
        if (y[i] == minority_label) minority_indices.push_back(static_cast<int>(i));
    int n_minority = static_cast<int>(minority_indices.size());
    int n_to_generate = majority_count - n_minority;

    std::vector<Sample> X_syn = X;
    std::vector<int> y_syn = y;

    std::uniform_int_distribution<int> pick(0, n_minority - 1);
    std::uniform_real_distribution<double> alpha_dist(0.0, 1.0);
    for (int g = 0; g < n_to_generate; ++g) {
        int idx1 = minority_indices[pick(rng)];
        int idx2 = minority_indices[pick(rng)];
        const Sample& a = X[idx1];
        const Sample& b = X[idx2];
        double alpha = alpha_dist(rng);
        Sample synthetic(a.size());
        for (std::size_t j = 0; j < a.size(); ++j)
            synthetic[j] = a[j] + alpha * (b[j] - a[j]);
        X_syn.push_back(std::move(synthetic));
        y_syn.push_back(minority_label);
    }
    return {X_syn, y_syn};
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> norm(0.0, 1.0);

    int n0 = 100, n1 = 20;
    std::vector<Sample> X;
    std::vector<int> y;
    for (int i = 0; i < n0; ++i) {
        Sample s(5);
        for (int j = 0; j < 5; ++j) s[j] = norm(rng);
        X.push_back(s);
        y.push_back(0);
    }
    for (int i = 0; i < n1; ++i) {
        Sample s(5);
        for (int j = 0; j < 5; ++j) s[j] = 5.0 + norm(rng);
        X.push_back(s);
        y.push_back(1);
    }

    int count0_before = static_cast<int>(std::count(y.begin(), y.end(), 0));
    int count1_before = static_cast<int>(std::count(y.begin(), y.end(), 1));

    auto [X_over, y_over] = random_oversample(X, y, rng);
    int count0_after = static_cast<int>(std::count(y_over.begin(), y_over.end(), 0));
    int count1_after = static_cast<int>(std::count(y_over.begin(), y_over.end(), 1));

    assert(count0_after == count1_after);
    assert(count0_after == count0_before);
    assert(count1_after > count1_before);

    auto [X_smote, y_smote] = smote_lite(X, y, 3, rng);
    int count0_smote = static_cast<int>(std::count(y_smote.begin(), y_smote.end(), 0));
    int count1_smote = static_cast<int>(std::count(y_smote.begin(), y_smote.end(), 1));

    assert(count0_smote == count1_smote);
    assert(count0_smote == count0_before);
    assert(X_smote.size() > X.size());

    std::printf("random_oversampling_balance.cpp: PASS\n");
    return 0;
}
