// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Apriori algorithm for frequent itemsets and association rules.
 *
 * Restored generate_rules() + rule asserts per Python oracle.
 */

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <algorithm>

using namespace std;

map<set<int>, double> apriori(const vector<set<int>>& transactions, double min_support) {
    map<set<int>, double> all_frequent;

    // Count 1-itemsets
    map<int, int> item_counts;
    for (const auto& trans : transactions) {
        for (int item : trans) {
            item_counts[item]++;
        }
    }

    // Filter by min_support
    int min_count = static_cast<int>(min_support * transactions.size());
    map<set<int>, double> current_frequent;
    for (const auto& [item, count] : item_counts) {
        if (count >= min_count) {
            set<int> itemset = {item};
            double support = static_cast<double>(count) / transactions.size();
            current_frequent[itemset] = support;
            all_frequent[itemset] = support;
        }
    }

    // Generate k-itemsets iteratively
    int k = 2;
    while (!current_frequent.empty()) {
        map<set<int>, int> candidates;
        vector<set<int>> frequent_list;
        for (const auto& [itemset, support] : current_frequent) {
            frequent_list.push_back(itemset);
        }

        for (size_t i = 0; i < frequent_list.size(); i++) {
            for (size_t j = i + 1; j < frequent_list.size(); j++) {
                set<int> candidate;
                set_union(frequent_list[i].begin(), frequent_list[i].end(),
                          frequent_list[j].begin(), frequent_list[j].end(),
                          inserter(candidate, candidate.begin()));
                if (static_cast<int>(candidate.size()) == k) {
                    candidates[candidate] = 0;
                }
            }
        }

        // Count support for candidates
        for (const auto& trans : transactions) {
            for (auto& [candidate, count] : candidates) {
                bool is_subset = true;
                for (int item : candidate) {
                    if (trans.find(item) == trans.end()) {
                        is_subset = false;
                        break;
                    }
                }
                if (is_subset) {
                    candidates[candidate]++;
                }
            }
        }

        // Filter by min_support
        map<set<int>, double> next_frequent;
        for (const auto& [itemset, count] : candidates) {
            if (count >= min_count) {
                double support = static_cast<double>(count) / transactions.size();
                next_frequent[itemset] = support;
                all_frequent[itemset] = support;
            }
        }

        if (next_frequent.empty()) break;

        current_frequent = next_frequent;
        k++;
    }

    return all_frequent;
}

vector<tuple<set<int>, set<int>, double>> generate_rules(
    const map<set<int>, double>& frequent_itemsets,
    double min_confidence
) {
    vector<tuple<set<int>, set<int>, double>> rules;

    for (const auto& [itemset, support] : frequent_itemsets) {
        if (itemset.size() < 2) continue;

        vector<int> items(itemset.begin(), itemset.end());
        int m = static_cast<int>(items.size());

        // Generate all non-empty proper subsets as antecedents
        int total_subsets = 1 << m;
        for (int mask = 1; mask < total_subsets - 1; ++mask) {
            set<int> antecedent;
            for (int i = 0; i < m; ++i) {
                if (mask & (1 << i)) antecedent.insert(items[i]);
            }
            set<int> consequent;
            for (int i = 0; i < m; ++i) {
                if (!(mask & (1 << i))) consequent.insert(items[i]);
            }

            auto it = frequent_itemsets.find(antecedent);
            if (it != frequent_itemsets.end() && it->second > 0.0) {
                double confidence = support / it->second;
                if (confidence >= min_confidence) {
                    rules.emplace_back(antecedent, consequent, confidence);
                }
            }
        }
    }

    return rules;
}

int main() {
    vector<set<int>> transactions = {
        {0, 1, 2},
        {0, 1, 4},
        {0, 1},
        {2, 3, 5},
        {2, 3},
        {1, 2},
        {3, 4, 5},
        {0, 1, 3},
    };

    // Find frequent itemsets (min support 30%)
    auto frequent = apriori(transactions, 0.3);

    // Check that planted itemset {0, 1} is frequent
    set<int> planted_itemset = {0, 1};
    assert(frequent.find(planted_itemset) != frequent.end());

    // Generate rules
    auto rules = generate_rules(frequent, 0.5);

    // Verify at least one rule found
    assert(!rules.empty());

    // Check that a rule involving the planted itemset exists
    bool rule_found = false;
    for (const auto& [ante, cons, conf] : rules) {
        set<int> union_set = ante;
        union_set.insert(cons.begin(), cons.end());
        if (union_set.find(0) != union_set.end() && union_set.find(1) != union_set.end()) {
            rule_found = true;
            break;
        }
    }
    assert(rule_found);

    cout << "apriori_frequent_itemsets: " << frequent.size() << " itemsets, "
         << rules.size() << " rules PASS" << endl;

    return 0;
}
