// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Heterogeneous treatment effects (CATE): treatment effect varies by subgroup.
 */

#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>
#include <algorithm>

double subgroup_ate(const std::vector<int>& t, const std::vector<double>& y,
                    const std::vector<int>& subgroup, int sg_val) {
    std::vector<double> y_t1, y_t0;
    for (size_t i = 0; i < t.size(); ++i) {
        if (subgroup[i] == sg_val) {
            if (t[i] == 1) y_t1.push_back(y[i]);
            else y_t0.push_back(y[i]);
        }
    }
    if (y_t1.empty() || y_t0.empty()) return 0.0;

    double sum_t1 = 0.0, sum_t0 = 0.0;
    for (double v : y_t1) sum_t1 += v;
    for (double v : y_t0) sum_t0 += v;
    return sum_t1 / y_t1.size() - sum_t0 / y_t0.size();
}

double pooled_ate(const std::vector<int>& t, const std::vector<double>& y) {
    std::vector<double> y_t1, y_t0;
    for (size_t i = 0; i < t.size(); ++i) {
        if (t[i] == 1) y_t1.push_back(y[i]);
        else y_t0.push_back(y[i]);
    }
    if (y_t1.empty() || y_t0.empty()) return 0.0;

    double sum_t1 = 0.0, sum_t0 = 0.0;
    for (double v : y_t1) sum_t1 += v;
    for (double v : y_t0) sum_t0 += v;
    return sum_t1 / y_t1.size() - sum_t0 / y_t0.size();
}

int main() {
    std::mt19937 rng(42);
    std::uniform_int_distribution<int> uniform01(0, 1);
    std::normal_distribution<double> normal(0.0, 0.5);

    const int n = 200;
    std::vector<int> subgroup, t;
    std::vector<double> y;

    for (int i = 0; i < n; ++i) {
        subgroup.push_back(uniform01(rng));
        t.push_back(uniform01(rng));
        double effect = (subgroup[i] == 0) ? 1.0 : 3.0;
        y.push_back(effect * t[i] + normal(rng));
    }

    double ate_group_0 = subgroup_ate(t, y, subgroup, 0);
    double ate_group_1 = subgroup_ate(t, y, subgroup, 1);
    double ate_pooled = pooled_ate(t, y);

    assert(std::abs(ate_group_0 - 1.0) < 0.5);
    assert(std::abs(ate_group_1 - 3.0) < 0.5);
    assert(std::abs(ate_group_1 - ate_group_0) > 1.0);
    assert(std::min(ate_group_0, ate_group_1) < ate_pooled &&
           ate_pooled < std::max(ate_group_0, ate_group_1) + 0.3);

    std::cout << "heterogeneous_effects_subgroups.cpp PASS" << std::endl;
    return 0;
}
