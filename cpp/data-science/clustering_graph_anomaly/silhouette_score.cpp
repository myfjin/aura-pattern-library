// Silhouette Score from scratch.
// C++17 self-contained implementation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <random>
#include <set>
#include <vector>

double euclideanDistance(const std::vector<double>& p1,
                         const std::vector<double>& p2) {
    double sum = 0.0;
    for (size_t i = 0; i < p1.size(); ++i) {
        double diff = p1[i] - p2[i];
        sum += diff * diff;
    }
    return std::sqrt(sum);
}

double silhouetteScore(const std::vector<std::vector<double>>& points,
                         const std::vector<int>& labels) {
    std::set<int> uniqueLabels(labels.begin(), labels.end());
    if (uniqueLabels.size() < 2) return 0.0;

    std::vector<double> silhouetteScores;

    for (size_t i = 0; i < points.size(); ++i) {
        int currentCluster = labels[i];

        // a: average distance to points in same cluster
        std::vector<size_t> sameCluster;
        for (size_t j = 0; j < points.size(); ++j) {
            if (labels[j] == currentCluster) sameCluster.push_back(j);
        }

        double a = 0.0;
        if (sameCluster.size() > 1) {
            for (size_t j : sameCluster) {
                if (j != i) a += euclideanDistance(points[i], points[j]);
            }
            a /= static_cast<double>(sameCluster.size() - 1);
        }

        // b: minimum average distance to points in other clusters
        double b = std::numeric_limits<double>::infinity();
        for (int clusterId : uniqueLabels) {
            if (clusterId == currentCluster) continue;
            std::vector<size_t> otherCluster;
            for (size_t j = 0; j < points.size(); ++j) {
                if (labels[j] == clusterId) otherCluster.push_back(j);
            }
            double avgDist = 0.0;
            for (size_t j : otherCluster) {
                avgDist += euclideanDistance(points[i], points[j]);
            }
            avgDist /= static_cast<double>(otherCluster.size());
            b = std::min(b, avgDist);
        }

        double denom = std::max(a, b);
        double s = denom > 0.0 ? (b - a) / denom : 0.0;
        silhouetteScores.push_back(s);
    }

    double sum = 0.0;
    for (double s : silhouetteScores) sum += s;
    return sum / silhouetteScores.size();
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> smallNoise(0.0, 0.4);

    // Two well-separated clusters
    std::vector<std::vector<double>> points;
    std::vector<int> correctLabels;
    for (int i = 0; i < 15; ++i) {
        points.push_back({ smallNoise(rng), smallNoise(rng) });
        correctLabels.push_back(0);
    }
    for (int i = 0; i < 15; ++i) {
        points.push_back({ 5.0 + smallNoise(rng), 5.0 + smallNoise(rng) });
        correctLabels.push_back(1);
    }

    std::vector<int> wrongLabels = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

    double correctScore = silhouetteScore(points, correctLabels);
    double wrongScore = silhouetteScore(points, wrongLabels);

    assert(correctScore >= 0.5);
    assert(correctScore > 0.0);
    assert(wrongScore >= 0.5);

    std::vector<int> scrambledLabels = correctLabels;
    std::shuffle(scrambledLabels.begin(), scrambledLabels.end(), rng);
    double scrambledScore = silhouetteScore(points, scrambledLabels);
    assert(scrambledScore < 0.5);

    std::cout << "silhouette_score PASS (correct=" << correctScore
              << ", wrong=" << wrongScore << ", scrambled=" << scrambledScore << ")\n";
    return 0;
}
