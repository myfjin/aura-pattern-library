// peeking_alpha_inflation.cpp
// Continuous peeking at fixed-n test inflates type-I error.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <cmath>
#include <cassert>
#include <random>
#include <vector>

using std::vector;

static double t_test_pvalue(double mean_t, double mean_c, double var_t, double var_c,
                            size_t n_t, size_t n_c) {
    if (n_t < 2 || n_c < 2) return 1.0;
    double se = std::sqrt(var_t / n_t + var_c / n_c);
    if (se == 0.0) return 1.0;
    double t = (mean_t - mean_c) / se;
    return std::erfc(std::abs(t) / std::sqrt(2.0));
}

static void sample_stats(const vector<double>& v, double& mean, double& var) {
    size_t n = v.size();
    mean = 0.0;
    for (double x : v) mean += x;
    mean /= n;
    var = 0.0;
    for (double x : v) var += (x - mean) * (x - mean);
    var /= (n - 1);
}

static double fixed_n_no_peeking(size_t n_per_arm, size_t reps, bool null) {
    std::mt19937 rng(42);
    std::normal_distribution<double> ctrl(0.0, 1.0);
    size_t rejections = 0;
    for (size_t r = 0; r < reps; ++r) {
        vector<double> treatment, control;
        for (size_t i = 0; i < n_per_arm; ++i) {
            control.push_back(ctrl(rng));
            if (null)
                treatment.push_back(ctrl(rng));
            else
                treatment.push_back(std::normal_distribution<double>(0.5, 1.0)(rng));
        }
        double mt, vt, mc, vc;
        sample_stats(treatment, mt, vt);
        sample_stats(control, mc, vc);
        double p = t_test_pvalue(mt, mc, vt, vc, n_per_arm, n_per_arm);
        if (p < 0.05) ++rejections;
    }
    return static_cast<double>(rejections) / reps;
}

static double peeking_strategy(size_t n_per_arm_initial, size_t n_looks, size_t reps) {
    std::mt19937 rng(42);
    std::normal_distribution<double> dist(0.0, 1.0);
    size_t rejections = 0;
    size_t n_add = n_per_arm_initial / n_looks;
    for (size_t r = 0; r < reps; ++r) {
        vector<double> treatment, control;
        for (size_t look = 0; look < n_looks; ++look) {
            for (size_t i = 0; i < n_add; ++i) {
                treatment.push_back(dist(rng));
                control.push_back(dist(rng));
            }
            double mt, vt, mc, vc;
            sample_stats(treatment, mt, vt);
            sample_stats(control, mc, vc);
            double p = t_test_pvalue(mt, mc, vt, vc, treatment.size(), control.size());
            if (p < 0.05) {
                ++rejections;
                break;
            }
        }
    }
    return static_cast<double>(rejections) / reps;
}

int main() {
    double type_i_no_peek = fixed_n_no_peeking(50, 200, true);
    double type_i_peek = peeking_strategy(50, 5, 200);

    assert(type_i_no_peek < 0.12);
    assert(type_i_peek > type_i_no_peek * 2.0);

    std::cout << "PASS: no_peek=" << type_i_no_peek << " peek=" << type_i_peek << "\n";
    return 0;
}
