// RTS Kalman smoother: forward-backward pass for optimal smoothing.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <cassert>

std::pair<std::vector<double>, std::vector<double>> kfForward(
    const std::vector<double>& observations, double process_var = 0.1, double meas_var = 1.0) {
    size_t n = observations.size();
    std::vector<double> x_filt(n), P_filt(n);
    x_filt[0] = observations[0];
    P_filt[0] = meas_var;
    for (size_t i = 1; i < n; ++i) {
        double x_pred = x_filt[i - 1];
        double P_pred = P_filt[i - 1] + process_var;
        double K = P_pred / (P_pred + meas_var);
        x_filt[i] = x_pred + K * (observations[i] - x_pred);
        P_filt[i] = (1.0 - K) * P_pred;
    }
    return {x_filt, P_filt};
}

std::pair<std::vector<double>, std::vector<double>> rtsBackwardPass(
    const std::vector<double>& x_filt, const std::vector<double>& P_filt,
    double process_var = 0.1) {
    size_t n = x_filt.size();
    std::vector<double> x_smooth(n), P_smooth(n);
    x_smooth.back() = x_filt.back();
    P_smooth.back() = P_filt.back();
    for (int i = static_cast<int>(n) - 2; i >= 0; --i) {
        double P_pred = P_filt[i] + process_var;
        double C = P_filt[i] / P_pred;
        x_smooth[i] = x_filt[i] + C * (x_smooth[i + 1] - x_filt[i]);
        P_smooth[i] = P_filt[i] + C * C * (P_smooth[i + 1] - P_pred);
    }
    return {x_smooth, P_smooth};
}

double rmse(const std::vector<double>& est, const std::vector<double>& truth) {
    double sum = 0.0;
    for (size_t i = 0; i < est.size(); ++i)
        sum += (est[i] - truth[i]) * (est[i] - truth[i]);
    return std::sqrt(sum / est.size());
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> walk_noise(0.0, 0.1);
    std::normal_distribution<double> meas_noise(0.0, 1.0);

    std::vector<double> true_traj = {0.0};
    for (int i = 0; i < 30; ++i)
        true_traj.push_back(true_traj.back() + walk_noise(gen));

    std::vector<double> observations;
    for (double x : true_traj)
        observations.push_back(x + meas_noise(gen));

    auto [x_filt, P_filt] = kfForward(observations, 0.1, 1.0);
    auto [x_smooth, P_smooth] = rtsBackwardPass(x_filt, P_filt, 0.1);

    assert(x_smooth.size() == observations.size());
    assert(P_smooth.size() == observations.size());

    double rmse_raw = rmse(observations, true_traj);
    double rmse_filt = rmse(x_filt, true_traj);
    double rmse_smooth = rmse(x_smooth, true_traj);

    assert(rmse_smooth < rmse_filt);
    assert(rmse_filt < rmse_raw);

    for (double p : P_filt) assert(p > 0.0);
    for (double p : P_smooth) assert(p > 0.0);
    for (size_t i = 0; i < P_smooth.size(); ++i)
        assert(P_smooth[i] <= P_filt[i] * 1.01);

    double min_val = observations[0], max_val = observations[0];
    for (double v : x_filt) { min_val = std::min(min_val, v); max_val = std::max(max_val, v); }
    for (double v : x_smooth) { min_val = std::min(min_val, v); max_val = std::max(max_val, v); }
    double range_val = max_val - min_val;
    assert(range_val > 0.0 && range_val < 20.0);

    std::cout << "RTS_KALMAN_SMOOTHER PASS: raw=" << rmse_raw
              << " filt=" << rmse_filt << " smooth=" << rmse_smooth << "\n";
    return 0;
}
