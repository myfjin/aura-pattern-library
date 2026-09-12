// perceptron.cpp
// Perceptron learning algorithm (from scratch).

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <random>
#include <cassert>

using std::vector;

static void perceptron_fit(const vector<vector<double>>& X,
                           const vector<int>& y,
                           double lr,
                           int max_iter,
                           vector<double>& weights,
                           double& bias) {
    size_t n = X.size(), d = X[0].size();
    weights.assign(d, 0.0);
    bias = 0.0;

    for (int it = 0; it < max_iter; ++it) {
        size_t errors = 0;
        for (size_t i = 0; i < n; ++i) {
            double z = bias;
            for (size_t j = 0; j < d; ++j) z += weights[j] * X[i][j];
            int pred = z >= 0 ? 1 : -1;
            int label = (y[i] == 0 || y[i] == 1) ? 2 * y[i] - 1 : y[i];
            if (pred != label) {
                int err = label - pred;
                for (size_t j = 0; j < d; ++j)
                    weights[j] += lr * err * X[i][j] / 2.0;
                bias += lr * err / 2.0;
                ++errors;
            }
        }
        if (errors == 0) break;
    }
}

static vector<int> perceptron_predict(const vector<vector<double>>& X,
                                     const vector<double>& weights,
                                     double bias) {
    vector<int> preds;
    for (const auto& row : X) {
        double z = bias;
        for (size_t j = 0; j < weights.size(); ++j) z += weights[j] * row[j];
        preds.push_back(z >= 0 ? 1 : 0);
    }
    return preds;
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uni(-3.0, 3.0);
    std::uniform_real_distribution<double> gap(0.5, 2.5);

    size_t n_samples = 40;
    vector<vector<double>> X;
    vector<int> y;

    for (size_t i = 0; i < n_samples / 2; ++i) {
        double x1 = uni(rng);
        double x2 = x1 - gap(rng);
        X.push_back({x1, x2});
        y.push_back(0);
    }
    for (size_t i = 0; i < n_samples / 2; ++i) {
        double x1 = uni(rng);
        double x2 = x1 + gap(rng);
        X.push_back({x1, x2});
        y.push_back(1);
    }

    vector<double> weights;
    double bias;
    perceptron_fit(X, y, 1.0, 50, weights, bias);
    auto preds = perceptron_predict(X, weights, bias);

    size_t correct = 0;
    for (size_t i = 0; i < n_samples; ++i)
        if (preds[i] == y[i]) ++correct;
    double accuracy = static_cast<double>(correct) / n_samples;

    assert(accuracy >= 0.9);

    std::cout << "PERCEPTRON PASS: accuracy = " << accuracy << ", weights = ";
    for (double w : weights) std::cout << w << " ";
    std::cout << "\n";
    return 0;
}
