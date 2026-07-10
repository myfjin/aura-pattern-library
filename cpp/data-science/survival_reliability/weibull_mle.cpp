// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

using namespace std;

pair<double, double> weibull_mle(const vector<double>& times, int max_iter = 100, double tol = 1e-10) {
    int n = times.size();
    vector<double> ln_t(n);
    for (int i = 0; i < n; ++i) ln_t[i] = log(times[i]);
    double mean_ln = accumulate(ln_t.begin(), ln_t.end(), 0.0) / n;

    double k = 1.0;
    for (int iter = 0; iter < max_iter; ++iter) {
        vector<double> tk(n);
        for (int i = 0; i < n; ++i) tk[i] = pow(times[i], k);
        double A = accumulate(tk.begin(), tk.end(), 0.0);
        double B = 0.0, C = 0.0;
        for (int i = 0; i < n; ++i) {
            B += tk[i] * ln_t[i];
            C += tk[i] * ln_t[i] * ln_t[i];
        }
        double g = 1.0 / k + mean_ln - B / A;
        double g_prime = -1.0 / (k * k) - (C * A - B * B) / (A * A);
        if (abs(g_prime) < 1e-14) break;
        double k_new = k - g / g_prime;
        if (k_new <= 0.0) k_new = k / 2.0;
        if (abs(k_new - k) < tol) { k = k_new; break; }
        k = k_new;
    }

    double sum_tk = 0.0;
    for (double t : times) sum_tk += pow(t, k);
    double lam = pow(sum_tk / n, 1.0 / k);
    return {k, lam};
}

int main() {
    mt19937 rng(42);
    uniform_real_distribution<double> u(0.0, 1.0);
    double k_true = 2.0, lam_true = 5.0;
    vector<double> times;
    for (int i = 0; i < 80; ++i) {
        times.push_back(lam_true * pow(-log(u(rng)), 1.0 / k_true));
    }

    auto [k_est, lam_est] = weibull_mle(times);
    assert(abs(k_est - k_true) < 0.3);
    assert(abs(lam_est - lam_true) < 0.5);

    vector<double> ln_t;
    for (double t : times) ln_t.push_back(log(t));
    vector<double> tk;
    for (double t : times) tk.push_back(pow(t, k_est));
    double A = accumulate(tk.begin(), tk.end(), 0.0);
    double B = 0.0;
    for (size_t i = 0; i < tk.size(); ++i) B += tk[i] * ln_t[i];
    double score_k = 1.0 / k_est + accumulate(ln_t.begin(), ln_t.end(), 0.0) / times.size() - B / A;
    assert(abs(score_k) < 1e-6);

    cout << "weibull_mle PASS\n";
    return 0;
}
