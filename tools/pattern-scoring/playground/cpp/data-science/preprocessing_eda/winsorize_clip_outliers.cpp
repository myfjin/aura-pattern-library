// Winsorization and Clipping Pattern.
// Converted from the Python oracle.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <random>
#include <cassert>

double percentile(const std::vector<double>& data, double p) {
    if (data.empty() || p < 0.0 || p > 100.0) throw std::invalid_argument("Invalid percentile");
    std::vector<double> sorted_data = data;
    std::sort(sorted_data.begin(), sorted_data.end());
    size_t n = sorted_data.size();
    if (n == 1) return sorted_data[0];
    double h = (p / 100.0) * (n - 1);
    size_t i = (size_t)h;
    double f = h - i;
    if (i >= n - 1) return sorted_data[n-1];
    return sorted_data[i] + f * (sorted_data[i+1] - sorted_data[i]);
}

std::vector<double> winsorize(const std::vector<double>& data, double lower_frac, double upper_frac) {
    double lower_pct = lower_frac * 100.0;
    double upper_pct = 100.0 - upper_frac * 100.0;
    double lower_bound = percentile(data, lower_pct);
    double upper_bound = percentile(data, upper_pct);
    std::vector<double> result;
    for (double x : data)
        result.push_back(std::max(lower_bound, std::min(x, upper_bound)));
    return result;
}

std::vector<double> clip(const std::vector<double>& data, double min_val, double max_val) {
    std::vector<double> result;
    for (double x : data)
        result.push_back(std::max(min_val, std::min(x, max_val)));
    return result;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> dist(50.0, 10.0);
    std::vector<double> normal_data;
    for (int i = 0; i < 80; ++i) normal_data.push_back(dist(rng));
    std::vector<double> outliers = {2.0, 200.0, -50.0, 250.0};
    std::vector<double> data_with_outliers = normal_data;
    data_with_outliers.insert(data_with_outliers.end(), outliers.begin(), outliers.end());
    size_t n_original = data_with_outliers.size();

    auto winsorized = winsorize(data_with_outliers, 0.05, 0.05);
    assert(winsorized.size() == n_original);

    auto wminmax = std::minmax_element(winsorized.begin(), winsorized.end());
    // The winsorized extrema must bound every winsorized value (trivially true).
    for (double val : winsorized) {
        assert(*wminmax.first <= val && val <= *wminmax.second);
    }

    double original_range = *std::max_element(data_with_outliers.begin(), data_with_outliers.end())
                          - *std::min_element(data_with_outliers.begin(), data_with_outliers.end());
    double winsorized_range = *wminmax.second - *wminmax.first;
    assert(winsorized_range < original_range * 0.7);

    auto clipped = clip(data_with_outliers, 10.0, 90.0);
    assert(clipped.size() == n_original);
    for (double x : clipped) assert(10.0 <= x && x <= 90.0);
    assert(*std::min_element(clipped.begin(), clipped.end()) == 10.0);
    assert(*std::max_element(clipped.begin(), clipped.end()) == 90.0);

    std::cout << "winsorize_clip_outliers: PASS\n";
    return 0;
}
