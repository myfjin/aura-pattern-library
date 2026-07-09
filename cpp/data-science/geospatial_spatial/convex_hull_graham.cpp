// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Graham Scan: Compute Convex Hull
 * 
 * Sort points by polar angle from lowest point, use stack to maintain left-turn invariant.
 */

#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <iostream>
#include <set>
#include <random>

struct Point {
    double x, y;
    bool operator<(const Point& other) const {
        return (y < other.y) || (y == other.y && x < other.x);
    }
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }
};

double cross_product(const Point& o, const Point& a, const Point& b) {
    /* Cross product of vectors OA and OB. */
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

std::vector<Point> convex_hull_graham(std::vector<Point> points) {
    /* Return convex hull vertices in CCW order. */
    if (points.size() < 3) {
        std::sort(points.begin(), points.end());
        return points;
    }

    // Find lowest point (lexicographic if tied)
    Point start = *std::min_element(points.begin(), points.end());

    // Sort by polar angle from start
    std::sort(points.begin(), points.end(), [&start](const Point& a, const Point& b) {
        if (a.x == start.x && a.y == start.y) return true;
        if (b.x == start.x && b.y == start.y) return false;
        double angle_a = std::atan2(a.y - start.y, a.x - start.x);
        double angle_b = std::atan2(b.y - start.y, b.x - start.x);
        return angle_a < angle_b;
    });

    // Graham scan with stack
    std::vector<Point> hull;
    for (const auto& p : points) {
        while (hull.size() > 1 && cross_product(hull[hull.size() - 2], hull.back(), p) <= 0) {
            hull.pop_back();
        }
        hull.push_back(p);
    }

    return hull;
}

int main() {
    // Square with center point
    std::vector<Point> square_pts = {{0, 0}, {1, 0}, {1, 1}, {0, 1}, {0.5, 0.5}};
    auto hull = convex_hull_graham(square_pts);
    assert(hull.size() == 4);

    // All hull vertices should be corners
    std::set<std::pair<double, double>> corners = {{0, 0}, {1, 0}, {1, 1}, {0, 1}};
    std::set<std::pair<double, double>> hull_set;
    for (const auto& p : hull) {
        hull_set.insert({p.x, p.y});
    }
    assert(hull_set == corners);

    // Triangle with interior point
    std::vector<Point> tri_pts = {{0, 0}, {1, 0}, {0.5, 1}, {0.5, 0.3}};
    auto hull_tri = convex_hull_graham(tri_pts);
    assert(hull_tri.size() == 3);

    // Collinear points
    std::vector<Point> line_pts = {{0, 0}, {1, 1}, {2, 2}, {0.5, 0.5}};
    auto hull_line = convex_hull_graham(line_pts);
    assert(hull_line.size() >= 2);

    // Dense cloud with clear extremes
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform(0.0, 1.0);
    std::vector<Point> cloud;
    for (int i = 0; i < 50; ++i) {
        cloud.push_back({uniform(rng), uniform(rng)});
    }
    cloud.push_back({0, 0});
    cloud.push_back({2, 0});
    cloud.push_back({2, 2});
    cloud.push_back({0, 2});

    auto hull_cloud = convex_hull_graham(cloud);
    bool has_lower_left = false;
    for (const auto& p : hull_cloud) {
        if (p.x < 0.01 && p.y < 0.01) {
            has_lower_left = true;
            break;
        }
    }
    assert(has_lower_left);
    assert(hull_cloud.size() >= 4);

    std::cout << "convex_hull_graham.cpp PASS" << std::endl;
    return 0;
}
