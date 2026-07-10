// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * 2D grid density binning: partition points into cells, count per-cell density.
 */

#include <vector>
#include <utility>
#include <map>
#include <cmath>
#include <random>
#include <cassert>
#include <iostream>

std::tuple<std::map<std::pair<int, int>, int>, double, double> grid_density_binning(
    const std::vector<std::pair<double, double>>& points, double grid_size) {
    if (points.empty()) return {{}, 1e18, -1e18};

    double minx = points[0].first, miny = points[0].second;
    double maxx = points[0].first, maxy = points[0].second;
    for (const auto& p : points) {
        if (p.first < minx) minx = p.first;
        if (p.first > maxx) maxx = p.first;
        if (p.second < miny) miny = p.second;
        if (p.second > maxy) maxy = p.second;
    }

    std::map<std::pair<int, int>, int> cell_counts;
    for (const auto& [x, y] : points) {
        int cell_x = static_cast<int>((x - minx) / grid_size);
        int cell_y = static_cast<int>((y - miny) / grid_size);
        cell_counts[{cell_x, cell_y}]++;
    }

    return {cell_counts, minx, miny};
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform(0.0, 10.0);

    std::vector<std::pair<double, double>> points;
    for (int i = 0; i < 100; ++i) {
        points.push_back({uniform(rng), uniform(rng)});
    }

    auto [cell_counts, minx, miny] = grid_density_binning(points, 2.0);

    int total = 0;
    for (const auto& kv : cell_counts) total += kv.second;
    assert(total == 100);

    for (const auto& kv : cell_counts) assert(kv.second > 0);
    assert(cell_counts.size() >= 2);
    assert(cell_counts.size() <= 100);

    // Plant a hotspot
    std::vector<std::pair<double, double>> cluster_points;
    std::uniform_real_distribution<double> small(-0.3, 0.3);
    for (int i = 0; i < 30; ++i) {
        cluster_points.push_back({5.0 + small(rng), 5.0 + small(rng)});
    }
    for (int i = 0; i < 20; ++i) {
        cluster_points.push_back({uniform(rng), uniform(rng)});
    }

    auto [cell_counts_cluster, _, __] = grid_density_binning(cluster_points, 1.0);
    int total_cluster = 0;
    for (const auto& kv : cell_counts_cluster) total_cluster += kv.second;
    assert(total_cluster == 50);

    int max_count = 0;
    for (const auto& kv : cell_counts_cluster) max_count = std::max(max_count, kv.second);
    assert(max_count >= 5);

    int high_count_cells = 0;
    for (const auto& kv : cell_counts_cluster) {
        if (kv.second >= 3) high_count_cells++;
    }
    assert(high_count_cells <= 8);

    auto [cell_counts_fine, ___, ____] = grid_density_binning(points, 1.0);
    int total_fine = 0;
    for (const auto& kv : cell_counts_fine) total_fine += kv.second;
    assert(total_fine == 100);
    assert(cell_counts_fine.size() > cell_counts.size());

    std::cout << "grid_density_binning.cpp PASS" << std::endl;
    return 0;
}
