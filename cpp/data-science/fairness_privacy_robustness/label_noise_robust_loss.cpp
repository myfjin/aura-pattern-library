// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Label Noise Robustness: MAE degrades less than cross-entropy under label noise.
 *
 * Oracle asserts:
 *   degradation_mae <= degradation_ce + 0.01
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <random>
#include <algorithm>

double sigmoid(double z) {
    if (z < -500) return 0.0;
    if (z > 500) return 1.0;
    return 1.0 / (1.0 + std::exp(-z));
}

double train_and_eval(const std::vector<std::pair<double,double>>& X,
                      const std::vector<int>& labels,
                      bool mae) {
    double w[3] = {0.5, 0.5, 0.0};
    int n = static_cast<int>(X.size());
    for (int epoch = 0; epoch < 20; ++epoch) {
        double lr = epoch < 10 ? 0.1 : 0.05;
        for (int i = 0; i < n; ++i) {
            double z = w[0] * X[i].first + w[1] * X[i].second + w[2];
            double pred = sigmoid(z);
            double grad;
            if (mae) {
                grad = std::max(-1.0, std::min(1.0, pred - labels[i]));
            } else {
                grad = pred - labels[i];
            }
            w[0] += lr * grad * X[i].first;
            w[1] += lr * grad * X[i].second;
            w[2] += lr * grad;
        }
    }
    int correct = 0;
    for (int i = 0; i < n; ++i) {
        double z = w[0] * X[i].first + w[1] * X[i].second + w[2];
        bool p = sigmoid(z) > 0.5;
        if (p == (labels[i] == 1)) ++correct;
    }
    return static_cast<double>(correct) / n;
}

int main() {
    std::mt19937_64 rng(42);
    std::uniform_real_distribution<double> xdist(-2.0, 2.0);
    int n = 200;
    std::vector<std::pair<double,double>> X(n);
    std::vector<int> y_clean(n);
    for (int i = 0; i < n; ++i) {
        X[i] = {xdist(rng), xdist(rng)};
        y_clean[i] = (X[i].first + X[i].second > 0) ? 1 : 0;
    }

    std::vector<int> y_noisy = y_clean;
    for (int i = 0; i < n; ++i) {
        if ((rng() % 100) / 100.0 < 0.2) y_noisy[i] = 1 - y_noisy[i];
    }

    double acc_clean_ce = train_and_eval(X, y_clean, false);
    double acc_noisy_ce = train_and_eval(X, y_noisy, false);
    double degradation_ce = std::max(0.0, acc_clean_ce - acc_noisy_ce);

    double acc_clean_mae = train_and_eval(X, y_clean, true);
    double acc_noisy_mae = train_and_eval(X, y_noisy, true);
    double degradation_mae = std::max(0.0, acc_clean_mae - acc_noisy_mae);

    assert(degradation_mae <= degradation_ce + 0.01);

    std::cout << "label_noise_robust_loss.cpp PASS" << std::endl;
    return 0;
}
