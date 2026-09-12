// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Pairwise learning-to-rank. Builds one training example per ordered item pair (label =
 * which should rank higher) over feature differences, fits a logistic model by batch
 * gradient descent, then scores and sorts items; a numerically-stable sigmoid avoids
 * exp overflow. Kendall's tau measures agreement between predicted and true orderings.
 * Use to learn a ranking function from relative-order supervision.
 * Guarantees: on a monotone feature->rank toy set, predicted order attains Kendall tau
 * above 0.7 against the true order.
 */
#include <map>
#include <string>
#include <vector>
#include <cassert>

double sigmoid(double x) {
    if (x >= 0.0) {
        double z = std::exp(-x);
        return 1.0 / (1.0 + z);
    } else {
        double z = std::exp(x);
        return z / (1.0 + z);
    }
}

struct PairwiseResult {
    double weight;
    double bias;
};

PairwiseResult fit_logistic_pairwise(
    const std::vector<std::string>& items,
    const std::vector<double>& features,
    const std::vector<std::string>& true_order) {
    std::map<std::string, std::size_t> item_to_idx;
    for (std::size_t i = 0; i < items.size(); ++i) item_to_idx[items[i]] = i;

    std::map<std::string, std::size_t> true_ranks;
    for (std::size_t i = 0; i < true_order.size(); ++i) true_ranks[true_order[i]] = i;

    std::vector<std::pair<double, int>> examples;
    for (std::size_t i = 0; i < items.size(); ++i) {
        for (std::size_t j = 0; j < items.size(); ++j) {
            if (i == j) continue;
            int label = true_ranks[items[i]] < true_ranks[items[j]] ? 1 : 0;
            examples.emplace_back(features[i] - features[j], label);
        }
    }

    double weight = 0.0, bias = 0.0;
    double lr = 0.01;
    std::size_t n_examples = examples.size();
    for (int epoch = 0; epoch < 50; ++epoch) {
        double grad_w = 0.0, grad_b = 0.0;
        for (const auto& ex : examples) {
            double feat_diff = ex.first;
            int label = ex.second;
            double pred = sigmoid(weight * feat_diff + bias);
            double error = pred - static_cast<double>(label);
            grad_w += error * feat_diff;
            grad_b += error;
        }
        weight -= lr * grad_w / static_cast<double>(n_examples);
        bias -= lr * grad_b / static_cast<double>(n_examples);
    }
    return {weight, bias};
}

double kendall_tau(const std::vector<std::string>& ranking1,
                   const std::vector<std::string>& ranking2) {
    std::size_t n = ranking1.size();
    std::map<std::string, std::size_t> rank1, rank2;
    for (std::size_t i = 0; i < n; ++i) {
        rank1[ranking1[i]] = i;
        rank2[ranking2[i]] = i;
    }

    std::size_t concordant = 0, total_pairs = 0;
    for (std::size_t i = 0; i < n; ++i) {
        for (std::size_t j = i + 1; j < n; ++j) {
            const std::string& item_i = ranking1[i];
            const std::string& item_j = ranking1[j];
            bool order1 = rank1[item_i] < rank1[item_j];
            bool order2 = rank2[item_i] < rank2[item_j];
            if (order1 == order2) ++concordant;
            ++total_pairs;
        }
    }
    return 2.0 * static_cast<double>(concordant) / static_cast<double>(total_pairs) - 1.0;
}

int main() {
    std::vector<std::string> items = {"A", "B", "C", "D", "E"};
    std::vector<std::string> true_order = {"A", "B", "C", "D", "E"};
    std::vector<double> features = {5.0, 4.2, 3.1, 2.0, 1.0};

    auto result = fit_logistic_pairwise(items, features, true_order);

    std::vector<double> scores;
    scores.reserve(items.size());
    for (double feat : features) scores.push_back(result.weight * feat + result.bias);

    std::vector<std::string> predicted_order = items;
    std::sort(predicted_order.begin(), predicted_order.end(),
              [&scores, &items](const std::string& a, const std::string& b) {
                  std::size_t ia = std::distance(
                      items.begin(), std::find(items.begin(), items.end(), a));
                  std::size_t ib = std::distance(
                      items.begin(), std::find(items.begin(), items.end(), b));
                  return scores[ia] > scores[ib];
              });

    double tau = kendall_tau(true_order, predicted_order);

    assert(tau > 0.7);
    assert(predicted_order == true_order || tau > 0.5);

    std::printf("True order: [A, B, C, D, E] | Predicted: [");
    for (std::size_t i = 0; i < predicted_order.size(); ++i) {
        if (i) std::printf(", ");
        std::printf("%s", predicted_order[i].c_str());
    }
    std::printf("] | Weight=%.2f | Bias=%.2f | Kendall tau=%.2f | PASS\n",
                result.weight, result.bias, tau);
    return 0;
}
