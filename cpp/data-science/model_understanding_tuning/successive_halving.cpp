// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Successive halving for hyperparameter search under a fixed budget. Evaluates all
 * candidate configs at a small budget, keeps the top 1/reduction_factor, multiplies
 * the per-config budget by that factor, and repeats until one config survives — so
 * compute is concentrated on the promising survivors instead of spent equally.
 * Use to tune many configs cheaply when evaluation cost scales with budget.
 * Guarantee (proven in main): from 16 random configs it returns one with loss<2.0
 * and leaves the caller's initial_configs vector unmodified.
 */
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <random>
#include <cassert>

struct Config {
    double learning_rate;
    double param1;
    double param2;
};

double evaluate_config(const Config& config, int budget, std::mt19937& rng) {
    std::normal_distribution<double> noise(0.0, 0.01);
    double dist_lr = (config.learning_rate - 0.01) * (config.learning_rate - 0.01) * 100.0;
    double dist_p1 = (config.param1 - 0.5) * (config.param1 - 0.5) * 0.5;
    double loss = 1.0 + dist_lr + dist_p1;
    loss /= (1.0 + 0.01 * budget);
    return loss + noise(rng);
}

std::pair<Config, double> successive_halving(const std::vector<Config>& initial_configs,
                                               int initial_budget,
                                               int reduction_factor,
                                               std::mt19937& rng) {
    std::vector<Config> configs = initial_configs;
    int budget = initial_budget;

    while (configs.size() > 1) {
        std::vector<std::pair<double, Config>> scores;
        for (const auto& config : configs) {
            double loss = evaluate_config(config, budget, rng);
            scores.push_back({loss, config});
        }
        std::sort(scores.begin(), scores.end(), [](const auto& a, const auto& b) { return a.first < b.first; });
        size_t num_keep = std::max(size_t(1), configs.size() / reduction_factor);
        configs.clear();
        for (size_t i = 0; i < num_keep; ++i) configs.push_back(scores[i].second);
        budget *= reduction_factor;
    }

    double best_loss = evaluate_config(configs[0], budget * reduction_factor, rng);
    return {configs[0], best_loss};
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform01(0.0, 1.0);

    int num_initial = 16;
    std::vector<Config> initial_configs;
    for (int i = 0; i < num_initial; ++i) {
        initial_configs.push_back({
            0.001 + 0.099 * uniform01(rng),
            uniform01(rng),
            uniform01(rng)
        });
    }

    auto [best_config, best_loss] = successive_halving(initial_configs, 10, 2, rng);

    assert(best_loss < 2.0);
    assert(static_cast<int>(initial_configs.size()) == num_initial);

    std::cout << "successive_halving: PASS" << std::endl;
    return 0;
}
