// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Tiny autoencoder trained from scratch with hand-written backpropagation. An
 * 8->2->8 sigmoid network learns to compress inputs through a 2-D bottleneck and
 * reconstruct them, updating encoder/decoder weights by gradient descent on squared
 * reconstruction error. Use to demonstrate unsupervised representation learning and
 * end-to-end backprop without a framework. Guarantee (proven in main): on correlated
 * 8-D data the trained reconstruction error is less than half the error of random
 * outputs — the bottleneck genuinely captured structure, not noise.
 */
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <vector>

class TinyAutoencoder {
public:
    TinyAutoencoder(int input_dim = 8, int bottleneck_dim = 2, double lr = 0.1)
        : input_dim_(input_dim), bottleneck_dim_(bottleneck_dim), lr_(lr),
          we_(bottleneck_dim, std::vector<double>(input_dim)),
          wd_(input_dim, std::vector<double>(bottleneck_dim)),
          be_(bottleneck_dim, 0.0),
          bd_(input_dim, 0.0) {
        std::normal_distribution<double> dist(0.0, 0.2);
        for (int i = 0; i < bottleneck_dim; ++i)
            for (int j = 0; j < input_dim; ++j)
                we_[i][j] = dist(rng_);
        for (int i = 0; i < input_dim; ++i)
            for (int j = 0; j < bottleneck_dim; ++j)
                wd_[i][j] = dist(rng_);
    }

    std::vector<double> encode(const std::vector<double>& x) const {
        std::vector<double> h(bottleneck_dim_);
        for (int i = 0; i < bottleneck_dim_; ++i) {
            double z = be_[i];
            for (int j = 0; j < input_dim_; ++j)
                z += we_[i][j] * x[j];
            h[i] = sigmoid(z);
        }
        return h;
    }

    std::vector<double> decode(const std::vector<double>& h) const {
        std::vector<double> recon(input_dim_);
        for (int i = 0; i < input_dim_; ++i) {
            double z = bd_[i];
            for (int j = 0; j < bottleneck_dim_; ++j)
                z += wd_[i][j] * h[j];
            recon[i] = sigmoid(z);
        }
        return recon;
    }

    std::pair<std::vector<double>, std::vector<double>> forward(const std::vector<double>& x) const {
        auto h = encode(x);
        auto recon = decode(h);
        return {h, recon};
    }

    void backward(const std::vector<double>& x, const std::vector<double>& h,
                  const std::vector<double>& recon) {
        std::vector<double> dz_d(input_dim_);
        for (int i = 0; i < input_dim_; ++i) {
            double drecon = recon[i] - x[i];
            dz_d[i] = drecon * sigmoid_derivative(recon[i]);
        }

        for (int i = 0; i < input_dim_; ++i) {
            for (int j = 0; j < bottleneck_dim_; ++j)
                wd_[i][j] -= lr_ * dz_d[i] * h[j];
            bd_[i] -= lr_ * dz_d[i];
        }

        std::vector<double> dz_e(bottleneck_dim_);
        for (int i = 0; i < bottleneck_dim_; ++i) {
            double dh = 0.0;
            for (int j = 0; j < input_dim_; ++j)
                dh += dz_d[j] * wd_[j][i];
            dz_e[i] = dh * sigmoid_derivative(h[i]);
        }

        for (int i = 0; i < bottleneck_dim_; ++i) {
            for (int j = 0; j < input_dim_; ++j)
                we_[i][j] -= lr_ * dz_e[i] * x[j];
            be_[i] -= lr_ * dz_e[i];
        }
    }

    double train(const std::vector<std::vector<double>>& data, int epochs) {
        for (int e = 0; e < epochs; ++e) {
            for (const auto& x : data) {
                auto [h, recon] = forward(x);
                backward(x, h, recon);
            }
        }

        double total_loss = 0.0;
        for (const auto& x : data) {
            auto [_, recon] = forward(x);
            double loss = 0.0;
            for (int i = 0; i < input_dim_; ++i)
                loss += (recon[i] - x[i]) * (recon[i] - x[i]);
            total_loss += loss / 2.0;
        }
        return data.empty() ? 0.0 : total_loss / static_cast<double>(data.size());
    }

private:
    static double sigmoid(double x) {
        if (x < -500.0) return 0.0;
        if (x > 500.0) return 1.0;
        return 1.0 / (1.0 + std::exp(-x));
    }

    static double sigmoid_derivative(double s) { return s * (1.0 - s); }

    int input_dim_, bottleneck_dim_;
    double lr_;
    std::vector<std::vector<double>> we_, wd_;
    std::vector<double> be_, bd_;
    static std::mt19937 rng_;
};

std::mt19937 TinyAutoencoder::rng_(42);

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> gauss(0.0, 1.0);

    // Generate correlated 8D data and normalize each sample to [0, 1]
    std::vector<std::vector<double>> data;
    for (int n = 0; n < 50; ++n) {
        double s1 = gauss(rng);
        double s2 = gauss(rng);
        std::vector<double> x = {
            s1,
            s1 + gauss(rng) * 0.1,
            s1 - gauss(rng) * 0.1,
            s1 * 0.7 + s2 * 0.3,
            s2,
            s2 + gauss(rng) * 0.1,
            s2 - gauss(rng) * 0.1,
            s2 * 0.7 + s1 * 0.3,
        };
        double x_min = *std::min_element(x.begin(), x.end());
        double x_max = *std::max_element(x.begin(), x.end());
        if (x_max > x_min) {
            for (double& v : x)
                v = (v - x_min) / (x_max - x_min);
        }
        data.push_back(x);
    }

    // Untrained baseline: random reconstruction
    std::uniform_real_distribution<double> uniform(0.0, 1.0);
    double random_recon_error = 0.0;
    for (const auto& x : data) {
        double error = 0.0;
        for (int i = 0; i < 8; ++i) {
            double r = uniform(rng);
            error += (r - x[i]) * (r - x[i]);
        }
        random_recon_error += error / 2.0;
    }
    random_recon_error /= static_cast<double>(data.size());

    // Train autoencoder
    TinyAutoencoder ae(8, 2, 0.5);
    double trained_error = ae.train(data, 100);

    std::cout << "Random reconstruction error: " << random_recon_error << "\n";
    std::cout << "Trained reconstruction error: " << trained_error << "\n";
    std::cout << "Improvement: " << (random_recon_error / trained_error) << "x\n";

    assert(trained_error < random_recon_error / 2.0);
    std::cout << "PASS\n";
    return 0;
}
