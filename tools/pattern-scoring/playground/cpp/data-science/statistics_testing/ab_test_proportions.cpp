// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * A/B Test for Two Proportions
 *
 * Core idea: Test whether two conversion rates differ using a z-test for proportions.
 * Compute pooled standard error under the null, then the z-statistic. Also compute effect
 * size (Cohen's h) to quantify the practical difference.
 */

#include <iostream>
#include <cmath>
#include <cassert>
#include <tuple>
#include <iomanip>

using namespace std;

// Approximate standard normal CDF using Hart's rational approximation
double normal_cdf(double z) {
    if (z < 0) {
        return 1 - normal_cdf(-z);
    }
    double t = 1.0 / (1.0 + 0.2316419 * z);
    double d = 0.3989423 * exp(-z * z / 2.0);
    double approx = 1.0 - d * t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))));
    return approx;
}

// Perform z-test for two proportions.
// Returns: (z_statistic, p_value_approx, cohens_h)
tuple<double, double, double> ab_test_proportions(int conversions_a, int trials_a, 
                                                    int conversions_b, int trials_b) {
    double p_a = (double)conversions_a / trials_a;
    double p_b = (double)conversions_b / trials_b;
    double diff = p_a - p_b;
    
    // Pooled proportion (under null: p_a == p_b)
    double p_pooled = (double)(conversions_a + conversions_b) / (trials_a + trials_b);
    
    // Standard error under null
    double se_null = sqrt(p_pooled * (1.0 - p_pooled) * (1.0 / trials_a + 1.0 / trials_b));
    
    // Z-statistic
    double z = (se_null > 0) ? diff / se_null : 0.0;
    
    // One-tailed p-value: P(Z > |z|)
    double p_one_tail = 1.0 - normal_cdf(abs(z));
    // Two-tailed
    double p_value = min(2.0 * p_one_tail, 1.0);
    
    // Cohen's h: effect size for proportions
    // h = 2 * (arcsin(sqrt(p_a)) - arcsin(sqrt(p_b)))
    double h_a = 2.0 * asin(sqrt(p_a));
    double h_b = 2.0 * asin(sqrt(p_b));
    double cohens_h = (h_a - h_b) / 2.0;
    
    return {z, p_value, cohens_h};
}

int main() {
    // Scenario 1: No difference (null)
    // Both groups have ~10% conversion
    auto [z_null, p_null, h_null] = ab_test_proportions(10, 100, 11, 100);
    cout << fixed << setprecision(3);
    cout << "Null case: z=" << z_null << ", p=" << p_null << ", Cohen's h=" << h_null << endl;
    
    assert(p_null > 0.05);  // Null case should have high p-value
    
    // Scenario 2: Real difference
    // Group A: 15%, Group B: 10%
    auto [z_alt, p_alt, h_alt] = ab_test_proportions(30, 200, 15, 200);
    cout << "Alt case: z=" << z_alt << ", p=" << p_alt << ", Cohen's h=" << h_alt << endl;
    
    assert(p_alt < 0.05);  // Alt case should have low p-value
    assert(abs(h_alt) > 0.1);  // Effect size should be non-negligible
    
    cout << "✓ A/B test for proportions PASSED" << endl;
    
    return 0;
}
