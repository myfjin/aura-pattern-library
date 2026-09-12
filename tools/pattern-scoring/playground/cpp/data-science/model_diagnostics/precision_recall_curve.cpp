// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Precision-recall curve and average precision for a binary classifier. Sweeps
 * every distinct score as a decision threshold, counting true/predicted positives
 * to produce (precision, recall) points, then integrates precision over recall by
 * the trapezoidal rule to get a single average-precision (AP) summary. Use to
 * judge ranking quality on imbalanced data, where PR/AP is more informative than
 * accuracy. Guarantee (proven in main): a well-separated classifier scores AP>0.8
 * while a random one scores AP<0.6, and strong AP strictly exceeds weak AP.
 */
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <set>
#include <vector>

using VecD = std::vector<double>;
using VecI = std::vector<int>;

static std::vector<std::pair<double, int>> generate_scored_labels(
    int n_positive, int n_negative, double noise, int seed) {
    std::mt19937 gen(static_cast<unsigned>(seed));
    std::normal_distribution<double> dist(0.0, noise);
    std::vector<std::pair<double, int>> data;
    data.reserve(n_positive + n_negative);
    auto clip = [](double s) {
        if (s < 0.0) return 0.0;
        if (s > 1.0) return 1.0;
        return s;
    };
    for (int i = 0; i < n_positive; ++i) {
        data.emplace_back(clip(0.7 + dist(gen)), 1);
    }
    for (int i = 0; i < n_negative; ++i) {
        data.emplace_back(clip(0.3 + dist(gen)), 0);
    }
    return data;
}

static void compute_pr_curve(const VecD& scores, const VecI& labels, int n_points,
                             VecD& thresholds, VecD& precisions, VecD& recalls) {
    auto n = scores.size();
    std::vector<std::size_t> idx(n);
    for (std::size_t i = 0; i < n; ++i) idx[i] = i;
    std::sort(idx.begin(), idx.end(), [&scores](std::size_t a, std::size_t b) {
        return scores[a] > scores[b];
    });
    VecD scores_sorted;
    VecI labels_sorted;
    scores_sorted.reserve(n);
    labels_sorted.reserve(n);
    for (auto i : idx) {
        scores_sorted.push_back(scores[i]);
        labels_sorted.push_back(labels[i]);
    }

    int n_pos = 0;
    for (int l : labels_sorted) if (l == 1) ++n_pos;

    std::set<double> tset;
    tset.insert(1.0);
    tset.insert(0.0);
    for (double s : scores_sorted) tset.insert(s);
    std::vector<double> tvec(tset.begin(), tset.end());
    std::sort(tvec.begin(), tvec.end(), std::greater<double>());
    if (tvec.size() > static_cast<std::size_t>(n_points)) {
        tvec.resize(n_points);
    }

    thresholds.clear();
    precisions.clear();
    recalls.clear();

    for (double threshold : tvec) {
        int pred_pos = 0;
        for (double s : scores_sorted) if (s >= threshold) ++pred_pos;
        int tp = 0;
        for (std::size_t i = 0; i < n; ++i) {
            if (scores_sorted[i] >= threshold && labels_sorted[i] == 1) ++tp;
        }
        double precision = (pred_pos == 0) ? 0.0 : static_cast<double>(tp) / pred_pos;
        double recall = (n_pos == 0) ? 0.0 : static_cast<double>(tp) / n_pos;
        thresholds.push_back(threshold);
        precisions.push_back(precision);
        recalls.push_back(recall);
    }
}

static double average_precision(const VecD& recalls, const VecD& precisions) {
    if (recalls.empty() || precisions.empty()) return 0.0;
    std::vector<std::pair<double, double>> pairs;
    for (std::size_t i = 0; i < recalls.size(); ++i) {
        pairs.emplace_back(recalls[i], precisions[i]);
    }
    std::sort(pairs.begin(), pairs.end());
    double ap = 0.0;
    for (std::size_t i = 1; i < pairs.size(); ++i) {
        double dr = pairs[i].first - pairs[i - 1].first;
        double p_avg = (pairs[i].second + pairs[i - 1].second) / 2.0;
        ap += dr * p_avg;
    }
    return ap;
}

int main() {
    std::mt19937 gen(42);
    std::uniform_real_distribution<double> uni(0.0, 1.0);

    // Strong classifier.
    auto data_strong = generate_scored_labels(50, 50, 0.1, 42);
    VecD scores_strong, prec_strong, rec_strong, thr_strong;
    VecI labels_strong;
    for (auto& p : data_strong) {
        scores_strong.push_back(p.first);
        labels_strong.push_back(p.second);
    }
    compute_pr_curve(scores_strong, labels_strong, 100, thr_strong, prec_strong, rec_strong);
    double ap_strong = average_precision(rec_strong, prec_strong);

    // Weak classifier: random scores/labels.
    std::vector<std::pair<double, int>> data_weak;
    for (int i = 0; i < 100; ++i) {
        data_weak.emplace_back(uni(gen), (uni(gen) < 0.5) ? 0 : 1);
    }
    VecD scores_weak, prec_weak, rec_weak, thr_weak;
    VecI labels_weak;
    for (auto& p : data_weak) {
        scores_weak.push_back(p.first);
        labels_weak.push_back(p.second);
    }
    compute_pr_curve(scores_weak, labels_weak, 100, thr_weak, prec_weak, rec_weak);
    double ap_weak = average_precision(rec_weak, prec_weak);

    assert(ap_strong > 0.8);
    assert(ap_weak < 0.6);
    assert(ap_strong > ap_weak);

    std::cout << "precision_recall_curve.cpp: PASS (ap_strong=" << ap_strong
              << ", ap_weak=" << ap_weak << ")" << std::endl;
    return 0;
}
