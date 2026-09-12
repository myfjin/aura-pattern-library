// permutation_feature_importance.cpp
// Permutation feature importance with simple linear model.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <cassert>
#include <algorithm>

#include <utility>

using std::vector;
using std::pair;
using std::tuple;

static double mean(const vector<double>& v) {
    double s = 0.0;
    for (double x : v) s += x;
    return s / v.size();
}

static tuple<double, double, double> train_simple_model(const vector<vector<double>>& X,
                                                const vector<double>& y) {
    size_t n = X.size();
    vector<double> x1(n), x2(n);
    for (size_t i = 0; i < n; ++i) { x1[i] = X[i][0]; x2[i] = X[i][1]; }
    double mx1 = mean(x1), mx2 = mean(x2), my = mean(y);
    double c1 = 0.0, c2 = 0.0, v1 = 0.0, v2 = 0.0;
    for (size_t i = 0; i < n; ++i) {
        c1 += (x1[i] - mx1) * (y[i] - my);
        c2 += (x2[i] - mx2) * (y[i] - my);
        v1 += (x1[i] - mx1) * (x1[i] - mx1);
        v2 += (x2[i] - mx2) * (x2[i] - mx2);
    }
    double w1 = v1 > 0 ? c1 / v1 : 0.0;
    double w2 = v2 > 0 ? c2 / v2 : 0.0;
    double b = my - w1 * mx1 - w2 * mx2;
    return {b, w1, w2};
}

static vector<double> predict(const vector<vector<double>>& X,
                          double b, double w1, double w2) {
    vector<double> r;
    for (const auto& x : X)
        r.push_back(b + w1 * x[0] + w2 * x[1]);
    return r;
}

static double mse(const vector<double>& y_true, const vector<double>& y_pred) {
    double s = 0.0;
    for (size_t i = 0; i < y_true.size(); ++i) {
        double d = y_true[i] - y_pred[i];
        s += d * d;
    }
    return s / y_true.size();
}

static pair<double, double> permutation_importance(vector<vector<double>> X_test,
                                         const vector<double>& y_test,
                                         double b, double w1, double w2) {
    auto y_pred_orig = predict(X_test, b, w1, w2);
    double baseline = mse(y_test, y_pred_orig);

    std::mt19937 rng(42);
    double imp1, imp2;

    for (size_t feat = 0; feat < 2; ++feat) {
        auto Xs = X_test;
        vector<double> vals;
        for (const auto& row : Xs) vals.push_back(row[feat]);
        std::shuffle(vals.begin(), vals.end(), rng);
        for (size_t i = 0; i < vals.size(); ++i) Xs[i][feat] = vals[i];
        auto yps = predict(Xs, b, w1, w2);
        double shuffled_mse = mse(y_test, yps);
        if (feat == 0) imp1 = shuffled_mse - baseline;
        else imp2 = shuffled_mse - baseline;
    }
    return {imp1, imp2};
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uni(-2.0, 2.0);
    std::normal_distribution<double> noise(0.0, 0.5);

    vector<vector<double>> train_X;
    vector<double> train_y;
    for (int i = 0; i < 100; ++i) {
        double x1 = uni(rng);
        double x2 = uni(rng);
        double y = 5.0 + 3.0 * x1 + noise(rng);
        train_X.push_back({x1, x2});
        train_y.push_back(y);
    }

    auto [b, w1, w2] = train_simple_model(train_X, train_y);

    vector<vector<double>> test_X;
    vector<double> test_y;
    for (int i = 0; i < 50; ++i) {
        double x1 = uni(rng);
        double x2 = uni(rng);
        double y = 5.0 + 3.0 * x1 + noise(rng);
        test_X.push_back({x1, x2});
        test_y.push_back(y);
    }

    auto [imp_f1, imp_f2] = permutation_importance(test_X, test_y, b, w1, w2);

    std::cout << "Feature 1 importance: " << imp_f1 << ", Feature 2 importance: " << imp_f2 << "\n";

    assert(imp_f1 > imp_f2);
    assert(imp_f1 > 0.5);

    std::cout << "Permutation Feature Importance: PASS\n";
    return 0;
}
