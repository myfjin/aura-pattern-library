// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Stratified treatment randomization vs simple randomization.
 * Splits units into two strata at the covariate median, then assigns half of
 * each stratum to treatment, forcing covariate balance the coin-flip design
 * cannot guarantee. Use to allocate treatment when a prognostic covariate should
 * be balanced across arms. Oracle over 50 replications: stratified covariate
 * imbalance is no worse than simple randomization and the ATE variance stays
 * comparable (within 10%).
 */
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <random>
#include <cassert>

std::vector<int> simple_randomization(int n, int seed) {
    std::mt19937 rng(seed);
    std::uniform_int_distribution<int> dist(0, 1);
    std::vector<int> out;
    for (int i = 0; i < n; ++i) out.push_back(dist(rng));
    return out;
}

std::vector<int> stratified_randomization(const std::vector<double>& x, int seed) {
    std::mt19937 rng(seed);
    std::vector<double> sorted_x = x;
    std::sort(sorted_x.begin(), sorted_x.end());
    double median_x = sorted_x[sorted_x.size() / 2];

    std::vector<size_t> strata_0, strata_1;
    for (size_t i = 0; i < x.size(); ++i) {
        if (x[i] <= median_x) strata_0.push_back(i);
        else strata_1.push_back(i);
    }

    std::vector<int> t_all(x.size(), 0);
    std::shuffle(strata_0.begin(), strata_0.end(), rng);
    std::shuffle(strata_1.begin(), strata_1.end(), rng);
    for (size_t i = 0; i < strata_0.size() / 2; ++i) t_all[strata_0[i]] = 1;
    for (size_t i = 0; i < strata_1.size() / 2; ++i) t_all[strata_1[i]] = 1;

    return t_all;
}

double covariate_balance(const std::vector<double>& x, const std::vector<int>& t) {
    double s1 = 0.0, s0 = 0.0;
    size_t c1 = 0, c0 = 0;
    for (size_t i = 0; i < x.size(); ++i) {
        if (t[i] == 1) { s1 += x[i]; c1++; }
        else { s0 += x[i]; c0++; }
    }
    if (c1 == 0 || c0 == 0) return 0.0;
    return std::abs(s1 / static_cast<double>(c1) - s0 / static_cast<double>(c0));
}

double ate_variance(const std::vector<int>& t, const std::vector<double>& y) {
    std::vector<double> y_t1, y_t0;
    for (size_t i = 0; i < t.size(); ++i) {
        if (t[i] == 1) y_t1.push_back(y[i]);
        else y_t0.push_back(y[i]);
    }
    if (y_t1.size() < 2 || y_t0.size() < 2) return 0.0;

    auto sample_var = [](const std::vector<double>& v) {
        double mean = 0.0;
        for (double x : v) mean += x;
        mean /= v.size();
        double s = 0.0;
        for (double x : v) s += (x - mean) * (x - mean);
        return s / static_cast<double>(v.size() - 1);
    };

    return sample_var(y_t1) / static_cast<double>(y_t1.size())
         + sample_var(y_t0) / static_cast<double>(y_t0.size());
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> gauss(0.0, 1.0);
    std::uniform_int_distribution<int> binary(0, 1);

    int n = 200;
    int reps = 50;

    std::vector<double> x;
    for (int i = 0; i < n; ++i) x.push_back(gauss(rng));

    double avg_balance_simple = 0.0, avg_balance_strat = 0.0;
    double avg_var_simple = 0.0, avg_var_strat = 0.0;

    for (int rep = 0; rep < reps; ++rep) {
        std::vector<double> y;
        for (int i = 0; i < n; ++i) {
            y.push_back(2.0 * binary(rng) + 0.8 * x[i] + 0.5 * gauss(rng));
        }

        auto t_simple = simple_randomization(n, 42 + rep);
        avg_balance_simple += covariate_balance(x, t_simple);
        avg_var_simple += ate_variance(t_simple, y);

        auto t_strat = stratified_randomization(x, 42 + rep);
        avg_balance_strat += covariate_balance(x, t_strat);
        avg_var_strat += ate_variance(t_strat, y);
    }

    avg_balance_simple /= reps;
    avg_balance_strat /= reps;
    avg_var_simple /= reps;
    avg_var_strat /= reps;

    assert(avg_balance_strat < avg_balance_simple + 0.01);
    assert(avg_var_strat < avg_var_simple * 1.1);

    std::cout << "stratified_randomization: PASS" << std::endl;
    return 0;
}
