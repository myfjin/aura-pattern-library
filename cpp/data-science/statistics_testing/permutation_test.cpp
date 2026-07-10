// permutation_test.cpp
// Two-sample permutation test for difference of means.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <cassert>
#include <algorithm>

#include <utility>

using std::vector;
using std::pair;

static pair<double, double> permutation_test(const vector<double>& group_a,
                                      const vector<double>& group_b,
                                      size_t n_perms) {
    vector<double> combined = group_a;
    combined.insert(combined.end(), group_b.begin(), group_b.end());
    size_t n_a = group_a.size();

    double mean_a = 0.0, mean_b = 0.0;
    for (double x : group_a) mean_a += x;
    for (double x : group_b) mean_b += x;
    mean_a /= group_a.size();
    mean_b /= group_b.size();
    double observed = mean_a - mean_b;

    std::mt19937 rng(42);
    size_t count_extreme = 0;
    vector<double> shuffled = combined;

    for (size_t p = 0; p < n_perms; ++p) {
        std::shuffle(shuffled.begin(), shuffled.end(), rng);
        double ma = 0.0, mb = 0.0;
        for (size_t i = 0; i < n_a; ++i) ma += shuffled[i];
        for (size_t i = n_a; i < shuffled.size(); ++i) mb += shuffled[i];
        ma /= n_a;
        mb /= (shuffled.size() - n_a);
        double perm_diff = ma - mb;
        if (std::abs(perm_diff) >= std::abs(observed))
            ++count_extreme;
    }

    return {observed, static_cast<double>(count_extreme) / n_perms};
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> null_dist(10.0, 2.0);
    std::normal_distribution<double> alt_dist(15.0, 2.0);

    vector<double> group_a_null, group_b_null;
    for (int i = 0; i < 20; ++i) {
        group_a_null.push_back(null_dist(rng));
        group_b_null.push_back(null_dist(rng));
    }
    auto [diff_null, p_null] = permutation_test(group_a_null, group_b_null, 5000);
    std::cout << "Null case: diff=" << diff_null << ", p=" << p_null << "\n";
    assert(p_null > 0.05);

    vector<double> group_a_alt, group_b_alt;
    for (int i = 0; i < 20; ++i) {
        group_a_alt.push_back(null_dist(rng));
        group_b_alt.push_back(alt_dist(rng));
    }
    auto [diff_alt, p_alt] = permutation_test(group_a_alt, group_b_alt, 5000);
    std::cout << "Alt case: diff=" << diff_alt << ", p=" << p_alt << "\n";
    assert(p_alt < 0.05);

    std::cout << "Permutation test PASSED\n";
    return 0;
}
