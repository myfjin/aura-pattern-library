// Seasonal Decomposition (naive additive)
// C++17 self-contained implementation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <vector>

std::vector<double> centeredMovingAverage(const std::vector<double>& series, int window) {
    int n = static_cast<int>(series.size());
    std::vector<double> result(n, std::numeric_limits<double>::quiet_NaN());
    int half_w = window / 2;
    for (int i = half_w; i < n - half_w; ++i) {
        double sum = 0.0;
        for (int j = i - half_w; j <= i + half_w; ++j) {
            sum += series[j];
        }
        result[i] = sum / window;
    }
    return result;
}

struct Decomposition {
    std::vector<double> trend;
    std::vector<double> seasonal;
    std::vector<double> residual;
};

Decomposition naiveSeasonalDecomposition(const std::vector<double>& series, int period) {
    int n = static_cast<int>(series.size());
    assert(period >= 2 && period <= n / 2);

    std::vector<double> trend = centeredMovingAverage(series, period);

    std::vector<std::vector<double>> seasonalValues(period);
    for (int i = 0; i < n; ++i) {
        if (!std::isnan(trend[i])) {
            seasonalValues[i % period].push_back(series[i] - trend[i]);
        }
    }

    std::vector<double> seasonalMeans(period, 0.0);
    for (int season = 0; season < period; ++season) {
        if (!seasonalValues[season].empty()) {
            double sum = 0.0;
            for (double v : seasonalValues[season]) sum += v;
            seasonalMeans[season] = sum / seasonalValues[season].size();
        }
    }

    Decomposition result;
    result.trend = trend;
    result.seasonal.reserve(n);
    result.residual.reserve(n);

    for (int i = 0; i < n; ++i) {
        double s = seasonalMeans[i % period];
        result.seasonal.push_back(s);
        if (!std::isnan(trend[i])) {
            result.residual.push_back(series[i] - trend[i] - s);
        } else {
            result.residual.push_back(std::numeric_limits<double>::quiet_NaN());
        }
    }

    return result;
}

double varianceExcludingNaN(const std::vector<double>& values) {
    std::vector<double> clean;
    for (double v : values) {
        if (!std::isnan(v)) clean.push_back(v);
    }
    if (clean.size() < 2) return 0.0;
    double mean = 0.0;
    for (double v : clean) mean += v;
    mean /= clean.size();
    double var = 0.0;
    for (double v : clean) var += (v - mean) * (v - mean);
    return var / clean.size();
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> noise(0.0, 0.5);

    constexpr int n = 120;
    std::vector<double> series;
    series.reserve(n);
    for (int i = 0; i < n; ++i) {
        double trend = 10.0 + 0.1 * i;
        double seasonal = 5.0 * ((i % 12) < 6 ? 1.0 : -1.0);
        series.push_back(trend + seasonal + noise(rng));
    }

    auto dec = naiveSeasonalDecomposition(series, 12);

    assert(static_cast<int>(dec.trend.size()) == n);
    assert(static_cast<int>(dec.seasonal.size()) == n);
    assert(static_cast<int>(dec.residual.size()) == n);

    double trendVar = varianceExcludingNaN(dec.trend);

    double seriesMean = 0.0;
    for (double x : series) seriesMean += x;
    seriesMean /= n;
    double seriesVar = 0.0;
    for (double x : series) seriesVar += (x - seriesMean) * (x - seriesMean);
    seriesVar /= n;

    assert(trendVar < seriesVar);

    // Seasonal periodicity: between-season variation should exist.
    std::vector<std::vector<double>> seasonGroups(12);
    for (int i = 0; i < n; ++i) {
        seasonGroups[i % 12].push_back(dec.seasonal[i]);
    }

    double seasonalMean = 0.0;
    for (double s : dec.seasonal) seasonalMean += s;
    seasonalMean /= n;

    double betweenSeasonVar = 0.0;
    for (int i = 0; i < 12; ++i) {
        double groupMean = 0.0;
        for (double v : seasonGroups[i]) groupMean += v;
        groupMean /= seasonGroups[i].size();
        double diff = groupMean - seasonalMean;
        betweenSeasonVar += diff * diff;
    }
    betweenSeasonVar /= 12.0;

    assert(betweenSeasonVar > 0.0);

    double residualVar = varianceExcludingNaN(dec.residual);
    assert(residualVar < seriesVar);

    std::cout << "seasonal_decomposition PASS (trendVar=" << trendVar
              << ", residualVar=" << residualVar << ")\n";
    return 0;
}
