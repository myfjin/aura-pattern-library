// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Laplace approximation: approximate posterior p(θ|data) with Gaussian at MAP.
 *
 * Oracle asserts:
 *   abs(theta_map - 2.0) < 0.5
 *   posterior_var > 0
 *   posterior_var < 1.0
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <random>

double log_posterior(double theta, const std::vector<double>& data,
                     double prior_mu = 0.0, double prior_sigma = 1.0) {
    double log_lik = 0.0;
    for (double y : data) log_lik -= 0.5 * (y - theta) * (y - theta);
    double log_prior = -0.5 * std::pow((theta - prior_mu) / prior_sigma, 2);
    return log_lik + log_prior;
}

double find_map(const std::vector<double>& data,
                double prior_mu = 0.0, double prior_sigma = 1.0,
                int max_iter = 100) {
    double theta = prior_mu;
    for (int i = 0; i < max_iter; ++i) {
        double grad = 0.0;
        for (double y : data) grad -= (theta - y);
        grad -= (theta - prior_mu) / (prior_sigma * prior_sigma);
        theta += 0.01 * grad;
    }
    return theta;
}

std::pair<double, double> laplace_approximation(const std::vector<double>& data,
                                               double prior_mu = 0.0,
                                               double prior_sigma = 1.0) {
    double theta_map = find_map(data, prior_mu, prior_sigma);
    int n = static_cast<int>(data.size());
    double hessian = n + 1.0 / (prior_sigma * prior_sigma);
    return {theta_map, 1.0 / hessian};
}

int main() {
    // Embedded Python seed=42 data
    std::vector<double> data = {
        1.4360846680085715, 3.11278345033504, 2.686728289993472, 1.3526930869132023,
        2.966242198830442, 1.183011657362203, 0.9755992130211796, 2.9244008130208205,
        0.8413744985427343, 1.6440246042745072, 2.7931911309099044, 1.7903528693045169,
        2.768258071785557, 1.5284969871051684, 2.304671359062072, 2.6058650469951333,
        1.346084701542402, 2.6223233308816193, 2.0166274556127676, 1.7877068250831342,
        2.1271034479603473, 2.1854181912034726, 2.187718181154005, 1.642274534387405,
        2.7111595395157886, 1.9037481309379458, 2.1505059308271427, 2.2151838777553507,
        1.8909304822814567, 0.31328888569926886, 1.7863002848712589, 2.9378083673098555,
        2.8164231313255928, 1.1003632394378445, 1.8927882610930222, 2.895781893976437,
        2.3192148154991378, 1.877250489870934, 2.693940037717797, 1.5991887296969403,
        1.9854495383074862, 3.849761094425946, 2.9295863488499044, 1.7625439878092387,
        2.0645534441812376, 2.09842214035368, 2.5522284787806907, 1.238309057077551,
        2.4335359896133955, 2.1322055173773256
    };

    auto [theta_map, posterior_var] = laplace_approximation(data, 0.0, 10.0);

    assert(std::abs(theta_map - 2.0) < 0.5);
    assert(posterior_var > 0.0);
    assert(posterior_var < 1.0);

    std::cout << "laplace_approximation_posterior.cpp PASS" << std::endl;
    return 0;
}
