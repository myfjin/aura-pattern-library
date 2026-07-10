// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Matrix factorization via stochastic gradient descent.
 *
 * Oracle asserts:
 *   final_rmse < 0.5
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <random>
#include <map>
#include <utility>

std::tuple<std::vector<std::vector<double>>, std::vector<std::vector<double>>, double> matrix_factorization_sgd(
    const std::map<std::pair<int, int>, double>& ratings,
    int num_users,
    int num_items,
    int rank = 2,
    double learning_rate = 0.01,
    double lambda_reg = 0.1,
    int epochs = 500) {

    std::mt19937_64 rng(42);
    std::normal_distribution<double> nd(0.0, 0.1);

    std::vector<std::vector<double>> U(num_users, std::vector<double>(rank));
    std::vector<std::vector<double>> V(num_items, std::vector<double>(rank));
    for (int u = 0; u < num_users; ++u)
        for (int f = 0; f < rank; ++f) U[u][f] = nd(rng);
    for (int i = 0; i < num_items; ++i)
        for (int f = 0; f < rank; ++f) V[i][f] = nd(rng);

    for (int epoch = 0; epoch < epochs; ++epoch) {
        for (const auto& kv : ratings) {
            int u = kv.first.first, i = kv.first.second;
            double rating = kv.second;
            double pred = 0.0;
            for (int f = 0; f < rank; ++f) pred += U[u][f] * V[i][f];
            double error = rating - pred;
            for (int f = 0; f < rank; ++f) {
                double dU = -error * V[i][f] + lambda_reg * U[u][f];
                double dV = -error * U[u][f] + lambda_reg * V[i][f];
                U[u][f] -= learning_rate * dU;
                V[i][f] -= learning_rate * dV;
            }
        }
    }

    double total_error = 0.0;
    int count = 0;
    for (const auto& kv : ratings) {
        int u = kv.first.first, i = kv.first.second;
        double pred = 0.0;
        for (int f = 0; f < rank; ++f) pred += U[u][f] * V[i][f];
        total_error += (kv.second - pred) * (kv.second - pred);
        ++count;
    }
    double rmse = std::sqrt(total_error / count);
    return {U, V, rmse};
}

int main() {
    std::map<std::pair<int, int>, double> ratings = {
        {{0, 0}, 3.545038800639072}, {{0, 1}, 2.9011197346232867}, {{0, 2}, 4.341624017502385}, {{0, 3}, 3.484482950778373},
        {{1, 0}, 3.363938167775254}, {{1, 1}, 2.8243307985837682}, {{1, 2}, 4.0807804775131835}, {{1, 3}, 3.476041457453464},
        {{2, 0}, 4.677818189554653}, {{2, 1}, 3.8174619810024026}, {{2, 2}, 5.0}, {{2, 3}, 4.672658744878833},
        {{3, 0}, 3.9989360646547163}, {{3, 1}, 3.0940015447269107}, {{3, 2}, 4.539139969426348}, {{3, 3}, 3.976038322972519},
        {{4, 0}, 3.1914376119909504}, {{4, 1}, 2.7818147975256826}, {{4, 2}, 4.003409712918887}, {{4, 3}, 3.250085058184115}
    };

    auto [U, V, final_rmse] = matrix_factorization_sgd(ratings, 5, 4, 2, 0.05, 0.01, 500);
    assert(final_rmse < 0.5);

    std::cout << "matrix_factorization_sgd.cpp PASS: rmse=" << final_rmse << std::endl;
    return 0;
}
