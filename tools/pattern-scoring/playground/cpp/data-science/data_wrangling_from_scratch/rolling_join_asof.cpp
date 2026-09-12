// As-Of Join (Rolling Join): for each left row, find the nearest preceding right row on a key.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cassert>
#include <algorithm>
#include <limits>

using Row = std::map<std::string, double>; // numeric columns only; keep tags separately

struct TaggedRow {
    int key;
    std::string side;
    std::map<std::string, double> values;
};

std::vector<TaggedRow> asofJoin(const std::vector<TaggedRow>& left,
                                const std::vector<TaggedRow>& right,
                                const std::string& /*key*/) {
    std::vector<TaggedRow> right_sorted = right;
    std::sort(right_sorted.begin(), right_sorted.end(), [](const TaggedRow& a, const TaggedRow& b) {
        return a.key < b.key;
    });

    std::vector<TaggedRow> result;
    for (const auto& left_row : left) {
        const TaggedRow* nearest = nullptr;
        for (auto it = right_sorted.rbegin(); it != right_sorted.rend(); ++it) {
            if (it->key <= left_row.key) {
                nearest = &(*it);
                break;
            }
        }
        TaggedRow merged = left_row;
        if (nearest != nullptr) {
            for (const auto& kv : nearest->values) {
                if (kv.first != "time")
                    merged.values[kv.first] = kv.second;
            }
        }
        result.push_back(merged);
    }
    return result;
}

std::vector<TaggedRow> bruteForceAsof(const std::vector<TaggedRow>& left,
                                    const std::vector<TaggedRow>& right,
                                    const std::string& /*key*/) {
    std::vector<TaggedRow> result;
    for (const auto& left_row : left) {
        const TaggedRow* nearest = nullptr;
        int best_key = std::numeric_limits<int>::min();
        for (const auto& right_row : right) {
            if (right_row.key <= left_row.key && right_row.key > best_key) {
                best_key = right_row.key;
                nearest = &right_row;
            }
        }
        TaggedRow merged = left_row;
        if (nearest != nullptr) {
            for (const auto& kv : nearest->values) {
                if (kv.first != "time")
                    merged.values[kv.first] = kv.second;
            }
        }
        result.push_back(merged);
    }
    return result;
}

int main() {
    std::vector<TaggedRow> trades = {
        {100, "trade", {{"price", 50}}},
        {150, "trade", {{"price", 51}}},
        {200, "trade", {{"price", 52}}},
    };
    std::vector<TaggedRow> quotes = {
        {80, "quote", {{"bid", 49}, {"ask", 50}}},
        {120, "quote", {{"bid", 50}, {"ask", 51}}},
        {180, "quote", {{"bid", 51}, {"ask", 52}}},
    };

    auto joined = asofJoin(trades, quotes, "time");
    auto brute_joined = bruteForceAsof(trades, quotes, "time");

    for (size_t i = 0; i < joined.size(); ++i) {
        assert(joined[i].key == brute_joined[i].key);
        assert(joined[i].values.at("bid") == brute_joined[i].values.at("bid"));
    }

    assert(joined[0].key == 100);
    assert(joined[0].values.at("bid") == 49);
    assert(joined[1].values.at("bid") == 50);
    assert(joined[2].values.at("bid") == 51);

    std::cout << "ROLLING_JOIN_ASOF PASS\n";
    return 0;
}
