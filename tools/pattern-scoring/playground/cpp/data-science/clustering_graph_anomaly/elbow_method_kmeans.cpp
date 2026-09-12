// Elbow Method + K-Means from scratch.
// C++17 self-contained port with full parity to Python oracle.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <array>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <random>
#include <tuple>
#include <vector>

// Python oracle generated points (seed 42)
static const double POINTS[60][2] = {{-0.05763613183117135, -0.06916144013260772}, {-0.044526344627064986, 0.28079349003954523}, {-0.05103531351315484, -0.598941365736383}, {0.1329273376270861, -0.1069349913988673}, {-0.08678347365807801, 0.04635391468034203}, {0.09291909476268835, 0.4654234746396572}, {0.26265460271946756, 0.04420287097753278}, {-0.29532864093792827, -0.40586494699508685}, {0.09853687808448079, 0.5244323308816193}, {0.016662745561353557, -0.04252931750831371}, {0.2127104881603477, -0.5814181192034712}, {-0.12491092685782393, 0.19614501303740992}, {0.3493617541517787, -0.09625186906205417}, {0.15063994347516407, 0.0992853797313658}, {0.3129307234814569, -0.4452888856992691}, {0.22730027503415431, -0.6058081566900559}, {-1.0479781688875407, -0.24275629127980106}, {-0.3663240185383979, 0.3504048972225626}, {0.265706359845158, -0.48762989651827815}, {0.33894456933920014, -0.4008811296969399}, {5.965502461465486, 5.882440088817387}, {6.0457679429843685, 6.327454524617507}, {6.255365516316977, 6.139954040747684}, {6.2599792391225195, 6.191396815060047}, {5.74920581391216, 5.713051562473369}, {5.812012690345594, 6.199730560190712}, {5.899953771601046, 6.934301688992219}, {5.6722829831254025, 5.560450160039137}, {6.307389406187879, 6.568739992537386}, {6.202277076335704, 6.334326938387069}, {6.570537990976865, 5.962389009593479}, {5.430816426744409, 5.787169380672515}, {6.3811583029266306, 5.422528637568685}, {6.0134125283149045, 6.101294943736825}, {5.873763134074531, 6.2894527945472385}, {6.232311896610627, 6.928563406760293}, {6.247987107109254, 5.756238616542775}, {5.775280963066388, 5.667367559503197}, {6.380909423926329, 5.773266866074519}, {5.971895690519761, 6.29972104771587}, {11.710614803739437, -0.11746318544708743}, {11.263485493758434, -0.4329914476154853}, {11.77290543512326, 0.16630439540666864}, {12.477397308977318, -0.007386725265484654}, {12.104545711679922, 0.06718774741889286}, {12.433896445381441, 0.3573420794952826}, {12.109477326163017, -0.4043777213781248}, {12.361354125737838, 0.1524188511823009}, {12.490776619885688, -0.011962637072485384}, {12.781240369793538, -0.14355053612872903}, {12.637224165705216, 0.04604758904289313}, {11.793492396301799, -0.4513791491169582}, {11.939587779384466, 0.5693284104668737}, {12.32654979864589, 0.2755535457064012}, {11.04965097076352, 0.2843856818280155}, {12.222340964367937, -0.21997051376213084}, {11.749046253527842, -0.0009241807254324256}, {12.689950505259493, -0.42204027976892977}, {11.828877986105486, 0.5447139001402336}, {11.8215396802289, -0.14570059034437607}};

static double euclidean_distance(const std::vector<double>& p1, const std::vector<double>& p2) {
    double sum = 0.0;
    for (std::size_t i = 0; i < p1.size(); ++i) {
        double d = p1[i] - p2[i];
        sum += d * d;
    }
    return std::sqrt(sum);
}

static std::tuple<std::vector<int>, std::vector<std::vector<double>>, double> kmeans(
    const std::vector<std::vector<double>>& points,
    int k,
    int max_iterations = 100,
    std::uint32_t seed = 42) {
    std::mt19937 rng(seed);
    std::size_t n_points = points.size();
    std::size_t point_dim = points[0].size();

    std::vector<std::vector<double>> centroids;
    centroids.push_back(points[rng() % n_points]);
    for (int c = 1; c < k; ++c) {
        std::vector<double> distances(n_points);
        for (std::size_t i = 0; i < n_points; ++i) {
            double best = std::numeric_limits<double>::infinity();
            for (const auto& cen : centroids) {
                double d = euclidean_distance(points[i], cen);
                if (d < best) best = d;
            }
            distances[i] = best * best;
        }
        double total_dist = 0.0;
        for (double d : distances) total_dist += d;
        if (total_dist > 0.0) {
            double r = std::uniform_real_distribution<double>(0.0, total_dist)(rng);
            double cumsum = 0.0;
            for (std::size_t i = 0; i < n_points; ++i) {
                cumsum += distances[i];
                if (cumsum >= r) {
                    centroids.push_back(points[i]);
                    break;
                }
            }
        } else {
            centroids.push_back(points[rng() % n_points]);
        }
    }

    std::vector<int> labels(n_points);
    for (int iter = 0; iter < max_iterations; ++iter) {
        std::vector<std::vector<double>> old_centroids = centroids;

        for (std::size_t i = 0; i < n_points; ++i) {
            int best_j = 0;
            double best_d = std::numeric_limits<double>::infinity();
            for (int j = 0; j < k; ++j) {
                double d = euclidean_distance(points[i], centroids[j]);
                if (d < best_d) {
                    best_d = d;
                    best_j = j;
                }
            }
            labels[i] = best_j;
        }

        std::vector<std::vector<double>> new_centroids(k, std::vector<double>(point_dim, 0.0));
        std::vector<int> counts(k, 0);
        for (std::size_t i = 0; i < n_points; ++i) {
            int cluster = labels[i];
            ++counts[cluster];
            for (std::size_t d = 0; d < point_dim; ++d) {
                new_centroids[cluster][d] += points[i][d];
            }
        }
        for (int j = 0; j < k; ++j) {
            if (counts[j] > 0) {
                for (std::size_t d = 0; d < point_dim; ++d) {
                    new_centroids[j][d] /= static_cast<double>(counts[j]);
                }
                centroids[j] = new_centroids[j];
            }
        }

        bool converged = true;
        for (int j = 0; j < k; ++j) {
            if (euclidean_distance(old_centroids[j], centroids[j]) >= 1e-6) {
                converged = false;
                break;
            }
        }
        if (converged) break;
    }

    double inertia = 0.0;
    for (std::size_t i = 0; i < n_points; ++i) {
        double d = euclidean_distance(points[i], centroids[labels[i]]);
        inertia += d * d;
    }
    return {labels, centroids, inertia};
}

static int elbow_knee(const std::vector<double>& inertias) {
    if (inertias.size() < 3) return 0;
    std::vector<double> diffs(inertias.size() - 1);
    for (std::size_t i = 0; i + 1 < inertias.size(); ++i) {
        diffs[i] = inertias[i] - inertias[i + 1];
    }
    std::vector<double> second_diffs(diffs.size() - 1);
    for (std::size_t i = 0; i + 1 < diffs.size(); ++i) {
        second_diffs[i] = diffs[i] - diffs[i + 1];
    }
    int knee_idx = 0;
    double best = second_diffs[0];
    for (std::size_t i = 1; i < second_diffs.size(); ++i) {
        if (second_diffs[i] > best) {
            best = second_diffs[i];
            knee_idx = static_cast<int>(i);
        }
    }
    return knee_idx + 1;
}

int main() {
    std::vector<std::vector<double>> points;
    for (int i = 0; i < 60; ++i) {
        points.push_back({POINTS[i][0], POINTS[i][1]});
    }

    std::vector<double> inertias;
    for (int k = 1; k <= 6; ++k) {
        auto km_result = kmeans(points, k, 50, 42);
        double inertia = std::get<2>(km_result);
        inertias.push_back(inertia);
    }

    int knee_idx = elbow_knee(inertias);
    int detected_k = knee_idx + 1;

    assert(detected_k == 3);
    assert(inertias[1] - inertias[2] > inertias[2] - inertias[3]);

    std::cout << "elbow_method_kmeans.cpp: knee detected at k=" << detected_k << " PASS\n";
    return 0;
}
