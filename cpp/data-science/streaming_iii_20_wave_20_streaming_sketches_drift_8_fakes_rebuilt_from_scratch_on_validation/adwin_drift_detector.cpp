// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * ADWIN0 adaptive-windowing drift detector (Bifet & Gavalda, 2007).
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>
#include <iomanip>
#include <random>

using namespace std;

double e_cut(int n0, int n1, double var_w, int n, double delta) {
    double m = 1.0 / (1.0 / n0 + 1.0 / n1);
    double dprime = delta / n;
    return sqrt((2.0 / m) * var_w * log(2.0 / dprime)) + (2.0 / (3.0 * m)) * log(2.0 / dprime);
}

pair<bool, int> adwin_drift_detector(const vector<double>& stream, double delta = 0.05) {
    assert(delta > 0 && delta < 1);
    
    vector<double> window;
    for (size_t i = 0; i < stream.size(); i++) {
        window.push_back(stream[i]);
        int n = window.size();
        
        if (n < 10) continue;
        
        double total = 0.0;
        for (double v : window) total += v;
        double mean_w = total / n;
        
        double var_w = 0.0;
        for (double v : window) var_w += (v - mean_w) * (v - mean_w);
        var_w /= n;
        
        int stride = max(1, n / 32);
        int cut_at = -1;
        double pref = 0.0;
        
        for (int j = 1; j < n; j++) {
            pref += window[j - 1];
            if (j % stride != 0 && j != n - 1) continue;
            
            int n0 = j, n1 = n - j;
            double mean0 = pref / n0;
            double mean1 = (total - pref) / n1;
            
            if (abs(mean0 - mean1) > e_cut(n0, n1, var_w, n, delta)) {
                cut_at = j;
                break;
            }
        }
        
        if (cut_at != -1) {
            window = vector<double>(window.begin() + cut_at, window.end());
            return {true, (int)i};
        }
    }
    
    return {false, -1};
}

int main() {
    mt19937 gen(42);
    uniform_real_distribution<double> uniform(0.0, 1.0);
    
    vector<double> stationary;
    for (int i = 0; i < 600; i++) {
        stationary.push_back(uniform(gen) < 0.2 ? 1.0 : 0.0);
    }
    auto [det_s, idx_s] = adwin_drift_detector(stationary, 0.05);
    cout << "stationary: detected=" << det_s << " at " << idx_s << " (want False)" << endl;
    
    vector<double> drift;
    for (int i = 0; i < 300; i++) {
        drift.push_back(uniform(gen) < 0.2 ? 1.0 : 0.0);
    }
    for (int i = 0; i < 300; i++) {
        drift.push_back(uniform(gen) < 0.6 ? 1.0 : 0.0);
    }
    auto [det_d, idx_d] = adwin_drift_detector(drift, 0.05);
    cout << "shift: detected=" << det_d << " at " << idx_d << " (want True, soon after 300)" << endl;
    
    assert(!det_s);
    assert(det_d);
    assert(idx_d >= 300 && idx_d <= 400);
    
    cout << "ADWIN PASS" << endl;
    
    return 0;
}
