// peeking_alpha_inflation — C++17 twin of the sealed DS oracle.
//
// Claim (mechanism, not tolerance-tuned): continuous peeking at a fixed-n test
// inflates the type-I error rate from the nominal ~5% to ~20-30%. Measured over
// replications under the null hypothesis.
//
// Oracle: ~/ai-lab/patterns_ds/harvested/peeking_alpha_inflation.py
// Seal   : 3abd742ac574c7f6f272dc8d5a9f2077e229464a05c77ab16b770523f0f0e6b4
// Builder seat: opus-A (4Q capped, 2026-07-12). Staging only — never self-approved.
//
// Portability: standard C++17, STL only. RNG is std::mt19937(42) (identical stream
// on every platform); gaussians come from an in-file Box-Muller, NOT
// std::normal_distribution (whose sequence differs across libstdc++/libc++). The
// twin therefore does NOT reproduce Python's Mersenne/gauss draw sequence — it is
// faithful by construction, and the two recovery asserts are mechanism claims that
// hold independent of the exact draws (see report Divergences).

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <vector>
#include <random>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <iomanip>

namespace {

// Single global RNG, mirroring the oracle's one module-level `random` instance
// seeded once at the top of main before any data is generated.
std::mt19937 g_rng;
bool   g_has_spare = false;
double g_spare     = 0.0;

// Canonical uniform in the open interval (0,1) from the full 32-bit mt19937
// output — never exactly 0 or 1, so std::log below is always safe.
inline double next_uniform() {
    return (static_cast<double>(g_rng()) + 0.5) * (1.0 / 4294967296.0);
}

// Standard-normal draw via Box-Muller (own impl for cross-toolchain determinism).
inline double next_gauss() {
    if (g_has_spare) { g_has_spare = false; return g_spare; }
    const double PI = 3.14159265358979323846;
    double u1 = next_uniform();
    double u2 = next_uniform();
    double r  = std::sqrt(-2.0 * std::log(u1));
    double a  = 2.0 * PI * u2;
    g_spare     = r * std::sin(a);
    g_has_spare = true;
    return r * std::cos(a);
}

// Two-sample t-test p-value (two-tailed), normal approximation — same as oracle.
double t_test_pvalue(double mean_treatment, double mean_control,
                     double var_t, double var_c, int n_t, int n_c) {
    if (n_t < 2 || n_c < 2) {
        return 1.0;
    }
    double se = std::sqrt(var_t / n_t + var_c / n_c);
    if (se == 0.0) {
        return 1.0;
    }
    double t_stat = (mean_treatment - mean_control) / se;
    double p_value = std::erfc(std::fabs(t_stat) / std::sqrt(2.0));
    return p_value;
}

// Fixed-n test without peeking; returns rejection rate.
double fixed_n_no_peeking(int n_per_arm, int reps, bool null_hyp) {
    int rejections = 0;

    for (int rep = 0; rep < reps; ++rep) {
        std::vector<double> treatment(static_cast<std::size_t>(n_per_arm));
        std::vector<double> control(static_cast<std::size_t>(n_per_arm));

        if (null_hyp) {
            // Under null: both arms from N(0,1).
            for (int i = 0; i < n_per_arm; ++i) treatment[i] = next_gauss();
            for (int i = 0; i < n_per_arm; ++i) control[i]   = next_gauss();
        } else {
            // Under alternative: treatment from N(0.5, 1).
            for (int i = 0; i < n_per_arm; ++i) treatment[i] = 0.5 + next_gauss();
            for (int i = 0; i < n_per_arm; ++i) control[i]   = next_gauss();
        }

        double mean_t = std::accumulate(treatment.begin(), treatment.end(), 0.0)
                        / n_per_arm;
        double mean_c = std::accumulate(control.begin(), control.end(), 0.0)
                        / n_per_arm;

        double ss_t = 0.0, ss_c = 0.0;
        for (double x : treatment) ss_t += (x - mean_t) * (x - mean_t);
        for (double x : control)   ss_c += (x - mean_c) * (x - mean_c);
        double var_t = ss_t / (n_per_arm - 1);
        double var_c = ss_c / (n_per_arm - 1);

        double p_val = t_test_pvalue(mean_t, mean_c, var_t, var_c,
                                     n_per_arm, n_per_arm);
        if (p_val < 0.05) {
            ++rejections;
        }
    }

    return static_cast<double>(rejections) / reps;
}

// Continuous peeking at interim analyses; returns rejection rate.
double peeking_strategy(int n_per_arm_initial, int n_looks, int reps) {
    int rejections = 0;

    for (int rep = 0; rep < reps; ++rep) {
        std::vector<double> treatment;
        std::vector<double> control;

        for (int look = 0; look < n_looks; ++look) {
            // Add more data.
            int n_add = n_per_arm_initial / n_looks;
            for (int i = 0; i < n_add; ++i) treatment.push_back(next_gauss());
            for (int i = 0; i < n_add; ++i) control.push_back(next_gauss());

            // Peek at p-value.
            int len_t = static_cast<int>(treatment.size());
            int len_c = static_cast<int>(control.size());
            double mean_t = std::accumulate(treatment.begin(), treatment.end(),
                                            0.0) / len_t;
            double mean_c = std::accumulate(control.begin(), control.end(),
                                            0.0) / len_c;

            double ss_t = 0.0, ss_c = 0.0;
            for (double x : treatment) ss_t += (x - mean_t) * (x - mean_t);
            for (double x : control)   ss_c += (x - mean_c) * (x - mean_c);
            double var_t = ss_t / std::max(len_t - 1, 1);
            double var_c = ss_c / std::max(len_c - 1, 1);

            double p_val = t_test_pvalue(mean_t, mean_c, var_t, var_c,
                                         len_t, len_c);

            if (p_val < 0.05) {
                ++rejections;
                break;  // Stop if we reject.
            }
        }
    }

    return static_cast<double>(rejections) / reps;
}

}  // namespace

int main() {
    // Deterministic demo (harvest law: seed 42) seeded BEFORE any data is
    // generated — makes the Monte-Carlo rates reproducible so the claim below
    // is stable, not a lucky run.
    g_rng.seed(42u);
    g_has_spare = false;

    // 2000 reps: enough to estimate the rejection rates tightly, so the real
    // effect (peeking at least doubles type-I) clears its margin robustly.
    double type_i_no_peek = fixed_n_no_peeking(50, 2000, true);
    double type_i_peek    = peeking_strategy(50, 5, 2000);

    // Peeking substantially inflates type-I (mechanism claim, not tolerance-tuned).
    assert(type_i_no_peek < 0.12);               // no-peek type-I should be ~5%
    assert(type_i_peek > type_i_no_peek * 2.0);  // peeking at least doubles type-I

    std::cout << std::fixed << std::setprecision(3)
              << "PASS \xE2\x80\x94 no_peek=" << type_i_no_peek
              << "  peek=" << type_i_peek << "  ("
              << std::setprecision(1) << (type_i_peek / type_i_no_peek)
              << "x inflation)" << std::endl;
    return 0;
}
