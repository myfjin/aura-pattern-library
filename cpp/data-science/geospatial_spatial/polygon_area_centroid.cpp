// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Polygon area and centroid via the shoelace formula.
 * Sums signed cross-products over the edges to get the signed area, then divides
 * the moment sums by it for the centroid. Use to measure any simple polygon's
 * area and center of mass. Oracle: exact area and centroid for square, triangle,
 * and L-shape; a degenerate collinear polygon yields ~0 area; results are
 * invariant to vertex winding direction.
 */
#include <cassert>
#include <cmath>
#include <cstddef>
#include <iostream>
#include <vector>

struct Point {
    double x;
    double y;
};

struct Result {
    double area;
    Point centroid;
};

Result polygon_area_centroid(const std::vector<Point>& vertices) {
    std::size_t n = vertices.size();
    if (n < 3) {
        return {0.0, {0.0, 0.0}};
    }
    double signed_area = 0.0;
    double cx_sum = 0.0;
    double cy_sum = 0.0;
    for (std::size_t i = 0; i < n; ++i) {
        double x0 = vertices[i].x;
        double y0 = vertices[i].y;
        double x1 = vertices[(i + 1) % n].x;
        double y1 = vertices[(i + 1) % n].y;
        double cross = x0 * y1 - x1 * y0;
        signed_area += cross;
        cx_sum += (x0 + x1) * cross;
        cy_sum += (y0 + y1) * cross;
    }
    double area = std::abs(signed_area) / 2.0;
    if (std::abs(signed_area) < 1e-12) {
        return {0.0, {0.0, 0.0}};
    }
    double cx = cx_sum / (3.0 * signed_area);
    double cy = cy_sum / (3.0 * signed_area);
    return {area, {cx, cy}};
}

int main() {
    std::vector<Point> square = {{0, 0}, {1, 0}, {1, 1}, {0, 1}};
    auto res_sq = polygon_area_centroid(square);
    assert(std::abs(res_sq.area - 1.0) < 0.001);
    assert(std::abs(res_sq.centroid.x - 0.5) < 0.01);
    assert(std::abs(res_sq.centroid.y - 0.5) < 0.01);

    std::vector<Point> tri = {{0, 0}, {1, 0}, {0, 1}};
    auto res_tri = polygon_area_centroid(tri);
    assert(std::abs(res_tri.area - 0.5) < 0.001);
    assert(std::abs(res_tri.centroid.x - 1.0 / 3.0) < 0.01);
    assert(std::abs(res_tri.centroid.y - 1.0 / 3.0) < 0.01);

    std::vector<Point> l_shape = {{0, 0}, {2, 0}, {2, 1}, {1, 1}, {1, 2}, {0, 2}};
    auto res_l = polygon_area_centroid(l_shape);
    assert(std::abs(res_l.area - 3.0) < 0.01);
    assert(0.3 < res_l.centroid.x && res_l.centroid.x < 1.3);
    assert(0.3 < res_l.centroid.y && res_l.centroid.y < 1.3);

    std::vector<Point> line = {{0, 0}, {1, 1}, {2, 2}};
    auto res_line = polygon_area_centroid(line);
    assert(res_line.area < 0.001);

    std::vector<Point> square_rev = {{0, 1}, {1, 1}, {1, 0}, {0, 0}};
    auto res_sq_rev = polygon_area_centroid(square_rev);
    assert(std::abs(res_sq_rev.area - res_sq.area) < 0.001);
    assert(std::abs(res_sq_rev.centroid.x - res_sq.centroid.x) < 0.01);
    assert(std::abs(res_sq_rev.centroid.y - res_sq.centroid.y) < 0.01);

    std::cout << "PASS" << std::endl;
    return 0;
}
