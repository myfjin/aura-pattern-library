// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Greedy hill climbing (step to the first neighbor that improves, stop at a local
 * optimum) wrapped in random restarts from uniformly-sampled start points, keeping the
 * best summit found. The landscape sin(5*pi*x)*cos(5*pi*y) + 0.1*(x^2+y^2) is riddled
 * with local maxima that trap a single climb.
 * Use when maximizing a rugged multimodal function where one greedy run gets stuck.
 * Guarantees: the multi-restart result is no worse than a single climb (within
 * tolerance) and clears a fixed quality floor the single run can miss.
 */

#include <cmath>
#include <tuple>
#include <random>
#include <cassert>
#include <iostream>
#include <utility>
#include <vector>
double rugged_landscape(double x, double y) {
    return std::sin(5.0 * M_PI * x) * std::cos(5.0 * M_PI * y) + 0.1 * (x * x + y * y);
}

std::tuple<double, double, double> hill_climbing(double x, double y, double step_size = 0.05,
                                                   double tolerance = 1e-4, int max_iters = 1000) {
    double best_x = x, best_y = y;
    double best_value = rugged_landscape(x, y);

    for (int iter = 0; iter < max_iters; ++iter) {
        std::vector<std::pair<double, double>> candidates = {
            {best_x + step_size, best_y},
            {best_x - step_size, best_y},
            {best_x, best_y + step_size},
            {best_x, best_y - step_size}
        };

        bool improved = false;
        for (auto& [cx, cy] : candidates) {
            cx = std::max(-1.0, std::min(1.0, cx));
            cy = std::max(-1.0, std::min(1.0, cy));
            double cv = rugged_landscape(cx, cy);
            if (cv > best_value + tolerance) {
                best_x = cx;
                best_y = cy;
                best_value = cv;
                improved = true;
                break;
            }
        }

        if (!improved) break;
    }

    return {best_x, best_y, best_value};
}

std::tuple<double, double, double> hill_climbing_with_restarts(int num_restarts = 10,
                                                                 double step_size = 0.05,
                                                                 std::pair<double, double> bounds = {-1.0, 1.0}) {
    double global_best_x = 0.0, global_best_y = 0.0, global_best_value = -1e18;

    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform(bounds.first, bounds.second);

    for (int r = 0; r < num_restarts; ++r) {
        double x_init = uniform(rng);
        double y_init = uniform(rng);
        auto [x, y, value] = hill_climbing(x_init, y_init, step_size);
        if (value > global_best_value) {
            global_best_value = value;
            global_best_x = x;
            global_best_y = y;
        }
    }

    return {global_best_x, global_best_y, global_best_value};
}

int main() {
    auto [x_single, y_single, value_single] = hill_climbing(0.2, 0.3, 0.05);
    auto [x_restart, y_restart, value_restart] = hill_climbing_with_restarts(20, 0.05);

    assert(value_restart >= value_single - 1e-4);
    assert(value_restart > -0.5);

    std::cout << "hill_climbing_restarts.cpp PASS" << std::endl;
    return 0;
}
