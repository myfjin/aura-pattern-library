// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <cstdio>
#include <random>
#include <vector>

std::vector<double> linear_interpolation(const std::vector<double>& signal, int factor) {
    std::vector<double> upsampled;
    size_t n = signal.size();
    if (n == 0) return upsampled;
    for (size_t i = 0; i + 1 < n; ++i) {
        upsampled.push_back(signal[i]);
        for (int j = 1; j < factor; ++j) {
            double t = static_cast<double>(j) / factor;
            double interpolated = (1.0 - t) * signal[i] + t * signal[i + 1];
            upsampled.push_back(interpolated);
        }
    }
    upsampled.push_back(signal.back());
    return upsampled;
}

std::vector<double> nearest_neighbor_interpolation(const std::vector<double>& signal, int factor) {
    std::vector<double> upsampled;
    size_t n = signal.size();
    if (n == 0) return upsampled;
    for (size_t i = 0; i + 1 < n; ++i) {
        upsampled.push_back(signal[i]);
        for (int j = 1; j < factor; ++j) upsampled.push_back(signal[i]);
    }
    upsampled.push_back(signal.back());
    return upsampled;
}

std::vector<double> downsample(const std::vector<double>& signal, int factor) {
    std::vector<double> out;
    for (size_t i = 0; i < signal.size(); i += factor) out.push_back(signal[i]);
    return out;
}

double rmse(const std::vector<double>& x, const std::vector<double>& y) {
    size_t m = std::min(x.size(), y.size());
    double sum = 0.0;
    for (size_t i = 0; i < m; ++i) sum += (x[i] - y[i]) * (x[i] - y[i]);
    return std::sqrt(sum / m);
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> noise(0.0, 0.05);

    int n = 50;
    std::vector<double> signal(n);
    for (int t = 0; t < n; ++t) {
        signal[t] = std::sin(2.0 * M_PI * t / 20.0) + noise(gen);
    }

    int upsample_factor = 3;
    auto linear_up = linear_interpolation(signal, upsample_factor);
    auto nearest_up = nearest_neighbor_interpolation(signal, upsample_factor);

    std::vector<double> true_upsampled(linear_up.size());
    for (size_t t = 0; t < true_upsampled.size(); ++t) {
        true_upsampled[t] = std::sin(2.0 * M_PI * t / (20.0 * upsample_factor));
    }

    double rmse_linear = rmse(linear_up, true_upsampled);
    double rmse_nearest = rmse(nearest_up, true_upsampled);

    assert(rmse_linear < rmse_nearest);

    auto downsampled = downsample(signal, upsample_factor);
    int expected_length = (n - 1) / upsample_factor + 1;
    assert(static_cast<int>(downsampled.size()) == expected_length);

    printf("Original: %d | Upsampled: %zu | Linear RMSE: %.4f | Nearest RMSE: %.4f | "
           "Improvement: %.1f%% | PASS\n",
           n, linear_up.size(), rmse_linear, rmse_nearest,
           (1.0 - rmse_linear / rmse_nearest) * 100.0);
    return 0;
}
