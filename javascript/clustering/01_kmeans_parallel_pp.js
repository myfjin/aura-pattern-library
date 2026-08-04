// @forge-family kmeans

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * k-means|| (scalable k-means++).
 *
 * k-means|| oversamples candidate centroids via probability proportional to
 * squared distance, then re-clusters those candidates with Lloyd's algorithm
 * using deterministic weights. A final Lloyd pass on the full data guarantees
 * the exact fixed point. A seeded PRNG is defined inside the fixture.
 *
 * @param {number[][]} X - data matrix
 * @param {number[]} y - unused target vector (harness contract)
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - maximum iterations
 * @returns {{centroids:number[][], k:number, assignments:number[]}}
 */
function kmeansParallelPp(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;
    const k = 3;

    let rngState = 20240805 >>> 0;
    function rand() {
        rngState = ((rngState * 1664525 + 1013904223) & 0xFFFFFFFF) >>> 0;
        return rngState / 0x100000000;
    }

    function dist2(a, b) {
        let s = 0;
        for (let f = 0; f < nf; f++) {
            const d = a[f] - b[f];
            s += d * d;
        }
        return s;
    }

    function nearest(x, centroids) {
        let best = 0;
        let bestD = dist2(x, centroids[0]);
        for (let c = 1; c < centroids.length; c++) {
            const d = dist2(x, centroids[c]);
            if (d < bestD) {
                bestD = d;
                best = c;
            }
        }
        return best;
    }

    function mean(indices, weights) {
        const mean = new Array(nf).fill(0);
        let total = 0;
        for (let i = 0; i < indices.length; i++) {
            const w = weights[i];
            total += w;
            const x = X[indices[i]];
            for (let f = 0; f < nf; f++) mean[f] += w * x[f];
        }
        if (total === 0) return X[0].slice();
        for (let f = 0; f < nf; f++) mean[f] /= total;
        return mean;
    }

    // k-means||: pick an initial point, then oversample candidates.
    let candidates = [X[Math.floor(rand() * n)].slice()];
    const oversampling = Math.max(k * 2, Math.floor(n / 4));
    let minD2 = new Array(n);
    for (let i = 0; i < n; i++) minD2[i] = dist2(X[i], candidates[0]);

    for (let round = 0; round < 5; round++) {
        let total = 0;
        for (let i = 0; i < n; i++) total += minD2[i];
        const prob = total === 0 ? 1 / n : oversampling / total;
        for (let i = 0; i < n; i++) {
            if (rand() < minD2[i] * prob) {
                candidates.push(X[i].slice());
            }
        }
        if (candidates.length >= k * 10) break;
        for (let i = 0; i < n; i++) {
            const c = nearest(X[i], candidates);
            minD2[i] = dist2(X[i], candidates[c]);
        }
    }

    if (candidates.length > k * 4) {
        // Thin the candidate set by farthest-point subsampling, deterministic.
        const keep = [candidates[0].slice()];
        const d2 = new Array(candidates.length).fill(0);
        while (keep.length < k * 4) {
            let total = 0;
            for (let i = 0; i < candidates.length; i++) {
                let minD = Infinity;
                for (const c of keep) minD = Math.min(minD, dist2(candidates[i], c));
                d2[i] = minD === Infinity ? 0 : minD;
                total += d2[i];
            }
            let threshold = rand() * total;
            let chosen = 0;
            for (let i = 0; i < candidates.length; i++) {
                threshold -= d2[i];
                if (threshold <= 0) {
                    chosen = i;
                    break;
                }
            }
            keep.push(candidates[chosen].slice());
        }
        candidates = keep;
    }

    // Re-cluster candidates: each candidate has weight = number of nearest X points.
    const candAssign = new Array(candidates.length).fill(0);
    for (let iter = 0; iter < iters; iter++) {
        let changed = 0;
        const counts = new Array(k).fill(0);
        for (let i = 0; i < n; i++) {
            counts[nearest(X[i], candidates.slice(0, k))]++;
        }
        for (let i = 0; i < candidates.length; i++) {
            const c = nearest(candidates[i], candidates.slice(0, k));
            if (candAssign[i] !== c) {
                candAssign[i] = c;
                changed++;
            }
        }
        const sums = new Array(k).fill(0).map(() => new Array(nf).fill(0));
        const weights = new Array(k).fill(0);
        for (let i = 0; i < candidates.length; i++) {
            const c = candAssign[i];
            // Weight candidate by the X points that would pick it in the current codebook.
            let w = 0;
            for (let j = 0; j < n; j++) {
                if (nearest(X[j], candidates) === i) w++;
            }
            weights[c] += w;
            const p = candidates[i];
            for (let f = 0; f < nf; f++) sums[c][f] += w * p[f];
        }
        for (let c = 0; c < k; c++) {
            if (weights[c] > 0) {
                for (let f = 0; f < nf; f++) candidates[c][f] = sums[c][f] / weights[c];
            }
        }
        if (changed === 0 && iter > 0) break;
    }

    let centroids = candidates.slice(0, k);

    // Final Lloyd pass on the full data set.
    const assignments = new Array(n).fill(0);
    for (let iter = 0; iter < iters; iter++) {
        let changed = 0;
        for (let i = 0; i < n; i++) {
            const c = nearest(X[i], centroids);
            if (assignments[i] !== c) {
                assignments[i] = c;
                changed++;
            }
        }
        const sums = new Array(k).fill(0).map(() => new Array(nf).fill(0));
        const counts = new Array(k).fill(0);
        for (let i = 0; i < n; i++) {
            const c = assignments[i];
            counts[c]++;
            const x = X[i];
            for (let f = 0; f < nf; f++) sums[c][f] += x[f];
        }
        for (let c = 0; c < k; c++) {
            if (counts[c] > 0) {
                for (let f = 0; f < nf; f++) centroids[c][f] = sums[c][f] / counts[c];
            }
        }
        if (changed === 0) break;
    }

    for (let i = 0; i < n; i++) assignments[i] = nearest(X[i], centroids);
    return { centroids, k, assignments };
}

globalThis.linearRegressionGD = kmeansParallelPp;
const linearRegressionGD = kmeansParallelPp;   // Forge Gate harness contract — do not remove
// Self-test: deterministic fixture from the Forge Gate kmeans oracle.
(function () {
    function lcg_next(s) {
        return ((s * 1664525 + 1013904223) & 0xFFFFFFFF) >>> 0;
    }
    function makeHarnessData() {
        let st = 12345 >>> 0;
        function normal_pair() {
            st = lcg_next(st);
            const u1 = Math.max(st / 0x100000000, 1e-10);
            st = lcg_next(st);
            const u2 = st / 0x100000000;
            const r = Math.sqrt(-2.0 * Math.log(u1));
            const theta = 2.0 * Math.PI * u2;
            return [r * Math.cos(theta), r * Math.sin(theta)];
        }
        const centers = [[0.0, 0.0], [5.0, 0.0], [2.5, 4.0]];
        const sigma = 0.5;
        const clusters = [[], [], []];
        for (let c = 0; c < 3; c++) {
            for (let i = 0; i < 20; i++) {
                const z = normal_pair();
                clusters[c].push([centers[c][0] + sigma * z[0], centers[c][1] + sigma * z[1]]);
            }
        }
        const X = [];
        for (let i = 0; i < 20; i++) {
            for (let c = 0; c < 3; c++) {
                X.push(clusters[c][i]);
            }
        }
        const y = [];
        return { X, y };
    }
    function assert(cond, msg) {
        if (!cond) {
            const e = new Error(msg);
            e.name = 'AssertionError';
            throw e;
        }
    }
    function approxEqual(a, b, relTol) {
        if (typeof a === 'number') {
            if (!isFinite(a) || !isFinite(b)) return false;
            if (a === 0 && b === 0) return true;
            return Math.abs(a - b) <= relTol * Math.max(Math.abs(a), Math.abs(b));
        }
        if (Array.isArray(a)) {
            if (!Array.isArray(b) || a.length !== b.length) return false;
            return a.every((v, i) => approxEqual(v, b[i], relTol));
        }
        return a === b;
    }
    function assertShape(result) {
        assert(result && typeof result === 'object', 'self-test: result is not an object');
        assert(result.k === 3, 'self-test: expected k=3, got ' + result.k);
        assert(Array.isArray(result.centroids) && result.centroids.length === 3, 'self-test: expected 3 centroids');
        result.centroids.forEach(function (c, i) {
            assert(Array.isArray(c) && c.length === 2, 'self-test: centroid ' + i + ' not length-2');
        });
        assert(Array.isArray(result.assignments) && result.assignments.length === 60, 'self-test: expected 60 assignments');
    }

    const { X, y } = makeHarnessData();
    const result = kmeansParallelPp(X, y, 0.05, 200);
    assertShape(result);

    const expectedCentroids = [[0.11307742202213614,-0.1340640949477895],[2.5341394147994447,3.8391060156544703],[5.011577170107475,-0.09160253629553519]];
    const expectedAssignments = [0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1];

    assert(approxEqual(result.centroids, expectedCentroids, 1e-9), 'self-test: centroids mismatch');
    assert(approxEqual(result.assignments, expectedAssignments, 1e-9), 'self-test: assignments mismatch');
})();

