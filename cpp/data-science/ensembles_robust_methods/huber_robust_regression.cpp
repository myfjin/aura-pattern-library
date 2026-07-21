// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Huber Loss Robust Regression.
 * Fits a line by gradient descent on the Huber loss (quadratic for small
 * residuals, linear beyond delta), so outliers get bounded gradient influence.
 * Use to fit slope/intercept when the data contains heavy-tailed or corrupted y
 * values. Oracle: on data with outliers, the Huber slope estimate is closer to
 * the true slope than ordinary least squares.
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <utility>

double huber_loss(double residual, double delta = 1.0) {
    double abs_res = std::abs(residual);
    if (abs_res <= delta) return 0.5 * residual * residual;
    return delta * (abs_res - 0.5 * delta);
}

double huber_gradient(double residual, double delta = 1.0) {
    double abs_res = std::abs(residual);
    if (abs_res <= delta) return residual;
    return (residual > 0) ? delta : -delta;
}

std::pair<double, double> fit_line_huber(const std::vector<double>& X,
                                         const std::vector<double>& y,
                                         double delta = 1.0,
                                         double learning_rate = 0.05,
                                         int iterations = 300) {
    int n = static_cast<int>(X.size());

    double mean_x = 0.0, mean_y = 0.0;
    for (double x : X) mean_x += x;
    for (double yy : y) mean_y += yy;
    mean_x /= n;
    mean_y /= n;

    double num = 0.0, denom = 0.0;
    for (int i = 0; i < n; ++i) {
        num += (X[i] - mean_x) * (y[i] - mean_y);
        denom += (X[i] - mean_x) * (X[i] - mean_x);
    }
    double m = (denom > 1e-10) ? num / denom : 0.0;
    double b = mean_y - m * mean_x;

    for (int iteration = 0; iteration < iterations; ++iteration) {
        double grad_m = 0.0, grad_b = 0.0;
        for (int i = 0; i < n; ++i) {
            double residual = y[i] - (m * X[i] + b);
            double h_grad = huber_gradient(residual, delta);
            grad_m -= X[i] * h_grad / n;
            grad_b -= h_grad / n;
        }
        double step_size = learning_rate / (1.0 + iteration / 100.0);
        m -= step_size * grad_m;
        b -= step_size * grad_b;
    }

    return {m, b};
}

std::pair<double, double> ordinary_least_squares(const std::vector<double>& X,
                                               const std::vector<double>& y) {
    int n = static_cast<int>(X.size());
    double mean_x = 0.0, mean_y = 0.0;
    for (double x : X) mean_x += x;
    for (double yy : y) mean_y += yy;
    mean_x /= n;
    mean_y /= n;

    double num = 0.0, denom = 0.0;
    for (int i = 0; i < n; ++i) {
        num += (X[i] - mean_x) * (y[i] - mean_y);
        denom += (X[i] - mean_x) * (X[i] - mean_x);
    }

    if (denom < 1e-10) return {0.0, mean_y};
    double m = num / denom;
    double b = mean_y - m * mean_x;
    return {m, b};
}

int main() {
    // Embedded Python data from seed=42
    std::vector<double> X = {
        0.9935462460613032, 3.5867384121231796, 1.8980856216107955, 6.62768738061978,
        5.9714595951954506, 1.2592388530804288, 0.686101528243559, 8.696954267695446,
        1.475541799414437, 9.84028131847739, 1.0992634788943556, 7.899846642347539,
        0.5239901786117651, 5.260855265978671, 5.132379576091917, 5.038386897858214,
        9.0875168790654, 0.31150639510343914, 1.0796182967922718, 4.435623293630087,
        0.6568223332011391, 3.251854433186679, 6.054267915353129, 7.017794185460662,
        8.88091021988493, 7.296125076345044, 3.1252357114186777, 4.742678855891027,
        0.853643573316194, 1.3011545357384335, 9.566246238469065, 8.736073722343185,
        7.2106067874614945, 5.779185183898549, 6.5673630298815215, 3.6756105061535016,
        5.741000043314627, 6.578312279988884, 7.624095179809979, 8.69862706536438,
        4.007843439995156, 7.461117620057067, 4.198324937645031, 7.76835619966741,
        0.8495703997717929, 6.7396871061311305, 6.619386928082612, 7.549431436683706,
        4.299136333978904, 6.671325587363496
    };

    std::vector<double> y = {
        1.6604666330972702, 7.79287977427315, 5.114310677157222, 13.805916403818394,
        13.028521853890723, 3.1548238931149575, 2.464958675721776, 18.730120521817216,
        13.11020628846412, 3.702855283590427, 8.421431866249344, 16.661360093711888,
        2.324735186533212, 10.663842751135562, 11.393756041640474, 26.985418753172453,
        18.94618453371834, -9.771091498992998, 3.839762241631788, -4.253214767241426,
        1.8910556777884506, -4.302022397258716, 12.640722259642082, 26.48663749591712,
        18.997588488469933, 15.146414782316235, 7.980209937655496, 10.266332735863607,
        2.690874878069781, 3.1197601366034795, 19.884765233743064, 0.45076521165039907,
        5.146520789525754, 12.107667210276853, 14.88597451578646, 8.958672136123225,
        26.616923819925233, 14.549532379291836, 11.156603518565078, 18.469530287325146,
        8.932103161321626, 15.829595124623413, 8.849099828894241, 17.119404324938607,
        3.080221491435568, 15.058798998184763, 13.865553072749659, 16.241114092173085,
        9.347473161596879, 13.822572803340451
    };

    auto [m_ols, b_ols] = ordinary_least_squares(X, y);
    auto [m_huber, b_huber] = fit_line_huber(X, y, 1.0, 0.01, 200);

    double true_m = 2.0;
    double ols_error = std::abs(m_ols - true_m);
    double huber_error = std::abs(m_huber - true_m);

    assert(huber_error < ols_error);

    std::cout << "huber_robust_regression.cpp PASS" << std::endl;
    return 0;
}
