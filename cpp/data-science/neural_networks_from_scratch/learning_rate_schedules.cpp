// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Learning rate schedules: constant vs step-decay vs cosine annealing.
 *
 * Oracle asserts:
 *   const_loss, step_loss, cosine_loss all < 0.1
 *   step_late_var < 1e-6
 *   cosine_late_var < 1e-6
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <random>
#include <functional>
#include <numeric>

class SimpleNet {
public:
    SimpleNet() {
        std::mt19937_64 rng(42);
        std::normal_distribution<double> nd(0.0, 0.5);
        for (int i = 0; i < 4; ++i) {
            w1[i][0] = nd(rng);
            w1[i][1] = nd(rng);
            b1[i] = 0.0;
        }
        for (int i = 0; i < 4; ++i) w2[i] = nd(rng);
        b2 = 0.0;
    }

    double sigmoid(double x) const {
        if (x < -500) return 0.0;
        if (x > 500) return 1.0;
        return 1.0 / (1.0 + std::exp(-x));
    }

    double sigmoid_derivative(double s) const { return s * (1.0 - s); }

    std::pair<double, std::vector<double>> forward(const std::vector<double>& x) {
        std::vector<double> h(4);
        for (int i = 0; i < 4; ++i) {
            double z = b1[i] + w1[i][0] * x[0] + w1[i][1] * x[1];
            h[i] = sigmoid(z);
        }
        double z2 = b2;
        for (int i = 0; i < 4; ++i) z2 += w2[i] * h[i];
        return {sigmoid(z2), h};
    }

    void backward(const std::vector<double>& x, double y_true, double y_pred,
                  const std::vector<double>& h, double lr) {
        double dy = y_pred - y_true;
        double dz2 = dy * sigmoid_derivative(y_pred);
        for (int i = 0; i < 4; ++i) w2[i] -= lr * dz2 * h[i];
        b2 -= lr * dz2;
        for (int i = 0; i < 4; ++i) {
            double dh = dz2 * w2[i] * sigmoid_derivative(h[i]);
            w1[i][0] -= lr * dh * x[0];
            w1[i][1] -= lr * dh * x[1];
            b1[i] -= lr * dh;
        }
    }

    double train(const std::vector<std::pair<std::vector<double>, double>>& data,
                 int epochs, std::function<double(int,int)> schedule) {
        std::vector<double> losses;
        for (int epoch = 0; epoch < epochs; ++epoch) {
            double lr = schedule(epoch, epochs);
            double total = 0.0;
            for (const auto& sample : data) {
                auto [yp, h] = forward(sample.first);
                total += (yp - sample.second) * (yp - sample.second) / 2.0;
                backward(sample.first, sample.second, yp, h, lr);
            }
            losses.push_back(total / data.size());
        }
        double mean = std::accumulate(losses.end() - 10, losses.end(), 0.0) / 10.0;
        double var = 0.0;
        for (int i = static_cast<int>(losses.size()) - 10; i < static_cast<int>(losses.size()); ++i)
            var += (losses[i] - mean) * (losses[i] - mean);
        late_var = var / 10.0;
        return losses.back();
    }

    double late_variance() const { return late_var; }

private:
    double w1[4][2];
    double b1[4];
    double w2[4];
    double b2;
    double late_var = 0.0;
};

int main() {
    std::mt19937_64 rng(42);
    std::normal_distribution<double> nd(0.0, 1.0);
    std::vector<std::pair<std::vector<double>, double>> data;
    for (int i = 0; i < 40; ++i) {
        std::vector<double> x = {nd(rng), nd(rng)};
        double y = (x[0] + x[1] > 0.0) ? 1.0 : 0.0;
        data.push_back({x, y});
    }

    auto constant_lr = [](int, int) { return 0.05; };
    auto step_decay_lr = [](int epoch, int) {
        if (epoch < 40) return 0.05;
        if (epoch < 80) return 0.025;
        return 0.0125;
    };
    auto cosine_lr = [](int epoch, int total) {
        double lr_min = 0.001, lr_max = 0.05;
        return lr_min + (lr_max - lr_min) * (1.0 + std::cos(M_PI * epoch / total)) / 2.0;
    };

    SimpleNet net_const, net_step, net_cos;
    double const_loss = net_const.train(data, 120, constant_lr);
    double step_loss = net_step.train(data, 120, step_decay_lr);
    double cosine_loss = net_cos.train(data, 120, cosine_lr);

    assert(const_loss < 0.1);
    assert(step_loss < 0.1);
    assert(cosine_loss < 0.1);
    assert(net_step.late_variance() < 1e-6);
    assert(net_cos.late_variance() < 1e-6);

    std::cout << "learning_rate_schedules.cpp PASS" << std::endl;
    return 0;
}
