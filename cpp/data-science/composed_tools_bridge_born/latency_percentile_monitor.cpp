// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Latency Percentile Monitor — p99 tracking in five floats per quantile.
 *
 * Oracle asserts:
 *   p99 relative error < 0.15 both phases
 *   p50 shift < 25%
 *   p99 doubles
 *   p99 marker count == 5
 */

#include <vector>
#include <cmath>
#include <cassert>
#include <iostream>
#include <random>
#include <algorithm>
#include <map>
#include <string>

class P2Quantile {
public:
    P2Quantile() : P2Quantile(0.5) {}
    explicit P2Quantile(double p_) : p(p_) {}

    void process(double x) {
        if (init.size() < 5) {
            init.push_back(x);
            if (init.size() == 5) {
                std::sort(init.begin(), init.end());
                q = init;
                n = {1, 2, 3, 4, 5};
                d = {1.0, 1.0 + 2.0 * p, 1.0 + 4.0 * p, 3.0 + 2.0 * p, 5.0};
            }
            return;
        }
        int k = 0;
        if (x < q[0]) { q[0] = x; k = 0; }
        else if (x >= q[4]) { q[4] = x; k = 3; }
        else {
            for (int i = 1; i < 5; ++i) {
                if (x < q[i]) { k = i - 1; break; }
            }
        }
        for (int i = k + 1; i < 5; ++i) ++n[i];
        std::vector<double> incr = {0.0, p / 2.0, p, (1.0 + p) / 2.0, 1.0};
        for (int i = 0; i < 5; ++i) d[i] += incr[i];
        for (int i = 1; i < 4; ++i) {
            double gap = d[i] - n[i];
            if ((gap >= 1.0 && n[i + 1] - n[i] > 1) ||
                (gap <= -1.0 && n[i - 1] - n[i] < -1)) {
                int s = gap >= 0 ? 1 : -1;
                int sidx = i + s;
                double qp = q[i] + s / static_cast<double>(n[i + 1] - n[i - 1]) * (
                    (n[i] - n[i - 1] + s) * (q[i + 1] - q[i]) / (n[i + 1] - n[i])
                    + (n[i + 1] - n[i] - s) * (q[i] - q[i - 1]) / (n[i] - n[i - 1]));
                if (!(q[i - 1] < qp && qp < q[i + 1])) {
                    int neighbor = sidx;
                    qp = q[i] + s * (q[neighbor] - q[i]) / (n[neighbor] - n[i]);
                }
                q[i] = qp;
                n[i] += s;
            }
        }
    }

    double query() const {
        if (init.size() < 5) {
            if (init.empty()) return 0.0;
            auto srt = init;
            std::sort(srt.begin(), srt.end());
            return srt[srt.size() / 2];
        }
        return q[2];
    }

    std::vector<double> markers() const { return q; }

private:
    double p;
    std::vector<double> init;
    std::vector<double> q;
    std::vector<int> n;
    std::vector<double> d;
};

class LatencyMonitor {
public:
    void record(const std::string& service, double latency_ms) {
        auto& s = services[service];
        if (s.find("count") == s.end()) {
            s["count"] = 0.0; s["total"] = 0.0;
            p50[service] = P2Quantile(0.5);
            p99[service] = P2Quantile(0.99);
        }
        s["count"] += 1.0;
        s["total"] += latency_ms;
        p50[service].process(latency_ms);
        p99[service].process(latency_ms);
    }

    std::map<std::string, double> snapshot(const std::string& service) const {
        const auto& s = services.at(service);
        return {
            {"count", s.at("count")},
            {"mean", s.at("total") / s.at("count")},
            {"p50", p50.at(service).query()},
            {"p99", p99.at(service).query()}
        };
    }

    int marker_count(const std::string& service) const {
        return static_cast<int>(p99.at(service).markers().size());
    }

private:
    std::map<std::string, std::map<std::string, double>> services;
    std::map<std::string, P2Quantile> p50;
    std::map<std::string, P2Quantile> p99;
};

double lognormalish(double base, double tail, std::mt19937_64& rng) {
    std::lognormal_distribution<double> ld(0.0, 0.4);
    double v = ld(rng) * base;
    if ((rng() % 100) / 100.0 < 0.01) v += tail * (rng() % 100) / 100.0;
    return v;
}

double exact_p99(const std::vector<double>& v) {
    auto s = v;
    std::sort(s.begin(), s.end());
    return s[static_cast<size_t>(v.size() * 0.99)];
}

int main() {
    std::mt19937_64 rng(42);
    std::uniform_real_distribution<double> uniform(0.0, 1.0);

    LatencyMonitor mon1, mon2;
    std::vector<double> phase1, phase2;
    for (int i = 0; i < 6000; ++i) phase1.push_back(lognormalish(50.0, 300.0, rng));
    rng.seed(42);
    for (int i = 0; i < 6000; ++i) {
        double v = lognormalish(50.0, 300.0, rng);
        if (uniform(rng) < 0.05) v = 500.0 + 300.0 * uniform(rng);
        phase2.push_back(v);
    }

    for (double v : phase1) mon1.record("api", v);
    for (double v : phase2) mon2.record("api", v);

    auto snap1 = mon1.snapshot("api");
    auto snap2 = mon2.snapshot("api");
    double e99_1 = exact_p99(phase1);
    double e99_2 = exact_p99(phase2);

    assert(std::abs(snap1["p99"] - e99_1) / e99_1 < 0.15);
    assert(std::abs(snap2["p99"] - e99_2) / e99_2 < 0.15);
    assert(std::abs(snap2["p50"] - snap1["p50"]) / snap1["p50"] < 0.25);
    assert(snap2["p99"] > 2.0 * snap1["p99"]);
    assert(mon2.marker_count("api") == 5);

    std::cout << "latency_percentile_monitor.cpp PASS" << std::endl;
    return 0;
}
