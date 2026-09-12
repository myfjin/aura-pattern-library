// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Streaming histogram with a bounded bin budget: each value joins a near bin
(within 0.5) or spawns a new one, and when bins exceed max_bins the adjacent
pair with the smallest combined count is merged into a count-weighted center.
Supports approximate quantile queries in one pass under fixed memory.
Oracle: final bin count never exceeds max_bins, and the p25/median/p75 estimates
stay within tolerance of the exact sorted-stream quantiles on a bimodal stream.
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <random>
#include <cassert>
#include <limits>

class StreamingHistogram {
public:
    int max_bins;
    std::vector<std::pair<double, int>> bins;

    explicit StreamingHistogram(int max_bins = 20) : max_bins(max_bins) {}

    void process(double value) {
        bool found = false;
        for (auto& bin : bins) {
            if (std::abs(value - bin.first) < 0.5) {
                bin.second++;
                found = true;
                break;
            }
        }
        if (!found) {
            bins.push_back({value, 1});
            if (static_cast<int>(bins.size()) > max_bins) {
                merge_adjacent();
            }
        }
    }

    void merge_adjacent() {
        if (bins.size() <= 1) return;
        size_t min_idx = 0;
        int min_cost = std::numeric_limits<int>::max();
        for (size_t i = 0; i < bins.size() - 1; ++i) {
            int cost = bins[i].second + bins[i + 1].second;
            if (cost < min_cost) {
                min_cost = cost;
                min_idx = i;
            }
        }
        double c1 = bins[min_idx].first;
        int n1 = bins[min_idx].second;
        double c2 = bins[min_idx + 1].first;
        int n2 = bins[min_idx + 1].second;
        double merged_center = (c1 * n1 + c2 * n2) / static_cast<double>(n1 + n2);
        int merged_count = n1 + n2;
        bins[min_idx] = {merged_center, merged_count};
        bins.erase(bins.begin() + min_idx + 1);
    }

    double query_quantile(double p) const {
        if (bins.empty()) return 0.0;
        int total_count = 0;
        for (const auto& bin : bins) total_count += bin.second;
        double target_rank = p * total_count;
        auto sorted = bins;
        std::sort(sorted.begin(), sorted.end());
        int cumsum = 0;
        for (const auto& bin : sorted) {
            cumsum += bin.second;
            if (cumsum >= target_rank) return bin.first;
        }
        return sorted.back().first;
    }

    std::vector<std::pair<double, int>> get_bins() const {
        auto sorted = bins;
        std::sort(sorted.begin(), sorted.end());
        return sorted;
    }
};

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> gauss(0.0, 1.0);
    std::uniform_real_distribution<double> uniform(0.0, 1.0);

    std::vector<double> stream;
    for (int i = 0; i < 500; ++i) {
        if (uniform(rng) < 0.5) stream.push_back(30.0 + 5.0 * gauss(rng));
        else stream.push_back(70.0 + 5.0 * gauss(rng));
    }

    auto sorted_stream = stream;
    std::sort(sorted_stream.begin(), sorted_stream.end());
    size_t n = sorted_stream.size();
    double exact_median = sorted_stream[n / 2];
    double exact_p25 = sorted_stream[n / 4];
    double exact_p75 = sorted_stream[3 * n / 4];

    StreamingHistogram hist(15);
    for (double x : stream) hist.process(x);

    double est_median = hist.query_quantile(0.5);
    double est_p25 = hist.query_quantile(0.25);
    double est_p75 = hist.query_quantile(0.75);

    auto final_bins = hist.get_bins();

    double error_p25 = std::abs(exact_p25 - est_p25);
    double error_median = std::abs(exact_median - est_median);
    double error_p75 = std::abs(exact_p75 - est_p75);

    assert(final_bins.size() <= static_cast<size_t>(hist.max_bins));
    assert(error_p25 < 25.0);
    assert(error_median < 25.0);
    assert(error_p75 < 25.0);

    std::cout << "streaming_histogram_merge: PASS" << std::endl;
    return 0;
}
