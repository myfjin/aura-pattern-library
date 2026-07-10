// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * 1D Kalman Filter.
 *
 * Oracle asserts:
 *   filtered_mse < raw_mse
 *   all gains in (0, 1)
 *   abs(gains_early - gains_late) < 0.1
 *   abs(filtered_mean - 10.0) < 0.5
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <numeric>

std::pair<std::vector<double>, std::vector<double>> kalman_filter_1d(
    const std::vector<double>& observations,
    double process_variance,
    double measurement_variance,
    double initial_state,
    double initial_estimate_error) {

    std::vector<double> filtered_states;
    std::vector<double> kalman_gains;
    double estimate_error = initial_estimate_error;
    double state = initial_state;

    for (double obs : observations) {
        double predicted_state = state;
        double predicted_error = estimate_error + process_variance;
        double kalman_gain = predicted_error / (predicted_error + measurement_variance);
        kalman_gains.push_back(kalman_gain);
        state = predicted_state + kalman_gain * (obs - predicted_state);
        estimate_error = (1.0 - kalman_gain) * predicted_error;
        filtered_states.push_back(state);
    }
    return {filtered_states, kalman_gains};
}

double compute_mse(const std::vector<double>& actual, const std::vector<double>& estimated) {
    double s = 0.0;
    for (size_t i = 0; i < actual.size(); ++i) s += std::pow(actual[i] - estimated[i], 2);
    return s / actual.size();
}

int main() {
    // Embedded Python seed=42 data
    std::vector<double> observations = {
        9.711819340844142, 9.654192799336961, 9.777368276864674, 11.403967450197726, 9.744823432434226,
        7.005293171318085, 10.664636688135431, 9.465325043005663, 9.56608263170961, 10.23176957340171,
        10.464595473813441, 12.327117373198286, 11.313273013597337, 10.221014354887664, 8.52335679531036,
        7.970675265024566, 10.492684390422404, 12.622161654408096, 10.083313727806768, 9.787353412458431,
        11.063552440801738, 7.0929094039826435, 9.375445365710881, 10.98072506518705, 11.746808770758893,
        9.51874065468973, 10.75319971737582, 10.496426898656829, 11.564653617407284, 7.773555571503655,
        11.136501375170772, 6.970959216549721, 4.760109155562296, 8.786218543600995, 8.16837990730801,
        11.752024486112813, 11.32853179922579, 7.56185051740861, 11.694722846696001, 7.995594351515301,
        9.827512307327432, 9.412200444086936, 10.228839714921843, 11.637272623087533, 11.276827581584888,
        10.699770203738417, 11.299896195612597, 10.956984075300237, 8.7460290695608, 8.565257812366845,
        9.060063451727972, 10.998652800953563, 9.49976885800523, 14.671508444961095, 8.361414915627012,
        7.802250800195683, 11.536947030939393, 12.84369996268693, 11.01138538167852, 11.671634691935347,
        12.852689954884324, 9.811945047967392, 7.154082133722046, 8.935846903362574, 11.905791514633153,
        7.112643187843424, 10.067062641574523, 10.506474718684125, 9.368815670372658, 11.447263972736193,
        11.161559483053132, 14.642817033801462, 11.239935535546271, 8.781193082713877, 8.876404815331938,
        8.336837797515987, 11.90454711963164, 8.866334330372599, 9.859478452598804, 11.49860523857935,
        8.553074018697187, 9.412684072764563, 6.317427468792168, 7.8350427619225735, 8.8645271756163,
        10.831521977033344, 12.386986544886595, 9.963066373672577, 10.522728558399606, 10.335938737094464,
        12.169482226907208, 11.786710397476414, 10.547386630815085, 7.978111393109376, 11.80677062868919,
        10.762094255911505, 12.45388309942844, 9.940186814637572, 13.906201848967692, 9.282247319356355
    };

    double true_value = 10.0;
    std::vector<double> true_series(100, true_value);

    double raw_mse = compute_mse(true_series, observations);

    auto [filtered, gains] = kalman_filter_1d(observations, 0.01, 4.0, 10.0, 1.0);
    double filtered_mse = compute_mse(true_series, filtered);

    assert(filtered_mse < raw_mse);
    for (double g : gains) assert(g > 0.0 && g < 1.0);

    double gains_early = std::accumulate(gains.begin(), gains.begin() + 10, 0.0) / 10.0;
    double gains_late = std::accumulate(gains.end() - 10, gains.end(), 0.0) / 10.0;
    assert(std::abs(gains_early - gains_late) < 0.1);

    double filtered_mean = std::accumulate(filtered.begin(), filtered.end(), 0.0) / filtered.size();
    assert(std::abs(filtered_mean - true_value) < 0.5);

    std::cout << "kalman_filter_1d.cpp PASS" << std::endl;
    return 0;
}
