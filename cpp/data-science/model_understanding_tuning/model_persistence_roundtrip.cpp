// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Model Persistence Roundtrip (Save and Reload).
 *
 * Oracle asserts:
 *   predictions identical after roundtrip
 *   intercept and weights match
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <random>

class SimpleLinearModel {
public:
    SimpleLinearModel(double intercept = 0.0, const std::vector<double>& weights = {})
        : intercept_(intercept), weights_(weights) {}

    std::vector<double> predict(const std::vector<std::vector<double>>& X) const {
        std::vector<double> preds;
        for (const auto& x : X) {
            double p = intercept_;
            for (size_t i = 0; i < x.size(); ++i) p += weights_[i] * x[i];
            preds.push_back(p);
        }
        return preds;
    }

    std::string to_json() const {
        std::ostringstream oss;
        oss << std::hexfloat;
        oss << "{\"intercept\":" << intercept_ << ",\"weights\":[";
        for (size_t i = 0; i < weights_.size(); ++i) {
            if (i) oss << ",";
            oss << weights_[i];
        }
        oss << "]}";
        return oss.str();
    }

    static SimpleLinearModel from_json(const std::string& s) {
        double intercept;
        std::vector<double> weights;
        size_t wstart = s.find("\"weights\":[");
        size_t wend = s.find("]}", wstart);
        size_t istart = s.find("\"intercept\":");
        size_t iend = s.find(",\"weights\"");
        intercept = std::stod(s.substr(istart + 12, iend - istart - 12));
        std::string inner = s.substr(wstart + 11, wend - wstart - 11);
        std::istringstream iss(inner);
        iss >> std::hexfloat;
        std::string token;
        while (std::getline(iss, token, ',')) if (!token.empty()) weights.push_back(std::stod(token));
        return SimpleLinearModel(intercept, weights);
    }

    double intercept() const { return intercept_; }
    const std::vector<double>& weights() const { return weights_; }

private:
    double intercept_;
    std::vector<double> weights_;
};

SimpleLinearModel fit_linear_model(const std::vector<std::vector<double>>& X,
                                 const std::vector<double>& y) {
    int n = static_cast<int>(X.size());
    int f = static_cast<int>(X[0].size());
    std::vector<double> x_means(f, 0.0);
    for (const auto& row : X) for (int j = 0; j < f; ++j) x_means[j] += row[j];
    for (double& m : x_means) m /= n;
    double y_mean = 0.0;
    for (double v : y) y_mean += v;
    y_mean /= n;

    std::vector<double> weights(f);
    for (int j = 0; j < f; ++j) {
        double cov_xy = 0.0, var_x = 0.0;
        for (int i = 0; i < n; ++i) {
            cov_xy += (X[i][j] - x_means[j]) * (y[i] - y_mean);
            var_x += (X[i][j] - x_means[j]) * (X[i][j] - x_means[j]);
        }
        cov_xy /= n; var_x /= n;
        weights[j] = var_x > 0 ? cov_xy / var_x : 0.0;
    }
    double intercept = y_mean;
    for (int j = 0; j < f; ++j) intercept -= weights[j] * x_means[j];
    return SimpleLinearModel(intercept, weights);
}

int main() {
    std::vector<std::vector<double>> X_train = {
        {0.557707193831535, -1.8999569791093323, -0.899882726523523},
        {0.7067979496916452, 1.5687182708193816, -1.6522446694823354},
        {-0.3123127212589183, -1.8808111222477186, -1.1254481007855865}
    };
    std::vector<double> y_train = {13.542768393721145, 8.395403267859386, 11.610687904377146};

    auto model = fit_linear_model(X_train, y_train);
    std::vector<std::vector<double>> X_test = {
        {-0.2313608027807703, -1.1451943960435989, -0.10725525636269495},
        {1.6047233033130168, 1.184099040507121, -1.321234415207781}
    };

    auto preds_original = model.predict(X_test);
    auto json_str = model.to_json();
    auto model_loaded = SimpleLinearModel::from_json(json_str);
    auto preds_loaded = model_loaded.predict(X_test);

    for (size_t i = 0; i < preds_original.size(); ++i)
        assert(std::abs(preds_original[i] - preds_loaded[i]) < 1e-10);

    assert(model.intercept() == model_loaded.intercept());
    assert(model.weights() == model_loaded.weights());

    std::cout << "model_persistence_roundtrip.cpp PASS" << std::endl;
    return 0;
}
