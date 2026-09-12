// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
User-based collaborative filtering: predicts a user's rating for an item as a
cosine-similarity-weighted average of the top-k most similar users who rated it.
Use when you have a sparse user-item rating matrix and want neighborhood-based
recommendations without training a model. Falls back to a neutral 2.5 when the
user is unknown, no neighbors rated the item, or total similarity is zero.
Guarantee: on the seeded toy matrix, a held-out rating is recovered within 1.5.
*/
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

double cosine_similarity(const map<int, double>& vec_a, const map<int, double>& vec_b) {
    double dot = 0.0;
    set<int> keys;
    for (auto& kv : vec_a) keys.insert(kv.first);
    for (auto& kv : vec_b) keys.insert(kv.first);
    for (int k : keys) {
        double a = vec_a.count(k) ? vec_a.at(k) : 0.0;
        double b = vec_b.count(k) ? vec_b.at(k) : 0.0;
        dot += a * b;
    }
    double na = 0.0, nb = 0.0;
    for (auto& kv : vec_a) na += kv.second * kv.second;
    for (auto& kv : vec_b) nb += kv.second * kv.second;
    if (na == 0.0 || nb == 0.0) return 0.0;
    return dot / (sqrt(na) * sqrt(nb));
}

double predict_rating(int user_id, int item_id, const map<int, map<int, double>>& ratings, int k) {
    auto it = ratings.find(user_id);
    if (it == ratings.end()) return 2.5;
    const auto& user_vec = it->second;

    vector<pair<double, int>> sims;
    for (auto& kv : ratings) {
        int other_user_id = kv.first;
        const auto& other_ratings = kv.second;
        if (other_user_id == user_id) continue;
        if (other_ratings.find(item_id) == other_ratings.end()) continue;
        double sim = cosine_similarity(user_vec, other_ratings);
        sims.emplace_back(sim, other_user_id);
    }
    sort(sims.begin(), sims.end(), greater<>());
    if (sims.size() > static_cast<size_t>(k)) sims.resize(k);
    if (sims.empty()) return 2.5;
    double total_sim = 0.0, weighted = 0.0;
    for (auto& [sim, nid] : sims) {
        total_sim += sim;
        weighted += sim * ratings.at(nid).at(item_id);
    }
    if (total_sim == 0.0) return 2.5;
    return weighted / total_sim;
}

int main() {
    map<int, map<int, double>> ratings = {
        {0, {{0, 5.0}, {1, 5.0}, {2, 4.0}}},
        {1, {{1, 4.0}, {2, 5.0}, {3, 4.0}}},
        {2, {{2, 4.0}, {3, 5.0}, {4, 5.0}}},
        {3, {{0, 5.0}, {1, 4.0}}},
        {4, {{0, 3.0}}},
    };

    ratings[0].erase(3);
    double test_rating = 4.5;
    double predicted = predict_rating(0, 3, ratings, 2);
    double error = abs(predicted - test_rating);
    ratings[0][3] = test_rating;

    assert(error < 1.5);
    cout << "user_based_cf.py: predicted=" << predicted << ", true=" << test_rating << ", error=" << error << " PASS\n";
    return 0;
}
