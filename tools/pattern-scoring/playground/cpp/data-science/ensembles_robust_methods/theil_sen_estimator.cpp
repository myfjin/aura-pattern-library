// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Theil-Sen robust linear regression (median of pairwise slopes).
 * Estimates the slope as the median of all pairwise point slopes and the
 * intercept as the median of per-point intercepts, giving ~29% breakdown against
 * outliers. Use for a simple regression when up to a quarter of the points may be
 * corrupted. Oracle: with 20% gross-outlier y values added, the Theil-Sen slope
 * error is smaller than the OLS slope error.
 */
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <functional>
#include <iostream>
#include <iomanip>
#include <map>
#include <numeric>
#include <random>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;

// Theil-Sen median-of-slopes robust regression vs OLS.

static uint64_t rng_state = 0x123456789abcdef0ULL;
static double uniform01() {
    rng_state = rng_state * 6364136223846793005ULL + 1442695040888963407ULL;
    return ((rng_state >> 11) & 0x1FFFFFFFFFFFFFULL) / 9007199254740992.0;
}
static double uniform(double a, double b) { return a + (b - a) * uniform01(); }
static double gauss(double mean, double std) {
    double u1 = uniform01(), u2 = uniform01();
    while (u1 == 0.0) u1 = uniform01();
    double mag = std * sqrt(-2.0 * log(u1));
    return mean + mag * cos(2.0 * M_PI * u2);
}

pair<double,double> theil_sen_estimator(const vector<double>& X, const vector<double>& y) {
    size_t n = X.size();
    if (n < 2) return n==0 ? make_pair(0.0,0.0) : make_pair(0.0,y[0]);
    vector<double> slopes;
    for (size_t i=0;i<n;++i)
        for (size_t j=i+1;j<n;++j)
            if (fabs(X[j]-X[i]) > 1e-10)
                slopes.push_back((y[j]-y[i])/(X[j]-X[i]));
    if (slopes.empty()) return {0.0, 0.0};
    sort(slopes.begin(), slopes.end());
    double m = slopes[slopes.size()/2];
    vector<double> intercepts(n);
    for (size_t i=0;i<n;++i) intercepts[i] = y[i] - m*X[i];
    sort(intercepts.begin(), intercepts.end());
    double b = intercepts[intercepts.size()/2];
    return {m,b};
}

pair<double,double> ordinary_least_squares(const vector<double>& X, const vector<double>& y) {
    size_t n = X.size();
    double mx=0, my=0;
    for (size_t i=0;i<n;++i){ mx += X[i]; my += y[i]; }
    mx /= (double)n; my /= (double)n;
    double num=0, den=0;
    for (size_t i=0;i<n;++i){ num += (X[i]-mx)*(y[i]-my); den += (X[i]-mx)*(X[i]-mx); }
    if (den < 1e-10) return {0.0, my};
    double m = num/den;
    return {m, my - m*mx};
}

int main() {
    const int n_inliers = 50;
    vector<double> X, y;
    for (int i=0;i<n_inliers;++i) {
        double x = uniform(0,10);
        double true_y = 1.5*x + 2.0;
        X.push_back(x);
        y.push_back(true_y + gauss(0,0.5));
    }
    int n_outliers = n_inliers/4;
    for (int i=0;i<n_outliers;++i) {
        X.push_back(uniform(0,10));
        y.push_back(uniform(-20,40));
    }
    auto [m_ols, b_ols] = ordinary_least_squares(X,y);
    auto [m_ts, b_ts] = theil_sen_estimator(X,y);
    double ols_err = fabs(m_ols - 1.5);
    double ts_err = fabs(m_ts - 1.5);
    printf("ols_slope_error=%.4f ts_slope_error=%.4f\n", ols_err, ts_err);
    assert(ts_err < ols_err);
    puts("PASS");
    return 0;
}
