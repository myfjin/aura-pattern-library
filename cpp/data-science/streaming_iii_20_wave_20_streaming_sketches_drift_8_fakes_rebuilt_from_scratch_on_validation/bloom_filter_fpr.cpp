// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Bloom Filter with Measured False-Positive Rate
 * 
 * Hash items to k positions in a bit array; false positive = query position all set but item not inserted.
 */

#include <vector>
#include <string>
#include <random>
#include <cassert>
#include <iostream>
#include <set>
#include <functional>

// Simple hash function using std::hash
size_t hash_string(const std::string& str, size_t seed = 0) {
    std::hash<std::string> hasher;
    return hasher(str) ^ seed;
}

double bloom_filter_fpr(const std::vector<std::string>& stream, size_t size = 2000, size_t k = 3) {
    /* Bloom filter membership test; return measured false-positive rate. */
    std::mt19937 rng(42);
    
    assert(size > 0 && k > 0);

    // Initialize bit array
    std::vector<bool> bits(size, false);

    // Insert stream items
    std::set<std::string> inserted(stream.begin(), stream.end());
    for (const auto& item : stream) {
        for (size_t i = 0; i < k; ++i) {
            size_t h = hash_string(item + "_" + std::to_string(i)) % size;
            bits[h] = true;
        }
    }

    // Test: query items not in stream for false positives
    std::vector<std::string> test_items;
    test_items.reserve(1000);
    for (int i = 0; i < 1000; ++i) {
        int val = std::uniform_int_distribution<int>(100000, 200000)(rng);
        if (inserted.find(std::to_string(val)) == inserted.end()) {
            test_items.push_back(std::to_string(val));
        }
    }

    int false_positives = 0;
    for (const auto& test_item : test_items) {
        bool test_passes = true;
        for (size_t i = 0; i < k; ++i) {
            size_t h = hash_string(test_item + "_" + std::to_string(i)) % size;
            if (!bits[h]) {
                test_passes = false;
                break;
            }
        }
        if (test_passes) {
            false_positives++;
        }
    }

    double measured_fpr = static_cast<double>(false_positives) / std::max(1, static_cast<int>(test_items.size()));

    // Theoretical FPR: (1 - e^(-k*n/m))^k
    size_t n = inserted.size();
    size_t m = size;
    double theoretical_fpr = std::pow(1.0 - std::exp(-static_cast<double>(k) * n / m), k);

    // Test for false negatives: all inserted items should pass membership test
    int false_negatives = 0;
    int test_count = std::min(100, static_cast<int>(inserted.size()));
    int tested = 0;
    for (const auto& item : inserted) {
        if (tested >= test_count) break;
        bool all_bits_set = true;
        for (size_t i = 0; i < k; ++i) {
            size_t h = hash_string(item + "_" + std::to_string(i)) % size;
            if (!bits[h]) {
                false_negatives++;
                all_bits_set = false;
                break;
            }
        }
        (void)all_bits_set;  // Suppress unused warning
        tested++;
    }

    assert(false_negatives == 0);
    assert(measured_fpr <= theoretical_fpr + 0.05);

    return measured_fpr;
}

int main() {
    std::mt19937 rng(42);
    std::uniform_int_distribution<int> uniform(0, 10000);

    std::vector<std::string> stream;
    stream.reserve(500);
    for (int i = 0; i < 500; ++i) {
        stream.push_back(std::to_string(uniform(rng)));
    }

    double fpr = bloom_filter_fpr(stream, 2000, 3);
    std::cout << "Bloom filter FPR: " << fpr << std::endl;
    std::cout << "bloom_filter_fpr.cpp PASS" << std::endl;
    return 0;
}
