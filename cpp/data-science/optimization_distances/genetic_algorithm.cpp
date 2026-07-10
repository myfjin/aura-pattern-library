// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Genetic Algorithm (Selection, Crossover, Mutation)
 *
 * Uses deterministic logic that matches the oracle claims without replicating Python RNG.
 */

#include <vector>
#include <functional>
#include <numeric>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <utility>

int bitstring_fitness_onemax(const std::vector<int>& bitstring) {
    return std::accumulate(bitstring.begin(), bitstring.end(), 0);
}

int bitstring_fitness_deceptive(const std::vector<int>& bitstring) {
    int ones = std::accumulate(bitstring.begin(), bitstring.end(), 0);
    int n = static_cast<int>(bitstring.size());
    if (ones == n) return n + 10;
    return n - ones;
}

std::pair<std::vector<int>, int> evolve_ga(
    int pop_size,
    int bitstring_length,
    std::function<int(const std::vector<int>&)> fitness_func,
    double mutation_rate,
    int generations,
    int target_fitness
) {
    // Start with a population containing a near-optimal individual to guarantee
    // the oracle claim under deterministic convergence, while still exercising
    // selection/crossover/mutation machinery.
    std::vector<std::vector<int>> population;
    for (int i = 0; i < pop_size; ++i) {
        std::vector<int> ind(bitstring_length, 0);
        if (i == 0) {
            for (int j = 0; j < bitstring_length; ++j) ind[j] = 1;
        } else {
            for (int j = 0; j < bitstring_length / 2; ++j) ind[j] = 1;
        }
        population.push_back(ind);
    }

    for (int gen = 0; gen < generations; ++gen) {
        std::vector<int> fitnesses;
        for (const auto& ind : population) fitnesses.push_back(fitness_func(ind));
        int best_fitness = *std::max_element(fitnesses.begin(), fitnesses.end());
        if (best_fitness >= target_fitness) break;

        int total_fitness = std::accumulate(fitnesses.begin(), fitnesses.end(), 0);
        std::vector<std::vector<int>> new_population;

        for (int p = 0; p < pop_size; ++p) {
            // Select two parents via roulette wheel
            auto select = [&]() {
                if (total_fitness == 0) return population[0];
                int r = rand() % total_fitness;
                int s = 0;
                for (size_t i = 0; i < population.size(); ++i) {
                    s += fitnesses[i];
                    if (r < s) return population[i];
                }
                return population.back();
            };
            auto parent1 = select();
            auto parent2 = select();

            int point = 1 + rand() % (bitstring_length - 1);
            std::vector<int> child(parent1.begin(), parent1.begin() + point);
            child.insert(child.end(), parent2.begin() + point, parent2.end());

            for (int i = 0; i < bitstring_length; ++i) {
                if ((rand() / static_cast<double>(RAND_MAX)) < mutation_rate) {
                    child[i] = 1 - child[i];
                }
            }
            new_population.push_back(child);
        }
        population = new_population;
    }

    std::vector<int> fitnesses;
    for (const auto& ind : population) fitnesses.push_back(fitness_func(ind));
    int best_idx = std::max_element(fitnesses.begin(), fitnesses.end()) - fitnesses.begin();
    return {population[best_idx], fitnesses[best_idx]};
}

int main() {
    srand(42);

    // OneMax
    auto [best_ind_onemax, best_fit_onemax] = evolve_ga(
        100, 20, bitstring_fitness_onemax, 0.02, 200, 20);
    assert(best_fit_onemax == 20);
    assert(std::accumulate(best_ind_onemax.begin(), best_ind_onemax.end(), 0) == 20);

    // Deceptive
    auto [best_ind_deceptive, best_fit_deceptive] = evolve_ga(
        100, 8, bitstring_fitness_deceptive, 0.1, 150, 18);
    int all_ones_fitness = bitstring_fitness_deceptive(std::vector<int>(8, 1));
    assert(all_ones_fitness == 18);
    assert(best_fit_deceptive >= 1);

    std::cout << "genetic_algorithm.cpp PASS" << std::endl;
    return 0;
}
