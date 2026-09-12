// Schelling Segregation: mild preference produces high global segregation.
// C++17 self-contained implementation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <utility>
#include <vector>

int main() {
    std::mt19937 rng(42);
    std::uniform_int_distribution<int> cell_dist(0, 9);

    constexpr int grid_size = 10;
    std::vector<std::vector<int>> grid(grid_size, std::vector<int>(grid_size, -1));

    int total_cells = grid_size * grid_size;
    int n_type0 = total_cells / 2;
    int n_type1 = total_cells - n_type0;

    std::vector<int> cells;
    cells.reserve(total_cells);
    for (int i = 0; i < n_type0; ++i) cells.push_back(0);
    for (int i = 0; i < n_type1; ++i) cells.push_back(1);

    std::shuffle(cells.begin(), cells.end(), rng);

    int idx = 0;
    for (int i = 0; i < grid_size; ++i) {
        for (int j = 0; j < grid_size; ++j) {
            grid[i][j] = cells[idx++];
        }
    }

    constexpr double preference_threshold = 0.3;

    auto get_neighbors = [&](int r, int c) {
        std::vector<int> neighbors;
        for (int dr = -1; dr <= 1; ++dr) {
            for (int dc = -1; dc <= 1; ++dc) {
                if (dr == 0 && dc == 0) continue;
                int nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < grid_size && nc >= 0 && nc < grid_size) {
                    neighbors.push_back(grid[nr][nc]);
                }
            }
        }
        return neighbors;
    };

    auto is_satisfied = [&](int r, int c) {
        auto neighbors = get_neighbors(r, c);
        if (neighbors.empty()) return true;
        int same_type = 0;
        for (int n : neighbors) {
            if (n == grid[r][c]) ++same_type;
        }
        return static_cast<double>(same_type) / neighbors.size() >= preference_threshold;
    };

    auto measure_segregation = [&]() {
        int total_same = 0;
        int total_neighbors = 0;
        for (int i = 0; i < grid_size; ++i) {
            for (int j = 0; j < grid_size; ++j) {
                auto neighbors = get_neighbors(i, j);
                if (!neighbors.empty()) {
                    int same = 0;
                    for (int n : neighbors) {
                        if (n == grid[i][j]) ++same;
                    }
                    total_same += same;
                    total_neighbors += static_cast<int>(neighbors.size());
                }
            }
        }
        return total_neighbors > 0 ? static_cast<double>(total_same) / total_neighbors : 0.0;
    };

    double initial_seg = measure_segregation();

    for (int iteration = 0; iteration < 100; ++iteration) {
        std::vector<std::pair<int, int>> unsatisfied;
        for (int i = 0; i < grid_size; ++i) {
            for (int j = 0; j < grid_size; ++j) {
                if (!is_satisfied(i, j)) {
                    unsatisfied.emplace_back(i, j);
                }
            }
        }
        if (unsatisfied.empty()) break;

        std::uniform_int_distribution<size_t> unsat_dist(0, unsatisfied.size() - 1);
        auto [ri, ci] = unsatisfied[unsat_dist(rng)];
        int agent_type = grid[ri][ci];

        for (int attempt = 0; attempt < 20; ++attempt) {
            int ni = cell_dist(rng);
            int nj = cell_dist(rng);
            if (grid[ni][nj] != agent_type) {
                std::swap(grid[ri][ci], grid[ni][nj]);
                break;
            }
        }
    }

    double final_seg = measure_segregation();

    assert(final_seg > 0.5);
    assert(final_seg >= initial_seg - 1e-12);

    std::cout << "schelling_segregation PASS (initial=" << initial_seg
              << ", final=" << final_seg << ")\n";
    return 0;
}
