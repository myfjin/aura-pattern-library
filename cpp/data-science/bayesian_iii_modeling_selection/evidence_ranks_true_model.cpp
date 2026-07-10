// Model evidence (via BIC) ranks the true generative model above the alternative.
// C++17 self-contained port with full parity to Python oracle.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cmath>
#include <vector>
#include <iostream>
#include <cassert>

// Python oracle generated data (seed 42, Gaussian N(3,1), n=40)
static const double DATA[40] = {2.8559096704220717, 2.8270963996684806, 2.8886841384323376, 3.701983725098863, 2.8724117162171128, 1.5026465856590425, 3.332318344067715, 2.732662521502832, 2.783041315854805, 3.115884786700855, 3.232297736906721, 4.163558686599143, 3.656636506798669, 3.1105071774438318, 2.2616783976551793, 1.985337632512283, 3.246342195211202, 4.311080827204048, 3.041656863903384, 2.8936767062292157, 3.5317762204008694, 1.546454701991322, 2.68772268285544, 3.4903625325935246, 3.873404385379447, 2.7593703273448646, 3.3765998586879102, 3.2482134493284143, 3.782326808703642, 1.8867777857518273, 3.568250687585386, 1.4854796082748603, 0.38005457778114815, 2.3931092718004976, 2.0841899536540054, 3.8760122430564063, 3.6642658996128947, 1.7809252587043047, 3.8473614233480005, 1.9977971757576503};

double gaussian_bic(const std::vector<double>& data) {
    size_t n = data.size();
    double mu = 0.0;
    for (double d : data) mu += d;
    mu /= static_cast<double>(n);
    double var = 0.0;
    for (double d : data) { double x = d - mu; var += x*x; }
    var /= static_cast<double>(n);
    double log_lik = 0.0;
    for (double d : data) {
        log_lik += -0.5 * std::log(2.0 * M_PI * var) - 0.5 * (d - mu) * (d - mu) / var;
    }
    return -2.0 * log_lik + 2.0 * std::log(static_cast<double>(n));
}

double exponential_bic(const std::vector<double>& data) {
    std::vector<double> pos;
    for (double d : data) if (d > 0) pos.push_back(d);
    size_t n = pos.size();
    double sum = 0.0;
    for (double d : pos) sum += d;
    double rate = static_cast<double>(n) / sum;
    double log_lik = 0.0;
    for (double d : pos) log_lik += std::log(rate) - rate * d;
    return -2.0 * log_lik + 1.0 * std::log(static_cast<double>(n));
}

int main() {
    std::vector<double> data(DATA, DATA + 40);
    double bic_true = gaussian_bic(data);
    double bic_alt = exponential_bic(data);
    assert(bic_true < bic_alt);
    assert(bic_alt - bic_true > 10.0);
    std::cout << "PASS" << std::endl;
    return 0;
}
