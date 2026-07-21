// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Accelerated failure time (AFT): log-linear regression on survival times.
 *
 * Model: log(T) = μ + β·x + σ·ε where T is survival time, x is covariate.
 * Core claim: linear relationship recovered; AFT coefficient close to truth.
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <numeric>
#include <cassert>
#include <iomanip>
#include <tuple>

using namespace std;

// Fit AFT model: log(T) = μ + β·x + ε
// Returns: (mu, beta, sigma)
tuple<double, double, double> aft_fit(const vector<double>& log_times, const vector<double>& x) {
    int n = log_times.size();
    double mean_x = accumulate(x.begin(), x.end(), 0.0) / n;
    double mean_log_t = accumulate(log_times.begin(), log_times.end(), 0.0) / n;
    
    double cov_x_logt = 0.0, var_x = 0.0;
    for (int i = 0; i < n; i++) {
        cov_x_logt += (x[i] - mean_x) * (log_times[i] - mean_log_t);
        var_x += (x[i] - mean_x) * (x[i] - mean_x);
    }
    cov_x_logt /= n;
    var_x /= n;
    
    if (var_x < 1e-14) {
        return {mean_log_t, 0.0, 1.0};
    }
    
    double beta = cov_x_logt / var_x;
    double mu = mean_log_t - beta * mean_x;
    
    // Compute sigma (residual std)
    double ss_res = 0.0;
    for (int i = 0; i < n; i++) {
        double residual = log_times[i] - (mu + beta * x[i]);
        ss_res += residual * residual;
    }
    double sigma = sqrt(ss_res / n);
    
    return {mu, beta, sigma};
}

int main() {
    // Seed the RNG with same seed as Python (42)
    mt19937 gen(42);
    normal_distribution<double> norm(0.0, 1.0);
    
    // Planted: log(T) = 2.0 + 0.5·x + N(0, 0.3)
    double mu_true = 2.0, beta_true = 0.5, sigma_true = 0.3;
    
    vector<double> x, log_times;
    for (int i = 0; i < 50; i++) {
        double xi = norm(gen);
        x.push_back(xi);
        log_times.push_back(mu_true + beta_true * xi + sigma_true * norm(gen));
    }
    
    auto [mu_est, beta_est, sigma_est] = aft_fit(log_times, x);
    
    cout << fixed << setprecision(4);
    cout << "Fitted: μ=" << mu_est << ", β=" << beta_est << ", σ=" << sigma_est << endl;
    
    // Assertions matching Python oracle
    assert(abs(mu_est - mu_true) < 0.3);
    assert(abs(beta_est - beta_true) < 0.3);
    assert(abs(sigma_est - sigma_true) < 0.2);
    
    cout << "PASS" << endl;
    
    return 0;
}
