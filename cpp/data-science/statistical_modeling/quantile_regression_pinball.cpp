// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Linear quantile regression via gradient descent on the pinball (quantile) loss:
fits a line whose predictions target a chosen conditional quantile tau instead of
the mean. Use to estimate the median or an upper/lower band (e.g. p90) of y given
x when you care about spread, not just the average.
Guarantees: the tau=0.5 fit leaves ~35-65% of points below it, the tau=0.9 fit
leaves ~75-99% below, and the p90 line sits above the median line at mid-x.
*/
#include <cassert>
#include <iostream>
#include <cmath>
#include <random>
#include <vector>

using VecD = std::vector<double>;

// pinball_loss kept for parity with Python oracle but unused in this test

static double pinball_loss_gradient(double y, double pred, double tau) {
    double r = y - pred;
    return (r >= 0.0) ? -tau : -(tau - 1.0);
}

static std::pair<double, double> quantile_regression_linear(
    const VecD& x_vals,
    const VecD& y_vals,
    double tau,
    double learning_rate,
    int n_iter) {
    std::size_t n = x_vals.size();
    double a = 0.0, b = 0.0;
    for (int it = 0; it < n_iter; ++it) {
        double grad_a = 0.0, grad_b = 0.0;
        for (std::size_t i = 0; i < n; ++i) {
            double pred = a + b * x_vals[i];
            double grad = pinball_loss_gradient(y_vals[i], pred, tau);
            grad_a += grad;
            grad_b += grad * x_vals[i];
        }
        a -= learning_rate * grad_a / static_cast<double>(n);
        b -= learning_rate * grad_b / static_cast<double>(n);
    }
    return {a, b};
}

static double count_below_line(const VecD& x_vals, const VecD& y_vals,
                               double a, double b) {
    std::size_t n = x_vals.size();
    std::size_t count = 0;
    for (std::size_t i = 0; i < n; ++i) {
        if (y_vals[i] <= a + b * x_vals[i]) ++count;
    }
    return static_cast<double>(count) / static_cast<double>(n);
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> noise(0.0, 0.5);

    const int n = 50;
    VecD x_vals, y_vals;
    for (int i = 0; i < n; ++i) {
        double x = i * 0.2;
        x_vals.push_back(x);
        y_vals.push_back(1.0 + 0.5 * x + noise(gen));
    }

    auto median = quantile_regression_linear(x_vals, y_vals, 0.5, 0.05, 5000);
    auto pct90 = quantile_regression_linear(x_vals, y_vals, 0.9, 0.05, 5000);

    double frac_median = count_below_line(x_vals, y_vals, median.first, median.second);
    double frac_90 = count_below_line(x_vals, y_vals, pct90.first, pct90.second);

    assert(0.35 < frac_median && frac_median < 0.65);
    assert(0.75 < frac_90 && frac_90 < 0.99);
    assert(pct90.first + pct90.second * 0.5 > median.first + median.second * 0.5);

    std::cout << "quantile_regression_pinball.cpp: frac_below_median=" << frac_median
              << ", frac_below_90=" << frac_90 << " PASS" << std::endl;
    return 0;
}
