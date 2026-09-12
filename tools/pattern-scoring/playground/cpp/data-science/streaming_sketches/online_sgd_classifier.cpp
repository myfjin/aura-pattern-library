// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Online (streaming) logistic-regression classifier trained by per-sample SGD: for
each incoming (x, label) it updates weights and bias once using the logistic loss
gradient, with a clamped sigmoid to avoid overflow. Use for incremental binary
classification when data arrives as a stream. Includes a multi-epoch batch variant
for comparison.
Guarantee: after a single pass over 200 two-cluster samples, online accuracy
exceeds 0.7 and its loss stays within 3x of the 5-epoch batch loss.
*/
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <random>
#include <utility>
#include <vector>

inline double logistic(double z) {
    if (z > 100.0) z = 100.0;
    if (z < -100.0) z = -100.0;
    return 1.0 / (1.0 + std::exp(-z));
}

std::pair<std::vector<double>, double> online_sgd_classifier(
    const std::vector<std::pair<std::vector<double>, double>>& stream,
    double learning_rate = 0.01,
    int epochs = 1) {
    std::size_t num_features = stream[0].first.size();
    std::vector<double> weights(num_features, 0.0);
    double bias = 0.0;

    for (int epoch = 0; epoch < epochs; ++epoch) {
        for (const auto& sample : stream) {
            const auto& x = sample.first;
            double y = sample.second;
            double z = bias;
            for (std::size_t i = 0; i < num_features; ++i) {
                z += weights[i] * x[i];
            }
            double pred = logistic(z);
            double error = pred - y;
            for (std::size_t i = 0; i < num_features; ++i) {
                weights[i] -= learning_rate * error * x[i];
            }
            bias -= learning_rate * error;
        }
    }

    double total_loss = 0.0;
    for (const auto& sample : stream) {
        const auto& x = sample.first;
        double y = sample.second;
        double z = bias;
        for (std::size_t i = 0; i < num_features; ++i) {
            z += weights[i] * x[i];
        }
        double pred = logistic(z);
        total_loss += -y * std::log(pred + 1e-7) - (1.0 - y) * std::log(1.0 - pred + 1e-7);
    }
    return {weights, total_loss / static_cast<double>(stream.size())};
}

std::pair<std::vector<double>, double> batch_sgd_classifier(
    const std::vector<std::vector<double>>& X,
    const std::vector<double>& y,
    double learning_rate = 0.01,
    int epochs = 10) {
    std::size_t num_features = X[0].size();
    std::vector<double> weights(num_features, 0.0);
    double bias = 0.0;

    for (int epoch = 0; epoch < epochs; ++epoch) {
        for (std::size_t idx = 0; idx < X.size(); ++idx) {
            const auto& x = X[idx];
            double label = y[idx];
            double z = bias;
            for (std::size_t i = 0; i < num_features; ++i) {
                z += weights[i] * x[i];
            }
            double pred = logistic(z);
            double error = pred - label;
            for (std::size_t i = 0; i < num_features; ++i) {
                weights[i] -= learning_rate * error * x[i];
            }
            bias -= learning_rate * error;
        }
    }

    double total_loss = 0.0;
    for (std::size_t idx = 0; idx < X.size(); ++idx) {
        const auto& x = X[idx];
        double label = y[idx];
        double z = bias;
        for (std::size_t i = 0; i < num_features; ++i) {
            z += weights[i] * x[i];
        }
        double pred = logistic(z);
        total_loss += -label * std::log(pred + 1e-7) - (1.0 - label) * std::log(1.0 - pred + 1e-7);
    }
    return {weights, total_loss / static_cast<double>(X.size())};
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> dist(0.0, 0.5);

    std::vector<std::pair<std::vector<double>, double>> stream;
    for (int i = 0; i < 200; ++i) {
        int label = rng() % 2;
        std::vector<double> x;
        if (label == 0) {
            x = {dist(rng) - 1.0, dist(rng) - 1.0};
        } else {
            x = {dist(rng) + 1.0, dist(rng) + 1.0};
        }
        stream.emplace_back(x, static_cast<double>(label));
    }

    std::vector<std::vector<double>> X_batch;
    std::vector<double> y_batch;
    for (const auto& sample : stream) {
        X_batch.push_back(sample.first);
        y_batch.push_back(sample.second);
    }

    auto online_result = online_sgd_classifier(stream, 0.05, 1);
    auto batch_result = batch_sgd_classifier(X_batch, y_batch, 0.05, 5);

    std::cout << std::fixed << std::setprecision(4);
    std::cout << "Online SGD loss (1 epoch): " << online_result.second << "\n";
    std::cout << "Batch SGD loss (5 epochs): " << batch_result.second << "\n";

    int online_correct = 0;
    int batch_correct = 0;
    for (const auto& sample : stream) {
        const auto& x = sample.first;
        double y = sample.second;
        double online_z = 0.0;
        for (std::size_t i = 0; i < x.size(); ++i) {
            online_z += online_result.first[i] * x[i];
        }
        double batch_z = 0.0;
        for (std::size_t i = 0; i < x.size(); ++i) {
            batch_z += batch_result.first[i] * x[i];
        }
        int online_pred = logistic(online_z) > 0.5 ? 1 : 0;
        int batch_pred = logistic(batch_z) > 0.5 ? 1 : 0;
        if (online_pred == static_cast<int>(y)) ++online_correct;
        if (batch_pred == static_cast<int>(y)) ++batch_correct;
    }

    double online_acc = static_cast<double>(online_correct) / static_cast<double>(stream.size());
    double batch_acc = static_cast<double>(batch_correct) / static_cast<double>(stream.size());
    std::cout << "Online accuracy: " << online_acc << "\n";
    std::cout << "Batch accuracy: " << batch_acc << "\n";

    assert(online_acc > 0.7);
    assert(online_result.second < batch_result.second * 3.0);

    std::cout << "Online SGD Classifier: PASS\n";
    return 0;
}
