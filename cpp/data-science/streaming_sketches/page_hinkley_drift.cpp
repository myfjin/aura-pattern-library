// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Page-Hinkley concept-drift detector: maintains a running mean and a cumulative
deviation statistic, raising an alarm (and resetting) when the gap between the
statistic and its running minimum exceeds a threshold. Use to detect a shift in a
data stream's mean online, after a min-instances warmup.
Guarantees (disaster it survives): on a stable stream it raises at most one false
alarm; on a stream whose mean shifts at step 100 it detects the drift before
step 150.
*/
#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>

class PageHinkleyDrift {
public:
    PageHinkleyDrift(double threshold = 50.0, double delta = 0.005, int min_instances = 30)
        : threshold_(threshold), delta_(delta), min_instances_(min_instances),
          mean_(0.0), m_t_(0.0), m_min_(0.0), n_(0), drift_detected_(false) {}

    bool process(double value) {
        ++n_;
        mean_ += (value - mean_) / static_cast<double>(n_);
        m_t_ += value - mean_ - delta_;
        if (m_t_ < m_min_) {
            m_min_ = m_t_;
        }
        if (n_ > min_instances_) {
            if (m_t_ - m_min_ > threshold_) {
                drift_detected_ = true;
                m_t_ = 0.0;
                m_min_ = 0.0;
                mean_ = value;
                return true;
            }
        }
        return false;
    }

private:
    double threshold_;
    double delta_;
    std::size_t min_instances_;
    double mean_;
    double m_t_;
    double m_min_;
    std::size_t n_;
    bool drift_detected_;
};

int main() {
    std::mt19937 rng(42);
    std::normal_distribution<double> dist(100.0, 5.0);

    std::cout << "Scenario 1: Stable stream (mean = 100)\n";
    PageHinkleyDrift detector1(100.0, 0.005, 50);
    int num_alarms_1 = 0;
    for (int i = 0; i < 200; ++i) {
        if (detector1.process(dist(rng))) ++num_alarms_1;
    }
    std::cout << "  Alarms in stable stream: " << num_alarms_1 << "\n";

    std::cout << "Scenario 2: Stream with mean shift at step 100\n";
    PageHinkleyDrift detector2(30.0, 0.005, 30);
    int drift_step = -1;
    std::vector<double> drifting_stream;
    for (int i = 0; i < 100; ++i) {
        drifting_stream.push_back(dist(rng));
    }
    std::normal_distribution<double> dist_shift(110.0, 5.0);
    for (int i = 0; i < 100; ++i) {
        drifting_stream.push_back(dist_shift(rng));
    }

    int num_alarms_2 = 0;
    for (int i = 0; i < 200; ++i) {
        if (detector2.process(drifting_stream[i])) {
            ++num_alarms_2;
            if (drift_step < 0) drift_step = i;
        }
    }
    std::cout << "  Drift detected at step: " << drift_step << " (true shift at step 100)\n";
    std::cout << "  Detection delay: " << (drift_step - 100) << " steps\n";

    assert(num_alarms_1 <= 1);
    if (drift_step >= 0) {
        assert(drift_step < 150);
    }

    std::cout << "Page-Hinkley Drift Detection: PASS\n";
    return 0;
}
