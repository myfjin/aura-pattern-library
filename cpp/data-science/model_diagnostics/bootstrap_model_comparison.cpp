// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Bootstrap Model Comparison
 * 
 * Compares two models using paired bootstrap resampling on the same test set.
 * Computes the win rate: how often Model A is better than Model B across bootstrap samples.
 */

#include <vector>
#include <random>
#include <cmath>
#include <cassert>
#include <iostream>
#include <utility>
#include <functional>

double mean_absolute_error(const std::vector<double>& y_true, const std::vector<double>& y_pred) {
    double sum = 0.0;
    for (size_t i = 0; i < y_true.size(); ++i) {
        sum += std::abs(y_true[i] - y_pred[i]);
    }
    return sum / y_true.size();
}

std::tuple<int, int, double> bootstrap_model_comparison(
    const std::vector<std::pair<double, double>>& test_data,
    std::function<double(double)> model1,
    std::function<double(double)> model2,
    int n_bootstraps = 100
) {
    /* Compare two models using bootstrap resampling. Returns (wins1, wins2, win_rate1). */
    int wins1 = 0, wins2 = 0;
    int n = static_cast<int>(test_data.size());

    std::mt19937 rng(42);
    std::uniform_int_distribution<int> uniform(0, n - 1);

    for (int b = 0; b < n_bootstraps; ++b) {
        // Resample test set with replacement
        std::vector<double> x_list, y_list;
        x_list.reserve(n);
        y_list.reserve(n);
        for (int i = 0; i < n; ++i) {
            auto sample = test_data[uniform(rng)];
            x_list.push_back(sample.first);
            y_list.push_back(sample.second);
        }

        // Compute predictions
        std::vector<double> pred1, pred2;
        pred1.reserve(n);
        pred2.reserve(n);
        for (double x : x_list) {
            pred1.push_back(model1(x));
            pred2.push_back(model2(x));
        }

        // Compute MAE
        double mae1 = mean_absolute_error(y_list, pred1);
        double mae2 = mean_absolute_error(y_list, pred2);

        // Lower MAE is better
        if (mae1 < mae2) {
            wins1++;
        } else if (mae2 < mae1) {
            wins2++;
        }
    }

    double win_rate1 = static_cast<double>(wins1) / n_bootstraps;
    return {wins1, wins2, win_rate1};
}

int main() {
    // Generate synthetic test data: y = 2*x + noise
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform_x(-5.0, 5.0);
    std::normal_distribution<double> normal(0.0, 1.0);

    std::vector<std::pair<double, double>> test_data(200);
    for (int i = 0; i < 200; ++i) {
        double x = uniform_x(rng);
        double y = 2.0 * x + normal(rng);
        test_data[i] = {x, y};
    }

    // Model A: good (2*x, true function)
    auto model_a = [](double x) { return 2.0 * x; };
    // Model B: mediocre (1.8*x, biased)
    auto model_b = [](double x) { return 1.8 * x; };

    // Model A vs Model B (A is better)
    auto [wins_a, wins_b, win_rate_a] = bootstrap_model_comparison(test_data, model_a, model_b, 100);

    // Model A should win significantly more often
    assert(win_rate_a > 0.7);

    // Test identical models
    auto [wins_same1, wins_same2, win_rate_same] = bootstrap_model_comparison(test_data, model_a, model_a, 100);

    // Identical models should have few wins (mostly ties)
    assert(wins_same1 + wins_same2 < 50);

    std::cout << "Bootstrap model comparison PASSED" << std::endl;
    return 0;
}
