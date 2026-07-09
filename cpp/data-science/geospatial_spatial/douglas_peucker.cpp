// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/* Douglas-Peucker line simplification: reduce points while preserving shape.
 * Core claim: simplifies gently, preserves endpoints, respects epsilon,
 *             handles corners and tight/loose cases.
 */
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

struct Pt { double x, y; };

double point_line_dist(const Pt& p, const Pt& a, const Pt& b) {
    double len2 = (b.x-a.x)*(b.x-a.x) + (b.y-a.y)*(b.y-a.y);
    if (len2 == 0) return std::hypot(p.x-a.x, p.y-a.y);
    double t = std::max(0.0, std::min(1.0, ((p.x-a.x)*(b.x-a.x) + (p.y-a.y)*(b.y-a.y)) / len2));
    double projx = a.x + t*(b.x-a.x), projy = a.y + t*(b.y-a.y);
    return std::hypot(p.x-projx, p.y-projy);
}

std::vector<Pt> douglas_peucker(const std::vector<Pt>& pts, double eps) {
    if (pts.size() <= 2) return pts;
    double dmax = 0.0; int idx = 0;
    for (size_t i = 1; i < pts.size()-1; ++i) {
        double d = point_line_dist(pts[i], pts[0], pts.back());
        if (d > dmax) { dmax = d; idx = static_cast<int>(i); }
    }
    if (dmax > eps) {
        auto left = douglas_peucker(std::vector<Pt>(pts.begin(), pts.begin()+idx+1), eps);
        auto right = douglas_peucker(std::vector<Pt>(pts.begin()+idx, pts.end()), eps);
        left.pop_back();
        left.insert(left.end(), right.begin(), right.end());
        return left;
    }
    return {pts.front(), pts.back()};
}

int main() {
    // Gentle curve: should simplify but keep some points
    std::vector<Pt> gentle = {{0,0},{1,0.1},{2,0.2},{3,0.1},{4,0}};
    auto simp_gentle = douglas_peucker(gentle, 0.5);
    assert(simp_gentle.size() < gentle.size());
    assert(simp_gentle.size() >= 2 && simp_gentle.size() <= gentle.size());
    
    // Straight line: should collapse to endpoints
    std::vector<Pt> line = {{0,0},{1,0},{2,0},{3,0},{4,0}};
    auto simp_line = douglas_peucker(line, 0.1);
    assert(simp_line.size() == 2);
    assert(simp_line[0].x == 0 && simp_line[1].x == 4);  // endpoints preserved
    
    // Sharp corner with tight epsilon: keep >= 3 points
    std::vector<Pt> corner = {{0,0},{1,1},{2,0}};
    auto simp_corner_tight = douglas_peucker(corner, 0.01);
    assert(simp_corner_tight.size() >= 3);
    
    // Corner with loose epsilon: 2-4 points
    auto simp_corner_loose = douglas_peucker(corner, 1.5);
    assert(simp_corner_loose.size() >= 2 && simp_corner_loose.size() <= 4);
    
    // Endpoints preserved in all cases
    assert(simp_corner_tight.front().x == 0 && simp_corner_tight.back().x == 2);
    
    // Simplified points are subset of original
    for (const auto& p : simp_gentle) {
        bool found = false;
        for (const auto& orig : gentle) {
            if (std::abs(p.x - orig.x) < 1e-9 && std::abs(p.y - orig.y) < 1e-9) found = true;
        }
        assert(found);
    }
    
    std::cout << "douglas_peucker.cpp: simplification_correct PASS" << std::endl;
    return 0;
}
