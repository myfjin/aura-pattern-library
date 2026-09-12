// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Three-way (train/validation/test) split that preserves per-class proportions. It
 * groups sample indices by label, shuffles each group with a deterministic LCG, then
 * slices each class by the train/val/test fractions so every split mirrors the overall
 * class balance. Fractions must sum to 1.
 * Use to carve a labeled dataset into three folds without skewing class ratios.
 * Guarantees: the three splits cover every sample, are pairwise disjoint (no leakage),
 * and each class proportion matches the full-set proportion within 0.05.
 */
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <functional>
#include <iostream>
#include <iomanip>
#include <map>
#include <numeric>
#include <random>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

// Three-way stratified split preserving class proportions.

static uint64_t rng_state = 0x123456789abcdef0ULL;
static double uniform01() {
    rng_state = rng_state * 6364136223846793005ULL + 1442695040888963407ULL;
    return ((rng_state >> 11) & 0x1FFFFFFFFFFFFFULL) / 9007199254740992.0;
}

void shuffle(vector<int>& v) {
    for (size_t i = v.size(); i > 0; --i) {
        size_t j = (size_t)(uniform01() * i);
        if (j == i) j = i - 1;
        swap(v[i-1], v[j]);
    }
}

struct SplitResult {
    vector<int> train_data, val_data, test_data;
    vector<int> train_labels, val_labels, test_labels;
};

SplitResult stratified_split(const vector<int>& data, const vector<int>& labels, double f_train, double f_val, double f_test) {
    assert(fabs(f_train+f_val+f_test - 1.0) < 0.01);
    unordered_map<int, vector<int>> groups;
    for (size_t i=0;i<labels.size();++i) groups[labels[i]].push_back((int)i);
    vector<int> train_idx, val_idx, test_idx;
    for (auto& kv : groups) {
        shuffle(kv.second);
        int n = (int)kv.second.size();
        int n_train = max(1, (int)(n * f_train));
        int n_val = max(1, (int)(n * f_val));
        int n_test = n - n_train - n_val;
        (void)n_test;
        for (int i=0;i<n_train;++i) train_idx.push_back(kv.second[i]);
        for (int i=n_train;i<n_train+n_val;++i) val_idx.push_back(kv.second[i]);
        for (int i=n_train+n_val;i<n;++i) test_idx.push_back(kv.second[i]);
    }
    shuffle(train_idx); shuffle(val_idx); shuffle(test_idx);
    SplitResult r;
    for (int i : train_idx) { r.train_data.push_back(data[i]); r.train_labels.push_back(labels[i]); }
    for (int i : val_idx) { r.val_data.push_back(data[i]); r.val_labels.push_back(labels[i]); }
    for (int i : test_idx) { r.test_data.push_back(data[i]); r.test_labels.push_back(labels[i]); }
    return r;
}

unordered_map<int,double> class_proportion(const vector<int>& labels) {
    unordered_map<int,int> counts;
    for (int l : labels) counts[l]++;
    unordered_map<int,double> prop;
    for (const auto& kv : counts) prop[kv.first] = (double)kv.second / (double)labels.size();
    return prop;
}

int main() {
    int n0=70, n1=30;
    vector<int> data(n0+n1), labels(n0+n1);
    iota(data.begin(), data.end(), 0);
    for (int i=0;i<n0;++i) labels[i]=0;
    for (int i=n0;i<n0+n1;++i) labels[i]=1;

    auto s = stratified_split(data, labels, 0.6, 0.2, 0.2);

    assert(s.train_labels.size()+s.val_labels.size()+s.test_labels.size() == labels.size());

    auto full_prop = class_proportion(labels);
    auto train_prop = class_proportion(s.train_labels);
    auto val_prop = class_proportion(s.val_labels);
    auto test_prop = class_proportion(s.test_labels);

    for (const auto& kv : full_prop) {
        assert(fabs(train_prop[kv.first]-kv.second) < 0.05);
        assert(fabs(val_prop[kv.first]-kv.second) < 0.05);
        assert(fabs(test_prop[kv.first]-kv.second) < 0.05);
    }

    assert(find(s.train_labels.begin(), s.train_labels.end(), 0) != s.train_labels.end());
    assert(find(s.train_labels.begin(), s.train_labels.end(), 1) != s.train_labels.end());
    assert(find(s.val_labels.begin(), s.val_labels.end(), 0) != s.val_labels.end());
    assert(find(s.val_labels.begin(), s.val_labels.end(), 1) != s.val_labels.end());
    assert(find(s.test_labels.begin(), s.test_labels.end(), 0) != s.test_labels.end());
    assert(find(s.test_labels.begin(), s.test_labels.end(), 1) != s.test_labels.end());

    set<int> t(s.train_data.begin(), s.train_data.end()), v(s.val_data.begin(),s.val_data.end()), te(s.test_data.begin(),s.test_data.end());
    vector<int> inter;
    set_intersection(t.begin(), t.end(), v.begin(), v.end(), back_inserter(inter)); assert(inter.empty());
    inter.clear();
    set_intersection(t.begin(), t.end(), te.begin(), te.end(), back_inserter(inter)); assert(inter.empty());
    inter.clear();
    set_intersection(v.begin(), v.end(), te.begin(), te.end(), back_inserter(inter)); assert(inter.empty());

    puts("three_way_stratified_split.cpp: PASS");
    return 0;
}
