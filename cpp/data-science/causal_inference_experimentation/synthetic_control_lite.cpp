// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Lightweight synthetic control: learns nonnegative, sum-to-one weights over
control units by projected gradient descent so their weighted average matches
the treated unit's pre-treatment trajectory; the post-period gap estimates the
effect. Use for single-unit causal inference with a donor pool. Oracle: on a
shared linear trend with a +5 post shock the estimated effect is within 2.0 of
5.0, and the fitted weights are all nonnegative and sum to 1.
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <random>
#include <cassert>

std::vector<double> fit_weights(const std::vector<double>& pre_treated,
                                   const std::vector<std::vector<double>>& pre_controls) {
    size_t n_controls = pre_controls.size();
    size_t n_periods = pre_treated.size();
    std::vector<double> weights(n_controls, 1.0 / static_cast<double>(n_controls));

    for (int iter = 0; iter < 100; ++iter) {
        std::vector<double> synthetic(n_periods, 0.0);
        for (size_t t = 0; t < n_periods; ++t) {
            for (size_t j = 0; j < n_controls; ++j) {
                synthetic[t] += weights[j] * pre_controls[j][t];
            }
        }

        std::vector<double> grads(n_controls, 0.0);
        for (size_t j = 0; j < n_controls; ++j) {
            for (size_t t = 0; t < n_periods; ++t) {
                grads[j] += 2.0 * (synthetic[t] - pre_treated[t]) * pre_controls[j][t];
            }
        }

        double step_size = 0.01;
        for (size_t j = 0; j < n_controls; ++j) weights[j] -= step_size * grads[j];

        double total = 0.0;
        for (double w : weights) total += std::max(0.0, w);
        if (total > 0.0) {
            for (double& w : weights) w = std::max(0.0, w) / total;
        }
    }

    return weights;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> noise(0.0, 1.0);

    size_t n_periods_pre = 10;
    size_t n_controls = 5;

    std::vector<double> trend(n_periods_pre);
    for (size_t t = 0; t < n_periods_pre; ++t) trend[t] = t * 2.0;

    std::vector<double> pre_treated(n_periods_pre);
    for (size_t t = 0; t < n_periods_pre; ++t) pre_treated[t] = trend[t] + noise(rng);

    std::vector<std::vector<double>> pre_controls(n_controls, std::vector<double>(n_periods_pre));
    for (size_t j = 0; j < n_controls; ++j) {
        for (size_t t = 0; t < n_periods_pre; ++t) {
            pre_controls[j][t] = trend[t] + noise(rng);
        }
    }

    auto weights = fit_weights(pre_treated, pre_controls);

    size_t n_periods_post = 10;
    double treatment_shock = 5.0;

    std::vector<double> post_treated(n_periods_post);
    double base = trend[n_periods_pre - 1];
    for (size_t t = 0; t < n_periods_post; ++t) {
        post_treated[t] = base + (n_periods_pre + t) * 2.0 + treatment_shock + noise(rng);
    }

    std::vector<std::vector<double>> post_controls(n_controls, std::vector<double>(n_periods_post));
    for (size_t j = 0; j < n_controls; ++j) {
        for (size_t t = 0; t < n_periods_post; ++t) {
            post_controls[j][t] = base + (n_periods_pre + t) * 2.0 + noise(rng);
        }
    }

    std::vector<double> synthetic_post(n_periods_post, 0.0);
    for (size_t t = 0; t < n_periods_post; ++t) {
        for (size_t j = 0; j < n_controls; ++j) {
            synthetic_post[t] += weights[j] * post_controls[j][t];
        }
    }

    double gap_sum = 0.0;
    for (size_t t = 0; t < n_periods_post; ++t) {
        gap_sum += post_treated[t] - synthetic_post[t];
    }
    double sc_effect = gap_sum / static_cast<double>(n_periods_post);
    double bias = std::abs(sc_effect - treatment_shock);

    assert(bias < 2.0);
    assert(std::abs(std::accumulate(weights.begin(), weights.end(), 0.0) - 1.0) < 0.01);
    for (double w : weights) assert(w >= 0.0);

    std::cout << "synthetic_control_lite: PASS" << std::endl;
    return 0;
}
