// rank_fusion_rrf.cpp — Reciprocal Rank Fusion.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

static double rrf_score(const std::string& item,
                        const std::vector<std::vector<std::string>>& rankings,
                        int k) {
    double score = 0.0;
    for (const auto& ranking : rankings) {
        auto it = std::find(ranking.begin(), ranking.end(), item);
        if (it != ranking.end()) {
            int rank = static_cast<int>(it - ranking.begin());
            score += 1.0 / (k + rank + 1);
        }
    }
    return score;
}

static std::vector<std::string> rrf_fusion(
        const std::vector<std::vector<std::string>>& rankings, int k) {
    std::set<std::string> all_items;
    for (const auto& ranking : rankings)
        all_items.insert(ranking.begin(), ranking.end());

    std::unordered_map<std::string, double> scores;
    for (const auto& item : all_items)
        scores[item] = rrf_score(item, rankings, k);

    std::vector<std::string> result(all_items.begin(), all_items.end());
    std::sort(result.begin(), result.end(),
              [&](const std::string& a, const std::string& b) {
                  return scores[a] > scores[b];
              });
    return result;
}

static double ndcg_simple(const std::vector<std::string>& ranking,
                          const std::vector<std::string>& ideal_order) {
    auto relevance = [&](const std::string& item, int rank) -> double {
        // item is relevant if it appears in ideal_order[:rank+1]
        if (rank + 1 > static_cast<int>(ideal_order.size())) return 0.0;
        for (int i = 0; i <= rank; ++i)
            if (ideal_order[i] == item) return 1.0;
        return 0.0;
    };

    double dcg = 0.0;
    for (std::size_t i = 0; i < ranking.size(); ++i) {
        dcg += relevance(ranking[i], static_cast<int>(i)) / std::log2(i + 2);
    }

    double ideal_dcg = 0.0;
    for (std::size_t i = 0; i < ideal_order.size(); ++i)
        ideal_dcg += 1.0 / std::log2(i + 2);

    return ideal_dcg > 0.0 ? dcg / ideal_dcg : 0.0;
}

int main() {
    std::vector<std::string> ideal = {"A", "B", "C", "D", "E"};
    std::vector<std::string> ranker1 = {"A", "C", "B", "E", "D"};
    std::vector<std::string> ranker2 = {"B", "A", "D", "C", "E"};

    double ndcg1 = ndcg_simple(ranker1, ideal);
    double ndcg2 = ndcg_simple(ranker2, ideal);

    auto fused = rrf_fusion({ranker1, ranker2}, 60);
    double ndcg_fused = ndcg_simple(fused, ideal);

    assert(ndcg_fused > ndcg1);
    assert(ndcg_fused > ndcg2);
    double avg = (ndcg1 + ndcg2) / 2.0;
    assert(ndcg_fused > avg);

    std::printf("Ranker1 NDCG: %.2f | Ranker2 NDCG: %.2f | Avg individual: %.2f | Fused: %.2f | PASS\n",
                ndcg1, ndcg2, avg, ndcg_fused);
    return 0;
}
