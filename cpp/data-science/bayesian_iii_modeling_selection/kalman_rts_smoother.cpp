// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Kalman filter + Rauch-Tung-Striebel (RTS) smoother.
 *
 * Oracle asserts:
 *   mean_mse_smooth < mean_mse_filt
 *   mean_mse_smooth < 0.9 * mean_mse_filt
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <random>

std::pair<std::vector<double>, std::vector<double>> kalman_filter(
    const std::vector<double>& y, double q, double r) {
    std::vector<double> x_hat;
    std::vector<double> p;
    double x = 0.0, pp = 1.0;
    for (double yi : y) {
        double x_pred = x;
        double p_pred = pp + q;
        double k = p_pred / (p_pred + r);
        x = x_pred + k * (yi - x_pred);
        pp = (1.0 - k) * p_pred;
        x_hat.push_back(x);
        p.push_back(pp);
    }
    return {x_hat, p};
}

std::vector<double> rts_smoother(const std::vector<double>& x_filt,
                                 const std::vector<double>& p_filt,
                                 double q) {
    std::vector<double> x_s = x_filt;
    for (int i = static_cast<int>(x_s.size()) - 2; i >= 0; --i) {
        double p_pred_next = p_filt[i] + q;
        double c = p_filt[i] / p_pred_next;
        x_s[i] = x_filt[i] + c * (x_s[i + 1] - x_filt[i]);
    }
    return x_s;
}

int main() {
    double q = 0.5, r = 1.0;
    int n = 40, reps = 200;
    double sum_mse_filt = 0.0, sum_mse_smooth = 0.0;

    for (int rep = 0; rep < reps; ++rep) {
        std::mt19937_64 rng(static_cast<uint64_t>(rep));
        std::normal_distribution<double> walk_noise(0.0, std::sqrt(q));
        std::normal_distribution<double> meas_noise(0.0, std::sqrt(r));

        std::vector<double> x_true(n, 0.0);
        for (int i = 1; i < n; ++i) x_true[i] = x_true[i - 1] + walk_noise(rng);
        std::vector<double> y(n);
        for (int i = 0; i < n; ++i) y[i] = x_true[i] + meas_noise(rng);

        auto [x_filt, p_filt] = kalman_filter(y, q, r);
        auto x_smooth = rts_smoother(x_filt, p_filt, q);

        double mf = 0.0, ms = 0.0;
        for (int i = 0; i < n; ++i) {
            mf += std::pow(x_filt[i] - x_true[i], 2);
            ms += std::pow(x_smooth[i] - x_true[i], 2);
        }
        sum_mse_filt += mf / n;
        sum_mse_smooth += ms / n;
    }

    double mean_mse_filt = sum_mse_filt / reps;
    double mean_mse_smooth = sum_mse_smooth / reps;

    assert(mean_mse_smooth < mean_mse_filt);
    assert(mean_mse_smooth < 0.9 * mean_mse_filt);

    std::cout << "kalman_rts_smoother.cpp PASS: filt=" << mean_mse_filt
              << " smooth=" << mean_mse_smooth << std::endl;
    return 0;
}
