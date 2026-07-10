// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <vector>

// Box-Muller normal variate, replaces random.gauss for determinism with fixed seed.
double box_muller(double u1, double u2) {
    double r = std::sqrt(-2.0 * std::log(u1));
    double theta = 2.0 * M_PI * u2;
    return r * std::cos(theta);
}

// Minimal LCG returning values in (0,1].
struct LCG {
    unsigned long long state;
    explicit LCG(unsigned long long seed) : state(seed) {}
    double next() {
        state = state * 6364136223846793005ULL + 1442695040888963407ULL;
        // Map to (0,1]
        return (static_cast<double>(state & 0x7FFFFFFFFFFFFFFFULL) + 1.0) /
               static_cast<double>(0x7FFFFFFFFFFFFFFFULL + 1ULL);
    }
    double gauss() {
        double u1 = next();
        double u2 = next();
        if (u1 <= 0.0) u1 = 1e-10;
        return box_muller(u1, u2);
    }
};

struct LinearModel {
    double intercept;
    std::vector<double> weights;
};

LinearModel train_linear_model(const std::vector<std::vector<double>>& X,
                               const std::vector<double>& y) {
    std::size_t n = X.size();
    double x1_mean = 0.0, x2_mean = 0.0, y_mean = 0.0;
    for (std::size_t i = 0; i < n; ++i) {
        x1_mean += X[i][0];
        x2_mean += X[i][1];
        y_mean += y[i];
    }
    x1_mean /= static_cast<double>(n);
    x2_mean /= static_cast<double>(n);
    y_mean /= static_cast<double>(n);

    double cov_x1_y = 0.0, cov_x2_y = 0.0, var_x1 = 0.0, var_x2 = 0.0;
    for (std::size_t i = 0; i < n; ++i) {
        double dx1 = X[i][0] - x1_mean;
        double dx2 = X[i][1] - x2_mean;
        double dy = y[i] - y_mean;
        cov_x1_y += dx1 * dy;
        cov_x2_y += dx2 * dy;
        var_x1 += dx1 * dx1;
        var_x2 += dx2 * dx2;
    }
    cov_x1_y /= static_cast<double>(n);
    cov_x2_y /= static_cast<double>(n);
    var_x1 /= static_cast<double>(n);
    var_x2 /= static_cast<double>(n);

    double w1 = var_x1 > 0.0 ? cov_x1_y / var_x1 : 0.0;
    double w2 = var_x2 > 0.0 ? cov_x2_y / var_x2 : 0.0;
    double intercept = y_mean - w1 * x1_mean - w2 * x2_mean;
    return {intercept, {w1, w2}};
}

double predict(double x1, double x2, double intercept, const std::vector<double>& weights) {
    return intercept + weights[0] * x1 + weights[1] * x2;
}

std::vector<double> partial_dependence(
    const std::vector<std::vector<double>>& X,
    double intercept,
    const std::vector<double>& weights,
    int feat_idx,
    const std::vector<double>& x_range) {
    std::vector<double> pd_values;
    pd_values.reserve(x_range.size());
    for (double x_val : x_range) {
        double sum = 0.0;
        for (const auto& row : X) {
            double x1 = (feat_idx == 0) ? x_val : row[0];
            double x2 = (feat_idx == 1) ? x_val : row[1];
            sum += predict(x1, x2, intercept, weights);
        }
        pd_values.push_back(sum / static_cast<double>(X.size()));
    }
    return pd_values;
}

bool is_monotone_increasing(const std::vector<double>& values, double tolerance = 0.1) {
    for (std::size_t i = 1; i < values.size(); ++i) {
        if (values[i] < values[i - 1] - tolerance) return false;
    }
    return true;
}

bool is_flat(const std::vector<double>& values, double tolerance = 0.5) {
    if (values.empty()) return false;
    double mean = 0.0;
    for (double v : values) mean += v;
    mean /= static_cast<double>(values.size());
    double var = 0.0;
    for (double v : values) var += (v - mean) * (v - mean);
    var /= static_cast<double>(values.size());
    return var < tolerance;
}

int main() {
    LCG rng(42);

    std::vector<std::vector<double>> train_X;
    std::vector<double> train_y;
    for (int i = 0; i < 100; ++i) {
        double x1 = rng.next() * 5.0;  // uniform(0,5)
        double x2 = rng.next() * 5.0;
        double y = 10.0 + 2.0 * x1 + 0.1 * x2 + rng.gauss() * 0.3;
        train_X.push_back({x1, x2});
        train_y.push_back(y);
    }

    LinearModel model = train_linear_model(train_X, train_y);

    std::vector<double> x_range;
    for (int i = 0; i <= 10; ++i) x_range.push_back(i * 0.5);

    auto pd_f1 = partial_dependence(train_X, model.intercept, model.weights, 0, x_range);
    auto pd_f2 = partial_dependence(train_X, model.intercept, model.weights, 1, x_range);

    std::printf("PD Feature 1: [");
    for (std::size_t i = 0; i < pd_f1.size(); ++i) {
        if (i) std::printf(", ");
        std::printf("%.2f", pd_f1[i]);
    }
    std::printf("]\n");

    std::printf("PD Feature 2: [");
    for (std::size_t i = 0; i < pd_f2.size(); ++i) {
        if (i) std::printf(", ");
        std::printf("%.2f", pd_f2[i]);
    }
    std::printf("]\n");

    assert(is_monotone_increasing(pd_f1));
    assert(is_flat(pd_f2));

    std::printf("Partial Dependence Plot: PASS\n");
    return 0;
}
