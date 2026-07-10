// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <random>
#include <cassert>

// Logistic function.
double logistic(double x) {
    if (x > 100.0) return 1.0;
    if (x < -100.0) return 0.0;
    return 1.0 / (1.0 + std::exp(-x));
}

std::vector<double> estimate_propensity(const std::vector<double>& x, const std::vector<int>& t) {
    size_t n = x.size();
    double beta = 0.0;
    for (int iter = 0; iter < 50; ++iter) {
        double grad = 0.0;
        for (size_t i = 0; i < n; ++i) {
            grad += (t[i] - logistic(beta * x[i])) * x[i];
        }
        beta += 0.01 * grad / static_cast<double>(n);
    }
    std::vector<double> p;
    for (double xi : x) p.push_back(logistic(beta * xi));
    return p;
}

std::pair<double, double> stratify_by_propensity(const std::vector<double>& propensity,
                                                const std::vector<int>& t,
                                                const std::vector<double>& y,
                                                int num_strata = 5) {
    size_t n = propensity.size();

    std::vector<size_t> sorted_indices(n);
    for (size_t i = 0; i < n; ++i) sorted_indices[i] = i;
    std::sort(sorted_indices.begin(), sorted_indices.end(),
              [&](size_t a, size_t b) { return propensity[a] < propensity[b]; });

    size_t stratum_size = n / num_strata;
    double stratified_ate = 0.0;

    for (int s = 0; s < num_strata; ++s) {
        size_t start = s * stratum_size;
        size_t end = (s < num_strata - 1) ? start + stratum_size : n;

        double t1_sum = 0.0, t0_sum = 0.0;
        size_t t1_count = 0, t0_count = 0;
        for (size_t idx = start; idx < end; ++idx) {
            size_t i = sorted_indices[idx];
            if (t[i] == 1) {
                t1_sum += y[i];
                t1_count++;
            } else {
                t0_sum += y[i];
                t0_count++;
            }
        }

        if (t1_count > 0 && t0_count > 0) {
            double ate_s = t1_sum / static_cast<double>(t1_count) - t0_sum / static_cast<double>(t0_count);
            stratified_ate += ate_s * static_cast<double>(end - start) / static_cast<double>(n);
        }
    }

    double t1_sum_all = 0.0, t0_sum_all = 0.0;
    size_t t1_count_all = 0, t0_count_all = 0;
    for (size_t i = 0; i < n; ++i) {
        if (t[i] == 1) {
            t1_sum_all += y[i];
            t1_count_all++;
        } else {
            t0_sum_all += y[i];
            t0_count_all++;
        }
    }
    double naive_ate = t1_sum_all / static_cast<double>(t1_count_all) - t0_sum_all / static_cast<double>(t0_count_all);

    return {stratified_ate, naive_ate};
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> gauss(0.0, 1.0);
    std::uniform_real_distribution<double> uniform(0.0, 1.0);

    int n = 200;
    std::vector<double> x;
    for (int i = 0; i < n; ++i) x.push_back(gauss(rng));

    std::vector<int> t;
    for (int i = 0; i < n; ++i) t.push_back(uniform(rng) < logistic(1.5 * x[i]) ? 1 : 0);

    std::vector<double> y;
    for (int i = 0; i < n; ++i) y.push_back(2.0 * t[i] + 1.2 * x[i] + 0.5 * gauss(rng));

    auto propensity = estimate_propensity(x, t);
    auto [stratified_ate, naive_ate] = stratify_by_propensity(propensity, t, y, 5);

    assert(std::abs(stratified_ate - 2.0) < 0.7);
    assert(std::abs(naive_ate - 2.0) > 0.3);
    assert(std::abs(stratified_ate - 2.0) < std::abs(naive_ate - 2.0) + 0.1);

    std::cout << "stratification_subclassification: PASS" << std::endl;
    return 0;
}
