// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * KL divergence, cross-entropy, and Jensen-Shannon divergence between discrete distributions.
 *
 * Oracle asserts:
 *   abs(kl_self) < 1e-9
 *   abs(hpq - (hp + dpq)) < 1e-9
 *   abs(js_pq - js_qp) < 1e-9
 *   0 <= js_pr <= 1
 *   abs(computed_kl - expected_kl) < 1e-9
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>

double kl_divergence(const std::vector<double>& p, const std::vector<double>& q) {
    double r = 0.0;
    for (size_t i = 0; i < p.size(); ++i) {
        if (p[i] > 1e-10) r += p[i] * std::log(p[i] / q[i]);
    }
    return r;
}

double cross_entropy(const std::vector<double>& p, const std::vector<double>& q) {
    double r = 0.0;
    for (size_t i = 0; i < p.size(); ++i) {
        if (p[i] > 1e-10) r -= p[i] * std::log(q[i]);
    }
    return r;
}

double shannon_entropy(const std::vector<double>& p) {
    double r = 0.0;
    for (double pi : p) {
        if (pi > 1e-10) r -= pi * std::log(pi);
    }
    return r;
}

double jensen_shannon_distance(const std::vector<double>& p,
                             const std::vector<double>& q) {
    std::vector<double> m(p.size());
    for (size_t i = 0; i < p.size(); ++i) m[i] = (p[i] + q[i]) / 2.0;
    double js_div = 0.5 * kl_divergence(p, m) + 0.5 * kl_divergence(q, m);
    return std::sqrt(js_div);
}

int main() {
    std::vector<double> p = {0.5, 0.3, 0.2};
    double kl_self = kl_divergence(p, p);
    assert(std::abs(kl_self) < 1e-9);

    std::vector<double> q = {0.4, 0.4, 0.2};
    double hp = shannon_entropy(p);
    double hpq = cross_entropy(p, q);
    double dpq = kl_divergence(p, q);
    assert(std::abs(hpq - (hp + dpq)) < 1e-9);

    double js_pq = jensen_shannon_distance(p, q);
    double js_qp = jensen_shannon_distance(q, p);
    assert(std::abs(js_pq - js_qp) < 1e-9);

    std::vector<double> r = {0.2, 0.5, 0.3};
    double js_pr = jensen_shannon_distance(p, r);
    assert(js_pr >= 0.0 && js_pr <= 1.0);

    std::vector<double> p_simple = {0.5, 0.5};
    std::vector<double> q_simple = {0.7, 0.3};
    double expected_kl = 0.5 * std::log(0.5 / 0.7) + 0.5 * std::log(0.5 / 0.3);
    double computed_kl = kl_divergence(p_simple, q_simple);
    assert(std::abs(computed_kl - expected_kl) < 1e-9);

    std::cout << "kl_divergence_cross_entropy.cpp PASS" << std::endl;
    return 0;
}
