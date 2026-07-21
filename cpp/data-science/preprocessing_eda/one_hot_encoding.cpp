// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * One-hot encoder. fit builds a vocabulary of unique categories (assigned indices in
 * sorted order); transform maps each value to a 0/1 indicator vector. Unseen categories
 * either throw (handle_unknown="error") or become an all-zero row (handle_unknown="ignore").
 * Use to turn a categorical feature into fixed-width binary columns for a model.
 * Guarantees: every known-category row sums to exactly 1, encode->decode round-trips
 * back to the original labels, and unknown categories follow the chosen policy.
 */
#include <cassert>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

class OneHotEncoder {
public:
    std::map<std::string, int> vocabulary;
    int n_features = 0;
    std::string handle_unknown = "error";

    explicit OneHotEncoder(std::string handle_unknown_ = "error")
        : handle_unknown(std::move(handle_unknown_)) {}

    OneHotEncoder& fit(const std::vector<std::string>& data) {
        std::set<std::string> uniq(data.begin(), data.end());
        vocabulary.clear();
        int i = 0;
        for (const auto& cat : uniq) {
            vocabulary[cat] = i++;
        }
        n_features = static_cast<int>(vocabulary.size());
        return *this;
    }

    std::vector<std::vector<int>> transform(const std::vector<std::string>& data) const {
        std::vector<std::vector<int>> result;
        result.reserve(data.size());
        for (const auto& value : data) {
            auto it = vocabulary.find(value);
            if (it == vocabulary.end()) {
                if (handle_unknown == "error") {
                    throw std::runtime_error("Unknown category: " + value);
                } else {
                    result.emplace_back(n_features, 0);
                }
            } else {
                std::vector<int> vec(n_features, 0);
                vec[it->second] = 1;
                result.push_back(std::move(vec));
            }
        }
        return result;
    }

    std::vector<std::vector<int>> fit_transform(const std::vector<std::string>& data) {
        return fit(data).transform(data);
    }
};

int main() {
    std::vector<std::string> animals = {"cat", "dog", "cat", "bird", "dog", "cat", "bird"};

    OneHotEncoder enc;
    auto transformed = enc.fit_transform(animals);

    assert((enc.vocabulary == std::map<std::string, int>{{"bird", 0}, {"cat", 1}, {"dog", 2}}));
    assert(enc.n_features == 3);

    for (std::size_t i = 0; i < transformed.size(); ++i) {
        int s = 0;
        for (int v : transformed[i]) s += v;
        assert(s == 1);
    }

    std::vector<std::string> decoded;
    for (const auto& vec : transformed) {
        int idx = static_cast<int>(std::find(vec.begin(), vec.end(), 1) - vec.begin());
        for (const auto& kv : enc.vocabulary) {
            if (kv.second == idx) {
                decoded.push_back(kv.first);
                break;
            }
        }
    }
    assert(decoded == animals);

    OneHotEncoder enc_ignore("ignore");
    enc_ignore.fit(animals);
    auto unknown_result = enc_ignore.transform({"cat", "elephant"});
    assert((unknown_result[0] == std::vector<int>{0, 1, 0}));
    assert((unknown_result[1] == std::vector<int>{0, 0, 0}));

    std::cout << "one_hot_encoding.cpp: PASS\n";
    return 0;
}
