// Verify analytic backprop gradients against finite-difference numerical gradients.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <cassert>
#include <algorithm>

struct TinyNetwork {
    double w1[2][2] = {{0.5, -0.3}, {0.2, 0.4}};
    double b1[2] = {0.1, -0.1};
    double w2[2] = {0.6, -0.5};
    double b2 = 0.2;

    static double sigmoid(double x) {
        if (x < -500.0) return 0.0;
        if (x >  500.0) return 1.0;
        return 1.0 / (1.0 + std::exp(-x));
    }

    static double sigmoid_derivative(double s) {
        return s * (1.0 - s);
    }

    struct ForwardResult {
        double y;
        double z1[2];
        double h[2];
    };

    ForwardResult forward(const std::vector<double>& x) const {
        ForwardResult out;
        out.z1[0] = b1[0] + w1[0][0] * x[0] + w1[0][1] * x[1];
        out.z1[1] = b1[1] + w1[1][0] * x[0] + w1[1][1] * x[1];
        out.h[0] = sigmoid(out.z1[0]);
        out.h[1] = sigmoid(out.z1[1]);
        double z2 = b2 + w2[0] * out.h[0] + w2[1] * out.h[1];
        out.y = sigmoid(z2);
        return out;
    }

    double loss(const std::vector<double>& x, double y_true) const {
        double y_pred = forward(x).y;
        return (y_pred - y_true) * (y_pred - y_true) / 2.0;
    }

    struct Gradients {
        double dw1[2][2];
        double db1[2];
        double dw2[2];
        double db2;
    };

    Gradients analytic_gradients(const std::vector<double>& x, double y_true) const {
        ForwardResult f = forward(x);
        double dL_dy = f.y - y_true;
        double dL_dz2 = dL_dy * sigmoid_derivative(f.y);

        Gradients g{};
        g.dw2[0] = dL_dz2 * f.h[0];
        g.dw2[1] = dL_dz2 * f.h[1];
        g.db2 = dL_dz2;

        double dL_dz1[2] = {
            dL_dz2 * w2[0] * sigmoid_derivative(f.h[0]),
            dL_dz2 * w2[1] * sigmoid_derivative(f.h[1])
        };

        g.dw1[0][0] = dL_dz1[0] * x[0];
        g.dw1[0][1] = dL_dz1[0] * x[1];
        g.dw1[1][0] = dL_dz1[1] * x[0];
        g.dw1[1][1] = dL_dz1[1] * x[1];
        g.db1[0] = dL_dz1[0];
        g.db1[1] = dL_dz1[1];

        return g;
    }
};

enum class ParamKind { W1, B1, W2, B2 };

double numerical_gradient(
    TinyNetwork& net,
    const std::vector<double>& x,
    double y_true,
    ParamKind kind,
    int i,
    int j,
    double eps = 1e-5) {

    double* ptr = nullptr;
    switch (kind) {
        case ParamKind::W1: ptr = &net.w1[i][j]; break;
        case ParamKind::B1: ptr = &net.b1[i]; break;
        case ParamKind::W2: ptr = &net.w2[i]; break;
        case ParamKind::B2: ptr = &net.b2; break;
    }

    double original = *ptr;
    *ptr = original + eps;
    double loss_plus = net.loss(x, y_true);
    *ptr = original - eps;
    double loss_minus = net.loss(x, y_true);
    *ptr = original;

    return (loss_plus - loss_minus) / (2.0 * eps);
}

double relative_error(double analytic, double numerical) {
    double denom = std::max(std::abs(analytic), std::abs(numerical));
    denom = std::max(denom, 1e-8);
    return std::abs(analytic - numerical) / denom;
}

int main() {
    TinyNetwork net;
    std::vector<double> x = {0.5, -0.3};
    double y_true = 0.7;

    TinyNetwork::Gradients ana = net.analytic_gradients(x, y_true);

    std::cout << "Gradient checks:" << std::endl;
    double max_rel_err = 0.0;

    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            double num = numerical_gradient(net, x, y_true, ParamKind::W1, i, j);
            double err = relative_error(ana.dw1[i][j], num);
            max_rel_err = std::max(max_rel_err, err);
            std::cout << "  w1[" << i << "][" << j << "]: analytic=" << std::fixed << std::setprecision(6) << ana.dw1[i][j]
                      << ", numerical=" << num << ", rel_err=" << std::scientific << err << std::endl;
        }
    }

    for (int i = 0; i < 2; ++i) {
        double num = numerical_gradient(net, x, y_true, ParamKind::B1, i, -1);
        double err = relative_error(ana.db1[i], num);
        max_rel_err = std::max(max_rel_err, err);
        std::cout << "  b1[" << i << "]: analytic=" << std::fixed << ana.db1[i]
                  << ", numerical=" << num << ", rel_err=" << std::scientific << err << std::endl;
    }

    for (int i = 0; i < 2; ++i) {
        double num = numerical_gradient(net, x, y_true, ParamKind::W2, i, -1);
        double err = relative_error(ana.dw2[i], num);
        max_rel_err = std::max(max_rel_err, err);
        std::cout << "  w2[" << i << "]: analytic=" << std::fixed << ana.dw2[i]
                  << ", numerical=" << num << ", rel_err=" << std::scientific << err << std::endl;
    }

    {
        double num = numerical_gradient(net, x, y_true, ParamKind::B2, -1, -1);
        double err = relative_error(ana.db2, num);
        max_rel_err = std::max(max_rel_err, err);
        std::cout << "  b2: analytic=" << std::fixed << ana.db2
                  << ", numerical=" << num << ", rel_err=" << std::scientific << err << std::endl;
    }

    std::cout << "\nMax relative error: " << std::scientific << max_rel_err << std::endl;
    assert(max_rel_err < 1e-4);
    std::cout << "PASS" << std::endl;
    return 0;
}
