// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * PageRank by power iteration on a directed graph. Each round redistributes rank along
 * out-edges scaled by the damping factor, adds a uniform teleport term, and spreads the
 * mass of dangling (out-degree-zero) nodes evenly so no probability leaks; iterates until
 * the L1 change falls below tol.
 * Use to score node importance in a link/citation/recommendation graph.
 * Guarantees: ranks form a probability distribution (sum ~ 1), every node gets positive
 * rank, and the hub node scores above the mean.
 */
#include <map>
#include <set>
#include <vector>
#include <cassert>
#include <cmath>
#include <cstdio>

std::map<int, double> pagerank_power_iteration(
    const std::map<int, std::vector<int>>& graph,
    double damping = 0.85,
    double tol = 1e-6,
    int max_iter = 100) {
    std::vector<int> nodes;
    {
        std::set<int> node_set;
        for (const auto& kv : graph) {
            node_set.insert(kv.first);
            for (int neighbor : kv.second) node_set.insert(neighbor);
        }
        nodes.assign(node_set.begin(), node_set.end());
    }
    std::size_t n = nodes.size();
    double init = 1.0 / static_cast<double>(n);

    std::map<int, double> rank;
    for (int node : nodes) rank[node] = init;

    std::vector<int> dangling;
    for (int node : nodes) {
        auto it = graph.find(node);
        if (it == graph.end() || it->second.empty()) dangling.push_back(node);
    }

    for (int iter = 0; iter < max_iter; ++iter) {
        std::map<int, double> new_rank;
        double teleport = (1.0 - damping) / static_cast<double>(n);
        for (int node : nodes) new_rank[node] = teleport;

        for (int node : nodes) {
            auto it = graph.find(node);
            if (it == graph.end()) continue;
            const std::vector<int>& neighbors = it->second;
            if (neighbors.empty()) continue;
            double share = rank[node] / static_cast<double>(neighbors.size());
            for (int neighbor : neighbors) {
                new_rank[neighbor] += damping * share;
            }
        }

        double dangling_sum = 0.0;
        for (int node : dangling) dangling_sum += rank[node];
        double dangling_share = damping * dangling_sum / static_cast<double>(n);
        for (int node : nodes) new_rank[node] += dangling_share;

        double diff = 0.0;
        for (int node : nodes) diff += std::abs(new_rank[node] - rank[node]);
        rank = new_rank;
        if (diff < tol) break;
    }

    return rank;
}

int main() {
    std::map<int, std::vector<int>> graph = {
        {0, {4}},
        {1, {0}},
        {2, {0}},
        {3, {0}},
        {4, {1, 2, 3}},
    };

    auto ranks = pagerank_power_iteration(graph, 0.85, 1e-6);

    double total = 0.0;
    for (const auto& kv : ranks) total += kv.second;
    assert(std::abs(total - 1.0) < 0.01);

    double mean_rank = total / static_cast<double>(ranks.size());
    assert(ranks[0] > mean_rank);

    for (const auto& kv : ranks) assert(kv.second > 0.0);

    std::printf("pagerank_power_iteration.cpp: ranks={%d: %.4f, %d: %.4f}, mean=%.4f PASS\n",
                0, ranks[0], 4, ranks[4], mean_rank);
    return 0;
}
