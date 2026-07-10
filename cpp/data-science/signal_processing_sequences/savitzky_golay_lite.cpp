// Savitzky-Golay filter: local polynomial smoothing.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <cassert>
#include <tuple>

std::tuple<double, double, double> fitPolynomialWindow(const std::vector<double>& window) {
    size_t n = window.size();
    std::vector<double> x(n);
    for (size_t i = 0; i < n; ++i) x[i] = static_cast<double>(i);

    double sum_x = 0.0, sum_x2 = 0.0, sum_x3 = 0.0, sum_x4 = 0.0;
    double sum_y = 0.0, sum_xy = 0.0, sum_x2y = 0.0;
    for (size_t i = 0; i < n; ++i) {
        double xi = x[i], yi = window[i];
        sum_x += xi;
        sum_x2 += xi * xi;
        sum_x3 += xi * xi * xi;
        sum_x4 += xi * xi * xi * xi;
        sum_y += yi;
        sum_xy += xi * yi;
        sum_x2y += xi * xi * yi;
    }

    double xtx[3][3] = {{static_cast<double>(n), sum_x, sum_x2},
                        {sum_x, sum_x2, sum_x3},
                        {sum_x2, sum_x3, sum_x4}};
    double xty[3] = {sum_y, sum_xy, sum_x2y};

    double det = xtx[0][0] * (xtx[1][1] * xtx[2][2] - xtx[1][2] * xtx[2][1])
               - xtx[0][1] * (xtx[1][0] * xtx[2][2] - xtx[1][2] * xtx[2][0])
               + xtx[0][2] * (xtx[1][0] * xtx[2][1] - xtx[1][1] * xtx[2][0]);
    if (std::abs(det) < 1e-10) return {0.0, 0.0, 0.0};

    double det_a = xty[0] * (xtx[1][1] * xtx[2][2] - xtx[1][2] * xtx[2][1])
                 - xtx[0][1] * (xty[1] * xtx[2][2] - xtx[1][2] * xty[2])
                 + xtx[0][2] * (xty[1] * xtx[2][1] - xtx[1][1] * xty[2]);

    double det_b = xtx[0][0] * (xty[1] * xtx[2][2] - xtx[1][2] * xty[2])
                 - xty[0] * (xtx[1][0] * xtx[2][2] - xtx[1][2] * xtx[2][0])
                 + xtx[0][2] * (xtx[1][0] * xty[2] - xty[1] * xtx[2][0]);

    double det_c = xtx[0][0] * (xtx[1][1] * xty[2] - xty[1] * xtx[2][1])
                 - xtx[0][1] * (xtx[1][0] * xty[2] - xty[1] * xtx[2][0])
                 + xty[0] * (xtx[1][0] * xtx[2][1] - xtx[1][1] * xtx[2][0]);

    return {det_a / det, det_b / det, det_c / det};
}

std::vector<double> savitzkyGolayFilter(const std::vector<double>& signal, int window_size = 5) {
    int n = static_cast<int>(signal.size());
    int half_window = window_size / 2;
    std::vector<double> filtered;
    for (int i = 0; i < n; ++i) {
        int left = std::max(0, i - half_window);
        int right = std::min(n - 1, i + half_window);
        std::vector<double> window(signal.begin() + left, signal.begin() + right + 1);
        auto [a, b, c] = fitPolynomialWindow(window);
        int center_idx = i - left;
        filtered.push_back(a + b * center_idx + c * center_idx * center_idx);
    }
    return filtered;
}

std::vector<double> movingAverageFilter(const std::vector<double>& signal, int window_size = 5) {
    int n = static_cast<int>(signal.size());
    int half_window = window_size / 2;
    std::vector<double> filtered;
    for (int i = 0; i < n; ++i) {
        int left = std::max(0, i - half_window);
        int right = std::min(n - 1, i + half_window);
        double sum = 0.0;
        for (int j = left; j <= right; ++j) sum += signal[j];
        filtered.push_back(sum / (right - left + 1));
    }
    return filtered;
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> noise(0.0, 0.3);

    const int n = 50;
    const int peak_idx = 25;
    const double height = 8.0, width = 2.0;
    std::vector<double> clean(n), signal(n);
    for (int t = 0; t < n; ++t) {
        clean[t] = 1.0 + 0.01 * t + height * std::exp(-((t - peak_idx) * (t - peak_idx)) / (2.0 * width * width));
        signal[t] = clean[t] + noise(gen);
    }

    auto sg_filtered = savitzkyGolayFilter(signal, 5);
    auto ma_filtered = movingAverageFilter(signal, 5);

    double true_peak = clean[peak_idx];
    double sg_peak = sg_filtered[peak_idx];
    double ma_peak = ma_filtered[peak_idx];
    double sg_err = std::abs(sg_peak - true_peak);
    double ma_err = std::abs(ma_peak - true_peak);

    assert(sg_err < 0.9);
    assert(ma_err > 1.1);
    assert(sg_err < 0.7 * ma_err);

    std::cout << "SAVITZKY_GOLAY_LITE PASS: true=" << true_peak
              << " sg=" << sg_peak << " ma=" << ma_peak << "\n";
    return 0;
}
