// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Convolution and Filtering
 * 
 * Convolve a signal with a kernel via discrete convolution.
 * Demonstrate smoothing (moving average) and edge detection (difference kernel).
 */

#include <vector>
#include <random>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>

std::vector<double> convolve(const std::vector<double>& signal, const std::vector<double>& kernel) {
    /* Discrete convolution (full mode). */
    int n = static_cast<int>(signal.size());
    int m = static_cast<int>(kernel.size());
    std::vector<double> output(n + m - 1, 0.0);

    for (int i = 0; i < n + m - 1; ++i) {
        for (int j = 0; j < m; ++j) {
            int signal_idx = i - j;
            if (signal_idx >= 0 && signal_idx < n) {
                output[i] += signal[signal_idx] * kernel[j];
            }
        }
    }

    return output;
}

std::vector<double> moving_average_kernel(int window_size) {
    return std::vector<double>(window_size, 1.0 / window_size);
}

std::vector<double> difference_kernel() {
    return {1.0, -1.0};
}

double mse(const std::vector<double>& x, const std::vector<double>& y) {
    int min_len = std::min(static_cast<int>(x.size()), static_cast<int>(y.size()));
    double sum = 0.0;
    for (int i = 0; i < min_len; ++i) {
        double diff = x[i] - y[i];
        sum += diff * diff;
    }
    return sum / min_len;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> normal(0.0, 2.0);

    // Create a smooth signal with noise
    const int n = 50;
    std::vector<double> true_signal(n);
    std::vector<double> noisy_signal(n);
    for (int i = 0; i < n; ++i) {
        true_signal[i] = 5.0 * (i / 10.0);
        noisy_signal[i] = true_signal[i] + normal(rng);
    }

    // Smooth via moving average convolution
    auto ma_kernel = moving_average_kernel(5);
    auto smoothed = convolve(noisy_signal, ma_kernel);
    smoothed.resize(n);  // Trim to original length

    // MSE: smoothed should be closer to true signal than noisy
    double mse_noisy = mse(true_signal, noisy_signal);
    double mse_smoothed = mse(true_signal, smoothed);
    assert(mse_smoothed < mse_noisy);

    // Edge detection: create a step signal
    std::vector<double> step_signal(50, 1.0);
    for (int i = 25; i < 50; ++i) step_signal[i] = 5.0;

    auto diff_kernel = difference_kernel();
    auto edges = convolve(step_signal, diff_kernel);

    // The maximum edge should occur at the step transition (index ~25)
    auto max_it = std::max_element(edges.begin(), edges.end());
    int max_edge_idx = static_cast<int>(std::distance(edges.begin(), max_it));
    assert(max_edge_idx >= 20 && max_edge_idx <= 30);

    std::cout << "convolution_filtering.cpp PASS" << std::endl;
    return 0;
}
