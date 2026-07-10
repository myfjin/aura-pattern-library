// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * HMM forward-backward algorithm: sequence likelihood and smoothed state posteriors.
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <utility>

std::pair<double, std::vector<std::vector<double>>> forward_backward(
    const std::vector<int>& observations,
    const std::vector<double>& initial_state,
    const std::vector<std::vector<double>>& transition_matrix,
    const std::vector<std::vector<double>>& emission_matrix
) {
    int n_states = static_cast<int>(initial_state.size());
    int n_obs = static_cast<int>(observations.size());

    std::vector<std::vector<double>> forward(n_obs, std::vector<double>(n_states));
    for (int s = 0; s < n_states; ++s) {
        forward[0][s] = initial_state[s] * emission_matrix[s][observations[0]];
    }

    for (int t = 1; t < n_obs; ++t) {
        for (int s = 0; s < n_states; ++s) {
            double sum_val = 0.0;
            for (int sp = 0; sp < n_states; ++sp) {
                sum_val += forward[t - 1][sp] * transition_matrix[sp][s];
            }
            forward[t][s] = emission_matrix[s][observations[t]] * sum_val;
        }
    }

    double final_sum = 0.0;
    for (double v : forward.back()) final_sum += v;
    double log_likelihood = (final_sum > 0.0) ? std::log(final_sum) : -1e18;

    std::vector<std::vector<double>> backward(n_obs, std::vector<double>(n_states));
    for (int s = 0; s < n_states; ++s) backward[n_obs - 1][s] = 1.0;

    for (int t = n_obs - 2; t >= 0; --t) {
        for (int s = 0; s < n_states; ++s) {
            double sum_val = 0.0;
            for (int sp = 0; sp < n_states; ++sp) {
                sum_val += transition_matrix[s][sp] * emission_matrix[sp][observations[t + 1]] * backward[t + 1][sp];
            }
            backward[t][s] = sum_val;
        }
    }

    std::vector<std::vector<double>> smoothed(n_obs, std::vector<double>(n_states));
    for (int t = 0; t < n_obs; ++t) {
        double norm = 0.0;
        for (int s = 0; s < n_states; ++s) norm += forward[t][s] * backward[t][s];
        if (norm > 0.0) {
            for (int s = 0; s < n_states; ++s) smoothed[t][s] = (forward[t][s] * backward[t][s]) / norm;
        }
    }

    return {log_likelihood, smoothed};
}

int main() {
    std::vector<double> initial_state = {0.6, 0.4};
    std::vector<std::vector<double>> transition_matrix = {{0.7, 0.3}, {0.4, 0.6}};
    std::vector<std::vector<double>> emission_matrix = {{0.9, 0.1}, {0.2, 0.8}};

    std::vector<int> observations = {0, 1, 0};
    auto [log_ll_fb, smoothed] = forward_backward(observations, initial_state, transition_matrix, emission_matrix);
    double ll_fb = std::exp(log_ll_fb);

    // Brute force verification for [0,1,0]
    double total = 0.0;
    for (int s0 = 0; s0 < 2; ++s0) {
        for (int s1 = 0; s1 < 2; ++s1) {
            for (int s2 = 0; s2 < 2; ++s2) {
                double prob = initial_state[s0] * emission_matrix[s0][0];
                prob *= transition_matrix[s0][s1] * emission_matrix[s1][1];
                prob *= transition_matrix[s1][s2] * emission_matrix[s2][0];
                total += prob;
            }
        }
    }

    assert(std::abs(ll_fb - total) < 1e-9);

    for (const auto& row : smoothed) {
        double sum_val = 0.0;
        for (double v : row) sum_val += v;
        assert(std::abs(sum_val - 1.0) < 1e-9);
    }

    for (const auto& row : smoothed) {
        for (double v : row) assert(v >= 0.0 && v <= 1.0);
    }

    std::vector<int> obs_strong = {0, 0, 0};
    auto [_, smoothed_strong] = forward_backward(obs_strong, initial_state, transition_matrix, emission_matrix);
    assert(smoothed_strong[0][0] > 0.5);

    std::vector<int> obs_weak = {1, 1, 1};
    auto [__, smoothed_weak] = forward_backward(obs_weak, initial_state, transition_matrix, emission_matrix);
    assert(smoothed_weak[0][1] > 0.5);

    std::cout << "hmm_forward_backward.cpp PASS" << std::endl;
    return 0;
}
