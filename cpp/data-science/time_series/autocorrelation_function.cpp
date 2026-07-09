// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Autocorrelation Function (ACF)
 * 
 * Compute the autocorrelation of a time series at multiple lags.
 * ACF(k) = correlation between y_t and y_{t-k}.
 * Include simple significance bounds (±2/sqrt(n)) to identify significant lags.
 * Use to detect seasonality and memory in the data.
 */

#include <vector>
#include <cmath>
#include <stdexcept>
#include <random>
#include <cassert>
#include <iostream>

std::vector<double> acf(const std::vector<double>& series, int nlags) {
    /*
     * Compute autocorrelation function at lags 0 to nlags.
     * ACF(k) = cov(y_t, y_{t-k}) / var(y_t)
     */
    if (nlags < 0 || nlags >= static_cast<int>(series.size())) {
        throw std::invalid_argument("nlags must be 0 <= nlags < len(series)");
    }

    // Demean
    double sum = 0.0;
    for (const auto& y : series) {
        sum += y;
    }
    double mean = sum / series.size();
    
    std::vector<double> centered;
    centered.reserve(series.size());
    for (const auto& y : series) {
        centered.push_back(y - mean);
    }

    // Compute variance (lag 0 autocovariance)
    double c0 = 0.0;
    for (const auto& x : centered) {
        c0 += x * x;
    }
    c0 /= centered.size();
    
    if (c0 < 1e-10) {
        return std::vector<double>(nlags + 1, 0.0);
    }

    std::vector<double> acf_vals;
    acf_vals.push_back(1.0);  // ACF at lag 0 is always 1

    for (int lag = 1; lag <= nlags; ++lag) {
        double cov_lag = 0.0;
        for (size_t i = 0; i < centered.size() - lag; ++i) {
            cov_lag += centered[i] * centered[i + lag];
        }
        cov_lag /= centered.size();
        acf_vals.push_back(cov_lag / c0);
    }

    return acf_vals;
}

double significance_bounds(int n) {
    /* Bartlett's approximate 95% confidence bound: ±2/sqrt(n) */
    return 2.0 / std::sqrt(static_cast<double>(n));
}

std::vector<int> identify_significant_lags(const std::vector<double>& acf_vals, int n) {
    /* Identify lags where |ACF| exceeds significance bounds. */
    double bound = significance_bounds(n);
    std::vector<int> sig_lags;
    for (size_t lag = 1; lag < acf_vals.size(); ++lag) {
        if (std::abs(acf_vals[lag]) > bound) {
            sig_lags.push_back(static_cast<int>(lag));
        }
    }
    return sig_lags;
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> normal(0.0, 1.0);

    // Generate AR(1) series with autocorrelation
    std::vector<double> series;
    series.push_back(0.0);
    for (int i = 0; i < 200; ++i) {
        series.push_back(0.6 * series.back() + normal(rng));
    }

    // Compute ACF
    auto acf_vals = acf(series, 20);

    // Check basic properties
    assert(acf_vals.size() == 21);
    assert(acf_vals[0] == 1.0);  // ACF at lag 0 should be 1.0

    // For AR(1) with phi=0.6, ACF should decay exponentially
    // ACF(k) ≈ 0.6^k
    assert(acf_vals[1] > 0.4 && acf_vals[1] < 0.8);  // ACF at lag 1 should be close to 0.6
    assert(acf_vals[1] > acf_vals[2]);  // ACF should decay
    assert(acf_vals[2] > acf_vals[5]);  // ACF should continue decaying

    // Test significance bounds
    double bound = significance_bounds(static_cast<int>(series.size()));
    assert(bound > 0.0 && bound < 0.2);

    // Find significant lags
    auto sig_lags = identify_significant_lags(acf_vals, static_cast<int>(series.size()));
    assert(!sig_lags.empty());  // Should have significant lags for AR series

    // The first lag should be significant
    bool lag1_found = false;
    for (int lag : sig_lags) {
        if (lag == 1) {
            lag1_found = true;
            break;
        }
    }
    assert(lag1_found);  // Lag 1 should be significant for AR(1)

    // Create white noise (no autocorrelation)
    std::vector<double> white_noise;
    white_noise.reserve(200);
    for (int i = 0; i < 200; ++i) {
        white_noise.push_back(normal(rng));
    }
    auto acf_white = acf(white_noise, 20);
    auto sig_white = identify_significant_lags(acf_white, static_cast<int>(white_noise.size()));

    // White noise should have few significant lags (some may occur by chance)
    assert(sig_white.size() < 5);

    std::cout << "autocorrelation_function.cpp PASS" << std::endl;
    return 0;
}
