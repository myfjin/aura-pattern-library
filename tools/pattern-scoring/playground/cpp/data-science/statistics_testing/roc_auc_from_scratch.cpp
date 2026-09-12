// ROC Curve and AUC computation from scratch.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cassert>
#include <cmath>

std::vector<std::pair<double, double>> rocCurvePoints(const std::vector<int>& y_true,
                                                     const std::vector<double>& y_scores) {
    std::vector<std::pair<double, int>> paired;
    for (size_t i = 0; i < y_true.size(); ++i)
        paired.emplace_back(y_scores[i], y_true[i]);
    std::sort(paired.begin(), paired.end(), [](auto& a, auto& b) {
        return a.first > b.first;
    });

    int n_pos = 0;
    for (int v : y_true) n_pos += v;
    int n_neg = static_cast<int>(y_true.size()) - n_pos;
    if (n_pos == 0 || n_neg == 0) return {{0, 0}, {1, 1}};

    std::vector<std::pair<double, double>> points = {{0.0, 0.0}};
    int tp = 0, fp = 0;
    for (auto& [score, label] : paired) {
        (void)score;
        if (label == 1) ++tp; else ++fp;
        points.emplace_back(static_cast<double>(fp) / n_neg, static_cast<double>(tp) / n_pos);
    }
    return points;
}

double aucFromRanks(const std::vector<int>& y_true, const std::vector<double>& y_scores) {
    int n_pos = 0;
    for (int v : y_true) n_pos += v;
    int n_neg = static_cast<int>(y_true.size()) - n_pos;
    if (n_pos == 0 || n_neg == 0) return 0.5;

    int concordant = 0;
    for (size_t i = 0; i < y_true.size(); ++i)
        if (y_true[i] == 1)
            for (size_t j = 0; j < y_true.size(); ++j)
                if (y_true[j] == 0 && y_scores[i] > y_scores[j])
                    ++concordant;
    return static_cast<double>(concordant) / (n_pos * n_neg);
}

double aucTrapezoid(const std::vector<std::pair<double, double>>& roc_points) {
    if (roc_points.size() < 2) return 0.0;
    double auc = 0.0;
    for (size_t i = 1; i < roc_points.size(); ++i) {
        double fpr_prev = roc_points[i - 1].first, tpr_prev = roc_points[i - 1].second;
        double fpr_curr = roc_points[i].first, tpr_curr = roc_points[i].second;
        auc += (tpr_prev + tpr_curr) / 2.0 * (fpr_curr - fpr_prev);
    }
    return auc;
}

int main() {
    // Perfect separation
    std::vector<int> y_true_perfect = {0, 0, 0, 1, 1, 1};
    std::vector<double> y_scores_perfect = {0.1, 0.2, 0.3, 0.8, 0.9, 1.0};
    double auc_perfect_rank = aucFromRanks(y_true_perfect, y_scores_perfect);
    auto roc_perfect = rocCurvePoints(y_true_perfect, y_scores_perfect);
    double auc_perfect_trap = aucTrapezoid(roc_perfect);
    std::cout << "Perfect: rank=" << auc_perfect_rank << " trap=" << auc_perfect_trap << "\n";
    assert(std::abs(auc_perfect_rank - 1.0) < 0.01);
    assert(std::abs(auc_perfect_trap - 1.0) < 0.01);

    // Weak signal
    std::vector<int> y_true_weak = {0, 1, 0, 1, 0, 1, 1, 0};
    std::vector<double> y_scores_weak = {0.3, 0.4, 0.35, 0.6, 0.2, 0.65, 0.55, 0.5};
    double auc_weak_rank = aucFromRanks(y_true_weak, y_scores_weak);
    auto roc_weak = rocCurvePoints(y_true_weak, y_scores_weak);
    double auc_weak_trap = aucTrapezoid(roc_weak);
    std::cout << "Weak: rank=" << auc_weak_rank << " trap=" << auc_weak_trap << "\n";
    assert(0.4 < auc_weak_rank && auc_weak_rank < 1.0);
    assert(0.4 < auc_weak_trap && auc_weak_trap < 1.0);

    // Strong signal
    std::vector<int> y_true_strong = {0, 0, 0, 1, 1, 1, 0, 1};
    std::vector<double> y_scores_strong = {0.2, 0.1, 0.3, 0.9, 0.8, 0.85, 0.35, 0.7};
    double auc_strong_rank = aucFromRanks(y_true_strong, y_scores_strong);
    auto roc_strong = rocCurvePoints(y_true_strong, y_scores_strong);
    double auc_strong_trap = aucTrapezoid(roc_strong);
    std::cout << "Strong: rank=" << auc_strong_rank << " trap=" << auc_strong_trap << "\n";
    assert(0.75 <= auc_strong_rank && auc_strong_rank <= 1.0);
    assert(0.75 <= auc_strong_trap && auc_strong_trap <= 1.0);

    std::cout << "ROC_AUC_FROM_SCRATCH PASS\n";
    return 0;
}
