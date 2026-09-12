// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/* Feature scaling toolkit: min-max, z-score, robust scaling.
 * Core claim: all scalers produce correct ranges, z-score gives mean=0/std=1,
 *             robust handles outliers, invertible.
 */
#include <cassert>
#include <cmath>
#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>

int main() {
    std::vector<double> data = {1.0, 2.0, 3.0, 4.0, 5.0, 100.0};
    double mean = std::accumulate(data.begin(), data.end(), 0.0) / data.size();
    double var = 0.0; for (double v : data) var += (v - mean) * (v - mean); var /= data.size();
    double stddev = std::sqrt(var);
    
    // Min-max scaling
    double mn = *std::min_element(data.begin(), data.end()), mx = *std::max_element(data.begin(), data.end());
    std::vector<double> scaled_minmax;
    for (double v : data) scaled_minmax.push_back((v - mn) / (mx - mn));
    assert(*std::min_element(scaled_minmax.begin(), scaled_minmax.end()) >= 0.0);
    assert(*std::max_element(scaled_minmax.begin(), scaled_minmax.end()) <= 1.0);
    assert(std::abs(*std::min_element(scaled_minmax.begin(), scaled_minmax.end()) - 0.0) < 1e-10);
    assert(std::abs(*std::max_element(scaled_minmax.begin(), scaled_minmax.end()) - 1.0) < 1e-10);
    
    // Z-score standardization
    std::vector<double> zscore;
    for (double v : data) zscore.push_back((v - mean) / stddev);
    double z_mean = std::accumulate(zscore.begin(), zscore.end(), 0.0) / zscore.size();
    double z_var = 0.0; for (double v : zscore) z_var += (v - z_mean) * (v - z_mean); z_var /= zscore.size();
    double z_std = std::sqrt(z_var);
    assert(std::abs(z_mean - 0.0) < 1e-10);
    assert(std::abs(z_std - 1.0) < 1e-10);
    
    // Robust scaling (median / IQR)
    std::vector<double> sorted = data;
    std::sort(sorted.begin(), sorted.end());
    double med = sorted[sorted.size()/2];
    double q1 = sorted[sorted.size()/4];
    double q3 = sorted[3*sorted.size()/4];
    double iqr = q3 - q1;
    std::vector<double> scaled_robust;
    for (double v : data) scaled_robust.push_back(iqr > 0 ? (v - med) / iqr : 0.0);
    bool all_finite = true;
    for (double v : scaled_robust) if (!std::isfinite(v)) all_finite = false;
    assert(all_finite);
    
    // Outlier detection
    double outlier_val = 100.0;
    double zscore_outlier = (outlier_val - mean) / stddev;
    double robust_outlier = (outlier_val - med) / iqr;
    assert(std::abs(zscore_outlier) > 1.0);
    assert(std::abs(robust_outlier) > 0.0);
    
    // Invertibility: min-max
    double orig_mm = scaled_minmax[0] * (mx - mn) + mn;
    assert(std::abs(orig_mm - data[0]) < 1e-10);
    
    // Invertibility: z-score
    double orig_z = zscore[0] * stddev + mean;
    assert(std::abs(orig_z - data[0]) < 1e-10);
    
    std::cout << "feature_scaling_toolkit.cpp: all_scalers_correct PASS" << std::endl;
    return 0;
}
