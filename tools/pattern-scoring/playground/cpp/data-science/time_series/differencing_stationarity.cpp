// Differencing for Stationarity — C++17 port.
// First-difference a random walk and a trend; check stationarity diagnostics.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

static vector<double> first_difference(const vector<double>& series) {
    vector<double> out;
    for (size_t i = 1; i < series.size(); ++i)
        out.push_back(series[i] - series[i - 1]);
    return out;
}

static double augmented_dickey_fuller_simple(const vector<double>& series) {
    int n = static_cast<int>(series.size());
    int half = n / 2;
    double mean1 = 0, mean2 = 0;
    for (int i = 0; i < half; ++i) mean1 += series[i];
    for (int i = half; i < n; ++i) mean2 += series[i];
    mean1 /= half; mean2 /= half;
    double var1 = 0, var2 = 0;
    for (int i = 0; i < half; ++i) var1 += pow(series[i] - mean1, 2);
    for (int i = half; i < n; ++i) var2 += pow(series[i] - mean2, 2);
    var1 /= half; var2 /= half;
    if (var1 < 1e-10 || var2 < 1e-10) return 0.0;
    return var2 / var1;
}

static double compute_mean_drift(const vector<double>& series, int window) {
    if (static_cast<int>(series.size()) < 2 * window)
        throw runtime_error("Series too short");
    double first_mean = 0, last_mean = 0;
    for (int i = 0; i < window; ++i) first_mean += series[i];
    for (size_t i = series.size() - window; i < series.size(); ++i) last_mean += series[i];
    first_mean /= window; last_mean /= window;
    return fabs(last_mean - first_mean);
}

int main() {
    mt19937 rng(42);
    normal_distribution<double> gauss(0.0, 1.0);

    // Random walk
    vector<double> series_rw = {0.0};
    for (int i = 0; i < 150; ++i)
        series_rw.push_back(series_rw.back() + gauss(rng));
    auto diff_rw = first_difference(series_rw);

    double vr_rw = augmented_dickey_fuller_simple(series_rw);
    double vr_diff = augmented_dickey_fuller_simple(diff_rw);
    assert(vr_diff < vr_rw);

    // Linear trend
    vector<double> series_trend;
    normal_distribution<double> noise(0.0, 0.5);
    for (int i = 0; i < 150; ++i)
        series_trend.push_back(5.0 + 0.3 * i + noise(rng));
    auto diff_trend = first_difference(series_trend);

    double drift_orig = compute_mean_drift(series_trend, 20);
    double drift_diff = compute_mean_drift(diff_trend, 20);
    assert(drift_diff < drift_orig);

    assert(diff_rw.size() == series_rw.size() - 1);
    assert(diff_trend.size() == series_trend.size() - 1);

    double diff_mean = 0;
    for (double x : diff_rw) diff_mean += x;
    diff_mean /= diff_rw.size();
    assert(fabs(diff_mean) < 1.0);

    double diff_trend_mean = 0;
    for (double x : diff_trend) diff_trend_mean += x;
    diff_trend_mean /= diff_trend.size();
    assert(fabs(diff_trend_mean) < 0.5);

    cout << "differencing_stationarity.cpp PASS\n";
    return 0;
}
