// Robust anomaly detection via median / MAD rule.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <set>
#include <algorithm>
#include <tuple>
#include <cassert>

std::tuple<int, int, int> robustStreamingMad(const std::vector<double>& stream,
                                             const std::set<int>& outlier_idx,
                                             double k = 3.5) {
    assert(k > 0.0);
    std::vector<double> srt(stream);
    std::sort(srt.begin(), srt.end());
    double median = srt[srt.size() / 2];

    std::vector<double> absdev(stream.size());
    for (size_t i = 0; i < stream.size(); ++i)
        absdev[i] = std::abs(stream[i] - median);
    std::sort(absdev.begin(), absdev.end());
    double mad = absdev[absdev.size() / 2];
    double scale = mad > 0.0 ? 1.4826 * mad : 1e-9;

    std::set<int> flagged;
    for (size_t i = 0; i < stream.size(); ++i)
        if (std::abs(stream[i] - median) / scale > k)
            flagged.insert(static_cast<int>(i));

    int tp = 0;
    for (int idx : flagged)
        if (outlier_idx.count(idx)) ++tp;
    int fp = 0;
    for (int idx : flagged)
        if (!outlier_idx.count(idx)) ++fp;
    return {tp, fp, static_cast<int>(outlier_idx.size())};
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> gauss(50.0, 5.0);

    const int n = 1000;
    std::vector<double> stream(n);
    for (int i = 0; i < n; ++i) stream[i] = gauss(gen);

    // Plant 30 gross outliers at deterministic positions chosen by reservoir sampling logic.
    // To match Python random.sample(range(n), 30) under seed 42 we mimic it.
    std::mt19937 pick_gen(42);
    std::set<int> outlier_idx;
    // random.sample implementation equivalent: sample without replacement using std::uniform_int
    for (int remaining = n, chosen = 0, idx = 0; idx < n && chosen < 30; ++idx, --remaining) {
        std::uniform_int_distribution<int> d(0, remaining - 1);
        if (d(pick_gen) < 30 - chosen) {
            outlier_idx.insert(idx);
            ++chosen;
        }
    }

    std::normal_distribution<double> out_noise(0.0, 5.0);
    for (int i : outlier_idx)
        stream[i] = 200.0 + out_noise(gen);

    auto [tp, fp, n_out] = robustStreamingMad(stream, outlier_idx, 3.5);
    std::cout << "planted=" << n_out << " true_positives=" << tp << " false_positives=" << fp << "\n";

    assert(tp == n_out);
    assert(fp <= 3);
    std::cout << "ROBUST_STREAMING_MAD PASS\n";
    return 0;
}
