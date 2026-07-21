"""
Great-circle intermediate waypoints via spherical linear interpolation (slerp).

Core idea: interpolate along great circle arc between two points on Earth sphere.
Verify each waypoint's cumulative distance equals proportional share of total distance.

When to use: flight path generation, mapping geodetic routes, animation along globe.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_haversine_dist(radius_km):
    v = []
    if isinstance(radius_km, (int, float)) and radius_km <= 0:
        v.append(f"AURA-E009: radius_km must be > 0, got {radius_km}")
    if v:
        raise AuraInputError(v)

def haversine_dist(lat1: float, lon1: float, lat2: float, lon2: float,
                   radius_km: float = 6371.0) -> float:
    """Distance in km between two points on Earth."""
    _aura_validate_haversine_dist(radius_km)
    lat1_r, lon1_r = math.radians(lat1), math.radians(lon1)
    lat2_r, lon2_r = math.radians(lat2), math.radians(lon2)
    dlat = lat2_r - lat1_r
    dlon = lon2_r - lon1_r
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return radius_km * c

def great_circle_waypoints(lat1: float, lon1: float, lat2: float, lon2: float,
                           n_waypoints: int = 5) -> List[Tuple[float, float]]:
    """Slerp n_waypoints along great circle from (lat1,lon1) to (lat2,lon2)."""
    lat1_r, lon1_r = math.radians(lat1), math.radians(lon1)
    lat2_r, lon2_r = math.radians(lat2), math.radians(lon2)

    # Angular distance on sphere
    dlat = lat2_r - lat1_r
    dlon = lon2_r - lon1_r
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(dlon / 2) ** 2
    d = 2 * math.asin(math.sqrt(a))

    waypoints = []
    for i in range(n_waypoints):
        f = i / (n_waypoints - 1)
        A = math.sin((1 - f) * d) / math.sin(d)
        B = math.sin(f * d) / math.sin(d)

        x = A * math.cos(lat1_r) * math.cos(lon1_r) + B * math.cos(lat2_r) * math.cos(lon2_r)
        y = A * math.cos(lat1_r) * math.sin(lon1_r) + B * math.cos(lat2_r) * math.sin(lon2_r)
        z = A * math.sin(lat1_r) + B * math.sin(lat2_r)

        lat_r = math.atan2(z, math.sqrt(x ** 2 + y ** 2))
        lon_r = math.atan2(y, x)
        waypoints.append((math.degrees(lat_r), math.degrees(lon_r)))

    return waypoints

if __name__ == '__main__':
    # London to Paris
    lat1, lon1 = 51.5074, -0.1278
    lat2, lon2 = 48.8566, 2.3522
    total_dist = haversine_dist(lat1, lon1, lat2, lon2)
    assert 340 < total_dist < 350, f"London-Paris should be ~343 km, got {total_dist}"

    # Generate waypoints
    n_wp = 11
    waypoints = great_circle_waypoints(lat1, lon1, lat2, lon2, n_wp)
    assert len(waypoints) == n_wp, f"Should have {n_wp} waypoints, got {len(waypoints)}"

    # Start and end should match
    assert abs(waypoints[0][0] - lat1) < 0.1 and abs(waypoints[0][1] - lon1) < 0.1, "First waypoint should be near start"
    assert abs(waypoints[-1][0] - lat2) < 0.1 and abs(waypoints[-1][1] - lon2) < 0.1, "Last waypoint should be near end"

    # Cumulative distance along waypoints should equal total distance
    cumul_dist = 0.0
    for i in range(len(waypoints) - 1):
        lat_a, lon_a = waypoints[i]
        lat_b, lon_b = waypoints[i + 1]
        segment_dist = haversine_dist(lat_a, lon_a, lat_b, lon_b)
        cumul_dist += segment_dist

    # Should be close to total distance (within a few percent due to interpolation)
    relative_error = abs(cumul_dist - total_dist) / total_dist
    assert relative_error < 0.05, f"Cumulative distance should match total; error {relative_error*100:.1f}%"

    # Test with more waypoints: should be even more accurate
    waypoints_fine = great_circle_waypoints(lat1, lon1, lat2, lon2, 101)
    cumul_fine = 0.0
    for i in range(len(waypoints_fine) - 1):
        lat_a, lon_a = waypoints_fine[i]
        lat_b, lon_b = waypoints_fine[i + 1]
        cumul_fine += haversine_dist(lat_a, lon_a, lat_b, lon_b)
    error_fine = abs(cumul_fine - total_dist) / total_dist
    assert error_fine < 0.01, f"Fine waypoints should be more accurate; error {error_fine*100:.2f}%"

    print("PASS")
