// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cstdio>
#include <random>
#include <set>
#include <vector>

std::vector<int> reservoir_sample(const std::vector<int>& stream, int k, std::mt19937& gen) {
    std::vector<int> reservoir;
    for (size_t i = 0; i < stream.size(); ++i) {
        if (static_cast<int>(i) < k) {
            reservoir.push_back(stream[i]);
        } else {
            std::uniform_int_distribution<int> dist(0, static_cast<int>(i));
            int j = dist(gen);
            if (j < k) reservoir[j] = stream[i];
        }
    }
    return reservoir;
}

bool verify_uniformity(const std::vector<std::vector<int>>& samples_per_run, int item_count) {
    std::vector<int> counts(item_count, 0);
    int total_samples = 0;
    for (const auto& samples : samples_per_run) {
        total_samples += static_cast<int>(samples.size());
        for (int item : samples) counts[item]++;
    }

    double expected = static_cast<double>(total_samples) / item_count;
    int close_counts = 0;
    int nonzero_counts = 0;
    for (int c : counts) {
        if (c > 0) ++nonzero_counts;
        if (c > 0 && 0.5 * expected <= c && c <= 2.0 * expected) ++close_counts;
    }

    // Tolerate a few items with zero counts; require 70% of seen items to be close.
    return close_counts >= static_cast<int>(nonzero_counts * 0.7);
}

int main() {
    std::mt19937 gen(42);

    // Scenario 1: sample 5 from [0..19].
    std::vector<int> stream1(20);
    for (int i = 0; i < 20; ++i) stream1[i] = i;
    auto sample_1 = reservoir_sample(stream1, 5, gen);
    assert(static_cast<int>(sample_1.size()) == 5);
    std::set<int> s1(sample_1.begin(), sample_1.end());
    assert(static_cast<int>(s1.size()) == 5);
    for (int x : sample_1) assert(0 <= x && x < 20);

    // Scenario 2: uniformity over 50 runs.
    int k = 10, n = 100, num_runs = 50;
    std::vector<std::vector<int>> samples_per_run;
    for (int run = 0; run < num_runs; ++run) {
        std::vector<int> stream(n);
        for (int i = 0; i < n; ++i) stream[i] = i;
        samples_per_run.push_back(reservoir_sample(stream, k, gen));
    }
    bool is_uniform = verify_uniformity(samples_per_run, n);
    assert(is_uniform);

    // Scenario 3: stream smaller than k.
    std::vector<int> tiny_stream = {0, 1, 2};
    auto sample_tiny = reservoir_sample(tiny_stream, 10, gen);
    assert(static_cast<int>(sample_tiny.size()) == 3);
    assert(sample_tiny[0] == 0 && sample_tiny[1] == 1 && sample_tiny[2] == 2);

    printf("Reservoir sampling PASSED\n");
    return 0;
}
