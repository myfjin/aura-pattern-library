// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Cox Partial Likelihood: Semiparametric Survival Model
 * 
 * Estimates hazard ratios via Newton-Raphson on partial likelihood.
 */

#include <vector>
#include <cmath>
#include <random>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <utility>

std::pair<double, double> cox_partial_likelihood_2cov(
    const std::vector<double>& times,
    const std::vector<int>& events,
    const std::vector<double>& x1,
    const std::vector<double>& x2,
    int max_iter = 20,
    double tol = 1e-6
) {
    /* Fit Cox model for 2 covariates via partial likelihood. */
    int n = static_cast<int>(times.size());
    double beta1 = 0.0, beta2 = 0.0;

    for (int iteration = 0; iteration < max_iter; ++iteration) {
        // Sort by time (ascending)
        std::vector<int> order(n);
        for (int i = 0; i < n; ++i) order[i] = i;
        std::sort(order.begin(), order.end(), [&times](int i, int j) { return times[i] < times[j]; });

        double score1 = 0.0, score2 = 0.0;
        double hess00 = 0.0, hess11 = 0.0, hess01 = 0.0;

        for (int i : order) {
            if (events[i] == 0) continue;

            // Risk set: all j with time_j >= time_i
            std::vector<int> at_risk;
            for (int j = 0; j < n; ++j) {
                if (times[j] >= times[i]) at_risk.push_back(j);
            }

            // Weighted sum over risk set
            double sum_exp = 0.0, sum_w_x1 = 0.0, sum_w_x2 = 0.0;
            double sum_w_x1x1 = 0.0, sum_w_x2x2 = 0.0, sum_w_x1x2 = 0.0;

            for (int j : at_risk) {
                double w = std::exp(beta1 * x1[j] + beta2 * x2[j]);
                sum_exp += w;
                sum_w_x1 += w * x1[j];
                sum_w_x2 += w * x2[j];
                sum_w_x1x1 += w * x1[j] * x1[j];
                sum_w_x2x2 += w * x2[j] * x2[j];
                sum_w_x1x2 += w * x1[j] * x2[j];
            }

            if (sum_exp < 1e-14) continue;

            double mean_x1 = sum_w_x1 / sum_exp;
            double mean_x2 = sum_w_x2 / sum_exp;

            // Score contribution
            score1 += x1[i] - mean_x1;
            score2 += x2[i] - mean_x2;

            // Hessian contribution
            double var_x1 = sum_w_x1x1 / sum_exp - mean_x1 * mean_x1;
            double var_x2 = sum_w_x2x2 / sum_exp - mean_x2 * mean_x2;
            double cov_x1x2 = sum_w_x1x2 / sum_exp - mean_x1 * mean_x2;

            hess00 += var_x1;
            hess11 += var_x2;
            hess01 += cov_x1x2;
        }

        // Newton step
        double det = hess00 * hess11 - hess01 * hess01;
        if (std::abs(det) < 1e-14) break;

        double inv00 = hess11 / det;
        double inv01 = -hess01 / det;
        double inv10 = -hess01 / det;
        double inv11 = hess00 / det;

        double delta1 = inv00 * score1 + inv01 * score2;
        double delta2 = inv10 * score1 + inv11 * score2;

        beta1 += delta1;
        beta2 += delta2;

        if (std::abs(delta1) < tol && std::abs(delta2) < tol) break;
    }

    return {beta1, beta2};
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> normal(0.0, 1.0);
    std::uniform_real_distribution<double> uniform(0.0, 1.0);
    std::exponential_distribution<double> exp_dist(0.3);

    // Planted: true hazard ratios β1=0.5, β2=-0.3
    const int n = 30;
    std::vector<double> x1(n), x2(n), times(n);
    std::vector<int> events(n);

    for (int i = 0; i < n; ++i) {
        x1[i] = normal(rng);
        x2[i] = normal(rng);
    }

    // Survival times: exp(lambda * exp(eta))
    for (int i = 0; i < n; ++i) {
        double eta = 0.5 * x1[i] - 0.3 * x2[i];
        double lambda_i = 0.5 * std::exp(eta);
        double t = -std::log(uniform(rng)) / lambda_i;
        double c_time = exp_dist(rng);
        times[i] = std::min(t, c_time);
        events[i] = (t <= c_time) ? 1 : 0;
    }

    auto [beta1, beta2] = cox_partial_likelihood_2cov(times, events, x1, x2);

    // Check: estimated betas close to true values (within ±0.5)
    assert(std::abs(beta1 - 0.5) < 0.5);
    assert(std::abs(beta2 - (-0.3)) < 0.5);

    std::cout << "cox_partial_likelihood_lite.cpp PASS" << std::endl;
    return 0;
}
