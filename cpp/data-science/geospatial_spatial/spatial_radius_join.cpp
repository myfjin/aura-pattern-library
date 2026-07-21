// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Spatial radius join: for each center, find all points within a given radius.
 * Hashes points into a uniform grid keyed by (x/grid_size, y/grid_size), then
 * probes only the center's own bucket plus its 8 neighbours instead of scanning
 * every point. Use when you need range-neighbour pairs over a 2-D point set and
 * a full O(centers*points) scan is too slow. Guarantee (proven in main): with
 * grid_size >= radius the grid result is IDENTICAL to brute force AND performs
 * strictly fewer distance checks — correctness is not traded for speed.
 */
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <map>
#include <random>
#include <utility>
#include <vector>

// Radius join via grid bucketing.

using Point = std::pair<double, double>;
using Pair = std::pair<int, int>;

std::pair<int, int> bucket_key(const Point& p, double grid_size) {
    return {static_cast<int>(p.first / grid_size), static_cast<int>(p.second / grid_size)};
}

double euclidean(const Point& a, const Point& b) {
    double dx = a.first - b.first;
    double dy = a.second - b.second;
    return std::sqrt(dx * dx + dy * dy);
}

std::pair<std::vector<Pair>, int> spatial_radius_join(const std::vector<Point>& points,
                                                   const std::vector<Point>& centers,
                                                   double radius, double grid_size) {
    std::map<std::pair<int, int>, std::vector<int>> point_buckets;
    for (int i = 0; i < static_cast<int>(points.size()); ++i) {
        point_buckets[bucket_key(points[i], grid_size)].push_back(i);
    }

    std::vector<Pair> result;
    int dist_checks = 0;

    for (int ci = 0; ci < static_cast<int>(centers.size()); ++ci) {
        auto cb = bucket_key(centers[ci], grid_size);
        for (int dx = -1; dx <= 1; ++dx) {
            for (int dy = -1; dy <= 1; ++dy) {
                auto key = std::make_pair(cb.first + dx, cb.second + dy);
                auto it = point_buckets.find(key);
                if (it == point_buckets.end()) continue;
                for (int pi : it->second) {
                    ++dist_checks;
                    if (euclidean(points[pi], centers[ci]) <= radius) {
                        result.emplace_back(ci, pi);
                    }
                }
            }
        }
    }
    return {result, dist_checks};
}

int main() {
    std::mt19937 gen(42);
    std::uniform_real_distribution<double> dist(0.0, 100.0);

    const int n_points = 200;
    const int n_centers = 20;
    std::vector<Point> points;
    for (int i = 0; i < n_points; ++i) points.emplace_back(dist(gen), dist(gen));
    std::vector<Point> centers;
    for (int i = 0; i < n_centers; ++i) centers.emplace_back(dist(gen), dist(gen));

    double radius = 10.0;
    double grid_size = 15.0;

    auto [grid_result, grid_checks] = spatial_radius_join(points, centers, radius, grid_size);

    std::vector<Pair> bf_result;
    int bf_checks = 0;
    for (int ci = 0; ci < n_centers; ++ci) {
        for (int pi = 0; pi < n_points; ++pi) {
            ++bf_checks;
            if (euclidean(points[pi], centers[ci]) <= radius) {
                bf_result.emplace_back(ci, pi);
            }
        }
    }

    assert(grid_result.size() == bf_result.size());
    std::sort(grid_result.begin(), grid_result.end());
    std::sort(bf_result.begin(), bf_result.end());
    assert(grid_result == bf_result);
    assert(grid_checks < bf_checks);

    std::cout << "PASS" << std::endl;
    return 0;
}
