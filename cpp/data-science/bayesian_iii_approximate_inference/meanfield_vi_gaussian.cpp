// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Mean-field variational inference for a Gaussian with unknown mean AND precision.
 *
 * Oracle asserts:
 *   abs(vi_mu - mu_true) < 0.4
 *   abs(vi_mu - sample_mean) < 0.05
 *   abs(vi_tau - 1/sample_var) < 0.3
 *   trajectory actually iterates
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <set>
#include <tuple>

std::tuple<double, double, std::vector<double>> meanfield_vi_normal_gamma(
    const std::vector<double>& data,
    double mu0 = 0.0, double lam0 = 0.01, double a0 = 0.01, double b0 = 0.01,
    int max_iter = 100) {

    int n = static_cast<int>(data.size());
    double s = 0.0;
    for (double x : data) s += x;
    double a_N = a0 + n / 2.0;
    double E_tau = 1.0;
    double mu_N = mu0;
    std::vector<double> traj;

    for (int i = 0; i < max_iter; ++i) {
        double lam_N = lam0 + n * E_tau;
        mu_N = (lam0 * mu0 + E_tau * s) / lam_N;
        double E_sq = 0.0;
        for (double x : data) E_sq += (x - mu_N) * (x - mu_N);
        E_sq += n / lam_N;
        double b_N = b0 + 0.5 * E_sq;
        E_tau = a_N / b_N;
        traj.push_back(mu_N);
    }
    return {mu_N, E_tau, traj};
}

int main() {
    std::vector<double> data = {
        1.8559096704220717, 1.8270963996684806, 1.8886841384323376, 2.701983725098863, 1.872411716217113,
        0.5026465856590425, 2.332318344067715, 1.7326625215028317, 1.783041315854805, 2.115884786700855,
        2.232297736906721, 3.163558686599143, 2.656636506798669, 2.1105071774438318, 1.2616783976551793,
        0.9853376325122829, 2.246342195211202, 3.311080827204048, 2.041656863903384, 1.8936767062292157,
        2.5317762204008694, 0.546454701991322, 1.6877226828554401, 2.4903625325935246, 2.873404385379447,
        1.7593703273448646, 2.3765998586879102, 2.2482134493284143, 2.782326808703642, 0.8867777857518273,
        2.568250687585386, 0.48547960827486025, -0.6199454222188518, 1.3931092718004974, 1.0841899536540054,
        2.8760122430564063, 2.6642658996128947, 0.7809252587043047, 2.8473614233480005, 0.9977971757576503,
        1.9137561536637158, 1.7061002220434678, 2.114419857460921, 2.818636311543767, 2.6384137907924434,
        2.3498851018692086, 2.6499480978062984, 2.4784920376501183, 1.3730145347804001, 1.2826289061834224
    };

    auto [vi_mu, vi_tau, traj] = meanfield_vi_normal_gamma(data);
    double n = data.size();
    double sample_mean = 0.0;
    for (double x : data) sample_mean += x;
    sample_mean /= n;
    double sample_var = 0.0;
    for (double x : data) sample_var += (x - sample_mean) * (x - sample_mean);
    sample_var /= n;

    assert(std::abs(vi_mu - 2.0) < 0.4);
    assert(std::abs(vi_mu - sample_mean) < 0.05);
    assert(std::abs(vi_tau - 1.0 / sample_var) < 0.3);

    std::set<double> unique;
    for (double t : traj) unique.insert(std::round(t * 1e6));
    assert(traj.front() != traj.back() && unique.size() > 1);

    std::cout << "meanfield_vi_gaussian.cpp PASS" << std::endl;
    return 0;
}
