// @forge-family kmeans

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/**
 * Canopy pre-clustering followed by Lloyd's k-means.
 *
 * A seeded PRNG is defined inside the fixture. Points are greedily grouped
 * into loose "canopies" using a distance threshold, then initial centroids are
 * derived from the densest canopies. A final Lloyd pass on the full data set
 * converges to the exact fixed point.
 *
 * @param {number[][]} X - data matrix
 * @param {number[]} y - unused target vector (harness contract)
 * @param {number} lr - unused learning rate (harness contract)
 * @param {number} iters - maximum Lloyd iterations
 * @returns {{centroids:number[][], k:number, assignments:number[]}}
 */
function kmeansCanopy(X, y, lr, iters) {
    const n = X.length;
    const nf = X[0].length;
    const k = 3;

    let rngState = 20240806 >>> 0;
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

    // Canopy construction: randomized order, two distance thresholds.
    const order = new Array(n).fill(0).map((_, i) => i);
    for (let i = n - 1; i > 0; i--) {
        const j = Math.floor(rand() * (i + 1));
        const tmp = order[i];
        order[i] = order[j];
        order[j] = tmp;
    }

    // Thresholds chosen relative to the data span.
    let span = 0;
    for (let f = 0; f < nf; f++) {
        let min = Infinity, max = -Infinity;
        for (let i = 0; i < n; i++) {
            const v = X[i][f];
            if (v < min) min = v;
            if (v > max) max = v;
        }
        const d = max - min;
        if (d > span) span = d;
    }
    const T1 = span * 0.45;
    const T2 = span * 0.30;
    const T1d2 = T1 * T1;
    const T2d2 = T2 * T2;

    const used = new Array(n).fill(false);
    const canopies = [];
    for (const idx of order) {
        if (used[idx]) continue;
        const center = X[idx].slice();
        const canopy = { center, members: [] };
        for (let i = 0; i < n; i++) {
            const d = dist2(X[i], center);
            if (d <= T1d2) canopy.members.push(i);
            if (d <= T2d2) used[i] = true;
        }
        canopies.push(canopy);
    }

    // Derive initial centroids from the largest canopies.
    canopies.sort((a, b) => b.members.length - a.members.length);
    let centroids = canopies.slice(0, k).map(c => {
        const mean = new Array(nf).fill(0);
        for (const i of c.members) {
            const x = X[i];
            for (let f = 0; f < nf; f++) mean[f] += x[f];
        }
        for (let f = 0; f < nf; f++) mean[f] /= c.members.length;
        return mean;
    });

    // Fill with k-means++ candidates if fewer than k canopies.
    if (centroids.length < k) {
        const d2 = new Array(n).fill(0);
        while (centroids.length < k) {
            let total = 0;
            for (let i = 0; i < n; i++) {
                let minD = dist2(X[i], centroids[0]);
                for (let c = 1; c < centroids.length; c++) minD = Math.min(minD, dist2(X[i], centroids[c]));
                d2[i] = minD;
                total += minD;
            }
            let threshold = rand() * total;
            let chosen = 0;
            for (let i = 0; i < n; i++) {
                threshold -= d2[i];
                if (threshold <= 0) {
                    chosen = i;
                    break;
                }
            }
            centroids.push(X[chosen].slice());
        }
    }

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

globalThis.linearRegressionGD = kmeansCanopy;
const linearRegressionGD = kmeansCanopy;   // Forge Gate harness contract — do not remove
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
    const result = kmeansCanopy(X, y, 0.05, 200);
    assertShape(result);

    const expectedCentroids = [[5.011577170107475,-0.09160253629553519],[0.11307742202213614,-0.1340640949477895],[2.5341394147994447,3.8391060156544703]];
    const expectedAssignments = [1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2];

    assert(approxEqual(result.centroids, expectedCentroids, 1e-9), 'self-test: centroids mismatch');
    assert(approxEqual(result.assignments, expectedAssignments, 1e-9), 'self-test: assignments mismatch');
})();

