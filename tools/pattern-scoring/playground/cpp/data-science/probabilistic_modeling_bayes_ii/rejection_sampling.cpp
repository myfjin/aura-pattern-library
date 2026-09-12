// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <cstdio>
#include <random>
#include <vector>

// Target unnormalized density: mixture of two bumps.
double target_density(double x) {
    return std::exp(-0.5 * std::pow((x - 2.0) / 0.7, 2)) +
           0.5 * std::exp(-0.5 * std::pow((x + 2.0) / 0.5, 2));
}

// Uniform proposal density on [-5, 5].
double proposal_density(double x) {
    if (-5.0 <= x && x <= 5.0) return 1.0 / 10.0;
    return 0.0;
}

int main() {
    std::mt19937 gen(42);
    std::uniform_real_distribution<double> uniform(-5.0, 5.0);
    std::uniform_real_distribution<double> unit(0.0, 1.0);

    // Estimate M via grid search (same grid as Python).
    double M_empirical = 0.0;
    for (int i = 0; i < 200; ++i) {
        double x = i * 0.05 - 5.0;
        double q = proposal_density(x);
        double ratio = target_density(x) / (q < 1e-10 ? 1e-10 : q);
        if (ratio > M_empirical) M_empirical = ratio;
    }
    double M = M_empirical * 3.0;

    int n_samples = 1000;
    std::vector<double> samples;
    samples.reserve(n_samples);
    int accepts = 0;

    while (static_cast<int>(samples.size()) < n_samples) {
        double x = uniform(gen);
        double u = unit(gen);
        double q = proposal_density(x);
        double ratio = target_density(x) / (M * (q < 1e-10 ? 1e-10 : q));
        if (u < ratio) {
            samples.push_back(x);
            ++accepts;
        }
    }

    double acceptance_rate = static_cast<double>(accepts) / n_samples;

    assert(static_cast<int>(samples.size()) == n_samples);
    assert(0.0 < acceptance_rate && acceptance_rate <= 1.0);

    double mean = 0.0;
    for (double x : samples) mean += x;
    mean /= n_samples;

    double var = 0.0;
    for (double x : samples) var += (x - mean) * (x - mean);
    var /= n_samples;

    // Numeric integration to compute reference moments.
    double dx = 0.01;
    int grid_steps = static_cast<int>(10.0 / dx);  // -5 to 5
    double Z = 0.0;
    double mean_num = 0.0;
    double var_num = 0.0;

    for (int i = 0; i < grid_steps; ++i) {
        double x = i * dx - 5.0;
        double d = target_density(x);
        Z += d * dx;
        mean_num += x * d * dx;
    }
    mean_num /= Z;

    for (int i = 0; i < grid_steps; ++i) {
        double x = i * dx - 5.0;
        double d = target_density(x);
        var_num += (x - mean_num) * (x - mean_num) * d * dx;
    }
    var_num /= Z;

    assert(std::fabs(mean - mean_num) < 0.5);
    assert(std::fabs(var - var_num) < 0.5);

    for (double x : samples) {
        assert(-5.0 <= x && x <= 5.0);
    }

    printf("PASS | samples=%zu mean=%.4f var=%.4f acc_rate=%.4f\n",
           samples.size(), mean, var, acceptance_rate);
    return 0;
}
