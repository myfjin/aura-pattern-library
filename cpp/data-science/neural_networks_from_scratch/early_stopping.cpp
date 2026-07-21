// Early stopping with patience-based validation monitoring.
// C++17 self-contained port with full parity to Python oracle.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstddef>
#include <iostream>
#include <limits>
#include <tuple>
#include <vector>
#include <array>

// Python oracle generated arrays (seed 42)
// TRAIN: 40 samples
static const double TRAIN_X[40][3] = {{-0.14409032957792836, -0.1729036003315193, -0.11131586156766246}, {0.7019837250988631, -0.938051221433234, -1.890670808223996}, {-0.216958684145195, 0.11588478670085507, 0.23229773690672087}, {1.163558686599143, 0.45775079868034557, 1.374572009300586}, {0.24634219521120196, 1.3110808272040482, 0.04165686390338389}, {-0.10632329377078427, -0.2919520493500683, -0.8640336647824881}, {0.8734043853794468, -0.2406296726551354, 0.3765998586879102}, {0.24821344932841446, -1.442384075548713, -1.1004490253591945}, {-2.619945422218852, -0.6068907281995026, -0.9158100463459947}, {0.8760122430564063, -1.4626372523069724, -1.3481291254367067}, {-0.08624384633628418, -0.29389977795653216, 0.11441985746092122}, {0.8186363115437669, 0.04979987060428201, 0.4587675249085922}, {-0.6269854652195999, -0.7173710938165775, -0.4699682741360139}, {0.4993264004767815, 1.3321850763038776, -0.5601180160332138}, {0.7684735154696964, 1.4218499813434655, 0.5056926908392599}, {0.8358173459676733, -0.8133465366338694, -0.9831640512552401}, {0.9528957573165765, -1.4436784060782881, 0.03353132078726135}, {0.2532373593420619, -0.07657981361926981, 0.6841563855459771}, {0.6199677677731354, -0.6094034586430621, -0.5617975923340306}, {-0.8315811012420066, -0.7584283020157357, 0.20057422382390788}, {-0.7234629906514067, -0.29365796361771856, -1.841286265603916}, {-1.0824786190387132, 0.6639902491785032, 3.4018171341494567}, {0.2613642791998029, 0.16796936854723213, 1.0847411134536038}, {0.8933551987382066, -0.31983680087093574, 0.17022075505539358}, {1.2269415497142202, -0.02990659268121346, 1.953100924483846}, {-0.3588763403218226, -0.276789903755044, -1.4876069347000385}, {-0.15103055153883657, 1.423321026167184, 0.8163744966147283}, {0.688883864266003, 1.957286909004152, -0.5844697242906552}, {-0.6273843661803962, -0.002310451813581064, 1.7248762631487318}, {-1.0551006994223244, -0.8804638741576063, -1.050107822530918}, {0.0977763472886767, -1.2412893766356956, 0.21994543015001286}, {-1.2096175969736347, -0.08910506621924207, 0.17719513005076098}, {1.3656894904327486, -1.303263971717364, -0.12213934352186545}, {0.32314565401410306, 0.39989892457213994, -0.1384633465248276}, {1.53354619573813, 0.7123855180787204, 0.05207118510394829}, {-0.5216496504181594, -0.7466955136120088, -0.2415977396016356}, {-0.6110248279848474, 0.3203918452051127, -1.5690014196757296}, {-0.39546257832617854, -1.2344225819976538, 3.0221662363670596}, {-1.1172448790608862, 0.4578503994915399, 0.5169870984137933}, {0.49165834283826976, -0.6147068034364989, -0.38100275986698967}};
static const double TRAIN_Y[40] = {0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0};

// VAL: 40 samples
static const double VAL_X[40][3] = {{1.2740732400944477, 0.6092723205658512, 0.28651602798177056}, {2.152795235100524, 0.2437030409721501, -0.2959642327720814}, {0.11196703758302992, 1.482768668437135, 0.11871248688680022}, {0.5193776551392121, 1.1957314403321633, -0.5128586102268294}, {-1.7265697692536455, 0.29942315221644095, 0.229734794523969}, {-0.6080101785608144, 0.8710863810424168, 0.6075673769845699}, {-0.9949924215994163, 0.5182184440212028, -0.1961049589025753}, {-1.483025270207281, 0.45295023306596854, -0.04521462667939092}, {-0.7452828991898676, 0.5229455868967482, 0.4880932721923791}, {-0.5775371839442981, 0.4003521905346774, 1.015064936192444}, {-0.7126666356857019, 0.3808900274015926, 0.0027557504813070922}, {2.266010310650884, -1.862302970778187, 0.6952839314064626}, {-0.3062450197812156, -0.10019754882983263, 1.9015889763832696}, {-0.008573151260794101, 2.2409437037755677, -0.44214796541354673}, {0.35051204134810954, -0.49084750167489155, -0.6906880126178839}, {0.06248312645153182, -0.28257152534910235, 0.20249158398642758}, {-2.105027867724164, 2.0024676886095993, -0.16699690878127882}, {1.7429055062339929, -1.0071121261064784, 0.29253570472426854}, {3.1649421014768855, -0.8697291831062892, -1.4952997731082656}, {-0.5465095353366406, 0.4724884273226057, 0.6933400400612962}, {1.2903666880214264, -0.2570123983933152, -1.602250759500302}, {-0.43502980447508566, 1.2402226948017574, 0.46566265317129135}, {-1.9569387853750035, -0.0350515116881563, 1.39816809132213}, {2.126548136950435, 0.5616866387847775, 0.3093023127995021}, {-1.240205667985729, -0.8432428739675053, 0.046915857506165795}, {0.5031977408135291, 0.5801841911197648, -0.47820855513413607}, {-1.1519422284235155, -0.7777818410999131, -1.1569743942597612}, {0.6434091827639932, -2.3122811060456603, -0.3332780256094936}, {0.44987833210121114, 1.5220127246649402, 0.07129967505097183}, {1.00128393951411, -0.3990040717810922, -0.7444039865320907}, {-0.6743930384374659, 1.5273357819018323, 0.9942211438977457}, {0.4873979264626153, 3.3302688635617717, -0.032341372526149416}, {0.6203496510288014, 0.3075915525585113, -0.22188569012415993}, {2.316171347771517, 1.5066048030371135, -1.3994796346205545}, {-0.3998463222852154, 0.4283365383682873, 0.7831832150420476}, {-1.3484470698133797, -2.255561587021803, -1.9063669687617821}, {-0.07111146334121905, -0.10320317903967742, 0.34521937611451436}, {-0.7696747778790584, -1.2242376759060625, -2.0230450575793495}, {0.32918735874743676, 0.37005395848777656, 0.9929936703557113}, {0.7907956879792326, -0.19071558093694238, 1.3492609627534853}};
static const double VAL_Y[40] = {1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0};

// NO_STOP
static const double NO_STOP_w1[6][3] = {{-0.06818345576327471, -0.3304181931590362, -0.26028922165178403}, {-0.2924058223526968, -1.0828683597501707, 0.07816302649288336}, {0.12494279588108294, -0.1811329054410491, -0.35692073504320737}, {0.18590191217763813, 0.8584352937738454, 0.019127576252490657}, {-0.2538168036048532, -0.2957236012114653, -0.03487821907258111}, {-0.6323827855207211, -0.06263034409903981, 0.030591132168390364}};
static const double NO_STOP_b1[6] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
static const double NO_STOP_w2[6] = {0.922339343883095, 0.47173688205668746, 0.5170146178249398, -0.35647427054962, 0.3349607716181215, -0.5696912372749584};
static const double NO_STOP_b2 = 0.0;

// WITH_STOP
static const double WITH_STOP_w1[6][3] = {{0.15598034834543495, 0.20936863020942936, -0.38320470803111817}, {0.9996899025807449, 0.2836868313753315, -0.9513641514472544}, {0.27642994329790427, -0.20370590944500405, 0.0006881079081509603}, {0.23288239545709155, 0.19526633365577106, -1.0195756715173077}, {-0.5791598718067922, 0.3863120792872959, 0.6506021246146453}, {0.9515764433312504, 0.9015841193265526, -1.0277683023152397}};
static const double WITH_STOP_b1[6] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
static const double WITH_STOP_w2[6] = {0.38474106046822537, -0.9581451005575518, 0.8068003642709977, 0.12667470141102424, -0.5705843939885196, 1.00495047354557};
static const double WITH_STOP_b2 = 0.0;


class NetworkWithEarlyStopping {
public:
    NetworkWithEarlyStopping(const double init_w1[6][3], const double init_b1[6],
                             const double init_w2[6], double init_b2) {
        for (std::size_t i = 0; i < 6; ++i) {
            for (std::size_t j = 0; j < 3; ++j) {
                w1[i][j] = init_w1[i][j];
            }
            b1[i] = init_b1[i];
            w2[i] = init_w2[i];
        }
        b2 = init_b2;
    }

    std::tuple<double, std::vector<double>> forward(const std::vector<double>& x) const {
        std::vector<double> h(6);
        for (std::size_t i = 0; i < 6; ++i) {
            double z1 = b1[i];
            for (std::size_t j = 0; j < 3; ++j) {
                z1 += w1[i][j] * x[j];
            }
            h[i] = sigmoid(z1);
        }
        double z2 = b2;
        for (std::size_t i = 0; i < 6; ++i) {
            z2 += w2[i] * h[i];
        }
        double y = sigmoid(z2);
        return {y, h};
    }

    void backward(const std::vector<double>& x, double y_true, double y_pred,
                  const std::vector<double>& h, double lr) {
        double dy = y_pred - y_true;
        for (std::size_t i = 0; i < 6; ++i) {
            w2[i] -= lr * dy * h[i];
        }
        b2 -= lr * dy;
        for (std::size_t i = 0; i < 6; ++i) {
            double grad = dy * w2[i] * sigmoid_derivative(h[i]);
            for (std::size_t j = 0; j < 3; ++j) {
                w1[i][j] -= lr * grad * x[j];
            }
            b1[i] -= lr * grad;
        }
    }

    using Weights = std::tuple<std::array<std::array<double, 3>, 6>, std::array<double, 6>, std::array<double, 6>, double>;

    Weights save_weights() const {
        std::array<std::array<double, 3>, 6> w1_copy{};
        std::array<double, 6> b1_copy{};
        std::array<double, 6> w2_copy{};
        for (std::size_t i = 0; i < 6; ++i) {
            for (std::size_t j = 0; j < 3; ++j) {
                w1_copy[i][j] = w1[i][j];
            }
            b1_copy[i] = b1[i];
            w2_copy[i] = w2[i];
        }
        return {w1_copy, b1_copy, w2_copy, b2};
    }

    void restore_weights(const Weights& weights) {
        const auto& w1_copy = std::get<0>(weights);
        const auto& b1_copy = std::get<1>(weights);
        const auto& w2_copy = std::get<2>(weights);
        for (std::size_t i = 0; i < 6; ++i) {
            for (std::size_t j = 0; j < 3; ++j) {
                w1[i][j] = w1_copy[i][j];
            }
            b1[i] = b1_copy[i];
            w2[i] = w2_copy[i];
        }
        b2 = std::get<3>(weights);
    }

    std::pair<int, double> train_with_early_stopping(
        const std::vector<std::pair<std::vector<double>, double>>& train_data,
        const std::vector<std::pair<std::vector<double>, double>>& val_data,
        int max_epochs = 100, int patience = 10, double lr = 0.1) {
        double best_val_loss = std::numeric_limits<double>::infinity();
        Weights best_weights = save_weights();
        int patience_counter = 0;
        int epoch_stopped = 0;

        for (int epoch = 0; epoch < max_epochs; ++epoch) {
            for (const auto& sample : train_data) {
                auto fwd_out = forward(sample.first);
                double y_pred = std::get<0>(fwd_out);
                const auto& h = std::get<1>(fwd_out);
                backward(sample.first, sample.second, y_pred, h, lr);
            }

            double val_loss = 0.0;
            for (const auto& sample : val_data) {
                double y_pred = std::get<0>(forward(sample.first));
                double diff = y_pred - sample.second;
                val_loss += diff * diff / 2.0;
            }
            val_loss /= static_cast<double>(val_data.size());

            if (val_loss < best_val_loss) {
                best_val_loss = val_loss;
                best_weights = save_weights();
                patience_counter = 0;
            } else {
                ++patience_counter;
            }

            if (patience_counter >= patience) {
                epoch_stopped = epoch + 1;
                break;
            }
        }

        restore_weights(best_weights);
        return {epoch_stopped > 0 ? epoch_stopped : max_epochs, best_val_loss};
    }

private:
    static double sigmoid(double x) {
        if (x < -500.0) return 0.0;
        if (x > 500.0) return 1.0;
        return 1.0 / (1.0 + std::exp(-x));
    }

    static double sigmoid_derivative(double s) {
        return s * (1.0 - s);
    }

    double w1[6][3];
    double b1[6];
    double w2[6];
    double b2;
};

int main() {
    std::vector<std::pair<std::vector<double>, double>> train_data;
    for (int i = 0; i < 40; ++i) {
        train_data.emplace_back(std::vector<double>{TRAIN_X[i][0], TRAIN_X[i][1], TRAIN_X[i][2]}, TRAIN_Y[i]);
    }

    std::vector<std::pair<std::vector<double>, double>> val_data;
    for (int i = 0; i < 40; ++i) {
        val_data.emplace_back(std::vector<double>{VAL_X[i][0], VAL_X[i][1], VAL_X[i][2]}, VAL_Y[i]);
    }

    // Baseline: train 100 epochs without early stopping.
    NetworkWithEarlyStopping net_no_stop(NO_STOP_w1, NO_STOP_b1, NO_STOP_w2, NO_STOP_b2);
    for (int epoch = 0; epoch < 100; ++epoch) {
        for (const auto& sample : train_data) {
            auto fwd_out_no = net_no_stop.forward(sample.first);
            double y_pred = std::get<0>(fwd_out_no);
            const auto& h = std::get<1>(fwd_out_no);
            net_no_stop.backward(sample.first, sample.second, y_pred, h, 0.1);
        }
    }

    double train_loss_no_stop = 0.0;
    for (const auto& sample : train_data) {
        double y_pred = std::get<0>(net_no_stop.forward(sample.first));
        double diff = y_pred - sample.second;
        train_loss_no_stop += diff * diff / 2.0;
    }
    train_loss_no_stop /= static_cast<double>(train_data.size());

    double val_loss_no_stop = 0.0;
    for (const auto& sample : val_data) {
        double y_pred = std::get<0>(net_no_stop.forward(sample.first));
        double diff = y_pred - sample.second;
        val_loss_no_stop += diff * diff / 2.0;
    }
    val_loss_no_stop /= static_cast<double>(val_data.size());

    // Train with early stopping.
    NetworkWithEarlyStopping net_with_stop(WITH_STOP_w1, WITH_STOP_b1, WITH_STOP_w2, WITH_STOP_b2);
    auto train_result = net_with_stop.train_with_early_stopping(
        train_data, val_data, 100, 10, 0.1);
    int epochs_trained = train_result.first;
    double best_val_loss = train_result.second;

    double train_loss_with_stop = 0.0;
    for (const auto& sample : train_data) {
        double y_pred = std::get<0>(net_with_stop.forward(sample.first));
        double diff = y_pred - sample.second;
        train_loss_with_stop += diff * diff / 2.0;
    }
    train_loss_with_stop /= static_cast<double>(train_data.size());
    double val_loss_with_stop = best_val_loss;

    std::cout << "Without early stopping: epochs=100, train_loss=" << train_loss_no_stop
              << ", val_loss=" << val_loss_no_stop << "\n";
    std::cout << "With early stopping: epochs=" << epochs_trained
              << ", train_loss=" << train_loss_with_stop
              << ", val_loss=" << val_loss_with_stop << "\n";

    assert(epochs_trained < 100);
    assert(val_loss_with_stop <= val_loss_no_stop * 1.1);

    std::cout << "PASS\n";
    return 0;
}
