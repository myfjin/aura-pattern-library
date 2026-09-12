// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Great-circle intermediate waypoints via spherical linear interpolation (slerp).
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <utility>

double haversine_dist(double lat1, double lon1, double lat2, double lon2, double radius_km = 6371.0) {
    double lat1_r = lat1 * M_PI / 180.0;
    double lon1_r = lon1 * M_PI / 180.0;
    double lat2_r = lat2 * M_PI / 180.0;
    double lon2_r = lon2 * M_PI / 180.0;

    double dlat = lat2_r - lat1_r;
    double dlon = lon2_r - lon1_r;
    double a = std::sin(dlat / 2.0) * std::sin(dlat / 2.0) +
               std::cos(lat1_r) * std::cos(lat2_r) *
               std::sin(dlon / 2.0) * std::sin(dlon / 2.0);
    double c = 2.0 * std::asin(std::sqrt(a));
    return radius_km * c;
}

std::vector<std::pair<double, double>> great_circle_waypoints(double lat1, double lon1,
                                                                 double lat2, double lon2,
                                                                 int n_waypoints = 5) {
    double lat1_r = lat1 * M_PI / 180.0;
    double lon1_r = lon1 * M_PI / 180.0;
    double lat2_r = lat2 * M_PI / 180.0;
    double lon2_r = lon2 * M_PI / 180.0;

    double dlat = lat2_r - lat1_r;
    double dlon = lon2_r - lon1_r;
    double a = std::sin(dlat / 2.0) * std::sin(dlat / 2.0) +
               std::cos(lat1_r) * std::cos(lat2_r) *
               std::sin(dlon / 2.0) * std::sin(dlon / 2.0);
    double d = 2.0 * std::asin(std::sqrt(a));

    std::vector<std::pair<double, double>> waypoints;
    for (int i = 0; i < n_waypoints; ++i) {
        double f = static_cast<double>(i) / (n_waypoints - 1);
        double A = std::sin((1.0 - f) * d) / std::sin(d);
        double B = std::sin(f * d) / std::sin(d);

        double x = A * std::cos(lat1_r) * std::cos(lon1_r) + B * std::cos(lat2_r) * std::cos(lon2_r);
        double y = A * std::cos(lat1_r) * std::sin(lon1_r) + B * std::cos(lat2_r) * std::sin(lon2_r);
        double z = A * std::sin(lat1_r) + B * std::sin(lat2_r);

        double lat_r = std::atan2(z, std::sqrt(x * x + y * y));
        double lon_r = std::atan2(y, x);
        waypoints.push_back({lat_r * 180.0 / M_PI, lon_r * 180.0 / M_PI});
    }

    return waypoints;
}

int main() {
    double lat1 = 51.5074, lon1 = -0.1278;
    double lat2 = 48.8566, lon2 = 2.3522;
    double total_dist = haversine_dist(lat1, lon1, lat2, lon2);
    assert(340.0 < total_dist && total_dist < 350.0);

    int n_wp = 11;
    auto waypoints = great_circle_waypoints(lat1, lon1, lat2, lon2, n_wp);
    assert(static_cast<int>(waypoints.size()) == n_wp);

    assert(std::abs(waypoints[0].first - lat1) < 0.1 && std::abs(waypoints[0].second - lon1) < 0.1);
    assert(std::abs(waypoints.back().first - lat2) < 0.1 && std::abs(waypoints.back().second - lon2) < 0.1);

    double cumul_dist = 0.0;
    for (size_t i = 0; i + 1 < waypoints.size(); ++i) {
        cumul_dist += haversine_dist(waypoints[i].first, waypoints[i].second,
                                      waypoints[i + 1].first, waypoints[i + 1].second);
    }
    double relative_error = std::abs(cumul_dist - total_dist) / total_dist;
    assert(relative_error < 0.05);

    auto waypoints_fine = great_circle_waypoints(lat1, lon1, lat2, lon2, 101);
    double cumul_fine = 0.0;
    for (size_t i = 0; i + 1 < waypoints_fine.size(); ++i) {
        cumul_fine += haversine_dist(waypoints_fine[i].first, waypoints_fine[i].second,
                                      waypoints_fine[i + 1].first, waypoints_fine[i + 1].second);
    }
    double error_fine = std::abs(cumul_fine - total_dist) / total_dist;
    assert(error_fine < 0.01);

    std::cout << "great_circle_waypoints.cpp PASS" << std::endl;
    return 0;
}
