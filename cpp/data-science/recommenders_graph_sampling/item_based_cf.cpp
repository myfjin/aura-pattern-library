// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Item-based collaborative filtering.
 *
 * Oracle asserts:
 *   len(recommendations) > 0
 *   all recommended item_id not in user's rated items
 *   len(recommended_items ∩ unseen_items) > 0
 */

#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>

double adjusted_cosine_similarity(const std::map<int, double>& item_a,
                                  const std::map<int, double>& item_b,
                                  const std::map<int, double>& user_means) {
    std::vector<int> common;
    for (const auto& kv : item_a) {
        if (item_b.find(kv.first) != item_b.end()) common.push_back(kv.first);
    }
    if (common.empty()) return 0.0;

    double dot = 0.0, na = 0.0, nb = 0.0;
    for (int u : common) {
        double adj_a = item_a.at(u) - user_means.at(u);
        double adj_b = item_b.at(u) - user_means.at(u);
        dot += adj_a * adj_b;
        na += adj_a * adj_a;
        nb += adj_b * adj_b;
    }
    if (na == 0.0 || nb == 0.0) return 0.0;
    return dot / (std::sqrt(na) * std::sqrt(nb));
}

std::vector<std::pair<int, double>> recommend_items(
    int user_id,
    const std::map<int, std::map<int, double>>& ratings_by_user,
    const std::map<int, std::map<int, double>>& ratings_by_item,
    int k = 3) {

    auto it = ratings_by_user.find(user_id);
    if (it == ratings_by_user.end()) return {};

    std::set<int> user_rated_items;
    for (const auto& kv : it->second) user_rated_items.insert(kv.first);

    std::map<int, double> user_means;
    for (const auto& kv : ratings_by_user) {
        double sum = 0.0;
        for (const auto& ir : kv.second) sum += ir.second;
        user_means[kv.first] = kv.second.empty() ? 0.0 : sum / kv.second.size();
    }

    std::map<int, double> item_scores;
    for (const auto& kv : ratings_by_item) {
        int item_id = kv.first;
        if (user_rated_items.count(item_id)) continue;

        double sim_sum = 0.0, weight_sum = 0.0;
        for (int rated_item_id : user_rated_items) {
            double sim = adjusted_cosine_similarity(kv.second, ratings_by_item.at(rated_item_id), user_means);
            double user_rating = it->second.at(rated_item_id);
            sim_sum += sim * user_rating;
            weight_sum += std::abs(sim);
        }
        if (weight_sum > 0.0) item_scores[item_id] = sim_sum / weight_sum;
    }

    std::vector<std::pair<int, double>> sorted_scores(item_scores.begin(), item_scores.end());
    std::sort(sorted_scores.begin(), sorted_scores.end(),
              [](const auto& a, const auto& b) { return a.second > b.second; });
    if (static_cast<int>(sorted_scores.size()) > k) sorted_scores.resize(k);
    return sorted_scores;
}

int main() {
    std::map<int, std::map<int, double>> ratings_by_user = {
        {0, {{0, 5.0}, {1, 4.0}}},
        {1, {{1, 4.0}, {2, 5.0}}},
        {2, {{2, 5.0}, {3, 4.0}}},
        {3, {{0, 3.0}, {3, 4.0}, {4, 5.0}}}
    };

    std::map<int, std::map<int, double>> ratings_by_item;
    for (const auto& kv : ratings_by_user) {
        for (const auto& ir : kv.second) {
            ratings_by_item[ir.first][kv.first] = ir.second;
        }
    }

    auto recs = recommend_items(0, ratings_by_user, ratings_by_item, 2);

    assert(!recs.empty());
    std::set<int> unseen = {2, 3, 4};
    std::set<int> recommended;
    for (const auto& p : recs) {
        assert(unseen.count(p.first));
        recommended.insert(p.first);
    }
    assert(!recommended.empty());

    std::cout << "item_based_cf.cpp PASS: recommendations=[";
    for (size_t i = 0; i < recs.size(); ++i) {
        if (i) std::cout << ", ";
        std::cout << "(" << recs[i].first << ", " << recs[i].second << ")";
    }
    std::cout << "]" << std::endl;
    return 0;
}
