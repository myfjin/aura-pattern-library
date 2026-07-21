// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Space-Saving approximate top-k "heavy hitters": tracks only k counters over a
stream; when a new item arrives with counters full, it evicts the current
minimum and inherits (min_count + 1), so a frequent latecomer can still surface.
Use when exact per-item frequencies over a large/unbounded stream cost too much
memory. Oracle: on a skewed stream the reported top-3 items and their order
match the exact counts, and each estimate is >= the true count and within
stream_size/k of it (never under-counts, bounded over-count).
*/
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <random>
#include <string>
#include <vector>

// Space-Saving top-k heavy hitters.

class SpaceSavingTopK {
public:
    explicit SpaceSavingTopK(int k) : k_(k) {}

    void process(const std::string& item) {
        auto it = counters_.find(item);
        if (it != counters_.end()) {
            ++(it->second);
        } else if (static_cast<int>(counters_.size()) < k_) {
            counters_[item] = 1;
        } else {
            auto min_it = std::min_element(counters_.begin(), counters_.end(),
                [](const auto& a, const auto& b) { return a.second < b.second; });
            int min_count = min_it->second;
            counters_.erase(min_it);
            counters_[item] = min_count + 1;
        }
    }

    std::vector<std::pair<std::string, int>> get_top_k() const {
        std::vector<std::pair<std::string, int>> items(counters_.begin(), counters_.end());
        std::sort(items.begin(), items.end(),
            [](const auto& a, const auto& b) { return a.second > b.second; });
        return items;
    }

private:
    int k_;
    std::map<std::string, int> counters_;
};

int main() {
    std::mt19937 gen(42);

    const std::vector<std::string> items = {
        "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"
    };

    std::vector<std::string> stream;
    for (size_t i = 0; i < items.size(); ++i) {
        int freq = std::max(1, 100 / static_cast<int>(i + 1));
        for (int j = 0; j < freq; ++j) stream.push_back(items[i]);
    }
    std::shuffle(stream.begin(), stream.end(), gen);

    const int m = 6;
    SpaceSavingTopK ss(m);
    for (const auto& item : stream) ss.process(item);

    auto top3 = ss.get_top_k();
    top3.resize(std::min(top3.size(), size_t(3)));

    std::map<std::string, int> exact_counts;
    for (const auto& item : stream) ++exact_counts[item];
    std::vector<std::pair<std::string, int>> exact_top3(exact_counts.begin(), exact_counts.end());
    std::sort(exact_top3.begin(), exact_top3.end(),
        [](const auto& a, const auto& b) { return a.second > b.second; });
    exact_top3.resize(std::min(exact_top3.size(), size_t(3)));

    double err_bound = static_cast<double>(stream.size()) / m;
    for (size_t rank = 0; rank < top3.size(); ++rank) {
        assert(top3[rank].first == exact_top3[rank].first);
        assert(exact_top3[rank].second <= top3[rank].second);
        assert(top3[rank].second <= exact_top3[rank].second + err_bound);
    }

    std::cout << "PASS" << std::endl;
    return 0;
}
