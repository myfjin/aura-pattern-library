// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstddef>
#include <iostream>
#include <random>
#include <vector>

struct MultiArmedBandit {
    std::vector<double> arm_means;
    std::vector<double> arm_stds;
    std::mt19937 rng;
    std::normal_distribution<double> normal;

    explicit MultiArmedBandit(const std::vector<double>& means,
                              const std::vector<double>& stds = {})
        : arm_means(means), rng(42), normal(0.0, 1.0) {
        if (stds.empty()) {
            arm_stds.assign(means.size(), 1.0);
        } else {
            arm_stds = stds;
        }
    }

    double pull(int arm) {
        return arm_means[arm] + arm_stds[arm] * normal(rng);
    }

    std::pair<double, std::vector<int>> run_pure_greedy(int num_pulls = 1000) {
        std::vector<double> estimated_means(arm_means.size(), 0.0);
        std::vector<int> pulls_per_arm(arm_means.size(), 0);
        std::vector<int> arm_sequence;
        arm_sequence.reserve(num_pulls);

        double total_reward = 0.0;
        for (std::size_t arm = 0; arm < arm_means.size(); ++arm) {
            estimated_means[arm] = pull(static_cast<int>(arm));
            pulls_per_arm[arm] = 1;
            total_reward += estimated_means[arm];
            arm_sequence.push_back(static_cast<int>(arm));
        }

        int best_arm = static_cast<int>(std::max_element(estimated_means.begin(), estimated_means.end()) - estimated_means.begin());
        for (int i = 0; i < num_pulls - static_cast<int>(arm_means.size()); ++i) {
            double reward = pull(best_arm);
            total_reward += reward;
            ++pulls_per_arm[best_arm];
            arm_sequence.push_back(best_arm);
        }
        return {total_reward, arm_sequence};
    }

    std::pair<double, std::vector<int>> run_epsilon_greedy(double epsilon = 0.1, int num_pulls = 1000) {
        std::vector<double> estimated_means(arm_means.size(), 0.0);
        std::vector<int> pull_counts(arm_means.size(), 0);
        std::vector<int> arm_sequence;
        arm_sequence.reserve(num_pulls);
        std::uniform_real_distribution<double> uni(0.0, 1.0);
        std::uniform_int_distribution<int> arm_chooser(0, static_cast<int>(arm_means.size()) - 1);

        double total_reward = 0.0;
        for (std::size_t arm = 0; arm < arm_means.size(); ++arm) {
            estimated_means[arm] = pull(static_cast<int>(arm));
            pull_counts[arm] = 1;
            total_reward += estimated_means[arm];
            arm_sequence.push_back(static_cast<int>(arm));
        }

        for (int i = 0; i < num_pulls - static_cast<int>(arm_means.size()); ++i) {
            int arm;
            if (uni(rng) < epsilon) {
                arm = arm_chooser(rng);
            } else {
                arm = static_cast<int>(std::max_element(estimated_means.begin(), estimated_means.end()) - estimated_means.begin());
            }
            double reward = pull(arm);
            total_reward += reward;
            ++pull_counts[arm];
            estimated_means[arm] += (reward - estimated_means[arm]) / pull_counts[arm];
            arm_sequence.push_back(arm);
        }
        return {total_reward, arm_sequence};
    }
};

int main() {
    std::vector<double> arm_means = {1.0, 1.5, 2.0, 0.5, 1.2};
    MultiArmedBandit bandit(arm_means);

    int num_pulls = 1000;
    auto greedy_result = bandit.run_pure_greedy(num_pulls);
    double reward_greedy = greedy_result.first;
    const auto& sequence_greedy = greedy_result.second;
    std::vector<int> pulls_per_arm_greedy(5, 0);
    for (int a : sequence_greedy) ++pulls_per_arm_greedy[a];

    auto epsilon_result = bandit.run_epsilon_greedy(0.1, num_pulls);
    double reward_epsilon = epsilon_result.first;
    const auto& sequence_epsilon = epsilon_result.second;
    std::vector<int> pulls_per_arm_epsilon(5, 0);
    for (int a : sequence_epsilon) ++pulls_per_arm_epsilon[a];

    assert(static_cast<int>(sequence_greedy.size()) == num_pulls);
    assert(static_cast<int>(sequence_epsilon.size()) == num_pulls);

    int pulls_arm2_epsilon = pulls_per_arm_epsilon[2];
    assert(pulls_arm2_epsilon > 0);
    assert(reward_greedy > 0);
    assert(reward_epsilon > 0);

    int max_pulls_epsilon = *std::max_element(pulls_per_arm_epsilon.begin(), pulls_per_arm_epsilon.end());
    assert(pulls_per_arm_epsilon[2] >= 0.5 * max_pulls_epsilon);

    std::cout << "epsilon_greedy_bandit.cpp: greedy_reward=" << reward_greedy
              << " epsilon_reward=" << reward_epsilon
              << " best_arm_pulls=" << pulls_per_arm_epsilon[2] << " PASS\n";
    return 0;
}
