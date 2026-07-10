// Network interference demo: spillover through a ring graph biases naive ATE.
// Fixed deterministic pseudo-random treatment assignment.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <vector>

static uint32_t rng_state = 42U;
int randint01() {
    rng_state = rng_state * 1103515245U + 12345U;
    return (rng_state >> 16) & 1U;
}

std::vector<double> simulate_spillover_network(int n,
                                               const std::vector<int>& treatment,
                                               double effect_direct,
                                               double effect_spillover) {
    std::vector<double> outcomes;
    outcomes.reserve(n);
    for (int i = 0; i < n; ++i) {
        double y = effect_direct * treatment[i];
        int left = (i - 1 + n) % n;
        int right = (i + 1) % n;
        y += effect_spillover * (treatment[left] + treatment[right]) / 2.0;
        y += (i % 3) * 0.1;
        outcomes.push_back(y);
    }
    return outcomes;
}

double naive_ate(const std::vector<int>& treatment,
                 const std::vector<double>& outcomes) {
    double sum_t1 = 0.0, sum_t0 = 0.0;
    int cnt_t1 = 0, cnt_t0 = 0;
    for (size_t i = 0; i < treatment.size(); ++i) {
        if (treatment[i] == 1) {
            sum_t1 += outcomes[i];
            ++cnt_t1;
        } else {
            sum_t0 += outcomes[i];
            ++cnt_t0;
        }
    }
    if (cnt_t1 == 0 || cnt_t0 == 0) return 0.0;
    return sum_t1 / cnt_t1 - sum_t0 / cnt_t0;
}

int main() {
    const int n = 100;
    const double true_direct_effect = 2.0;
    const double true_spillover_effect = 0.8;

    rng_state = 42U;
    std::vector<int> treatment_high_spill;
    for (int i = 0; i < n; ++i) treatment_high_spill.push_back(randint01());

    auto outcomes_high = simulate_spillover_network(n, treatment_high_spill,
                                                    true_direct_effect,
                                                    true_spillover_effect);
    double ate_high = naive_ate(treatment_high_spill, outcomes_high);

    std::vector<int> treatment_low_spill(n, 0);
    for (int i = 0; i < 10; ++i) treatment_low_spill[i] = 1;
    auto outcomes_low = simulate_spillover_network(n, treatment_low_spill,
                                                   true_direct_effect,
                                                   true_spillover_effect);
    double ate_low = naive_ate(treatment_low_spill, outcomes_low);

    assert(ate_high < ate_low);
    assert(std::fabs(ate_high - ate_low) > 0.2);

    std::printf("network_interference_demo.cpp: PASS (high=%.4f low=%.4f)\n",
                ate_high, ate_low);
    return 0;
}
