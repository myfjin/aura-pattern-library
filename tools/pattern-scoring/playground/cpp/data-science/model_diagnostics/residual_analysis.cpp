// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Residual analysis for detecting model mis-specification. Fits a model, then
 * correlates its residuals against a candidate feature (here x^2): if the residuals
 * still carry structure that correlates with an omitted term, the model is missing
 * that term. Use as a diagnostic to decide whether to add nonlinearity/features.
 * Guarantee (proven in main): on quadratic data a linear fit leaves residuals
 * strongly correlated with x^2 (|r|>0.5), while the quadratic fit removes that
 * structure (its correlation drops below 30% of the linear one).
 */
#include <cassert>
#include <cmath>
#include <cstdio>
#include <random>
#include <tuple>
#include <vector>

std::vector<std::pair<double, double>> generate_quadratic_data(int n, int seed) {
    std::mt19937 gen(seed);
    std::uniform_real_distribution<double> xdist(-4.0, 4.0);
    std::normal_distribution<double> noise(0.0, 0.3);
    std::vector<std::pair<double, double>> data;
    for (int i = 0; i < n; ++i) {
        double x = xdist(gen);
        double y = 1.0 + 0.5 * x + 0.3 * x * x + noise(gen);
        data.emplace_back(x, y);
    }
    return data;
}

std::pair<double, double> fit_linear_model(const std::vector<double>& x_list,
                                          const std::vector<double>& y_list) {
    int n = static_cast<int>(x_list.size());
    double x_mean = 0.0, y_mean = 0.0;
    for (int i = 0; i < n; ++i) {
        x_mean += x_list[i];
        y_mean += y_list[i];
    }
    x_mean /= n;
    y_mean /= n;

    double num = 0.0, den = 0.0;
    for (int i = 0; i < n; ++i) {
        double dx = x_list[i] - x_mean;
        num += dx * (y_list[i] - y_mean);
        den += dx * dx;
    }

    if (std::fabs(den) < 1e-12) return {y_mean, 0.0};
    double b = num / den;
    double a = y_mean - b * x_mean;
    return {a, b};
}

std::tuple<double, double, double> fit_quadratic_model(const std::vector<double>& x_list,
                                                       const std::vector<double>& y_list) {
    int n = static_cast<int>(x_list.size());
    double sx0 = n, sx1 = 0.0, sx2 = 0.0, sx3 = 0.0, sx4 = 0.0;
    double sy = 0.0, sxy = 0.0, sx2y = 0.0;
    for (int i = 0; i < n; ++i) {
        double x = x_list[i];
        double y = y_list[i];
        double x2 = x * x;
        sx1 += x;
        sx2 += x2;
        sx3 += x2 * x;
        sx4 += x2 * x2;
        sy += y;
        sxy += x * y;
        sx2y += x2 * y;
    }

    double det = (sx0 * (sx2 * sx4 - sx3 * sx3) -
                  sx1 * (sx1 * sx4 - sx3 * sx2) +
                  sx2 * (sx1 * sx3 - sx2 * sx2));

    if (std::fabs(det) < 1e-10) return {0.0, 0.0, 0.0};

    double a = (sy * (sx2 * sx4 - sx3 * sx3) -
                sxy * (sx1 * sx4 - sx3 * sx2) +
                sx2y * (sx1 * sx3 - sx2 * sx2)) / det;

    double b = (sx0 * (sxy * sx4 - sx3 * sx2y) -
                sy * (sx1 * sx4 - sx3 * sx2) +
                sx2y * (sx1 * sx3 - sx2 * sx2)) / det;

    double c = (sx0 * (sx2 * sx2y - sx3 * sxy) -
                sx1 * (sx1 * sx2y - sx3 * sy) +
                sy * (sx1 * sx3 - sx2 * sx2)) / det;

    return {a, b, c};
}

double pearson_correlation(const std::vector<double>& u, const std::vector<double>& v) {
    int n = static_cast<int>(u.size());
    double u_mean = 0.0, v_mean = 0.0;
    for (int i = 0; i < n; ++i) {
        u_mean += u[i];
        v_mean += v[i];
    }
    u_mean /= n;
    v_mean /= n;

    double num = 0.0, u_var = 0.0, v_var = 0.0;
    for (int i = 0; i < n; ++i) {
        double du = u[i] - u_mean;
        double dv = v[i] - v_mean;
        num += du * dv;
        u_var += du * du;
        v_var += dv * dv;
    }

    if (u_var == 0.0 || v_var == 0.0) return 0.0;
    return num / std::sqrt(u_var * v_var);
}

int main() {
    auto data = generate_quadratic_data(100, 42);
    std::vector<double> x_list, y_list;
    for (const auto& p : data) {
        x_list.push_back(p.first);
        y_list.push_back(p.second);
    }

    auto [a_lin, b_lin] = fit_linear_model(x_list, y_list);
    std::vector<double> residuals_lin;
    for (int i = 0; i < static_cast<int>(x_list.size()); ++i)
        residuals_lin.push_back(y_list[i] - (a_lin + b_lin * x_list[i]));

    std::vector<double> x_squared;
    for (double x : x_list) x_squared.push_back(x * x);

    double corr_lin = pearson_correlation(residuals_lin, x_squared);
    assert(std::fabs(corr_lin) > 0.5);

    auto [a_quad, b_quad, c_quad] = fit_quadratic_model(x_list, y_list);
    std::vector<double> residuals_quad;
    for (int i = 0; i < static_cast<int>(x_list.size()); ++i)
        residuals_quad.push_back(y_list[i] - (a_quad + b_quad * x_list[i] + c_quad * x_list[i] * x_list[i]));

    double corr_quad = pearson_correlation(residuals_quad, x_squared);
    assert(std::fabs(corr_quad) < std::fabs(corr_lin) * 0.3);

    printf("residual_analysis.cpp: PASS | corr_lin=%.3f corr_quad=%.3f\n", corr_lin, corr_quad);
    return 0;
}
