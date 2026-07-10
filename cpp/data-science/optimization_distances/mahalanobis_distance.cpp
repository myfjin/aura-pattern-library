// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Mahalanobis Distance.
 *
 * Oracle asserts:
 *   mdist_self < 1e-10
 *   mdist_perp > mdist_aligned
 *   edist_aligned == edist_perp
 *   mdist_aligned, mdist_perp >= 0
 *   cov symmetric
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>

std::vector<std::vector<double>> matrix_invert_2x2(const std::vector<std::vector<double>>& M) {
    double a = M[0][0], b = M[0][1], c = M[1][0], d = M[1][1];
    double det = a * d - b * c;
    assert(std::abs(det) > 1e-12);
    return {{d / det, -b / det}, {-c / det, a / det}};
}

std::vector<std::vector<double>> compute_covariance_2d(const std::vector<std::pair<double, double>>& points) {
    int n = static_cast<int>(points.size());
    double mx = 0.0, my = 0.0;
    for (const auto& p : points) { mx += p.first; my += p.second; }
    mx /= n; my /= n;
    double cxx = 0.0, cyy = 0.0, cxy = 0.0;
    for (const auto& p : points) {
        double dx = p.first - mx, dy = p.second - my;
        cxx += dx * dx; cyy += dy * dy; cxy += dx * dy;
    }
    return {{cxx / n, cxy / n}, {cxy / n, cyy / n}};
}

double mahalanobis_distance(const std::pair<double, double>& point,
                           const std::pair<double, double>& mean,
                           const std::vector<std::vector<double>>& cov_inv) {
    double dx = point.first - mean.first, dy = point.second - mean.second;
    double t1 = cov_inv[0][0] * dx + cov_inv[0][1] * dy;
    double t2 = cov_inv[1][0] * dx + cov_inv[1][1] * dy;
    double q = dx * t1 + dy * t2;
    if (q < 0.0) q = 0.0;
    return std::sqrt(q);
}

double euclidean_distance(const std::pair<double, double>& p,
                         const std::pair<double, double>& q) {
    return std::sqrt(std::pow(p.first - q.first, 2) + std::pow(p.second - q.second, 2));
}

int main() {
    std::vector<std::pair<double, double>> points = {{0.0, 0.1}, {1.0, 1.1}, {2.0, 1.9}, {3.0, 2.9}, {4.0, 4.1}};
    double mx = 0.0, my = 0.0;
    for (const auto& p : points) { mx += p.first; my += p.second; }
    std::pair<double, double> mean = {mx / points.size(), my / points.size()};

    auto cov = compute_covariance_2d(points);
    auto cov_inv = matrix_invert_2x2(cov);

    double mdist_self = mahalanobis_distance(mean, mean, cov_inv);
    assert(mdist_self < 1e-10);

    std::pair<double, double> aligned = {mean.first + 1.0, mean.second + 1.0};
    std::pair<double, double> perp = {mean.first + 1.0, mean.second - 1.0};
    double mdist_aligned = mahalanobis_distance(aligned, mean, cov_inv);
    double mdist_perp = mahalanobis_distance(perp, mean, cov_inv);
    assert(mdist_perp > mdist_aligned);

    double edist_aligned = euclidean_distance(aligned, mean);
    double edist_perp = euclidean_distance(perp, mean);
    assert(std::abs(edist_aligned - edist_perp) < 1e-6);

    assert(mdist_aligned >= 0.0 && mdist_perp >= 0.0);
    assert(std::abs(cov[0][1] - cov[1][0]) < 1e-10);

    std::cout << "mahalanobis_distance.cpp PASS" << std::endl;
    return 0;
}
