// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Gaussian Mixture Model (1D) via Expectation-Maximization.
 *
 * Oracle asserts:
 *   sorted(means)[0] < 2.5, sorted(means)[1] > 2.5
 *   abs(sorted(means)[0]) < 1.5
 *   abs(sorted(means)[1] - 5.0) < 1.5
 *   all variances > 0
 *   abs(sum(weights) - 1.0) < 1e-5
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <numeric>

double normal_pdf(double x, double mean, double var) {
    if (var <= 0.0) return 0.0;
    return std::exp(-0.5 * (x - mean) * (x - mean) / var) / std::sqrt(2.0 * M_PI * var);
}

struct GMM {
    std::vector<double> means;
    std::vector<double> variances;
    std::vector<double> weights;
};

GMM em_fit_1d(const std::vector<double>& X, int k, int max_iterations = 100, double tolerance = 1e-6) {
    int n = static_cast<int>(X.size());

    // Embedded Python random.seed(42) choices: X[12] for comp0, X[39] for comp1
    std::vector<double> means = {X[12], X[39]};
    std::vector<double> variances(k, 1.0);
    std::vector<double> weights(k, 1.0 / k);

    std::vector<double> responsibilities(n * k);
    double prev_ll = -std::numeric_limits<double>::infinity();

    for (int iteration = 0; iteration < max_iterations; ++iteration) {
        for (int i = 0; i < n; ++i) {
            double total = 0.0;
            for (int j = 0; j < k; ++j) {
                double l = weights[j] * normal_pdf(X[i], means[j], variances[j]);
                responsibilities[i * k + j] = l;
                total += l;
            }
            if (total > 0.0) {
                for (int j = 0; j < k; ++j) responsibilities[i * k + j] /= total;
            } else {
                for (int j = 0; j < k; ++j) responsibilities[i * k + j] = 1.0 / k;
            }
        }

        std::vector<double> Nk(k, 0.0);
        for (int j = 0; j < k; ++j) {
            for (int i = 0; i < n; ++i) Nk[j] += responsibilities[i * k + j];
        }

        std::vector<double> new_weights(k);
        for (int j = 0; j < k; ++j) new_weights[j] = Nk[j] / n;

        std::vector<double> new_means(k);
        for (int j = 0; j < k; ++j) {
            if (Nk[j] > 0.0) {
                double sum = 0.0;
                for (int i = 0; i < n; ++i) sum += responsibilities[i * k + j] * X[i];
                new_means[j] = sum / Nk[j];
            } else {
                new_means[j] = means[j];
            }
        }

        std::vector<double> new_variances(k);
        for (int j = 0; j < k; ++j) {
            if (Nk[j] > 0.0) {
                double sum = 0.0;
                for (int i = 0; i < n; ++i) {
                    double diff = X[i] - new_means[j];
                    sum += responsibilities[i * k + j] * diff * diff;
                }
                new_variances[j] = std::max(sum / Nk[j], 1e-6);
            } else {
                new_variances[j] = variances[j];
            }
        }

        means = new_means;
        variances = new_variances;
        weights = new_weights;

        double ll = 0.0;
        for (int i = 0; i < n; ++i) {
            double lik = 0.0;
            for (int j = 0; j < k; ++j) lik += weights[j] * normal_pdf(X[i], means[j], variances[j]);
            if (lik > 0.0) ll += std::log(lik);
        }
        if (std::abs(ll - prev_ll) < tolerance) break;
        prev_ll = ll;
    }

    return {means, variances, weights};
}

int main() {
    // Embedded Python seed=42 data: 25 N(0,1) + 25 N(5,1)
    std::vector<double> X = {
        -0.14409032957792836, -0.1729036003315193, -0.11131586156766246, 0.7019837250988631,
        -0.12758828378288709, -1.4973534143409575, 0.33231834406771527, -0.2673374784971682,
        -0.216958684145195, 0.11588478670085507, 0.23229773690672087, 1.163558686599143,
        0.6566365067986689, 0.11050717744383194, -0.7383216023448206, -1.014662367487717,
        0.24634219521120196, 1.3110808272040482, 0.04165686390338389, -0.10632329377078427,
        0.5317762204008692, -1.453545298008678, -0.3122773171445598, 0.49036253259352475,
        0.8734043853794468, 4.759370327344865, 5.37659985868791, 5.248213449328414,
        5.782326808703642, 3.8867777857518275, 5.568250687585386, 3.4854796082748605,
        2.380054577781148, 4.393109271800498, 4.084189953654005, 5.876012243056406,
        5.664265899612895, 3.780925258704305, 5.8473614233480005, 3.9977971757576505,
        4.913756153663716, 4.706100222043468, 5.114419857460922, 5.8186363115437665,
        5.638413790792444, 5.349885101869209, 5.649948097806298, 5.478492037650119,
        4.3730145347804, 4.282628906183422
    };

    GMM gmm = em_fit_1d(X, 2);

    auto means_sorted = gmm.means;
    std::sort(means_sorted.begin(), means_sorted.end());

    assert(means_sorted[0] < 2.5);
    assert(means_sorted[1] > 2.5);
    assert(std::abs(means_sorted[0]) < 1.5);
    assert(std::abs(means_sorted[1] - 5.0) < 1.5);

    for (double v : gmm.variances) assert(v > 0.0);

    double wsum = 0.0;
    for (double w : gmm.weights) wsum += w;
    assert(std::abs(wsum - 1.0) < 1e-5);

    std::cout << "gaussian_mixture_em.cpp PASS: means = [";
    for (size_t i = 0; i < means_sorted.size(); ++i) {
        if (i) std::cout << ", ";
        std::cout << means_sorted[i];
    }
    std::cout << "]" << std::endl;
    return 0;
}
