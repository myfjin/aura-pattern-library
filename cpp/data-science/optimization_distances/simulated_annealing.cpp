// Simulated Annealing.
// C++17 self-contained implementation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <tuple>
#include <utility>

inline double rastrigin1D(double x) {
    return (x - 3.0) * (x - 3.0) + 10.0 * (1.0 - std::cos(2.0 * M_PI * (x - 3.0)));
}

inline double rastrigin2D(double x, double y) {
    return rastrigin1D(x) + rastrigin1D(y);
}

std::tuple<double, double, double> simulatedAnnealing(
    double xInit, double yInit,
    double (*func)(double, double),
    double boundsLow, double boundsHigh,
    double initialTemp,
    double coolingRate,
    int maxIters,
    std::mt19937& rng) {

    double x = xInit, y = yInit;
    double currentValue = func(x, y);
    double bestX = x, bestY = y, bestValue = currentValue;
    double temperature = initialTemp;
    std::uniform_real_distribution<double> uniform(0.0, 1.0);

    for (int iter = 0; iter < maxIters; ++iter) {
        double scale = 0.5 * temperature;
        std::normal_distribution<double> noise(0.0, scale);

        double xNew = x + noise(rng);
        double yNew = y + noise(rng);

        xNew = std::max(boundsLow, std::min(boundsHigh, xNew));
        yNew = std::max(boundsLow, std::min(boundsHigh, yNew));

        double newValue = func(xNew, yNew);
        double delta = newValue - currentValue;

        if (delta < 0.0 || uniform(rng) < std::exp(-delta / temperature)) {
            x = xNew;
            y = yNew;
            currentValue = newValue;

            if (currentValue < bestValue) {
                bestX = x;
                bestY = y;
                bestValue = currentValue;
            }
        }

        temperature *= coolingRate;
        if (temperature < 1e-8) break;
    }

    return { bestX, bestY, bestValue };
}

int main() {
    std::mt19937 rng(42);

    double xInit = 0.0;
    double yInit = 0.0;
    double boundsLow = -5.0;
    double boundsHigh = 8.0;

    auto [bestX, bestY, bestValue] = simulatedAnnealing(
        xInit, yInit, rastrigin2D,
        boundsLow, boundsHigh,
        /*initialTemp=*/50.0,
        /*coolingRate=*/0.995,
        /*maxIters=*/20000,
        rng);

    constexpr double tolerance = 2.0;
    assert(bestValue < tolerance);

    double distanceFromOptimum = std::sqrt((bestX - 3.0) * (bestX - 3.0) +
                                           (bestY - 3.0) * (bestY - 3.0));
    assert(distanceFromOptimum < 2.0);

    std::cout << "simulated_annealing PASS (bestValue=" << bestValue
              << ", distanceFromOpt=" << distanceFromOptimum << ")\n";
    return 0;
}
