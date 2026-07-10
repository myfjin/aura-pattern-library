// Inlined from dynamic_range_compression.h
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <vector>
static const std::vector<double> PY_VALUES = {
    0.001,0.01,0.10000000000000001,1,10,100,1000,639.42715903108524,25.011730211911715,275.0300433398009,223.2115149380846,736.4714776927982,676.69981072342387,892.17967552527773,86.939745690583536,421.9223977634507,29.798189640850907
};
#include <cassert>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>

std::vector<double> log_compress(const std::vector<double>& values, double offset = 1.0) {
    std::vector<double> out;
    out.reserve(values.size());
    for (double v : values) out.push_back(std::log(std::abs(v) + offset));
    return out;
}

std::vector<double> log_decompress(const std::vector<double>& compressed, double offset = 1.0) {
    std::vector<double> out;
    out.reserve(compressed.size());
    for (double c : compressed) out.push_back(std::exp(c) - offset);
    return out;
}

std::vector<double> mu_law_compress(const std::vector<double>& values, double mu = 255.0) {
    std::vector<double> out;
    out.reserve(values.size());
    for (double v : values) {
        double c = std::log(1.0 + mu * std::abs(v)) / std::log(1.0 + mu);
        out.push_back(v >= 0.0 ? c : -c);
    }
    return out;
}

std::vector<double> mu_law_decompress(const std::vector<double>& compressed, double mu = 255.0) {
    std::vector<double> out;
    out.reserve(compressed.size());
    for (double c : compressed) {
        double v = (std::exp(std::abs(c) * std::log(1.0 + mu)) - 1.0) / mu;
        out.push_back(c >= 0.0 ? v : -v);
    }
    return out;
}

double dynamic_range(const std::vector<double>& values) {
    std::vector<double> abs_vals;
    for (double v : values) if (v != 0.0) abs_vals.push_back(std::abs(v));
    if (abs_vals.empty()) return 1.0;
    return *std::max_element(abs_vals.begin(), abs_vals.end()) / *std::min_element(abs_vals.begin(), abs_vals.end());
}

int main() {
    auto values = PY_VALUES;
    double dr_original = dynamic_range(values);

    auto log_compressed = log_compress(values, 0.1);
    double dr_log = dynamic_range(log_compressed);
    auto log_reconstructed = log_decompress(log_compressed, 0.1);

    double log_reconstruction_error = 0.0;
    for (size_t i = 0; i < values.size(); ++i) {
        double err = std::abs(values[i] - log_reconstructed[i]) / (std::abs(values[i]) + 1e-6);
        if (err > log_reconstruction_error) log_reconstruction_error = err;
    }

    auto mu_compressed = mu_law_compress(values, 255.0);
    double dr_mu = dynamic_range(mu_compressed);
    auto mu_reconstructed = mu_law_decompress(mu_compressed, 255.0);

    double mu_reconstruction_error = 0.0;
    for (size_t i = 0; i < values.size(); ++i) {
        double err = std::abs(values[i] - mu_reconstructed[i]) / (std::abs(values[i]) + 1e-6);
        if (err > mu_reconstruction_error) mu_reconstruction_error = err;
    }

    assert(dr_log < dr_original);
    assert(dr_mu < dr_original);
    assert(log_reconstruction_error < 0.05);
    assert(mu_reconstruction_error < 0.05);

    std::cout << "Original range: " << dr_original << "x | "
              << "Log compressed: " << dr_log << "x (" << (dr_log / dr_original * 100.0) << "%) | "
              << "u-law compressed: " << dr_mu << "x (" << (dr_mu / dr_original * 100.0) << "%) | "
              << "Log error: " << log_reconstruction_error << " | "
              << "u-law error: " << mu_reconstruction_error << " | PASS\n";
    return 0;
}