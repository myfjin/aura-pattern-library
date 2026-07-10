// Weighted Reservoir Sampling (A-Res Algorithm)
// Converted from the Python oracle.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <random>
#include <cmath>
#include <cassert>
#include <map>

using std::string;
using std::vector;
using std::pair;

struct WeightedReservoirSampler {
    int k;
    struct Item { double key; string item; double weight; };
    vector<Item> reservoir;
    std::mt19937& rng;

    WeightedReservoirSampler(int k_, std::mt19937& rng_) : k(k_), rng(rng_) {}

    void process(const string& item, double weight) {
        if (weight <= 0.0) return;
        std::uniform_real_distribution<double> u(0.0, 1.0);
        double key = std::pow(u(rng), 1.0 / weight);
        if ((int)reservoir.size() < k) {
            reservoir.push_back({key, item, weight});
        } else {
            if (key > reservoir[0].key) {
                reservoir[0] = {key, item, weight};
            }
        }
        std::sort(reservoir.begin(), reservoir.end(),
                  [](const Item& a, const Item& b) { return a.key < b.key; });
    }

    vector<pair<string,double>> get_sample() const {
        vector<pair<string,double>> result;
        for (const auto& it : reservoir)
            result.emplace_back(it.item, it.weight);
        return result;
    }
};

int main() {
    std::mt19937 rng(42);
    vector<pair<string,double>> weighted_items = {
        {"rare1", 10.0}, {"rare2", 8.0}, {"common1", 1.0},
        {"common2", 0.5}, {"common3", 0.5}
    };

    const int num_runs = 100;
    const int sample_size = 3;
    std::map<string, int> item_counts;
    for (const auto& p : weighted_items) item_counts[p.first] = 0;

    for (int run = 0; run < num_runs; ++run) {
        WeightedReservoirSampler sampler(sample_size, rng);
        vector<pair<string,double>> stream;
        for (const auto& p : weighted_items) {
            int times = std::max(1, (int)p.second);
            for (int i = 0; i < times; ++i)
                stream.emplace_back(p.first, p.second);
        }
        std::shuffle(stream.begin(), stream.end(), rng);
        for (const auto& s : stream)
            sampler.process(s.first, s.second);
        for (const auto& s : sampler.get_sample())
            item_counts[s.first]++;
    }

    for (const auto& p : weighted_items) {
        double freq = item_counts[p.first] / double(num_runs);
        std::cout << p.first << " (weight " << p.second << "): " << freq << "\n";
    }

    double rare_freq = (item_counts["rare1"] + item_counts["rare2"]) / double(num_runs) / 2.0;
    double common_freq = (item_counts["common1"] + item_counts["common2"] + item_counts["common3"]) / double(num_runs) / 3.0;
    assert(rare_freq > common_freq);
    assert(rare_freq > 0.3);
    std::cout << "Weighted Reservoir Sampling: PASS\n";
    return 0;
}
