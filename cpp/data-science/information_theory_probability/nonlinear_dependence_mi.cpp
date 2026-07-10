// Mutual information detects nonlinear dependence that Pearson correlation misses.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <algorithm>
#include <cassert>
#include <utility>

static double empirical_mean(const std::vector<double>& samples) {
    if (samples.empty()) return 0.0;
    double s = 0.0;
    for (double x : samples) s += x;
    return s / static_cast<double>(samples.size());
}

static double empirical_std(const std::vector<double>& samples) {
    std::size_t n = samples.size();
    if (n < 2) return 0.0;
    double mean = empirical_mean(samples);
    double s = 0.0;
    for (double x : samples) {
        double d = x - mean;
        s += d * d;
    }
    double variance = s / static_cast<double>(n - 1);
    return std::sqrt(variance);
}

static double pearson_correlation(const std::vector<double>& x, const std::vector<double>& y) {
    assert(x.size() == y.size());
    std::size_t n = x.size();

    double mean_x = empirical_mean(x);
    double mean_y = empirical_mean(y);

    double cov = 0.0;
    for (std::size_t i = 0; i < n; ++i) {
        cov += (x[i] - mean_x) * (y[i] - mean_y);
    }
    cov /= static_cast<double>(n - 1);

    double std_x = empirical_std(x);
    double std_y = empirical_std(y);
    if (std_x < 1e-10 || std_y < 1e-10) return 0.0;
    return cov / (std_x * std_y);
}

static double binned_entropy(const std::vector<double>& samples, int num_bins) {
    if (samples.empty()) return 0.0;

    double min_val = samples[0];
    double max_val = samples[0];
    for (double s : samples) {
        if (s < min_val) min_val = s;
        if (s > max_val) max_val = s;
    }
    if (min_val == max_val) return 0.0;

    double bin_width = (max_val - min_val) / static_cast<double>(num_bins);
    if (bin_width <= 0.0) return 0.0;

    std::vector<int> counts(num_bins, 0);
    for (double s : samples) {
        int idx = static_cast<int>((s - min_val) / bin_width);
        if (idx >= num_bins) idx = num_bins - 1;
        ++counts[idx];
    }

    double entropy = 0.0;
    double n = static_cast<double>(samples.size());
    for (int c : counts) {
        if (c == 0) continue;
        double p = static_cast<double>(c) / n;
        entropy -= p * std::log2(p);
    }
    return entropy;
}

static double binned_mutual_information(
    const std::vector<double>& x,
    const std::vector<double>& y,
    int num_bins) {

    assert(x.size() == y.size());
    if (x.empty()) return 0.0;

    double h_x = binned_entropy(x, num_bins);
    double h_y = binned_entropy(y, num_bins);

    double min_x = x[0], max_x = x[0];
    for (double v : x) {
        if (v < min_x) min_x = v;
        if (v > max_x) max_x = v;
    }
    double min_y = y[0], max_y = y[0];
    for (double v : y) {
        if (v < min_y) min_y = v;
        if (v > max_y) max_y = v;
    }

    double bin_width_x = (max_x - min_x) / static_cast<double>(num_bins);
    double bin_width_y = (max_y - min_y) / static_cast<double>(num_bins);
    if (bin_width_x <= 0.0 || bin_width_y <= 0.0) return 0.0;

    std::vector<int> joint_counts(num_bins * num_bins, 0);
    std::size_t n = x.size();
    for (std::size_t i = 0; i < n; ++i) {
        int bx = static_cast<int>((x[i] - min_x) / bin_width_x);
        if (bx >= num_bins) bx = num_bins - 1;
        int by = static_cast<int>((y[i] - min_y) / bin_width_y);
        if (by >= num_bins) by = num_bins - 1;
        ++joint_counts[bx * num_bins + by];
    }

    double h_xy = 0.0;
    double nd = static_cast<double>(n);
    for (int c : joint_counts) {
        if (c == 0) continue;
        double p = static_cast<double>(c) / nd;
        h_xy -= p * std::log2(p);
    }

    double mi = h_x + h_y - h_xy;
    return std::max(mi, 0.0);
}

static double independent_mi_baseline(
    const std::vector<double>& x,
    const std::vector<double>& y,
    int num_bins,
    std::mt19937& rng) {

    std::vector<double> y_shuffled = y;
    std::shuffle(y_shuffled.begin(), y_shuffled.end(), rng);
    return binned_mutual_information(x, y_shuffled, num_bins);
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> dist01(0.0, 1.0);
    std::normal_distribution<double> dist001(0.0, 0.1);

    const int n = 2000;
    const int num_bins = 15;

    // Nonlinear: y = x^2 + noise
    std::vector<double> x_nonlinear(n);
    std::vector<double> y_nonlinear(n);
    for (int i = 0; i < n; ++i) {
        x_nonlinear[i] = dist01(rng);
        double noise = dist001(rng);
        y_nonlinear[i] = x_nonlinear[i] * x_nonlinear[i] + noise;
    }

    double corr_nonlinear = pearson_correlation(x_nonlinear, y_nonlinear);
    double mi_nonlinear = binned_mutual_information(x_nonlinear, y_nonlinear, num_bins);

    assert(std::abs(corr_nonlinear) < 0.15);
    assert(mi_nonlinear > 1.0);
    assert(mi_nonlinear > std::abs(corr_nonlinear));
    assert(mi_nonlinear > 2.0 * std::abs(corr_nonlinear));

    std::cout << "Nonlinear y=x^2: Pearson r = " << corr_nonlinear
              << ", MI = " << mi_nonlinear << " bits" << std::endl;

    // Independent: y is random noise
    std::vector<double> y_independent(n);
    for (int i = 0; i < n; ++i) y_independent[i] = dist01(rng);

    double corr_indep = pearson_correlation(x_nonlinear, y_independent);
    double mi_indep = binned_mutual_information(x_nonlinear, y_independent, num_bins);

    assert(std::abs(corr_indep) < 0.15);
    assert(mi_indep < 0.2);

    // Shuffled baseline
    double mi_baseline = independent_mi_baseline(x_nonlinear, y_nonlinear, num_bins, rng);
    assert(mi_baseline < 0.2);

    // Strong linear: y = 2*x + noise
    std::vector<double> y_linear(n);
    for (int i = 0; i < n; ++i) {
        y_linear[i] = 2.0 * x_nonlinear[i] + dist001(rng);
    }

    double corr_linear = pearson_correlation(x_nonlinear, y_linear);
    double mi_linear = binned_mutual_information(x_nonlinear, y_linear, num_bins);

    assert(corr_linear > 0.95);
    assert(mi_linear > 1.0);

    std::cout << "Linear y=2x: Pearson r = " << corr_linear
              << ", MI = " << mi_linear << " bits" << std::endl;

    std::cout << "PASS" << std::endl;
    return 0;
}
