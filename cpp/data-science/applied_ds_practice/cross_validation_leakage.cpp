// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/* Cross-validation leakage: feature selection before CV inflates accuracy.
 *
 * Core claim: leaky CV (select on full data) overestimates vs correct CV.
 */
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <vector>

std::vector<double> univariate_correlation(
    const std::vector<std::vector<double>>& X,
    const std::vector<int>& y
) {
    int n = static_cast<int>(X.size());
    int p = static_cast<int>(X[0].size());
    std::vector<double> corrs(p, 0.0);

    double y_mean = 0.0;
    for (int yi : y) y_mean += yi;
    y_mean /= n;

    for (int j = 0; j < p; ++j) {
        double x_mean = 0.0;
        for (int i = 0; i < n; ++i) x_mean += X[i][j];
        x_mean /= n;

        double cov = 0.0, var_x = 0.0, var_y = 0.0;
        for (int i = 0; i < n; ++i) {
            cov += (X[i][j] - x_mean) * (y[i] - y_mean);
            var_x += (X[i][j] - x_mean) * (X[i][j] - x_mean);
            var_y += (y[i] - y_mean) * (y[i] - y_mean);
        }
        cov /= n; var_x /= n; var_y /= n;
        double denom = std::sqrt(std::max(var_x * var_y, 1e-10));
        corrs[j] = denom > 0 ? std::abs(cov / denom) : 0.0;
    }
    return corrs;
}

std::vector<int> select_top_features(
    const std::vector<std::vector<double>>& X,
    const std::vector<int>& y,
    int k
) {
    auto corrs = univariate_correlation(X, y);
    std::vector<std::pair<double, int>> indexed;
    for (int i = 0; i < static_cast<int>(corrs.size()); ++i) {
        indexed.push_back({corrs[i], i});
    }
    // Sort descending
    for (size_t i = 0; i < indexed.size(); ++i) {
        for (size_t j = i + 1; j < indexed.size(); ++j) {
            if (indexed[j].first > indexed[i].first) {
                std::swap(indexed[i], indexed[j]);
            }
        }
    }
    std::vector<int> result;
    for (int i = 0; i < k && i < static_cast<int>(indexed.size()); ++i) {
        result.push_back(indexed[i].second);
    }
    return result;
}

std::vector<int> knn_classify(
    const std::vector<std::vector<double>>& X_train,
    const std::vector<int>& y_train,
    const std::vector<std::vector<double>>& X_test,
    int k = 5
) {
    std::vector<int> preds;
    for (const auto& x_test : X_test) {
        std::vector<std::pair<double, int>> distances;
        for (size_t i = 0; i < X_train.size(); ++i) {
            double dist = 0.0;
            for (size_t j = 0; j < X_train[i].size(); ++j) {
                dist += (x_test[j] - X_train[i][j]) * (x_test[j] - X_train[i][j]);
            }
            distances.push_back({std::sqrt(dist), y_train[i]});
        }
        // Sort by distance
        for (size_t i = 0; i < distances.size(); ++i) {
            for (size_t j = i + 1; j < distances.size(); ++j) {
                if (distances[j].first < distances[i].first) {
                    std::swap(distances[i], distances[j]);
                }
            }
        }
        int votes_0 = 0, votes_1 = 0;
        for (int i = 0; i < k && i < static_cast<int>(distances.size()); ++i) {
            if (distances[i].second == 1) votes_1++;
            else votes_0++;
        }
        preds.push_back(votes_1 > votes_0 ? 1 : 0);
    }
    return preds;
}

double accuracy(const std::vector<int>& y_true, const std::vector<int>& y_pred) {
    int correct = 0;
    for (size_t i = 0; i < y_true.size(); ++i) {
        if (y_true[i] == y_pred[i]) correct++;
    }
    return y_true.empty() ? 0.0 : static_cast<double>(correct) / y_true.size();
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> noise_strong(0.0, 0.3);
    std::normal_distribution<double> noise_weak(0.0, 1.0);
    std::uniform_real_distribution<double> uniform(0.0, 1.0);

    int n_samples = 200;
    int n_noise = 500;
    int n_true = 5;
    int n_features = n_noise + n_true;

    std::vector<std::vector<double>> X(n_samples, std::vector<double>(n_features));
    std::vector<int> y(n_samples);

    for (int i = 0; i < n_samples; ++i) {
        std::vector<double> true_part;
        for (int j = 0; j < n_true; ++j) {
            X[i][j] = noise_strong(gen);
            true_part.push_back(X[i][j]);
        }
        for (int j = n_true; j < n_features; ++j) {
            X[i][j] = noise_weak(gen);
        }

        // Labels mostly random but slightly correlated with true features
        bool label = uniform(gen) < 0.5;
        bool any_large = false;
        for (double xi : true_part) {
            if (xi > 0.5) any_large = true;
        }
        if (any_large) {
            label = uniform(gen) < 0.6;
        }
        y[i] = label ? 1 : 0;
    }

    // 4-fold CV
    int fold_size = n_samples / 4;
    std::vector<double> fold_accs_leaky;
    std::vector<double> fold_accs_correct;

    for (int fold_idx = 0; fold_idx < 4; ++fold_idx) {
        int test_start = fold_idx * fold_size;
        int test_end = (fold_idx + 1) * fold_size;

        std::vector<std::vector<double>> X_test(X.begin() + test_start, X.begin() + test_end);
        std::vector<int> y_test(y.begin() + test_start, y.begin() + test_end);

        std::vector<std::vector<double>> X_train;
        std::vector<int> y_train;
        for (int i = 0; i < test_start; ++i) {
            X_train.push_back(X[i]);
            y_train.push_back(y[i]);
        }
        for (int i = test_end; i < n_samples; ++i) {
            X_train.push_back(X[i]);
            y_train.push_back(y[i]);
        }

        // LEAKY: select on FULL data
        auto selected_leaky = select_top_features(X, y, 10);
        std::vector<std::vector<double>> X_train_leaky, X_test_leaky;
        for (const auto& row : X_train) {
            std::vector<double> proj;
            for (int idx : selected_leaky) proj.push_back(row[idx]);
            X_train_leaky.push_back(proj);
        }
        for (const auto& row : X_test) {
            std::vector<double> proj;
            for (int idx : selected_leaky) proj.push_back(row[idx]);
            X_test_leaky.push_back(proj);
        }
        auto preds_leaky = knn_classify(X_train_leaky, y_train, X_test_leaky, 5);
        fold_accs_leaky.push_back(accuracy(y_test, preds_leaky));

        // CORRECT: select on train only
        auto selected_correct = select_top_features(X_train, y_train, 10);
        std::vector<std::vector<double>> X_train_correct, X_test_correct;
        for (const auto& row : X_train) {
            std::vector<double> proj;
            for (int idx : selected_correct) proj.push_back(row[idx]);
            X_train_correct.push_back(proj);
        }
        for (const auto& row : X_test) {
            std::vector<double> proj;
            for (int idx : selected_correct) proj.push_back(row[idx]);
            X_test_correct.push_back(proj);
        }
        auto preds_correct = knn_classify(X_train_correct, y_train, X_test_correct, 5);
        fold_accs_correct.push_back(accuracy(y_test, preds_correct));
    }

    double mean_leaky = 0.0, mean_correct = 0.0;
    for (double a : fold_accs_leaky) mean_leaky += a;
    for (double a : fold_accs_correct) mean_correct += a;
    mean_leaky /= fold_accs_leaky.size();
    mean_correct /= fold_accs_correct.size();

    assert(mean_leaky > mean_correct);
    assert(mean_leaky - mean_correct > 0.05);

    std::cout << "PASS" << std::endl;
    return 0;
}
