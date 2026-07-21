// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Position-bias click model with inverse-propensity correction. Simulates user clicks
 * where click probability is true relevance discounted by a rank-dependent examination
 * factor 1/(1 + position*bias), so top-listed items get clicked even when less relevant.
 * IPW then divides each doc's clicks by its (floored) propensity to recover relevance.
 * Use to de-bias click logs before ranking by observed clicks.
 * Guarantees: ranking by raw clicks fails to put the most-relevant doc first, while the
 * IPW-corrected ranking restores it to the top.
 */
#include <random>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cassert>
#include <iostream>

std::map<std::string, int> generate_clicks_with_position_bias(
    const std::vector<std::string>& ranking,
    const std::map<std::string, double>& true_relevances,
    double position_bias,
    std::mt19937& gen) {

    std::map<std::string, int> clicks;
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    for (const auto& doc : ranking) clicks[doc] = 0;

    for (std::size_t position = 0; position < ranking.size(); ++position) {
        const std::string& doc = ranking[position];
        double position_bias_factor = 1.0 / (1.0 + static_cast<double>(position) * position_bias);
        double click_prob = position_bias_factor * true_relevances.at(doc);
        for (int user = 0; user < 200; ++user) {
            if (dist(gen) < click_prob) {
                clicks[doc] += 1;
            }
        }
    }
    return clicks;
}

std::map<std::string, double> inverse_propensity_weighting(
    const std::map<std::string, int>& clicks,
    const std::vector<std::string>& ranking,
    double position_bias) {

    std::map<std::string, double> weighted;
    for (std::size_t position = 0; position < ranking.size(); ++position) {
        const std::string& doc = ranking[position];
        double position_bias_factor = 1.0 / (1.0 + static_cast<double>(position) * position_bias);
        double denom = std::max(position_bias_factor, 0.1);
        weighted[doc] = static_cast<double>(clicks.at(doc)) / denom;
    }
    return weighted;
}

int main() {
    std::mt19937 gen(42);

    std::map<std::string, double> true_relevances = {
        {"A", 0.8}, {"B", 0.2}, {"C", 0.15}, {"D", 0.15}
    };

    std::vector<std::string> ranking = {"D", "C", "B", "A"};

    auto clicks = generate_clicks_with_position_bias(ranking, true_relevances, 2.0, gen);

    std::vector<std::string> naive_ranking = ranking;
    std::sort(naive_ranking.begin(), naive_ranking.end(),
              [&clicks](const std::string& a, const std::string& b) {
                  return clicks.at(a) > clicks.at(b);
              });

    auto weighted = inverse_propensity_weighting(clicks, ranking, 2.0);
    std::vector<std::string> ipw_ranking = ranking;
    std::sort(ipw_ranking.begin(), ipw_ranking.end(),
              [&weighted](const std::string& a, const std::string& b) {
                  return weighted.at(a) > weighted.at(b);
              });

    std::vector<std::string> true_ranking = ranking;
    std::sort(true_ranking.begin(), true_ranking.end(),
              [&true_relevances](const std::string& a, const std::string& b) {
                  return true_relevances.at(a) > true_relevances.at(b);
              });

    assert(naive_ranking[0] != "A");
    assert(ipw_ranking[0] == "A");

    std::cout << "True ranking: ";
    for (const auto& d : true_ranking) std::cout << d;
    std::cout << " | Naive (biased): ";
    for (const auto& d : naive_ranking) std::cout << d;
    std::cout << " | IPW (corrected): ";
    for (const auto& d : ipw_ranking) std::cout << d;
    std::cout << " | PASS" << std::endl;
    return 0;
}
