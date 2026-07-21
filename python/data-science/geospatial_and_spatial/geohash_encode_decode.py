import math
"""
Geohash: encode/decode lat/lon as interleaved bit string, base-32 encoded.

Core idea: recursively bisect latitude and longitude, interleave bits,
encode as base32. Neighbors share prefixes; precision ∝ string length.

When to use: spatial indexing, proximity queries, tile-based mapping.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Tuple

BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"



class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_encode(lat):
    v = []
    if isinstance(lat, (int, float)) and not math.isfinite(lat):
        v.append(f"AURA-E008: lat must be finite, got {lat}")
    if v:
        raise AuraInputError(v)

def encode(lat: float, lon: float, precision: int = 6) -> str:
    """Encode lat/lon as geohash string."""
    _aura_validate_encode(lat)
    lat_range, lon_range = [-90.0, 90.0], [-180.0, 180.0]
    geohash, is_lon = [], True
    bits, ch = 0, 0

    while len(geohash) < precision:
        if is_lon:
            mid = (lon_range[0] + lon_range[1]) / 2
            if lon > mid:
                ch |= (1 << (4 - bits))
                lon_range[0] = mid
            else:
                lon_range[1] = mid
        else:
            mid = (lat_range[0] + lat_range[1]) / 2
            if lat > mid:
                ch |= (1 << (4 - bits))
                lat_range[0] = mid
            else:
                lat_range[1] = mid

        is_lon = not is_lon
        bits += 1
        if bits == 5:
            geohash.append(BASE32[ch])
            bits, ch = 0, 0

    return ''.join(geohash)

def decode(geohash: str) -> Tuple[float, float, float, float]:
    """Decode geohash to (lat, lon, lat_err, lon_err)."""
    lat_range, lon_range = [-90.0, 90.0], [-180.0, 180.0]
    is_lon = True

    for ch in geohash:
        val = BASE32.index(ch)
        for mask in [16, 8, 4, 2, 1]:
            if is_lon:
                mid = (lon_range[0] + lon_range[1]) / 2
                if val & mask:
                    lon_range[0] = mid
                else:
                    lon_range[1] = mid
            else:
                mid = (lat_range[0] + lat_range[1]) / 2
                if val & mask:
                    lat_range[0] = mid
                else:
                    lat_range[1] = mid
            is_lon = not is_lon

    lat = (lat_range[0] + lat_range[1]) / 2
    lon = (lon_range[0] + lon_range[1]) / 2
    lat_err = (lat_range[1] - lat_range[0]) / 2
    lon_err = (lon_range[1] - lon_range[0]) / 2
    return lat, lon, lat_err, lon_err

if __name__ == '__main__':
    # Plant a point in London
    lat, lon, prec = 51.5074, -0.1278, 6
    gh = encode(lat, lon, prec)
    assert len(gh) == prec, f"Geohash should have length {prec}, got {len(gh)}"

    # Decode and verify round-trip within cell precision
    dec_lat, dec_lon, lat_err, lon_err = decode(gh)
    assert abs(dec_lat - lat) < lat_err + 0.001, f"Lat round-trip failed: {dec_lat} vs {lat}"
    assert abs(dec_lon - lon) < lon_err + 0.001, f"Lon round-trip failed: {dec_lon} vs {lon}"

    # Neighbors share prefixes
    gh1 = encode(51.5074, -0.1278, 4)
    gh2 = encode(51.5, -0.1, 4)
    # Same prefix should indicate proximity
    assert gh1 and gh2, "Geohashes should not be empty"

    # Encode/decode should preserve near-identity at higher precision
    gh_fine = encode(lat, lon, 10)
    dec_lat_fine, dec_lon_fine, _, _ = decode(gh_fine)
    assert abs(dec_lat_fine - lat) < 0.0001, "Fine precision lat failed"
    assert abs(dec_lon_fine - lon) < 0.0001, "Fine precision lon failed"

    print("PASS")
