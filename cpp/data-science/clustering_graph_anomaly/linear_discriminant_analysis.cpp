// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Linear Discriminant Analysis (LDA) from scratch.
 *
 * Oracle asserts:
 *   accuracy >= 0.9
 *   weights non-zero
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <random>

std::vector<std::vector<double>> matrix_inverse_2x2(const std::vector<std::vector<double>>& m) {
    double det = m[0][0] * m[1][1] - m[0][1] * m[1][0];
    if (std::abs(det) < 1e-10) return {{1.0, 0.0}, {0.0, 1.0}};
    double inv = 1.0 / det;
    return {{inv * m[1][1], -inv * m[0][1]}, {-inv * m[1][0], inv * m[0][0]}};
}

std::vector<std::vector<double>> matrix_multiply_2x2(const std::vector<std::vector<double>>& a,
                                                const std::vector<std::vector<double>>& b) {
    return {
        {a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]},
        {a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]}
    };
}

std::pair<double, std::vector<double>> power_iteration_2x2(const std::vector<std::vector<double>>& m,
                                                              int iterations = 100) {
    std::vector<double> v = {1.0, 1.0};
    for (int i = 0; i < iterations; ++i) {
        std::vector<double> new_v = {
            m[0][0] * v[0] + m[0][1] * v[1],
            m[1][0] * v[0] + m[1][1] * v[1]
        };
        double norm = std::sqrt(new_v[0] * new_v[0] + new_v[1] * new_v[1]);
        if (norm < 1e-10) break;
        v[0] = new_v[0] / norm; v[1] = new_v[1] / norm;
    }
    double eigen = v[0] * (m[0][0] * v[0] + m[0][1] * v[1]) + v[1] * (m[1][0] * v[0] + m[1][1] * v[1]);
    return {eigen, v};
}

std::pair<std::vector<double>, double> lda_2d(const std::vector<std::pair<double, double>>& points,
                                              const std::vector<int>& labels) {
    std::vector<std::pair<double, double>> class_0, class_1;
    for (size_t i = 0; i < points.size(); ++i) {
        if (labels[i] == 0) class_0.push_back(points[i]);
        else class_1.push_back(points[i]);
    }

    auto mean = [](const std::vector<std::pair<double, double>>& c) {
        double sx = 0.0, sy = 0.0;
        for (const auto& p : c) { sx += p.first; sy += p.second; }
        return std::make_pair(sx / c.size(), sy / c.size());
    };
    auto m0 = mean(class_0), m1 = mean(class_1);

    auto scatter = [](const std::vector<std::pair<double, double>>& c,
                      const std::pair<double, double>& m) {
        std::vector<std::vector<double>> s = {{0.0, 0.0}, {0.0, 0.0}};
        for (const auto& p : c) {
            double dx = p.first - m.first, dy = p.second - m.second;
            s[0][0] += dx * dx; s[0][1] += dx * dy;
            s[1][0] += dy * dx; s[1][1] += dy * dy;
        }
        return s;
    };
    auto s0 = scatter(class_0, m0), s1 = scatter(class_1, m1);
    std::vector<std::vector<double>> s_w = {
        {s0[0][0] + s1[0][0], s0[0][1] + s1[0][1]},
        {s0[1][0] + s1[1][0], s0[1][1] + s1[1][1]}
    };

    double dm0 = m0.first - m1.first, dm1 = m0.second - m1.second;
    std::vector<std::vector<double>> s_b = {{dm0 * dm0, dm0 * dm1}, {dm1 * dm0, dm1 * dm1}};

    auto s_w_inv = matrix_inverse_2x2(s_w);
    auto s_w_inv_s_b = matrix_multiply_2x2(s_w_inv, s_b);
    auto [_, weights] = power_iteration_2x2(s_w_inv_s_b, 50);

    double proj0 = m0.first * weights[0] + m0.second * weights[1];
    double proj1 = m1.first * weights[0] + m1.second * weights[1];
    double threshold = (proj0 + proj1) / 2.0;
    return {weights, threshold};
}

int main() {
    std::mt19937_64 rng(42);
    std::normal_distribution<double> c0(1.0, 0.5), c1(4.0, 0.5);
    std::vector<std::pair<double, double>> points;
    std::vector<int> labels;
    for (int i = 0; i < 30; ++i) { points.push_back({c0(rng), c0(rng)}); labels.push_back(0); }
    for (int i = 0; i < 30; ++i) { points.push_back({c1(rng), c1(rng)}); labels.push_back(1); }

    auto [weights, threshold] = lda_2d(points, labels);

    int correct = 0;
    for (size_t i = 0; i < points.size(); ++i) {
        double proj = points[i].first * weights[0] + points[i].second * weights[1];
        int pred = proj > threshold ? 1 : 0;
        if (pred == labels[i]) ++correct;
    }
    double accuracy = static_cast<double>(correct) / points.size();

    assert(accuracy >= 0.9);
    assert(weights[0] * weights[0] + weights[1] * weights[1] > 0.0);

    std::cout << "linear_discriminant_analysis.cpp PASS: accuracy=" << accuracy << std::endl;
    return 0;
}
