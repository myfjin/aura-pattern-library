// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Tornado sensitivity analysis: for a profit model, perturb each input +/-10% one
at a time (others held at base), measure the swing in output, and rank inputs by
absolute impact. Use to find which driver a deterministic model is most sensitive
to before investing in better estimates for it.
Guarantee: on the base case, the top driver is price or volume, and every input
(including overhead and cost) shows a strictly positive sensitivity.
*/
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

double profit(double price, double volume, double cost, double overhead) {
    double revenue = price * volume;
    double total_cost = cost * volume + overhead;
    return revenue - total_cost;
}

int main() {
    // Base case values
    double base_price = 100.0;
    double base_volume = 1000.0;
    double base_cost = 30.0;
    double base_overhead = 10000.0;

    double base_profit = profit(base_price, base_volume, base_cost, base_overhead);
    (void)base_profit; // unused but retained for parity with oracle

    std::unordered_map<std::string, double> inputs = {
        {"price", base_price},
        {"volume", base_volume},
        {"cost", base_cost},
        {"overhead", base_overhead},
    };

    std::unordered_map<std::string, double> sensitivities;

    for (const auto& [input_name, base_value] : inputs) {
        double high_value = base_value * 1.1;
        double low_value = base_value * 0.9;

        double profit_high = 0.0, profit_low = 0.0;

        for (const auto& [name, value] : inputs) {
            double v_high = (name == input_name) ? high_value : value;
            double v_low  = (name == input_name) ? low_value  : value;

            if (name == "price") {
                profit_high += 0.0; // placeholder
            }
            (void)v_high;
            (void)v_low;
        }

        // Explicit compute using helper
        profit_high = profit(
            (input_name == "price") ? high_value : inputs.at("price"),
            (input_name == "volume") ? high_value : inputs.at("volume"),
            (input_name == "cost") ? high_value : inputs.at("cost"),
            (input_name == "overhead") ? high_value : inputs.at("overhead"));
        profit_low = profit(
            (input_name == "price") ? low_value : inputs.at("price"),
            (input_name == "volume") ? low_value : inputs.at("volume"),
            (input_name == "cost") ? low_value : inputs.at("cost"),
            (input_name == "overhead") ? low_value : inputs.at("overhead"));

        double impact = std::abs(profit_high - profit_low);
        sensitivities[input_name] = impact;
    }

    std::vector<std::pair<std::string, double>> ranked;
    for (const auto& kv : sensitivities)
        ranked.emplace_back(kv.first, kv.second);
    std::sort(ranked.begin(), ranked.end(), [](const auto& a, const auto& b) {
        return a.second > b.second;
    });

    const std::string& top_driver = ranked[0].first;
    assert(top_driver == "price" || top_driver == "volume");

    assert(sensitivities.at("overhead") > 0.0);
    assert(sensitivities.at("cost") > 0.0);

    std::cout << "PASS\n";
    return 0;
}
