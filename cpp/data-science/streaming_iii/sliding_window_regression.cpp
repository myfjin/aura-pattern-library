// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <utility>
#include <vector>

// Sliding-window OLS regression tracking a planted slope drift.

double compute_slope(const std::vector<std::pair<double, double>>& pairs) {
    if (pairs.size() < 2) return 0.0;
    double sum_x = 0.0, sum_y = 0.0;
    for (const auto& p : pairs) {
        sum_x += p.first;
        sum_y += p.second;
    }
    double mean_x = sum_x / pairs.size();
    double mean_y = sum_y / pairs.size();

    double numerator = 0.0, denominator = 0.0;
    for (const auto& p : pairs) {
        double dx = p.first - mean_x;
        double dy = p.second - mean_y;
        numerator += dx * dy;
        denominator += dx * dx;
    }
    return numerator / std::max(1e-9, denominator);
}

double sliding_window_regression(const std::vector<std::pair<double, double>>& stream, int window_size) {
    assert(window_size > 0);

    size_t n = stream.size();
    size_t halfway = n / 2;

    auto true_slope_first = compute_slope(std::vector<std::pair<double, double>>(stream.begin(), stream.begin() + halfway));
    auto true_slope_second = compute_slope(std::vector<std::pair<double, double>>(stream.begin() + halfway, stream.end()));
    double true_drift = std::abs(true_slope_second - true_slope_first);

    std::vector<double> slopes;
    for (size_t i = 0; i + window_size <= stream.size(); ++i) {
        auto window = std::vector<std::pair<double, double>>(stream.begin() + i, stream.begin() + i + window_size);
        slopes.push_back(compute_slope(window));
    }

    double final_slope = slopes.empty() ? 0.0 : slopes.back();

    if (true_drift > 0.1) {
        assert(std::abs(final_slope - true_slope_second) < 0.5);
    } else {
        assert(std::abs(final_slope - true_slope_second) < 0.3);
    }

    return final_slope;
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> noise(0.0, 0.1);

    std::vector<std::pair<double, double>> stream;
    for (int i = 0; i < 100; ++i) {
        double x = i / 50.0;
        double y = x * 2.0 + noise(gen);
        stream.emplace_back(x, y);
    }
    for (int i = 100; i < 200; ++i) {
        double x = i / 50.0;
        double y = x * 0.5 + noise(gen);
        stream.emplace_back(x, y);
    }

    double slope = sliding_window_regression(stream, 50);
    std::cout << "PASS (final slope=" << slope << ")" << std::endl;
    return 0;
}
