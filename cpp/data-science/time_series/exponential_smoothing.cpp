// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/* Exponential Smoothing: SES and Holt's double exponential smoothing.
 * Core claim: smoothed series less variable than raw, Holt detects trend,
 *             forecasts have correct length and Holt rises with trend.
 */
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <vector>

std::vector<double> ses(const std::vector<double>& series, double alpha) {
    std::vector<double> sm(series);
    for (size_t i = 1; i < series.size(); ++i)
        sm[i] = alpha * series[i] + (1.0 - alpha) * sm[i-1];
    return sm;
}

std::pair<std::vector<double>, std::vector<double>> holt(
    const std::vector<double>& series, double alpha, double beta
) {
    std::vector<double> levels, trends;
    double level = series[0];
    double trend = (series.size() > 1) ? series[1] - series[0] : 0.0;
    levels.push_back(level); trends.push_back(trend);
    for (size_t i = 1; i < series.size(); ++i) {
        double new_level = alpha * series[i] + (1.0 - alpha) * (level + trend);
        double new_trend = beta * (new_level - level) + (1.0 - beta) * trend;
        level = new_level; trend = new_trend;
        levels.push_back(level); trends.push_back(trend);
    }
    return {levels, trends};
}

double variance(const std::vector<double>& v) {
    double m = 0.0; for (double x : v) m += x; m /= v.size();
    double s = 0.0; for (double x : v) s += (x-m)*(x-m); return s / v.size();
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> noise(0.0, 0.5);
    std::vector<double> series;
    double val = 10.0;
    for (int i = 0; i < 50; ++i) {
        val += 0.3 + noise(gen);
        series.push_back(val);
    }

    // SES
    auto smoothed = ses(series, 0.2);
    assert(smoothed.size() == series.size());
    assert(smoothed[0] == series[0]);
    assert(variance(smoothed) < variance(series));

    // Holt's
    auto [levels, trends] = holt(series, 0.2, 0.1);
    assert(levels.size() == series.size());
    assert(trends.size() == series.size());
    assert(levels[0] == series[0]);

    // avg_trend > 0 (oracle's check, not just last trend)
    double avg_trend = 0.0;
    for (double t : trends) avg_trend += t;
    avg_trend /= trends.size();
    assert(avg_trend > 0.0);

    // Forecasts
    std::vector<double> ses_fcst(5, smoothed.back());
    std::vector<double> holt_fcst;
    for (int h = 0; h < 5; ++h)
        holt_fcst.push_back(levels.back() + trends.back() * (h + 1));

    assert(ses_fcst.size() == 5);
    assert(holt_fcst.size() == 5);
    assert(holt_fcst.back() > holt_fcst.front());  // trend-aware forecast rises

    std::cout << "exponential_smoothing.cpp PASS" << std::endl;
    return 0;
}
