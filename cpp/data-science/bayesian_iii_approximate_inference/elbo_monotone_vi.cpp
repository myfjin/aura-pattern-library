// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/* ELBO monotonicity in coordinate-ascent variational inference. */
#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>

static const std::vector<double> DATA = {
    1.8559096704220717,
    1.8270963996684806,
    1.8886841384323376,
    2.701983725098863,
    1.872411716217113,
    0.5026465856590425,
    2.332318344067715,
    1.7326625215028317,
    1.783041315854805,
    2.115884786700855,
    2.232297736906721,
    3.163558686599143,
    2.656636506798669,
    2.1105071774438318,
    1.2616783976551793,
    0.9853376325122829,
    2.246342195211202,
    3.311080827204048,
    2.041656863903384,
    1.8936767062292157,
    2.5317762204008694,
    0.546454701991322,
    1.6877226828554401,
    2.4903625325935246,
    2.873404385379447,
    1.7593703273448646,
    2.3765998586879102,
    2.2482134493284143,
    2.782326808703642,
    0.8867777857518273
};

double true_log_evidence(const std::vector<double>& data, double mu0=0.0, double s0=10.0) {
    int n = static_cast<int>(data.size());
    double ssum = 0.0, s_centered = 0.0;
    for (double y : data) { ssum += y; s_centered += (y - mu0) * (y - mu0); }
    double quad = s_centered - s0 / (1.0 + s0 * n) * (ssum - n * mu0) * (ssum - n * mu0);
    return -0.5 * (n * std::log(2.0 * M_PI) + std::log(1.0 + s0 * n) + quad);
}

double elbo(const std::vector<double>& data, double m, double s, double mu0=0.0, double s0=10.0) {
    double ll = 0.0;
    for (double y : data) ll += -0.5 * std::log(2.0 * M_PI) - 0.5 * ((y - m) * (y - m) + s);
    double lp = -0.5 * std::log(2.0 * M_PI * s0) - 0.5 * ((m - mu0) * (m - mu0) + s) / s0;
    double entropy = 0.5 * std::log(2.0 * M_PI * M_E * s);
    return ll + lp + entropy;
}

std::vector<double> cavi_elbo_sequence(const std::vector<double>& data, double mu0=0.0, double s0=10.0, int cycles=15) {
    int n = static_cast<int>(data.size());
    double sum = 0.0;
    for (double y : data) sum += y;
    double m = -5.0, s = 5.0;
    std::vector<double> seq;
    seq.push_back(elbo(data, m, s, mu0, s0));
    for (int i = 0; i < cycles; ++i) {
        m = (sum + mu0 / s0) / (n + 1.0 / s0);
        seq.push_back(elbo(data, m, s, mu0, s0));
        s = 1.0 / (n + 1.0 / s0);
        seq.push_back(elbo(data, m, s, mu0, s0));
    }
    return seq;
}

int main() {
    auto seq = cavi_elbo_sequence(DATA);
    double log_ev = true_log_evidence(DATA);
    for (size_t i = 0; i + 1 < seq.size(); ++i) assert(seq[i + 1] >= seq[i] - 1e-9);
    for (double e : seq) assert(e <= log_ev + 1e-6);
    assert(seq.back() - seq.front() > 50.0);
    assert(std::abs(seq.back() - log_ev) < 0.1);
    std::cout << "elbo_monotone_vi PASS" << std::endl;
    return 0;
}
