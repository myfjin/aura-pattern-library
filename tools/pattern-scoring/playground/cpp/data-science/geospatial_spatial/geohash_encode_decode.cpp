// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Geohash: encode/decode lat/lon as interleaved bit string, base-32 encoded.
 */

#include <string>
#include <vector>
#include <tuple>
#include <cmath>
#include <cassert>
#include <iostream>
#include <utility>
#include <cstring>

const char* BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz";

std::string geohash_encode(double lat, double lon, int precision) {
    double lat_range[2] = {-90.0, 90.0};
    double lon_range[2] = {-180.0, 180.0};
    bool is_lon = true;
    int bits = 0, ch = 0;
    std::string geohash;

    while (static_cast<int>(geohash.size()) < precision) {
        if (is_lon) {
            double mid = (lon_range[0] + lon_range[1]) / 2.0;
            if (lon > mid) {
                ch |= (1 << (4 - bits));
                lon_range[0] = mid;
            } else {
                lon_range[1] = mid;
            }
        } else {
            double mid = (lat_range[0] + lat_range[1]) / 2.0;
            if (lat > mid) {
                ch |= (1 << (4 - bits));
                lat_range[0] = mid;
            } else {
                lat_range[1] = mid;
            }
        }

        is_lon = !is_lon;
        bits += 1;
        if (bits == 5) {
            geohash.push_back(BASE32[ch]);
            bits = 0;
            ch = 0;
        }
    }

    return geohash;
}

std::tuple<double, double, double, double> geohash_decode(const std::string& geohash) {
    double lat_range[2] = {-90.0, 90.0};
    double lon_range[2] = {-180.0, 180.0};
    bool is_lon = true;

    for (char c : geohash) {
        const char* pos = std::strchr(BASE32, c);
        int val = static_cast<int>(pos - BASE32);
        int masks[5] = {16, 8, 4, 2, 1};
        for (int mask : masks) {
            if (is_lon) {
                double mid = (lon_range[0] + lon_range[1]) / 2.0;
                if (val & mask) lon_range[0] = mid;
                else lon_range[1] = mid;
            } else {
                double mid = (lat_range[0] + lat_range[1]) / 2.0;
                if (val & mask) lat_range[0] = mid;
                else lat_range[1] = mid;
            }
            is_lon = !is_lon;
        }
    }

    double lat = (lat_range[0] + lat_range[1]) / 2.0;
    double lon = (lon_range[0] + lon_range[1]) / 2.0;
    double lat_err = (lat_range[1] - lat_range[0]) / 2.0;
    double lon_err = (lon_range[1] - lon_range[0]) / 2.0;
    return {lat, lon, lat_err, lon_err};
}

int main() {
    double lat = 51.5074, lon = -0.1278;
    int prec = 6;
    std::string gh = geohash_encode(lat, lon, prec);
    assert(static_cast<int>(gh.size()) == prec);

    auto [dec_lat, dec_lon, lat_err, lon_err] = geohash_decode(gh);
    assert(std::abs(dec_lat - lat) < lat_err + 0.001);
    assert(std::abs(dec_lon - lon) < lon_err + 0.001);

    std::string gh1 = geohash_encode(51.5074, -0.1278, 4);
    std::string gh2 = geohash_encode(51.5, -0.1, 4);
    assert(!gh1.empty() && !gh2.empty());

    std::string gh_fine = geohash_encode(lat, lon, 10);
    auto [dec_lat_fine, dec_lon_fine, _, __] = geohash_decode(gh_fine);
    assert(std::abs(dec_lat_fine - lat) < 0.0001);
    assert(std::abs(dec_lon_fine - lon) < 0.0001);

    std::cout << "geohash_encode_decode.cpp PASS" << std::endl;
    return 0;
}
