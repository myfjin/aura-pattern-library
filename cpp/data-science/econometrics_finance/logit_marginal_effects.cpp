// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Logit marginal effects: average partial derivatives of predicted probability.
 *
 * Oracle asserts:
 *   abs(ame_analytical - ame_numerical) < 0.01
 *   ame_analytical > 0
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>

double logit_predict(double x, double beta) {
    return 1.0 / (1.0 + std::exp(-beta * x));
}

double logit_marginal_effect(double x, double beta) {
    double p = logit_predict(x, beta);
    return beta * p * (1.0 - p);
}

double average_marginal_effect(const std::vector<double>& x_values, double beta) {
    double s = 0.0;
    for (double x : x_values) s += logit_marginal_effect(x, beta);
    return s / x_values.size();
}

double numerical_gradient(double x, double beta, double eps = 1e-6) {
    double p_plus = logit_predict(x + eps, beta);
    double p_minus = logit_predict(x - eps, beta);
    return (p_plus - p_minus) / (2.0 * eps);
}

int main() {
    // Embedded Python seed=42 sample
    std::vector<double> x_sample = {
        -0.14409032957792836, -0.1729036003315193, -0.11131586156766246, 0.7019837250988631,
        -0.12758828378288709, -1.4973534143409575, 0.33231834406771527, -0.2673374784971682,
        -0.216958684145195, 0.11588478670085507, 0.23229773690672087, 1.163558686599143,
        0.6566365067986689, 0.11050717744383194, -0.7383216023448206, -1.014662367487717,
        0.24634219521120196, 1.3110808272040482, 0.04165686390338389, -0.10632329377078427,
        0.5317762204008692, -1.453545298008678, -0.3122773171445598, 0.49036253259352475,
        0.8734043853794468, -0.2406296726551354, 0.3765998586879102, 0.24821344932841446,
        0.7823268087036421, -1.1132222142481727, 0.5682506875853858, -1.5145203917251397,
        -2.619945422218852, -0.6068907281995026, -0.9158100463459947, 0.8760122430564063,
        0.664265899612895, -1.2190747412956953, 0.8473614233480004, -1.0022028242423497,
        -0.08624384633628418, -0.29389977795653216, 0.11441985746092122, 0.8186363115437669,
        0.6384137907924435, 0.3498851018692087, 0.6499480978062986, 0.4784920376501184,
        -0.6269854652195999, -0.7173710938165775
    };

    double beta_true = 1.5;
    double ame_analytical = average_marginal_effect(x_sample, beta_true);
    double ame_numerical = 0.0;
    for (double x : x_sample) ame_numerical += numerical_gradient(x, beta_true);
    ame_numerical /= x_sample.size();

    assert(std::abs(ame_analytical - ame_numerical) < 0.01);
    assert(ame_analytical > 0.0);

    std::cout << "logit_marginal_effects.cpp PASS" << std::endl;
    return 0;
}
