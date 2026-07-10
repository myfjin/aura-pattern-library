// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <numeric>

// Simple threshold classifier on feature 0.
struct BaseModel1 {
    double threshold = 0.0;
    void fit(const std::vector<std::pair<double, double>>& X, const std::vector<int>&) {
        std::vector<double> values;
        for (const auto& x : X) values.push_back(x.first);
        std::sort(values.begin(), values.end());
        threshold = values[values.size() / 2];
    }
    std::vector<double> predict(const std::vector<std::pair<double, double>>& X) const {
        std::vector<double> out;
        for (const auto& x : X) out.push_back(x.first > threshold ? 1.0 : 0.0);
        return out;
    }
};

// Simple threshold classifier on feature 1.
struct BaseModel2 {
    double threshold = 0.0;
    void fit(const std::vector<std::pair<double, double>>& X, const std::vector<int>&) {
        std::vector<double> values;
        for (const auto& x : X) values.push_back(x.second);
        std::sort(values.begin(), values.end());
        threshold = values[values.size() / 2];
    }
    std::vector<double> predict(const std::vector<std::pair<double, double>>& X) const {
        std::vector<double> out;
        for (const auto& x : X) out.push_back(x.second > threshold ? 1.0 : 0.0);
        return out;
    }
};

// Fit simple linear meta-learner: y = b0 + b1*x1 + b2*x2.
// For this demo we fit to the first base feature only, matching the Python oracle.
std::pair<double, std::vector<double>> fit_linear_model(const std::vector<std::vector<double>>& X_base,
                                                         const std::vector<double>& y) {
    size_t n = X_base.size();
    if (n == 0) return {0.0, {0.0, 0.0}};
    size_t m = X_base[0].size();

    double mean_x = 0.0;
    for (const auto& x : X_base) mean_x += std::accumulate(x.begin(), x.end(), 0.0);
    mean_x /= static_cast<double>(n * m);

    double mean_y = std::accumulate(y.begin(), y.end(), 0.0) / static_cast<double>(n);

    double numerator = 0.0, denominator = 0.0;
    for (size_t i = 0; i < n; ++i) {
        double dx = X_base[i][0] - mean_x;
        numerator += dx * (y[i] - mean_y);
        denominator += dx * dx;
    }

    double b1 = denominator > 1e-10 ? numerator / denominator : 0.0;
    double b0 = mean_y - b1 * mean_x;
    return {b0, {b1, 0.0}};
}

double predict_linear(const std::vector<double>& X, double b0, const std::vector<double>& coef) {
    double pred = b0;
    for (size_t i = 0; i < coef.size(); ++i) pred += X[i] * coef[i];
    return pred;
}

std::vector<std::vector<double>> generate_base_predictions(const std::vector<std::pair<double, double>>& X,
                                                            const std::vector<int>& y,
                                                            BaseModel1& model1,
                                                            BaseModel2& model2,
                                                            int k_folds = 5) {
    size_t n = X.size();
    size_t fold_size = n / k_folds;
    std::vector<std::vector<double>> meta_features(n, std::vector<double>(2, 0.0));

    for (int fold = 0; fold < k_folds; ++fold) {
        size_t val_start = fold * fold_size;
        size_t val_end = (fold < k_folds - 1) ? val_start + fold_size : n;

        std::vector<std::pair<double, double>> X_train;
        std::vector<int> y_train;
        for (size_t i = 0; i < n; ++i) {
            if (i < val_start || i >= val_end) {
                X_train.push_back(X[i]);
                y_train.push_back(y[i]);
            }
        }
        std::vector<std::pair<double, double>> X_val(X.begin() + val_start, X.begin() + val_end);

        model1.fit(X_train, y_train);
        auto preds1 = model1.predict(X_val);
        model2.fit(X_train, y_train);
        auto preds2 = model2.predict(X_val);

        for (size_t i = 0, val_idx = val_start; val_idx < val_end; ++i, ++val_idx) {
            meta_features[val_idx][0] = preds1[i];
            meta_features[val_idx][1] = preds2[i];
        }
    }
    return meta_features;
}

std::vector<int> predict_stacking(const std::vector<std::pair<double, double>>& X,
                                   BaseModel1& model1,
                                   BaseModel2& model2,
                                   double b0, const std::vector<double>& coef) {
    auto preds1 = model1.predict(X);
    auto preds2 = model2.predict(X);

    std::vector<int> predictions;
    for (size_t i = 0; i < X.size(); ++i) {
        std::vector<double> meta_input = {preds1[i], preds2[i]};
        double meta_pred = predict_linear(meta_input, b0, coef);
        predictions.push_back(meta_pred >= 0.5 ? 1 : 0);
    }
    return predictions;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> dist(0.0, 1.0);

    // Generate classification data
    int n_per_class = 50;
    std::vector<std::pair<double, double>> X;
    std::vector<int> y;

    for (int i = 0; i < n_per_class; ++i) {
        double x1 = 2.0 + 2.5 * dist(rng);
        double x2 = 2.0 + 2.5 * dist(rng);
        X.push_back({x1, x2});
        y.push_back(0);
    }
    for (int i = 0; i < n_per_class; ++i) {
        double x1 = 8.0 + 2.5 * dist(rng);
        double x2 = 8.0 + 2.5 * dist(rng);
        X.push_back({x1, x2});
        y.push_back(1);
    }

    // Split into train and test
    size_t n_train = static_cast<size_t>(0.7 * X.size());
    auto X_train = std::vector<std::pair<double, double>>(X.begin(), X.begin() + n_train);
    auto y_train = std::vector<int>(y.begin(), y.begin() + n_train);
    auto X_test = std::vector<std::pair<double, double>>(X.begin() + n_train, X.end());
    auto y_test = std::vector<int>(y.begin() + n_train, y.end());

    // Evaluate base models on test set
    BaseModel1 base_model1;
    BaseModel2 base_model2;
    base_model1.fit(X_train, y_train);
    base_model2.fit(X_train, y_train);

    auto base1_preds = base_model1.predict(X_test);
    double base1_acc = 0.0;
    for (size_t i = 0; i < y_test.size(); ++i)
        if ((base1_preds[i] >= 0.5 ? 1 : 0) == y_test[i]) base1_acc += 1.0;
    base1_acc /= y_test.size();

    auto base2_preds = base_model2.predict(X_test);
    double base2_acc = 0.0;
    for (size_t i = 0; i < y_test.size(); ++i)
        if ((base2_preds[i] >= 0.5 ? 1 : 0) == y_test[i]) base2_acc += 1.0;
    base2_acc /= y_test.size();

    // Fit stacking on training data using the SAME model instances.
    BaseModel1 stack_model1;
    BaseModel2 stack_model2;
    auto meta_X = generate_base_predictions(X_train, y_train, stack_model1, stack_model2, 5);
    std::vector<double> y_train_f(y_train.begin(), y_train.end());
    auto [b0, coef] = fit_linear_model(meta_X, y_train_f);

    // Predict with stacking on test set
    auto stack_preds = predict_stacking(X_test, stack_model1, stack_model2, b0, coef);
    double stack_acc = 0.0;
    for (size_t i = 0; i < y_test.size(); ++i)
        if (stack_preds[i] == y_test[i]) stack_acc += 1.0;
    stack_acc /= y_test.size();

    double avg_base_acc = (base1_acc + base2_acc) / 2.0;
    assert(stack_acc > avg_base_acc);

    std::cout << "stacking_ensemble: base1_acc=" << base1_acc
              << ", base2_acc=" << base2_acc
              << ", stack_acc=" << stack_acc
              << " PASS" << std::endl;
    return 0;
}
