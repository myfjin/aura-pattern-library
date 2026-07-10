// Rolling Z-Score Anomaly Detection.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <set>
#include <cassert>

std::pair<std::vector<double>, std::vector<int>> rollingZscore(const std::vector<double>& series,
                                                          int window, double threshold = 3.0) {
    if (window < 2 || window > static_cast<int>(series.size()))
        throw std::invalid_argument("window must be between 2 and len(series)");

    std::vector<double> z_scores;
    std::vector<int> anomaly_indices;
    for (size_t i = 0; i < series.size(); ++i) {
        size_t start = (i >= static_cast<size_t>(window - 1)) ? i - window + 1 : 0;
        size_t end = i + 1;
        double sum = 0.0;
        for (size_t j = start; j < end; ++j) sum += series[j];
        double mean_val = sum / (end - start);

        double variance = 0.0;
        for (size_t j = start; j < end; ++j)
            variance += (series[j] - mean_val) * (series[j] - mean_val);
        variance /= (end - start);
        double std_val = std::sqrt(variance);

        double z_score = std_val < 1e-10 ? 0.0 : (series[i] - mean_val) / std_val;
        z_scores.push_back(z_score);
        if (std::abs(z_score) > threshold)
            anomaly_indices.push_back(static_cast<int>(i));
    }
    return {z_scores, anomaly_indices};
}

int main() {
    std::mt19937 gen(42);
    std::normal_distribution<double> gauss(10.0, 1.0);

    std::vector<double> series(100);
    for (double& v : series) v = gauss(gen);

    std::vector<int> spike_indices = {20, 45, 75};
    for (int idx : spike_indices) series[idx] += 10.0;

    auto [z_scores, anomalies] = rollingZscore(series, 10, 2.5);

    assert(!anomalies.empty());
    for (int spike_idx : spike_indices) {
        bool found = false;
        for (int a : anomalies)
            if (std::abs(a - spike_idx) <= 2) { found = true; break; }
        assert(found);
    }

    std::set<int> anomaly_set(anomalies.begin(), anomalies.end());
    std::vector<double> normal_z, anomaly_z;
    for (size_t i = 0; i < z_scores.size(); ++i) {
        if (anomaly_set.count(static_cast<int>(i)))
            anomaly_z.push_back(z_scores[i]);
        else
            normal_z.push_back(z_scores[i]);
    }
    double avg_normal = 0.0;
    for (double z : normal_z) avg_normal += std::abs(z);
    avg_normal /= normal_z.size();

    double avg_anomaly = 0.0;
    for (double z : anomaly_z) avg_anomaly += std::abs(z);
    avg_anomaly /= anomaly_z.size();

    assert(avg_normal < 1.5);
    assert(avg_anomaly > 2.0);

    std::cout << "ROLLING_ZSCORE_ANOMALY PASS\n";
    return 0;
}
