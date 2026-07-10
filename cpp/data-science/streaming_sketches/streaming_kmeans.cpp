// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <cmath>
#include <limits>
#include <algorithm>
#include <random>
#include <cassert>

class StreamingKMeans {
public:
    int k;
    std::vector<std::vector<double>> centroids;
    std::vector<int> counts;

    explicit StreamingKMeans(int k = 3) : k(k) {}

    void initialize(const std::vector<std::vector<double>>& first_points) {
        centroids.assign(first_points.begin(), first_points.begin() + k);
        counts.assign(k, 1);
    }

    int nearest_centroid(const std::vector<double>& point) const {
        double best_dist = std::numeric_limits<double>::infinity();
        int best_idx = 0;
        for (size_t i = 0; i < centroids.size(); ++i) {
            double dist = 0.0;
            for (size_t j = 0; j < point.size(); ++j) {
                dist += (point[j] - centroids[i][j]) * (point[j] - centroids[i][j]);
            }
            if (dist < best_dist) {
                best_dist = dist;
                best_idx = i;
            }
        }
        return best_idx;
    }

    void process(const std::vector<double>& point) {
        if (centroids.empty()) return;
        int idx = nearest_centroid(point);
        double lr = 1.0 / static_cast<double>(counts[idx] + 1);
        for (size_t j = 0; j < point.size(); ++j) {
            centroids[idx][j] += lr * (point[j] - centroids[idx][j]);
        }
        counts[idx]++;
    }

    std::vector<std::vector<double>> get_centroids() const {
        std::vector<std::vector<double>> out;
        for (const auto& c : centroids) out.push_back(c);
        return out;
    }
};

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> gauss(0.0, 1.0);

    std::vector<std::vector<double>> stream;

    for (int t = 0; t < 150; ++t) {
        double drift = t * 0.01;
        std::vector<std::pair<double, double>> centers = {
            {0 + drift, 0 + drift},
            {3 + drift, 0 - drift},
            {0 - drift, 3 + drift}
        };
        for (int cluster_idx = 0; cluster_idx < 3; ++cluster_idx) {
            double cx = centers[cluster_idx].first;
            double cy = centers[cluster_idx].second;
            stream.push_back({cx + 0.3 * gauss(rng), cy + 0.3 * gauss(rng)});
        }
    }

    std::shuffle(stream.begin(), stream.end(), rng);

    StreamingKMeans kmeans(3);
    kmeans.initialize(stream);

    for (const auto& point : stream) kmeans.process(point);

    auto final_centroids = kmeans.get_centroids();

    std::vector<std::pair<double, double>> expected = {
        {1.5, 1.5}, {4.5, -1.5}, {-1.5, 4.5}
    };

    double total_dist = 0.0;
    for (const auto& e : expected) {
        double min_dist = std::numeric_limits<double>::infinity();
        for (const auto& c : final_centroids) {
            double d = std::sqrt((e.first - c[0]) * (e.first - c[0]) + (e.second - c[1]) * (e.second - c[1]));
            min_dist = std::min(min_dist, d);
        }
        total_dist += min_dist;
    }
    double avg_dist = total_dist / expected.size();

    assert(avg_dist < 2.0);

    std::cout << "streaming_kmeans: PASS" << std::endl;
    return 0;
}
