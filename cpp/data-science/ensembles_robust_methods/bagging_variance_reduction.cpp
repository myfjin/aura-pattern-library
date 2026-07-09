// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Bagging for Variance Reduction
 * 
 * Bagging (bootstrap aggregating) trains many copies of an UNSTABLE base learner
 * on bootstrap resamples and averages them. The averaged predictor has markedly
 * lower variance across retrainings than a single base learner.
 */

#include <vector>
#include <random>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <cassert>
#include <iostream>

struct Stump {
    double threshold;
    double left_mean;
    double right_mean;
};

double true_fn(double x) {
    return 2.0 * x;
}

std::pair<std::vector<double>, std::vector<double>> make_training_set(int n, std::mt19937& rng) {
    std::uniform_real_distribution<double> uniform(0.0, 10.0);
    std::normal_distribution<double> normal(0.0, 3.0);
    
    std::vector<double> X(n), y(n);
    for (int i = 0; i < n; ++i) {
        X[i] = uniform(rng);
        y[i] = true_fn(X[i]) + normal(rng);
    }
    return {X, y};
}

Stump fit_stump(const std::vector<double>& X, const std::vector<double>& y) {
    /* Regression stump: best single split by SSE — deliberately UNSTABLE. */
    int n = static_cast<int>(X.size());
    
    // Create order indices
    std::vector<int> order(n);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int i, int j) { return X[i] < X[j]; });
    
    std::vector<double> xs(n), ys(n);
    for (int i = 0; i < n; ++i) {
        xs[i] = X[order[i]];
        ys[i] = y[order[i]];
    }
    
    // Prefix sums
    std::vector<double> prefix(n + 1, 0.0), prefix_sq(n + 1, 0.0);
    for (int i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + ys[i];
        prefix_sq[i + 1] = prefix_sq[i] + ys[i] * ys[i];
    }
    
    // Find best split
    double best_sse = std::numeric_limits<double>::infinity();
    double best_thr = xs[n / 2];
    double best_lm = 0.0, best_rm = 0.0;
    
    for (int k = 1; k < n; ++k) {
        int nl = k, nr = n - k;
        double sl = prefix[k], sr = prefix[n] - prefix[k];
        double ssl = prefix_sq[k] - sl * sl / nl;
        double ssr = (prefix_sq[n] - prefix_sq[k]) - sr * sr / nr;
        double sse = ssl + ssr;
        
        if (sse < best_sse) {
            best_sse = sse;
            best_thr = (xs[k - 1] + xs[k]) / 2.0;
            best_lm = sl / nl;
            best_rm = sr / nr;
        }
    }
    
    return {best_thr, best_lm, best_rm};
}

double predict_stump(double x, const Stump& s) {
    return (x <= s.threshold) ? s.left_mean : s.right_mean;
}

std::vector<Stump> fit_bagged(const std::vector<double>& X, const std::vector<double>& y, int n_models, std::mt19937& rng) {
    std::vector<Stump> models;
    models.reserve(n_models);
    int n = static_cast<int>(X.size());
    std::uniform_int_distribution<int> uniform(0, n - 1);
    
    for (int m = 0; m < n_models; ++m) {
        std::vector<double> X_boot(n), y_boot(n);
        for (int i = 0; i < n; ++i) {
            int idx = uniform(rng);
            X_boot[i] = X[idx];
            y_boot[i] = y[idx];
        }
        models.push_back(fit_stump(X_boot, y_boot));
    }
    return models;
}

double predict_bagged(double x, const std::vector<Stump>& models) {
    double sum = 0.0;
    for (const auto& m : models) {
        sum += predict_stump(x, m);
    }
    return sum / models.size();
}

double variance(const std::vector<double>& vals) {
    double mean = std::accumulate(vals.begin(), vals.end(), 0.0) / vals.size();
    double sum_sq = 0.0;
    for (const auto& v : vals) {
        sum_sq += (v - mean) * (v - mean);
    }
    return sum_sq / (vals.size() - 1);  // sample variance
}

int main() {
    std::mt19937 rng(42);
    
    // Bias–variance protocol: draw R INDEPENDENT training sets
    const int R = 30;
    std::vector<double> test_points = {1.0, 3.0, 5.0, 7.0, 9.0};
    std::vector<std::vector<double>> single_preds(test_points.size());
    std::vector<std::vector<double>> bagged_preds(test_points.size());
    
    for (int r = 0; r < R; ++r) {
        auto [X, y] = make_training_set(60, rng);
        Stump stump = fit_stump(X, y);
        auto ensemble = fit_bagged(X, y, 25, rng);
        
        for (size_t j = 0; j < test_points.size(); ++j) {
            double x0 = test_points[j];
            single_preds[j].push_back(predict_stump(x0, stump));
            bagged_preds[j].push_back(predict_bagged(x0, ensemble));
        }
    }
    
    double single_var_sum = 0.0, bagged_var_sum = 0.0;
    for (size_t j = 0; j < test_points.size(); ++j) {
        single_var_sum += variance(single_preds[j]);
        bagged_var_sum += variance(bagged_preds[j]);
    }
    double single_var = single_var_sum / test_points.size();
    double bagged_var = bagged_var_sum / test_points.size();
    
    // The reduction must be SUBSTANTIAL, not merely directional.
    assert(bagged_var < 0.5 * single_var);
    
    std::cout << "bagging_variance_reduction: retraining variance " << single_var 
              << " -> " << bagged_var << " (" << (bagged_var / single_var * 100) 
              << "% of single) PASS" << std::endl;
    return 0;
}
