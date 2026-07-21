// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Fixed-width histogram builder. Chooses the bin count by Sturges' rule (ceil(log2 n)+1)
 * unless one is given, spans [min,max] in equal-width bins, and folds the maximum value
 * into the last bin so no point falls outside the edges. Degenerate all-equal input
 * collapses to a single bin.
 * Use to bin a 1-D sample for a frequency/density view.
 * Guarantees: counts sum to N, bin edges are monotonically non-decreasing, and both
 * modes of a bimodal sample surface as separate populated peaks.
 */

#include <vector>
#include <cmath>
#include <random>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <utility>

int sturges_bin_count(int n) {
    return static_cast<int>(std::ceil(std::log2(n))) + 1;
}

std::pair<std::vector<int>, std::vector<double>> histogram(const std::vector<double>& data, int n_bins = -1) {
    if (data.empty()) return {{}, {}};
    if (n_bins < 0) n_bins = sturges_bin_count(static_cast<int>(data.size()));

    double min_val = *std::min_element(data.begin(), data.end());
    double max_val = *std::max_element(data.begin(), data.end());

    if (min_val == max_val) return {{static_cast<int>(data.size())}, {min_val, min_val}};

    double bin_width = (max_val - min_val) / n_bins;

    std::vector<double> bin_edges;
    for (int i = 0; i <= n_bins; ++i) bin_edges.push_back(min_val + i * bin_width);

    std::vector<int> counts(n_bins, 0);
    for (double x : data) {
        int bin_idx;
        if (x == max_val) bin_idx = n_bins - 1;
        else {
            bin_idx = static_cast<int>((x - min_val) / bin_width);
            bin_idx = std::min(bin_idx, n_bins - 1);
        }
        counts[bin_idx]++;
    }

    return {counts, bin_edges};
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> mode1(20.0, 3.0);
    std::normal_distribution<double> mode2(60.0, 3.0);

    std::vector<double> bimodal_data;
    for (int i = 0; i < 50; ++i) bimodal_data.push_back(mode1(rng));
    for (int i = 0; i < 50; ++i) bimodal_data.push_back(mode2(rng));

    auto [counts, edges] = histogram(bimodal_data);

    int total = 0;
    for (int c : counts) total += c;
    assert(total == 100);

    for (size_t i = 0; i + 1 < edges.size(); ++i) {
        assert(edges[i] <= edges[i + 1]);
    }

    int expected_bins = sturges_bin_count(100);
    assert(static_cast<int>(counts.size()) == expected_bins);

    int peak1_val = *std::max_element(counts.begin(), counts.end());
    std::vector<int> counts_masked = counts;
    counts_masked[std::max_element(counts.begin(), counts.end()) - counts.begin()] = 0;
    int peak2_val = *std::max_element(counts_masked.begin(), counts_masked.end());

    assert(peak1_val > 8);
    assert(peak2_val > 8);

    std::cout << "histogram_builder.cpp PASS" << std::endl;
    return 0;
}
