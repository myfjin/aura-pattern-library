// random_projection_jl.cpp — Johnson-Lindenstrauss random projection.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <numeric>
#include <random>
#include <vector>

using Point = std::vector<double>;
using Matrix = std::vector<Point>;

static Matrix random_projection_matrix(int original_dim, int target_dim, unsigned seed) {
    std::mt19937 rng(seed);
    std::normal_distribution<double> norm(0.0, 1.0);
    Matrix m(target_dim, Point(original_dim));
    for (int i = 0; i < target_dim; ++i)
        for (int j = 0; j < original_dim; ++j)
            m[i][j] = norm(rng);
    for (int i = 0; i < target_dim; ++i) {
        double nrm = std::sqrt(std::inner_product(m[i].begin(), m[i].end(), m[i].begin(), 0.0));
        if (nrm > 1e-10)
            for (double& v : m[i]) v /= nrm;
    }
    return m;
}

static Point project_point(const Point& p, const Matrix& proj) {
    Point out(proj.size(), 0.0);
    for (std::size_t i = 0; i < proj.size(); ++i)
        for (std::size_t j = 0; j < p.size(); ++j)
            out[i] += proj[i][j] * p[j];
    return out;
}

static double euclidean_distance(const Point& a, const Point& b) {
    double s = 0.0;
    for (std::size_t i = 0; i < a.size(); ++i) {
        double d = a[i] - b[i];
        s += d * d;
    }
    return std::sqrt(s);
}

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> norm(0.0, 1.0);

    const int original_dim = 50;
    const int target_dim = 20;
    const int num_points = 42;

    // three cluster centers
    std::vector<Point> centers;
    for (int c = 0; c < 3; ++c) {
        Point center(original_dim);
        for (int d = 0; d < original_dim; ++d) center[d] = 6.0 * norm(rng);
        centers.push_back(std::move(center));
    }

    std::vector<Point> points;
    for (int k = 0; k < num_points; ++k) {
        Point p(original_dim);
        for (int d = 0; d < original_dim; ++d)
            p[d] = centers[k % 3][d] + norm(rng);
        points.push_back(std::move(p));
    }

    std::vector<double> original_dists;
    for (int i = 0; i < num_points; ++i)
        for (int j = i + 1; j < num_points; ++j)
            original_dists.push_back(euclidean_distance(points[i], points[j]));

    Matrix proj = random_projection_matrix(original_dim, target_dim, 42);
    std::vector<Point> projected;
    for (const auto& p : points) projected.push_back(project_point(p, proj));

    std::vector<double> projected_dists;
    for (int i = 0; i < num_points; ++i)
        for (int j = i + 1; j < num_points; ++j)
            projected_dists.push_back(euclidean_distance(projected[i], projected[j]));

    double mean_o = std::accumulate(original_dists.begin(), original_dists.end(), 0.0) /
                    original_dists.size();
    double mean_p = std::accumulate(projected_dists.begin(), projected_dists.end(), 0.0) /
                    projected_dists.size();

    double cov = 0.0, var_o = 0.0, var_p = 0.0;
    for (std::size_t i = 0; i < original_dists.size(); ++i) {
        double do_ = original_dists[i] - mean_o;
        double dp = projected_dists[i] - mean_p;
        cov += do_ * dp;
        var_o += do_ * do_;
        var_p += dp * dp;
    }

    double correlation = 0.0;
    if (var_o > 0 && var_p > 0)
        correlation = cov / std::sqrt(var_o * var_p);

    std::printf("random_projection_jl.cpp: distance correlation %.3f\n", correlation);
    assert(correlation > 0.9);
    assert(correlation < 1.1);
    std::printf("PASS\n");
    return 0;
}
