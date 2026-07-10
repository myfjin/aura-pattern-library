// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <random>
#include <vector>

std::pair<double, double> local_linear_fit(const std::vector<double>& x_window,
                                          const std::vector<double>& y_window) {
    size_t n = x_window.size();
    if (n < 2) return {0.0, 0.0};

    double mean_x = 0.0, mean_y = 0.0;
    for (size_t i = 0; i < n; ++i) {
        mean_x += x_window[i];
        mean_y += y_window[i];
    }
    mean_x /= n;
    mean_y /= n;

    double ss_xx = 0.0, ss_xy = 0.0;
    for (size_t i = 0; i < n; ++i) {
        double dx = x_window[i] - mean_x;
        ss_xx += dx * dx;
        ss_xy += dx * (y_window[i] - mean_y);
    }

    if (ss_xx < 1e-6) return {mean_y, 0.0};

    double b = ss_xy / ss_xx;
    double a = mean_y - b * mean_x;
    return {a, b};
}

int main() {
    std::mt19937 gen(42);
    std::uniform_real_distribution<double> uni(0.0, 10.0);
    std::normal_distribution<double> noise(0.0, 0.3);

    int n = 300;
    std::vector<double> X(n);
    for (int i = 0; i < n; ++i) X[i] = uni(gen);
    std::sort(X.begin(), X.end());

    double cutoff = 5.0;
    double true_rd_effect = 3.0;
    std::vector<int> T(n);
    std::vector<double> Y(n);
    for (int i = 0; i < n; ++i) {
        T[i] = (X[i] >= cutoff) ? 1 : 0;
        Y[i] = 0.5 * X[i] + true_rd_effect * T[i] + noise(gen);
    }

    double bandwidth = 2.0;
    std::vector<int> left_indices, right_indices;
    for (int i = 0; i < n; ++i) {
        if (cutoff - bandwidth <= X[i] && X[i] < cutoff)
            left_indices.push_back(i);
        if (cutoff <= X[i] && X[i] <= cutoff + bandwidth)
            right_indices.push_back(i);
    }

    assert(static_cast<int>(left_indices.size()) > 1 &&
           static_cast<int>(right_indices.size()) > 1);

    std::vector<double> x_left, y_left, x_right, y_right;
    for (int idx : left_indices) {
        x_left.push_back(X[idx]);
        y_left.push_back(Y[idx]);
    }
    for (int idx : right_indices) {
        x_right.push_back(X[idx]);
        y_right.push_back(Y[idx]);
    }

    auto [a_left, b_left] = local_linear_fit(x_left, y_left);
    auto [a_right, b_right] = local_linear_fit(x_right, y_right);

    double y_left_at_cutoff = a_left + b_left * cutoff;
    double y_right_at_cutoff = a_right + b_right * cutoff;
    double rd_estimate = y_right_at_cutoff - y_left_at_cutoff;
    double bias = std::fabs(rd_estimate - true_rd_effect);

    assert(bias < 1.0);
    assert(static_cast<int>(left_indices.size()) >= 20);
    assert(static_cast<int>(right_indices.size()) >= 20);

    printf("True RD effect: %.2f | RD estimate: %.2f | Bias: %.2f | "
           "Left obs: %zu | Right obs: %zu | PASS\n",
           true_rd_effect, rd_estimate, bias,
           left_indices.size(), right_indices.size());
    return 0;
}
