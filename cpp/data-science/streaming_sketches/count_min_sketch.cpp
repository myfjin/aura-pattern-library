// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Count-Min Sketch for Frequency Estimation
 * 
 * A streaming data structure using hash functions to estimate item frequencies with bounded error.
 */

#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <random>
#include <functional>
#include <set>

class CountMinSketch {
public:
    int width, depth;
    double epsilon;
    std::vector<std::vector<int>> table;
    std::vector<int> seeds;

    int hash(const std::string& item, int seed) const {
        std::hash<std::string> hasher;
        return static_cast<int>((hasher(item) ^ seed) % width);
    }

public:
    CountMinSketch(int w = 100, int d = 5, double eps = 0.01)
        : width(w), depth(d), epsilon(eps), table(d, std::vector<int>(w, 0)) {
        for (int i = 0; i < depth; ++i) seeds.push_back(42 + i);
    }

    void increment(const std::string& item, int count = 1) {
        for (int d = 0; d < depth; ++d) {
            int idx = hash(item, seeds[d]);
            table[d][idx] += count;
        }
    }

    int query(const std::string& item) const {
        int min_val = table[0][hash(item, seeds[0])];
        for (int d = 1; d < depth; ++d) {
            int val = table[d][hash(item, seeds[d])];
            if (val < min_val) min_val = val;
        }
        return min_val;
    }
};

int main() {
    std::mt19937 rng(42);

    // Create stream with planted heavy hitters
    std::vector<std::string> stream;
    for (int i = 0; i < 50; ++i) stream.push_back("cat");
    for (int i = 0; i < 40; ++i) stream.push_back("dog");

    std::vector<std::string> light_items = {"bird", "fish", "lion", "tiger", "ant", "bee", "fox", "owl"};
    std::uniform_int_distribution<int> light_dist(1, 5);
    for (const auto& item : light_items) {
        for (int i = 0; i < light_dist(rng); ++i) {
            stream.push_back(item);
        }
    }

    // Shuffle
    std::shuffle(stream.begin(), stream.end(), rng);

    // Process stream
    CountMinSketch sketch(100, 5);
    for (const auto& item : stream) {
        sketch.increment(item);
    }

    // Query estimates
    int cat_est = sketch.query("cat");
    int dog_est = sketch.query("dog");

    // The sketch provides upper bounds: estimate >= true count
    assert(cat_est >= 50);
    assert(dog_est >= 40);

    // Verify epsilon error bound (rough check)
    int total_stream = static_cast<int>(stream.size());
    int max_allowed_error = static_cast<int>(sketch.epsilon * total_stream) + 5;
    assert(cat_est - 50 <= max_allowed_error);

    std::cout << "Count-Min Sketch: PASS" << std::endl;
    return 0;
}
